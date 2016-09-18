from fpdf import FPDF


# Change to resize pdf page
width = 1100
height = 900

pdf = FPDF(unit="pt", format=[width, height])


def creator(pdflist):
    print('Started pdf creation...')

    # Just to make it look cool in the console
    counter = 1
    total = len(pdflist)

    for image in pdflist:  # Add images to file
        pdf.add_page()
        pdf.image(image)
        print('Added image ' + str(counter) + ' of ' + str(total))
        counter += 1
    pdf.output("output.pdf", "F")  # Name for the PDF file

    print('Completed pdf creation...')
