import resizer as scale
import urllib.request
import requests
import pdf


def exists(path):  # Check that image exists
    r = requests.head(path)
    return r.status_code == requests.codes.ok


def downloader(url):
    print('Started download process...')
    files = []  #List to create the PDF
    formatter = url.replace('page_1.jpg', '')
    changer = 1
    while True:
        changer2 = formatter + 'page_' + str(changer) + '.jpg'
        filename = str(changer) + '.jpg'
        if exists(changer2):  # Download images
            opener = open(str(changer) + '.jpg', 'wb')
            opener.write(urllib.request.urlopen(changer2).read())
            opener.close()  # Save images
            print('Correctly saved file ' + filename + ' From URI: ' + changer2)
            scale.resizer(filename)  # Resize images
            print('Correctly scaled file ' + filename + ' to the size 1060*750 px')
            files.append(filename)  # Add filename to list, so we make the pdf later
            changer += 1  # Go for the next one
        else:
            break  # No more images

    print('Completed download process...')
    pdf.creator(files)  # Time to create the pdf
