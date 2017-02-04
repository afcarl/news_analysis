#Source validation

The idea here is to validate news stories through a web of trust.  If the article sources trusted sources, it is given a trusted score and a classification is decided as to whether it is trusted or not.

Tools for NLP:
	* nltk
	* spacy
	* textacy
	* vader
	* sentlex
	* stanford coreNLP

We could use structure of the page for a feature

Check for conflict of interest

Bias:
author bias: did they come down for or against this topic in the past.
website bias: does the website have many pro or con for the article

Can we decide ground truth from the world (the internet)?

Big win:
Given an authoratitative source, can we decide whether or not a given article comforms or goes against that authoraitative source?

Smaller win:
Equivalence classes is also a win.


##Features

* How much advertising there is?
* Amount of space taken up by images
* Which news sources are being shown on the website
	* google add sense
* Document length
* Part-of-speech composition
* Average sentence length
* Measure of vocabulary complexity
* Frequency of rare words
* Result of sentiment/emotional analysis
* List of entities - number of entities, average number of entities per sentence?
* Measure of sentence complexity - number of clauses or depth of sentence dependency trees.
* Number of linked articles
* Features of linked articles?
