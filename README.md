# qoogle

The following is a project that I worked on for my information retrieval class (CS 121). It is a search engine that can be used in two different ways; via command line or via GUI. This guide will walk you through how to get the search engine working on your device from start to finish.


### Getting Set Up

First and foremost you're going to need to download [this folder](https://canvas.eee.uci.edu/courses/9972/files/3219997/download?verifier=KMaq3Ct8OalHmjoJy7ENjX5K4VmiEs2r09QifZm4&wrap=1). It contains the raw webpages that the main file will use to generate an inverted index which is used for the search engine. The actual inverted index has already been made but the files are still needed for the GUI based search engine to get links from.

Once you have all of the raw webpages, you're going to make sure to download all the necessary packages so that the program can work. For this project the only package you're going to need is BeautifulSoup. This packaged is used for most of the xml file reading. To do this run the following command:

```
pip install beautifulsoup4
```

Now that you have the raw webpages and BeautifulSoup, you're ready to start the actual program.


### Building the Inverted Index

The search engine needs an inverted index in order to retrieve the information you ask it for. The inverted index used for this search engine is already in this repository but if you wanted to build it for whatever reason you can do so by simply running the following command:

```
python main.py
```

This command runs the main file which goes through each and every individual word in all of the raw webpages. For each word in a webpage, the main program calculates a tf and idf score (term frequency and inverse document frequency). It adds this tf-idf score to a master dictionary which contains every word across all the webpages. As the program runs through the webpages, repeated words have the tf-idf score appended to the end of the value entry, this creates a posting list. There is also weighting involved in the calculation of tf-idf scores, so words found under an h1 header would be considered more important than normal words.

After some time the program should comeplete and you will now have a fully constructed inverted index. If you look into the file, it will be a massive tab separated file (.tsv) where the keys are words and the values are the posting lists. The posting lists have all of the if-idf scores separated by underscore for readability. You are now ready to run the actual search engine! The next two sections will cover the two methods which can be used to search for a word or words.


### Running the Search Engine: Command Line

This search engine is capable of querying one to x amount of words. For the best results search for words that are related, otherwise the results may be slightly skewed. I'll get into the actual way that the engine searches for results but first I'll show you how to run the actual program. All you do is type the following command:

```
python query.py FIRST_QUERY SECOND_QUERY ETC_QUERY
```

When typing queries make sure that they are spelled correctly and that they are separated by space. Once you hit enter after typing in this command, a list of up to 10 results will be displayed. When searching with a single query, this list is the top 10 links containing the query you searched for. When searching with multiple queries, the results will prioritize sites containing both words, then revert to highest singular queries. Say that there are only 6 sites containing both "compueter" and "science", the 7th link and onwards would then be links to pages with the highest singular occurance of "computer" or "science". That's pretty much all you need to know to run the search engine via command line!


### Running the Search Engine: GUI

It is very simple to run the search engine via GUI. The command below will actually get the GUI up and running. Once the GUI is running, simply type in your query and press search. The results will be displayed in priority of tf-idf score. The top 10 results of a query will be displayed and you can go to any of the webpages by clicking the links. If your query pulled less than 10 results, then only that amount will be shown in the results. The prioritaztion of the top 10 search results for multiple word queries is exactly the same as when you run from the command line. That's pretty much all you'll need to know to run the search engine via GUI.

```
python GUI.py
```


### Authors

* **Qasim Shareh** - Most developement; main.py, query.py, GUI.py
* **Tyler Valdivieso** - Assistance on; main.py, query.py
* **James Ostergaard** - Assistance on; query.py


### Acknowledgements

* Big thank you to Prajal Trivedi for helping our group towards the pathway of success.
* Big thank you to Professor Sergio Gago-Masague for teaching such a great class.
* Big thank you to Chick-fil-A for allowing us to hold our group meetings in their restaurant.


