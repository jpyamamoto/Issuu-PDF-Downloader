import re
import urllib

# ----------
# CONSTANTS
# ----------
WIDTH_IMAGE = 1600
HEIGHT_IMAGE = 750
WIDTH_PDF = 1100
HEIGHT_PDF = 900
NAME_PDF = 'output.pdf'


def main():
    import core.downloader as program

    print("Starting...\n")
    url = input("Enter the url of the PDF:")

    url_open1 = str(urllib.request.urlopen(url).read().decode("utf-8"))

    # Credits to https://txt2re.com/ for the regex (Almost all of it)
    # Sorry, I'm not lazy, but I hate making regex's
    re1 = '.*?'
    re2 = '((?:http|https)(?::\\/{2}[\\w]+)(?:[\\/|\\.]?)(?:[^\\s"]*)(?:png|jpg))'

    rg = re.compile(re1+re2, re.IGNORECASE | re.DOTALL)
    m = rg.search(url_open1)
    if m:
        httpurl = m.group(1)
        print('Starting from URI: ' + httpurl)
        program.downloader(httpurl)
    else:
        print("Error! No image was found")


if __name__ == '__main__':
    main()
