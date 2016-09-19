# Issuu-PDF-Downloader
Program on python which downloads Issuu files as PDF

Issuu is a platform which allows users to upload PDF's and protect them from downloading (they didn't count with me)

However, while doing research on the source code, I was able to find its weakness. It stores each page of the PDF as a .jpg in a certain location, and labels it as page_1 <-- number of the page.

So, with this little code in python you're able to take advantage of this weakness and download any file you wish.



You have to run the file framework.py and paste the url of the file you want to download, that's it.

It will give you the images as well as a PDF.

You can change the image size in the resize.py file.

In order to change the size of the page of the PDF, you must modify the pdf.py file.

Testing that this works