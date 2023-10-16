import tkinter as tk
from tkinter import filedialog
import docx2pdf
import pdf2docx

class DocumentConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер файлов")
        self.root.geometry('720x480')
        self.root.resizable(width=False, height=False)
        self.root['bg'] = '#808080'
        
        self.setup_ui()

    def setup_ui(self):
        self.pdf_to_docx_button = tk.Button(self.root, text="PDF to DOCX", font=('Arial', 20, 'bold'), fg='#FF0000', bg='#FFFFFF', command=self.pdf_to_docx)
        self.pdf_to_docx_button.pack(pady=10)

        self.docx_to_pdf_button = tk.Button(self.root, text="DOCX to PDF", font=('Arial', 20, 'bold'), fg='#FF0000', bg='#FFFFFF', command=self.docx_to_pdf)
        self.docx_to_pdf_button.pack(pady=10)

        self.success_label = tk.Label(self.root, fg="red", bg="gray", font=('Arial', 20, 'bold'))
        self.success_label.pack(pady=10)

    def pdf_to_docx(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            docx_file = file_path[:-4] + ".docx"
            pdf2docx.convert(file_path, docx_file)
            self.success_label.config(text="Конвертация из PDF в DOCX прошла успешно")

    def docx_to_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
        if file_path:
            pdf_file = file_path[:-5] + ".pdf"
            docx2pdf.convert(file_path, pdf_file)
            self.success_label.config(text="Конвертация из DOCX в PDF прошла успешно")

if __name__ == '__main__':
    root = tk.Tk()
    app = DocumentConverter(root)
    root.mainloop()