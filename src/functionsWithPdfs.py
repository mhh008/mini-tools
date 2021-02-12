from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog, Button, Label, END, Toplevel, Entry, simpledialog, ttk, HORIZONTAL
import os.path


class PDFFunctions:

    timer_id = None

    def __init__(self, master):
        self.merge_pdf_files = ""
        self.merge_dest_directory = ""

        self.password_pdf_file = ""

        self.Subwindow = Toplevel(master)
        self.Subwindow.title('PDF Funktionen')
        self.Subwindow.geometry('400x400')

        Label(self.Subwindow, text='Mehrere PDF Dateien zusammenführen', font=('arial', 12, 'normal')).grid(row=0,
                                                                                                            columnspan=3)

        # Select Files for merging
        Label(self.Subwindow, text='PDF\'s auswählen: ', font=('arial', 10, 'normal')).grid(row=1, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_files_merge).grid(row=1, column=1)
        self.selected_files_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_files_show.config(state='disable')
        self.selected_files_show.grid(row=1, column=2)

        # Select Folder vor merging destination
        Label(self.Subwindow, text='Zielordner auswählen: ', font=('arial', 10, 'normal')).grid(row=2, column=0)
        Button(self.Subwindow, text='Orderauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_directory_merge).grid(row=2, column=1)
        self.selected_direc_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_direc_show.config(state='disable')
        self.selected_direc_show.grid(row=2, column=2)

        # Get Name for merged file
        Label(self.Subwindow, text='Name für die neue Datei: ', font=('arial', 10, 'normal')).grid(row=3, column=0)
        self.merge_file_name = Entry(self.Subwindow, font=('arial', 10, 'normal'))
        self.merge_file_name.grid(row=3, column=2)

        Button(self.Subwindow, text='Dateien zusammenfügen', bg='#F0F8FF', font=('arial', 10, 'normal'), command=self.merge_pdfs_a).grid(row=4, columnspan=3)

        # Space
        Label(self.Subwindow, text="").grid(row=5)
        ttk.Separator(self.Subwindow, orient=HORIZONTAL).grid(row=6, columnspan=3, sticky='ew')
        Label(self.Subwindow, text="").grid(row=7)

        # PDF with password
        Label(self.Subwindow, text='PDF mit Passwort schützen', font=('arial', 12, 'normal')).grid(row=8, columnspan=3)

        # Select file
        Label(self.Subwindow, text='PDF auswählen: ', font=('arial', 10, 'normal')).grid(row=9, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_file_password).grid(row=9, column=1)
        self.selected_file_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_file_show.config(state='disable')
        self.selected_file_show.grid(row=9, column=2)

        # Enter Password1
        Label(self.Subwindow, text='Passwort wählen: ', font=('arial', 10, 'normal')).grid(row=10, column=0)
        self.enter_pwd_1 = Entry(self.Subwindow, font=('arial', 10, 'normal'))
        self.enter_pwd_1.grid(row=10, column=2)

        # Enter Password2
        Label(self.Subwindow, text='Passwort wiederholen: ', font=('arial', 10, 'normal')).grid(row=11, column=0)
        self.enter_pwd_2 = Entry(self.Subwindow, font=('arial', 10, 'normal'), show='*')
        self.enter_pwd_2.grid(row=11, column=2)

        #Button
        Button(self.Subwindow, text='Bestätigen', bg='#F0F8FF', font=('arial', 10, 'normal'), command=self.password_pdf_safe).grid(row=12, column=1)

    def select_files_merge(self):
        files = filedialog.askopenfilenames(parent=self.Subwindow, title='Dateiauswählen',
                                            filetypes=[('pdf file', '.pdf')])
        self.merge_pdf_files = list(files)

        self.selected_files_show.config(state='normal')
        self.selected_files_show.delete(0, END)

        files_show = ""
        for item in files:
            files_show = files_show + item.split('/')[len(item.split('/')) - 1] + ", "

        files_show = files_show[:-2]

        self.selected_files_show.insert(0, files_show)
        self.selected_files_show.config(state='disabled')

    def select_directory_merge(self):
        directory = filedialog.askdirectory(parent=self.Subwindow, title='Zielordner auswählen')
        self.merge_dest_directory = directory

        self.selected_direc_show.config(state='normal')
        self.selected_direc_show.delete(0, END)
        self.selected_direc_show.insert(0, directory)
        self.selected_direc_show.config(state='disabled')

    def select_file_password(self):
        file = filedialog.askopenfilename(parent=self.Subwindow, title="Dateiauswahl", filetypes=[('pdf file', '.pdf')])
        self.password_pdf_file = file

        self.selected_file_show.config(state='normal')
        self.selected_file_show.delete(0, END)
        self.selected_file_show.insert(0, file.split('/')[len(file.split('/')) - 1])
        self.selected_file_show.config(state='disabled')

    def check_pwds(self):
        if self.enter_pwd_1.get() == self.enter_pwd_2.get():
            return True
        else:
            return False

    def merge_pdfs_a(self):
        if self.merge_pdf_files == "":
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es müssen Dateien ausgewählt sein')
            return
        if self.merge_dest_directory == "":
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es muss ein Zielordner ausgewählt sein')
            return
        if self.merge_file_name.get() == "":
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es muss ein Dateiname eingegeben sein')
            return

        merged_path = self.merge_dest_directory + '/' + self.merge_file_name.get() + '.pdf'
        PDFFunctions.merge_pdfs(merged_path, self.merge_pdf_files)
        simpledialog.messagebox.showinfo(title="Information", message="PDFs zussammengefügt und an "
                                                                      "folgendem Ort gespeichert:\n" + merged_path)

    def password_pdf_safe(self):
        if self.password_pdf_file == "":
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es muss eine Datei ausgewählt sein')
            return
        if not (self.check_pwds()):
            simpledialog.messagebox.showwarning(title='Hinweis',
                                                message='Die Passwörter müssen übereinstimmen.\nBitte erneut eingeben')
            self.enter_pwd_1.delete(0, END)
            self.enter_pwd_2.delete(0, END)
            return

        enc_path = PDFFunctions.password_pdf(self.password_pdf_file, self.enter_pwd_1.get())
        simpledialog.messagebox.showinfo(title='Information',
                                         message='PDF Datei durch Passwort geschützt und an folgendem Ort gespeichert:\n\n' + enc_path + '\n\nVergessen Sie nicht die urspürngliche Datei gegebenenfalls zu löschen')
        return

    @staticmethod
    def password_pdf(file_path, password):
        print('drin')
        pdf_reader = PdfFileReader(file_path)
        pdf_writer = PdfFileWriter()

        for page in range(pdf_reader.getNumPages()):
            print('1')
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, use_128bit=True)

        encrypted_path = file_path[:-4] + ".encrypted.pdf"
        num = 1
        while True:
            print('2')
            if os.path.isfile(encrypted_path):  # if file already exists chage name
                encrypted_path = file_path[:-4] + "(" + str(num) + ")" + ".encrypted.pdf"
                num = num + 1
            else:  # file does not exists, so go on
                break

        with open(encrypted_path, "wb") as out:
            pdf_writer.write(out)

        return encrypted_path

    @staticmethod
    def merge_pdfs(result_path, file_list):
        pdf_writer = PdfFileWriter()

        for file in file_list:
            pdf_reader = PdfFileReader(file)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        with open(result_path, 'wb') as out:
            pdf_writer.write(out)
