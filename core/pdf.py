from fpdf import FPDF
from PIL import Image

pdf = FPDF()


def creator(pdflist):
    print('Started pdf creation...')

    for imageFile in pdflist:
        cover = Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        pdf.add_page(format=(width, height))

        pdf.image(imageFile, 0, 0, width, height)
    pdf.output("output.pdf", "F")

    print('Completed pdf creation...')
