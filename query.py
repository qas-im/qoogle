import sys													# import sys to get command line arguments

if __name__ == "__main__":									# if file is not being imported
	if len(sys.argv) == 2:									# for one word query
		query = sys.argv[1].lower()							# set search to be first argument from command line
		data = {}											# initialize data dictionary
		book_data = {}                                      # create dictionary to hold all data
		book = open("./WEBPAGES_RAW/bookkeeping.tsv","r")   # open bookkeeping.tvs to read through
		for line in book:									# iterate through each line in bookkeeping
			line = line.split()								# split each line into key and value
			book_data[line[0]] = line[1]					# add key to book_data with value
		
		index = open("index.txt","r")						# open index.txt to be read from
		for line in index:									# iterate through each line in index
			line = line.split()								# split line to make into key value pairs
			data[line[0]] = line[1]							# add key and value to data dict
		
		q_data = []											# create empty list which will hold query_data
		query_info = data[query].split(";")					# split query_info by ";" to get each docs info
		for doc in query_info:								# iterate through each doc in given query
			doc = doc.split("_")							# split doc on "_" to get each category
			q_data.append(doc)								# append doc categories into q_data
		
		q_data_s = sorted(q_data,key=lambda x: -float(x[1]))	# sort q_data by word count
		entries = 1												# entry count to keep track of how many prints
		print("Top 10 Results For \""+sys.argv[1]+"\" In Index")
		for entry in q_data_s[:10]:								# iterate through sorted_q_data starting at top
			location = book_data[entry[0]]						# location of file being presented
			print("{:2}: {}".format(entries,location))			# formatting to above print statement
			entries += 1										# increment entries
	
	
	elif len(sys.argv) > 2:			# case for multiline query
		query_list = []				# initialize empty query list
		for arg in sys.argv[1:]:	# iterate through argv (ignoring first element)
			query_list.append(arg)	# append each arg to query list
		
		book_data = {}
		book = open("./WEBPAGES_RAW/bookkeeping.tsv","r")
		for line in book:
			line = line.split()
			book_data[line[0]] = line[1]
		
		data = {}
		index = open("index.txt","r")
		for line in index:
			line = line.split()
			data[line[0]] = line[1]
		
		
		doc_data = {}							# doc_data dict KEY=PATH//VAL=PATH_COUNT
		#tfidf_data = {}							# tfidf_data dict KEY=PATH//VAL=SUM_OF_TFIDFs
		for query in query_list:				# iterate through each query
			post_list = data[query].split(";")	# separate post list by ";"
			for post in post_list:				# iterate through each post entry in post_list
				post = post.split("_")			# split post entry on "_"
				doc = post[0]					# first index is doc path
				tfidf = float(post[1])			# second index is tfidf score
				if doc not in doc_data:			# check to see if doc isn't added to doc_data
					doc_data[doc] = [1,tfidf]	# if so initialize the doc count to 1
					#doc_data[doc][1] = tfidf
					#tfidf_data[doc] = tfidf		# initialize tfidf_data entry to tfidf
				else:							# if doc already in doc_data
					doc_data[doc][0] += 1		# increment doc_data count
					doc_data[doc][1] += tfidf
					#tfidf_data[doc] += tfidf	# add on top of previous tfidf_data
		
		print("Top 10 Results For \""+" ".join(query_list)+"\" In Index")
		entries = 1
		for k,v in sorted(doc_data.items(), key=lambda x: (-x[1][0],-x[1][1]))[:10]:
			print("{:2}: {}".format(entries,book_data[k]))
			entries += 1
		
def get_query(query_list):
	result_list = []
	
	book_data = {}
	book = open("./WEBPAGES_RAW/bookkeeping.tsv","r")
	for line in book:
		line = line.split()
		book_data[line[0]] = line[1]
	
	data = {}
	index = open("index.txt","r")
	for line in index:
		line = line.split()
		data[line[0]] = line[1]
	
	
	doc_data = {}
	for query in query_list:
		post_list = data[query].split(";")
		for post in post_list:
			post = post.split("_")
			doc = post[0]
			tfidf = float(post[1])
			if doc not in doc_data:
				doc_data[doc] = [1,tfidf]
			else:
				doc_data[doc][0] += 1
				doc_data[doc][1] += tfidf
	
	for k,v in sorted(doc_data.items(), key=lambda x: (-x[1][0],-x[1][1]))[:10]:
		result_list.append("http://"+book_data[k])

	return result_list		
