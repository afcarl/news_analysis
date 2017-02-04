import requests
import lxml.html

url = "https://www.nytimes.com/2017/02/04/us/politics/visa-ban-trump-judge-james-robart.html?ref=politics"

html = lxml.html.fromstring(requests.get(url).text)
article = html.xpath("//article")
text = "\n".join([elem.text_content() for elem in article[0].xpath("//p[@class='story-body-text story-content']")])

import code
code.interact(local=locals())
