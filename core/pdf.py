from fpdf import FPDF
from PIL import Image
from framework import pdf_size

pdf = FPDF()


def creator(pdflist, pdf_size):
    print('Started pdf creation...')

    for imageFile in pdflist:
        cover = Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # get page orientation from image size
        orientation = 'P' if width < height else 'L'

        #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

        pdf.add_page(orientation=orientation)

        pdf.image(imageFile, 0, 0, width, height)
    pdf.output("file.pdf", "F")

    print('Completed pdf creation...')
