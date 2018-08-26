from urlparse import urlparse		# imported to parse through html files
from bs4 import BeautifulSoup		# imported to get text from html files
import math

def clean_word(word):
	result = ""						# initialize cleaned word string
	for char in word.lower():		# iterate through each character in word
		if char.isalpha():			# if word is alphanumerical
			result += char			# add to result
		else:						# otherwise
			result += " "			# add a blank spac 
	return result					# return result in the end

if __name__ == "__main__":
	data = {}											# create dictionary to hold all data
	count = 0											# ***TEMPORARY COUNTER FOR TESTING
	book = open("./WEBPAGES_RAW/bookkeeping.tsv","r")	# open bookkeeping.tvs to read through
	for line in book:									# loop through every path/url pair	
		t_data = {}										# temporary t_data which will be used for each html
		p_data = {}										# temporary p_data which will keep track of path
		line = line.split()								# split line to separate path from url
		html_path = "./WEBPAGES_RAW/"+line[0]			# initialize path to file string to be read from
		html = open(html_path,"rb").read().decode('ascii', 'ignore')		# open and read file as well as decode to avoid UnicodeEncodeError
		soup = BeautifulSoup(html,"html.parser")		# turn html into soup for easier parsing
		
		
		# search for words in title (worth 5)
		title = soup.find_all("title")
		for content in title:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 5
						p_data[key] = line[0]
					else:
						t_data[key] += 5
		
		
		# search for words in body (worth 1)
		body = soup.find_all("body")				# collect all body information from the soup
		for content in body:						# iterate through content in collected body data
			for word in content.text.split():		# iterate through the split text from content
				cleaned_word = clean_word(word)		# collect cleaned word
				for key in cleaned_word.split():	# iterate through split/cleaned word
					if key not in t_data:			# if key not in t_data
						t_data[key] = 1				# initialize key value to 1
						p_data[key] = line[0]		# link path to key for later storage
					else:							# if key is in t_data
						t_data[key] += 1			# add one to it
		
		
		# search for words in h1 (worth 4)
		h1 = soup.find_all("h1")					# collect all h1 information from soup
		for content in h1:							# iterate through h1 content line by line
			for word in content.text.split():		# iterate through individual words in split content
				cleaned_word = clean_word(word)		# remove non alpha characters from word
				for key in cleaned_word.split():	# split word into keys to account for new spaces
					if key not in t_data:			# check to see if key is in data yet
						t_data[key] = 4				# if not initialize key value to four		
						p_data[key] = line[0]		# as well as including path data
					else:							# if key is already in data
						t_data[key] += 4			# add four to the count
		
		
		# search for words in h2 (worth 3)
		h2 = soup.find_all("h2")
		for content in h2:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 3
						p_data[key] = line[0]
					else:
						t_data[key] += 3
		
		
		# search for words in h3 (worth 2)
		h3 = soup.find_all("h3")
		for content in h3:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 2
						p_data[key] = line[0]
					else:
						t_data[key] += 2
		
		
		# search for words in h4 (worth 1)
		h4 = soup.find_all("h4")
		for content in h4:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 1
						p_data[key] = line[0]
					else:
						t_data[key] += 1
		
		
		# search for words in h5 (worth 1)
		h5 = soup.find_all("h5")
		for content in h5:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 1
						p_data[key] = line[0]
					else:
						t_data[key] += 1
		
		
		# search for words in h6 (worth 1)
		h6 = soup.find_all("h6")
		for content in h6:
			for word in content.text.split():
				cleaned_word = clean_word(word)
				for key in cleaned_word.split():
					if key not in t_data:
						t_data[key] = 1
						p_data[key] = line[0]
					else:
						t_data[key] += 1
		
		
		
		# transfer temp data to master data
		for k,v in t_data.items():					# take values from t_data to add to data
			if k not in data:						# if key isn't in data
				data[k] = p_data[k]+"_"+str(v)		# add the key with its value
			else:									# if the key is in data
				data[k] += ";"+p_data[k]+"_"+str(v)	# add the value to the back of it
		count += 1									# increment line count by 1 after each line read
		if count % 1000 == 0:
			print("CURRENT STATUS --> "+str(count))


	# calcutlate tfids here
	tfidf_data = {}
	for k,v in data.items():
		doc_count = v.count(";") + 1
		raw_idf = count/doc_count
		idf = round(math.log(raw_idf),2)
		for doc in v.split(";"):
			doc_info = doc.split("_")
			tf = 1 + round(math.log(int(doc_info[1])),2)
			tfidf = round(tf*idf,2)
			if k not in tfidf_data:
				tfidf_data[k] = doc_info[0]+"_"+str(tfidf)
			else:
				tfidf_data[k] += ";"+doc_info[0]+"_"+str(tfidf)


	# write to index
	index = open("index.txt","w")						# open index.txt to be written to
	token_count = 0										# initialize int keeping track of token_count
	for k,v in sorted(tfidf_data.items()):				# iterate through k,v pairs in sorted data
		token_count += 1								# increment token count
		try:											# try only added to avoid UnicodeEncodeError
			to_write = str(k) + "\t" + str(v) + "\n"	# prime entry to be written
			index.write(to_write)						# write the formatted entry
		except:											# except case
			pass										# ignore files with UnicodeEncodeError
	index.close()										# close file to avoid corruption
	print("line count: "+str(count))
	print("amount of unique tokens: "+str(token_count))
