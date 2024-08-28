import PyPDF2
import os

# enter path to pdf files to be concatenated
pdf_path = ''

# enter name of primary, final pdf file
main_pdf_file = ''
#os.system('ls {}'.format(pdf_path))

def create_pdf(pathname):
        single_pdfs = []

        pdf_list = os.listdir(pdf_path)

        writer = PyPDF2.PdfWriter()
        for pdf in pdf_list:
                single_pdfs.append(pdf)
        single_pdfs.sort() # sort pdf chapters from beginning to end
        for file in single_pdfs:
                with open(pdf_path+file, 'rb') as f:
                         reader = PyPDF2.PdfReader(f)
                         for page in reader.pages:
                                writer.add_page(page)
        
        with open(pdf_path+main_pdf_file, 'wb') as output_file:
                 writer.write(output_file)


create_pdf(pdf_path)

