import PyPDF2
import sys

inputs = sys.argv[1:]

source_pdf = PyPDF2.PdfFileReader(open(inputs[0], 'rb'))
watermark = PyPDF2.PdfFileReader(open(inputs[1], 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(source_pdf.getNumPages()):
  page = source_pdf.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
