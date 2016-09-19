import re
import urllib
import core.downloader as program


print("Starting...")
print()
url = input("Enter the url of the PDF:")

url_open1 = urllib.request.urlopen(url).read()
url_open1 = str(url_open1.decode("utf-8"))

# Credits to https://txt2re.com/ for the regex (Almost all of it)
# Sorry, I'm not lazy, but I hate making regex's
re1 = '.*?'
re2 = '((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)(?:png|jpg))'

rg = re.compile(re1+re2, re.IGNORECASE | re.DOTALL)
m = rg.search(url_open1)
if m:
    httpurl1 = m.group(1)
    print('Starting from URI: ' + httpurl1)
    program.downloader(httpurl1)
else:
    print("Error! No image was found")
