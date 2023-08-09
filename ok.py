import PyPDF2

def extract_data_from_pdf(pdf_path):
   extracted_data = []

   with open(pdf_path, 'rb') as pdf_file:
       pdf_reader = PyPDF2.PdfReader(pdf_file)
       num_pages = len(pdf_reader.pages)

       for page_num in range(num_pages):
           page = pdf_reader.pages[page_num]
           text = page.extract_text()
           extracted_data.append(text)

   return extracted_data

pdf_path = 'path/to/your/pdf/file.pdf'
extracted_data = extract_data_from_pdf(pdf_path)

for data in extracted_data:
   print(data)
