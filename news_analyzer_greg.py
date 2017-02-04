import requests
import lxml.html
import spacy
from collections import Counter

def getFeatures(url):
    html = lxml.html.fromstring(requests.get(url).text)
    article = html.xpath("//article")
    text = "\n".join([elem.text_content() for elem in article[0].xpath("//p[@class='story-body-text story-content']")])
    nlp = spacy.load('en')
    doc = nlp(text)
    
    features = {}
    features['length'] = len(doc)
    
    partsOfSpeech = [word.tag_ for word in doc]
    posCount = Counter(partsOfSpeech)

    return posCount


url = "https://www.nytimes.com/2017/02/04/us/politics/visa-ban-trump-judge-james-robart.html?ref=politics"

print getFeatures(url)

#import code
#code.interact(local=locals())

