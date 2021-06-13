from PyPDF2 import PdfFileReader
from pathlib import Path
# Prerequisite: have a PDF called textbook.pdf in the current working directory
pdf_path = (Path.cwd() / 'textbook.pdf')
pdf  = PdfFileReader(str(pdf_path))
print(f'Document Information:\n {pdf.documentInfo}\n')
print(f'Total number of pages is {pdf.getNumPages()}\n')
text = pdf.getPage(1).extractText()
print(f'Text on page 1 is:\n\n {text}')

