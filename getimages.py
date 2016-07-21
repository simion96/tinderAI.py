import urllib
import re
import time

regexRule = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
extension = ".jpg"
liked = ""
round = ""
roundIdentifier = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("liked", "r") as text_file:
    liked = text_file.read()
with open("identifier.txt", "r") as text_file:
    round = text_file.read()
if round == "":
    round = "A"
folder = "ladies/"
counter = 0
name = folder + str(counter)


#urllib.urlretrieve("http://images.gotinder.com/5553606c7edc79cb1fa8ad5a/18d73531-3dc5-438e-9e21-52b4d5271dcc.jpg", "name")
links = re.findall(regexRule, liked)
#print links

for link in links:
    urllib.urlretrieve(link, folder+link[27:51]+extension)
    counter+=1
    name = folder + str(counter)+round+extension

open("identifier.txt", "w").close()
if (round != "Z"):
    with open("identifier.txt", "w") as text_file:
        text_file.write(roundIdentifier[roundIdentifier.index(round)+1])


print ""
#print newS
#print type(newS)
