import urllib.request

url = input("Enter the url you want to get the information from: ")

if str(url)[:8] == "http://":
    url = url
elif str(url)[:9] == "https://":
    url = url
else:
    url = "http://" + str(url)

content = urllib.request.urlopen(url)

info =  content.read()

print (info)
