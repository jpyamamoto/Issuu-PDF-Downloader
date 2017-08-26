from fpdf import FPDF
from framework import WIDTH_PDF, HEIGHT_PDF, NAME_PDF


pdf = FPDF(unit="pt", format=[WIDTH_PDF, HEIGHT_PDF])


def creator(pdflist):
    print('Started pdf creation...')

    # Just to make it look cool in the console
    counter = 1
    total = len(pdflist)

    for image in pdflist:
        # Add images to file
        pdf.add_page()
        pdf.image(image)
        print('Added image ' + str(counter) + ' of ' + str(total))
        counter += 1
    pdf.output(NAME_PDF, "F")

    print('Completed pdf creation...')
