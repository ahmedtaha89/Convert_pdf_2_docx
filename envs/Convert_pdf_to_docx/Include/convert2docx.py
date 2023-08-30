import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert_pdf_to_docx():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        docx_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("DOCX files", "*.docx")])
        if docx_path:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            result_label.config(text="Conversion completed successfully.")

# Create the main application window
app = tk.Tk()
app.title("PDF to DOCX Converter")

# Create a button to trigger the conversion
convert_button = tk.Button(app, text="Convert PDF to DOCX", command=convert_pdf_to_docx)
convert_button.pack(pady=150, padx=150)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 12, "italic"))
result_label.pack()

# Run the GUI event loop
app.mainloop()
