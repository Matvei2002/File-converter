import tkinter as tk
from tkinter import filedialog
import docx2pdf
import pdf2docx

root = tk.Tk()
root.title("Конвертер файлов")
root.geometry('720x480')
root.resizable(width=False, height=False)
root['bg'] = '#808080'


def pdf_to_docx():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        docx_file = file_path[:-4] + ".docx"
        pdf2docx.parse(file_path, docx_file)
        success_label.config(text="Конвертация прошла успешно")

def docx_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    if file_path:
        pdf_file = file_path[:-5] + ".pdf"
        docx2pdf.convert(file_path, pdf_file)
        success_label.config(text="Конвертация прошла успешно")

pdf_to_docx_button = tk.Button(root, text="PDF to DOCX", font='Arial 20 bold',
       fg='#FF0000', bg='#FFFFFF', command=pdf_to_docx)
pdf_to_docx_button.pack(pady=10)

docx_to_pdf_button = tk.Button(root, text="DOCX to PDF", font='Arial 20 bold',
       fg='#FF0000', bg='#FFFFFF', command=docx_to_pdf)
docx_to_pdf_button.pack(pady=10)

success_label = tk.Label(root, fg="red", bg="gray", font='Arial 20 bold')
success_label.pack(pady=10)

root.mainloop()