import core.resizer as scale
import urllib
import requests
import core.pdf as pdf
from framework import WIDTH_IMAGE, HEIGHT_IMAGE


def exists(path):
    # Check that image exists
    r = requests.head(path)
    return r.status_code == requests.codes.ok


def downloader(url):
    print('Started download process...')
    # List to create the PDF
    files = []
    formatter = url.replace('page_1.jpg', '')
    changer = 1
    while True:
        changer2 = formatter + 'page_' + str(changer) + '.jpg'
        filename = str(changer) + '.jpg'
        if exists(changer2):
            # Download images
            opener = open(str(changer) + '.jpg', 'wb')
            opener.write(urllib.request.urlopen(changer2).read())
            # Save images
            opener.close()
            print('Correctly saved file ' + filename + ' From URI: ' + changer2)
            # Resize images
            scale.scale(filename, WIDTH_IMAGE, HEIGHT_IMAGE)
            print('Correctly scaled file {}. Width: {}px. Height: {}px.'.format(
                filename, WIDTH_IMAGE, HEIGHT_IMAGE))
            # Add filename to list, so we make the pdf later
            files.append(filename)
            # Go for the next one
            changer += 1
        else:
            # No more images
            break

    print('Completed download process...')
    # Time to create the pdf
    pdf.creator(files)
