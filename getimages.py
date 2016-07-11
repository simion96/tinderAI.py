import urllib
import re

regexRule = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

liked = ""
with open("liked", "r") as text_file:
    liked = text_file.read()
folder = "ladies/"
counter = 0
name = folder + str(counter)


#urllib.urlretrieve("http://images.gotinder.com/5553606c7edc79cb1fa8ad5a/18d73531-3dc5-438e-9e21-52b4d5271dcc.jpg", "name")
links = re.findall(regexRule, liked)
print links

for link in links:
    urllib.urlretrieve(link, name)
    counter+=1
    name = folder + str(counter)


#print newS
#print type(newS)
