import twitter
import urllib2
import datetime

#get History/ Current Session
currentSession = open("C:\Users\Daniel\AppData\Local\Google\Chrome\User Data\Default\Current Session")
now = currentSession.read()

#Read the 4 keys using split
file = open("keys.txt")
cred = file.readline().strip().split(",") 

#finding the page from the session i accessed earlier
firstSesh = now.rfind("http")
lastSesh = now.find(chr(0), firstSesh)
url = now[firstSesh:lastSesh]

#urllib grabbing the url from history
urlreceived = urllib2.urlopen(url)
html = urlreceived.read()

#getting the title of the website
firstTitle = html.find("<title>") + len("<title>") 
endTitle = html.find("</title>", firstTitle)

titlez = html[firstTitle:endTitle]

stamp = datetime.datetime.utcnow()
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])

#POSTING IT ON TWITTER
response = api.PostUpdate(" i like " + str(titlez) + " accessed " + str(stamp) + "check it out :" + url)

statuses = api.GetUserTimeline(3096334917) 
print ("done")