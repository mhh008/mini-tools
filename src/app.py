import tkinter as tk

from src.Nato import Nato
from src.functionsWithPdfs import PDFFunctions
from src.OTPFunctions import OTPFunctions
from src.germanyIncomeTax import IncomeTax


class App(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.buttonNATO = tk.Button(self, text="NATO Alphabet buchstabieren",
                                    font=('arial', 10, 'normal'), command=self.create_nato_Window)
        self.buttonNATO.pack(side="top")

        self.buttonPDF = tk.Button(self, text='PDF Dateien zusammenfügen, mit Passwort schützen',
                                   font=('arial', 10, 'normal'), command=self.create_pdf_Window)
        self.buttonPDF.pack(side='top')

        self.buttonPDF = tk.Button(self, text='Dateiverschlüsselung mit OTP (One-Time-Pad)',
                                   font=('arial', 10, 'normal'), command=self.create_otp_Window)
        self.buttonPDF.pack(side='top')

        self.buttonPDF = tk.Button(self, text='Einkommensteuer aus zu versteuerendem Einkommen berechnen',
                                   font=('arial', 10, 'normal'), command=self.create_tax_Window)
        self.buttonPDF.pack(side='top')

    def create_nato_Window(self):
        Nato(self)

    def create_pdf_Window(self):
        PDFFunctions(self)

    def create_otp_Window(self):
        OTPFunctions(self)

    def create_tax_Window(self):
        IncomeTax(self)


def gui():
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
