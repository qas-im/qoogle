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

to be written...


### Running the Search Engine: GUI

to be written...


### Authors

* **Qasim Shareh** - Most developement; main.py, query.py, GUI.py
* **Tyler Valdivieso** - Assistance on; main.py, query.py
* **James Ostergaard** - Assistance on; query.py


### Acknowledgements

* Big thank you to Prajal Trivedi for helping our group towards the pathway of success.
* Big thank you to Sergio Gago-Masague for teaching such a great class.
* Big thank you to Chick-fil-A for allowing us to hold our group meetings in restaurant.

