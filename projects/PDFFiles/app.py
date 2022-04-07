# Within this  folder are several PDF files to work with

import PyPDF2

# To open a PDF file there can be used the open statement or the with statement

with open ('flexbox.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print ('reader = ',reader)
    print ('type(reader) = ',type(reader))
    # This instruction returns a <class 'PyPDF2.pdf.PdfFileReader'> object    
    print(reader.numPages)
    # This attribute returns the number of pages of a PDF file
    page = reader.getPage(10)
    # Note : Pages are indexed from 0 on
    print ('page = ',page)
    print ('type(page) = ',type(page))
    # This instruction returns a <class 'PyPDF2.pdf.PageObject'>
    page.rotateClockwise(180)
    # This Method modifies the object and roates X page
    writer = PyPDF2.PdfFileWriter()
    print ('writer = ',writer)
    print ('type(writer) = ',type(writer))
    # This instruction returns a <class 'PyPDF2.pdf.PdfFileWriter'>
    writer.addPage(page)
    # The 'addPage()' method adds a <class 'PyPDF2.pdf.PageObject'> to a <class 'PyPDF2.pdf.PdfFileWriter'>
    with open ('flexboxV2.pdf','wb') as result:
        writer.write(result)
        # The 'write()' method writes in the file 'result' the 'writer' content

merger = PyPDF2.PdfFileMerger()
pdf_files = ['flexbox.pdf','grid.pdf']

for pdf_file in pdf_files:
    merger.append(pdf_file)
    # The 'append()' method recieves the path of a PDF file and merges the in order

merger.write('flex-Grid-Guide.pdf')
