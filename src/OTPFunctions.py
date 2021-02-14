from tkinter import filedialog, simpledialog, Button, Toplevel, Label, Entry, END, ttk, HORIZONTAL
import os


class OTPFunctions:

    def __init__(self, master):
        self.origFile = ""
        self.hideFile = ""

        self.decDirec = ""
        self.decHide = ""
        self.decKey = ""

        self.encOTP = ""

        self.decOTP = ""
        self.decOTPKey = ""

        self.Subwindow = Toplevel(master)
        self.Subwindow.title('OTP Dateiverschlüsselung')

        # Part hiding file behind other
        Label(self.Subwindow, text='Datei hinter einer anderen mit Key File verstecken',
              font=('arial', 12, 'normal')).grid(row=0, columnspan=3)

        Label(self.Subwindow, text='Originaldatei auswählen: ', font=('arial', 10, 'normal')).grid(row=1, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_origFile_behind).grid(row=1, column=1)
        self.selected_origFile_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_origFile_show.grid(row=1, column=2)
        self.selected_origFile_show.config(state='disable')

        Label(self.Subwindow, text='Datei hinter der versteck werden soll: ', font=('arial', 10, 'normal')).grid(row=2,
                                                                                                                 column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_hideFile_behind).grid(row=2, column=1)
        self.selected_hideFile_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_hideFile_show.grid(row=2, column=2)
        self.selected_hideFile_show.config(state='disable')

        Button(self.Subwindow, text='Datei verstecken', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.hide_file_behind).grid(row=3, columnspan=3)

        # Space
        Label(self.Subwindow, text="").grid(row=4)
        ttk.Separator(self.Subwindow, orient=HORIZONTAL).grid(row=5, columnspan=3, sticky='ew')
        Label(self.Subwindow, text="").grid(row=6)

        # Restore hidden file
        Label(self.Subwindow, text='Versteckte Datei mit Key File wiederherstellen',
              font=('arial', 12, 'normal')).grid(row=7, columnspan=3)

        Label(self.Subwindow, text='Zielordner für entschlüsselte Datei: ', font=('arial', 10, 'normal')).grid(row=8,
                                                                                                               column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_decDirec_behind).grid(row=8, column=1)
        self.selected_decDirec_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_decDirec_show.grid(row=8, column=2)
        self.selected_decDirec_show.config(state='disable')

        Label(self.Subwindow, text='Datei hinter der versteckt wurde: ', font=('arial', 10, 'normal')).grid(row=9,
                                                                                                            column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_decHide_behind).grid(row=9, column=1)
        self.selected_decHide_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_decHide_show.grid(row=9, column=2)
        self.selected_decHide_show.config(state='disable')

        Label(self.Subwindow, text='Schlüssel Datei (key): ', font=('arial', 10, 'normal')).grid(row=10, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_decKey_behind).grid(row=10, column=1)
        self.selected_decKey_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_decKey_show.grid(row=10, column=2)
        self.selected_decKey_show.config(state='disable')

        Button(self.Subwindow, text='Datei wiederherstellen', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.dec_file_behind).grid(row=11, columnspan=3)

        # Space
        Label(self.Subwindow, text="").grid(row=12)
        ttk.Separator(self.Subwindow, orient=HORIZONTAL).grid(row=13, columnspan=3, sticky='ew')
        Label(self.Subwindow, text="").grid(row=14)

        # encrypt file with OTP
        Label(self.Subwindow, text='Datei durch OTP (One-Time-Pad) Key Datei verschlüsseln',
              font=('arial', 12, 'normal')).grid(row=15, columnspan=3)

        Label(self.Subwindow, text='Zu verschlüsselnde Datei: ', font=('arial', 10, 'normal')).grid(row=16, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_enc_otp).grid(row=16, column=1)
        self.selected_encOTP_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_encOTP_show.grid(row=16, column=2)
        self.selected_encOTP_show.config(state='disable')

        Button(self.Subwindow, text='Datei verschlüsseln', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.enc_file_otp).grid(row=17, columnspan=3)

        # Space
        Label(self.Subwindow, text="").grid(row=18)
        ttk.Separator(self.Subwindow, orient=HORIZONTAL).grid(row=19, columnspan=3, sticky='ew')
        Label(self.Subwindow, text="").grid(row=20)

        # decrypt file with OTP key
        Label(self.Subwindow, text='Durch OTP verschlüsselte Datei entschlüsseln',
              font=('arial', 12, 'normal')).grid(row=21, columnspan=3)

        Label(self.Subwindow, text='Verschlüsselte Datei: ', font=('arial', 10, 'normal')).grid(row=22, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_dec_otp).grid(row=22, column=1)
        self.selected_decOTP_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_decOTP_show.grid(row=22, column=2)
        self.selected_decOTP_show.config(state='disable')

        Label(self.Subwindow, text='Key datei: ', font=('arial', 10, 'normal')).grid(row=23, column=0)
        Button(self.Subwindow, text='Dateiauswahl', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.select_key_otp).grid(row=23, column=1)
        self.selected_decOTPKey_show = Entry(self.Subwindow, bg="gray", font=('arial', 10, 'normal'))
        self.selected_decOTPKey_show.grid(row=23, column=2)
        self.selected_decOTPKey_show.config(state='disable')

        Button(self.Subwindow, text='Datei entschlüsseln', bg='#F0F8FF', font=('arial', 10, 'normal'),
               command=self.dec_file_otp).grid(row=24,
                                               columnspan=3)

        # Space
        Label(self.Subwindow, text="").grid(row=25)

    def select_origFile_behind(self):
        original_path = filedialog.askopenfilename(parent=self.Subwindow, title='Originaldateiauswählen')
        self.origFile = original_path

        self.selected_origFile_show.config(state='normal')
        self.selected_origFile_show.delete(0, END)
        self.selected_origFile_show.insert(0, original_path.split('/')[len(original_path.split('/')) - 1])
        self.selected_origFile_show.config(state='disabled')

    def select_hideFile_behind(self):
        hide_path = filedialog.askopenfilename(parent=self.Subwindow, title='Datei hinter der versteck werden soll')
        self.hideFile = hide_path

        self.selected_hideFile_show.config(state='normal')
        self.selected_hideFile_show.delete(0, END)
        self.selected_hideFile_show.insert(0, hide_path.split('/')[len(hide_path.split('/')) - 1])
        self.selected_hideFile_show.config(state='disabled')

    def hide_file_behind(self):
        if (self.origFile == "") or (self.hideFile == ""):
            simpledialog.messagebox.showwarning(title='Hinweis', message='Die Dateiauswahl muss erfolgt sein')
            return

        OTPFunctions.equalize(self.origFile, self.hideFile)
        original = open(self.origFile, 'rb').read()
        encrypted = open(self.hideFile, 'rb').read()
        key_path = self.origFile + '.enc.key'
        key = bytes(a ^ b for (a, b) in zip(original, encrypted))
        with open(key_path, 'wb') as key_out:
            key_out.write(key)

        simpledialog.messagebox.showinfo(title='Information', message='Datei versteckt und Schlüssel erstellt unter:\n'
                                                                      + key_path + '\n\nDie Originaldatei ggf. löschen')

    def select_decDirec_behind(self):
        direc = filedialog.askdirectory(parent=self.Subwindow, title='Ordner für Entschlüsselte Datei')
        self.decDirec = direc

        self.selected_decDirec_show.config(state='normal')
        self.selected_decDirec_show.delete(0, END)
        self.selected_decDirec_show.insert(0, direc.split('/')[len(direc.split('/')) - 1])
        self.selected_decDirec_show.config(state='disabled')

    def select_decHide_behind(self):
        file = filedialog.askopenfilename(parent=self.Subwindow, title='Datei hinter der versteckt wurde auswählen')
        self.decHide = file

        self.selected_decHide_show.config(state='normal')
        self.selected_decHide_show.delete(0, END)
        self.selected_decHide_show.insert(0, file.split('/')[len(file.split('/')) - 1])
        self.selected_decHide_show.config(state='disabled')

    def select_decKey_behind(self):
        key = filedialog.askopenfilename(parent=self.Subwindow, title='Key Datei auswählen')
        self.decKey = key

        self.selected_decKey_show.config(state='normal')
        self.selected_decKey_show.delete(0, END)
        self.selected_decKey_show.insert(0, key.split('/')[len(key.split('/')) - 1])
        self.selected_decKey_show.config(state='disabled')

    def dec_file_behind(self):
        if (self.decDirec == '') or (self.decHide == '') or (self.decKey == ''):
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es müssen Dateien ausgewählt sein.')
            return

        decrypted_path = self.decDirec + '/' + self.decKey.split('/')[len(self.decKey.split('/')) - 1][:-8]

        encrypted = open(self.decHide, 'rb').read()
        key = open(self.decKey, 'rb').read()
        decrypted = bytes(a ^ b for (a, b) in zip(encrypted, key))
        with open(decrypted_path, 'wb') as decrypted_out:
            decrypted_out.write(decrypted)

        simpledialog.messagebox.showinfo(title='Information', message='Datei entschlüsselt und gespeichert:\n\n'
                                                                      + decrypted_path)

    def select_enc_otp(self):
        file = filedialog.askopenfilename(parent=self.Subwindow, title='Zu verschlüsselnde Datei auswählen')
        self.encOTP = file

        self.selected_encOTP_show.config(state='normal')
        self.selected_encOTP_show.delete(0, END)
        self.selected_encOTP_show.insert(0, file.split('/')[len(file.split('/')) - 1])
        self.selected_encOTP_show.config(state='disabled')

    def enc_file_otp(self):
        if self.encOTP == '':
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es muss eine Datei ausgewählt sein.')
            return

        original = open(self.encOTP, 'rb').read()
        key = os.urandom(len(original))
        encrypted = bytes(a ^ b for (a, b) in zip(original, key))

        encrypted_path = self.encOTP + '.enc'
        key_path = self.encOTP + '.enc.key'

        with open(key_path, 'wb') as key_out:
            key_out.write(key)

        with open(encrypted_path, 'wb') as encrypted_out:
            encrypted_out.write(encrypted)

        simpledialog.messagebox.showinfo(title='Information',
                                         message='Datei verschlüsselt und gespeichert:\n\n %s \n\n Schlüsseldatei: '
                                                 '\n\n %s \n\nDie Originaldatei ggf. löschen' % (
                                                     encrypted_path, key_path))

    def select_dec_otp(self):
        file = filedialog.askopenfilename(parent=self.Subwindow, title='Zu entschlüsselnde Datei auswählen')
        self.decOTP = file

        self.selected_decOTP_show.config(state='normal')
        self.selected_decOTP_show.delete(0, END)
        self.selected_decOTP_show.insert(0, file.split('/')[len(file.split('/')) - 1])
        self.selected_decOTP_show.config(state='disabled')

    def select_key_otp(self):
        file = filedialog.askopenfilename(parent=self.Subwindow, title='Schlüssel (Key) Datei auswählen')
        self.decOTPKey = file

        self.selected_decOTPKey_show.config(state='normal')
        self.selected_decOTPKey_show.delete(0, END)
        self.selected_decOTPKey_show.insert(0, file.split('/')[len(file.split('/')) - 1])
        self.selected_decOTPKey_show.config(state='disabled')

    def dec_file_otp(self):
        if (self.decOTP == '') or (self.decOTPKey == ''):
            simpledialog.messagebox.showwarning(title='Hinweis', message='Es müssen Dateien ausgewählt sein.')
            return

        key_path = self.decOTPKey
        to_decrypt_path = self.decOTP

        key = open(key_path, 'rb').read()
        encrypted = open(to_decrypt_path, 'rb').read()
        decrypted = bytes(a ^ b for (a, b) in zip(key, encrypted))

        with open(to_decrypt_path[:-4], 'wb') as decrypted_out:
            decrypted_out.write(decrypted)

        simpledialog.messagebox.showinfo(title='Information',
                                         message='Datei entschlüsselt und gespeichert: \n\n%s' % (to_decrypt_path[:-4]))

    @staticmethod
    def equalize(path_1, path_2):
        data1 = open(path_1, "rb").read()  # read file path_1 in byte mode
        data2 = open(path_2, "rb").read()  # read file path_2 in byte mode
        len_data1 = len(data1)  # measure length of file1
        len_data2 = len(data2)  # measure lenth of file2
        if len_data1 > len_data2:  # If file1 is longer then file 2, add random bytes to file1
            data2 += os.urandom(len_data1 - len_data2)
        else:  # Else add random bytes to file2
            data1 += os.urandom(len_data2 - len_data1)
        with open(path_2, "wb") as out:
            out.write(data2)
        with open(path_1, "wb") as out:
            out.write(data1)
