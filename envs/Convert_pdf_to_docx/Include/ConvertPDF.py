from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    # pdf_file = r"D:\book\python-cheat-sheet.pdf"   # Replace with your PDF file's path
    # docx_file = r"D:\book\output.docx" # Replace with the desired output DOCX file path
    
    pdf_file = r"D:\Convert_pdf_2_docx\venv\Code\Copy of 1. Python.pdf"   # Replace with your PDF file's path
    docx_file = r"D:\Convert_pdf_2_docx\venv\Code\Copy1.docx" # Replace with the desired output DOCX file path
    
    convert_pdf_to_docx(pdf_file, docx_file)
    print("Conversion complete.")
