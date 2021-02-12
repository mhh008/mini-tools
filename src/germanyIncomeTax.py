# Calculation of income tax from taxable income for Germany
from tkinter import *


class IncomeTax:

    def __init__(self, master):
        self.Subwindow = Toplevel(master)
        self.Subwindow.title('Einkommensteuer aus zu versteuerndem Einkommen berechnen')

        Label(self.Subwindow, text='Zu versteuerndes Einkommen     ', font=('arial', 10, 'normal')).grid(row=0)
        self.input_zVEk = Entry(self.Subwindow)
        self.input_zVEk.grid(row=0, column=1)
        Label(self.Subwindow, text='EUR', font=('arial', 11, 'normal')).grid(row=0, column=2)

        self.input_zVEk.bind('<Return>', self.keyboard_trigger)

        self.splitting = IntVar()
        Checkbutton(self.Subwindow, text='Zusammenveranlagung', variable=self.splitting).grid(row=2, column=1,
                                                                                              columnspan=2)
        Button(self.Subwindow, text="Berechnen", command=self.call_calc).grid(row=3)

        Label(self.Subwindow, text='Zu zahlende Einkommensteuer:  ', font=('arial', 10, 'normal')).grid(row=4)
        self.output_Est = Entry(self.Subwindow, bg="gray", font=('arial', 11, 'bold'))
        self.output_Est.config(state='disabled')
        self.output_Est.grid(row=4, column=1)
        Label(self.Subwindow, text='EUR', font=('arial', 11, 'normal')).grid(row=4, column=2)

        Label(self.Subwindow, text='Durchschnitssteuersatz:  ', font=('arial', 10, 'normal')).grid(row=5)
        self.output_rate = Entry(self.Subwindow, bg='gray', font=('arial', 11, 'bold'))
        self.output_rate.config(state='disabled')
        self.output_rate.grid(row=5, column=1)
        Label(self.Subwindow, text='%', font=('arial', 11, 'normal')).grid(row=5, column=2)

        print(self.splitting)

    def keyboard_trigger(self, event):
        self.call_calc()

    def call_calc(self):
        zVEk = self.input_zVEk.get()
        zVEk = zVEk.replace(',', '.')
        zVEk = float(zVEk)

        if self.splitting.get() == 0:
            est = IncomeTax.calc_income_tax(zVEk, False)
        else:
            est = IncomeTax.calc_income_tax(zVEk, True)

        rate = IncomeTax.calc_average_tax_rate(zVEk, est) * 100

        self.output_Est.config(state='normal')
        self.output_Est.delete(0, END)
        self.output_Est.insert(0, f'{est:,}'.replace(',', '.'))
        self.output_Est.config(state='disabled')

        self.output_rate.config(state='normal')
        self.output_rate.delete(0, END)
        self.output_rate.insert(0, str('%.2f' % rate).replace('.', ','))
        self.output_rate.config(state='disabled')

    @staticmethod
    def calc_income_tax(taxable_income, assessment):  # Assesment TRUE: Joint assessment (marriage) -> splitting tariff
        taxable_income_round = int(taxable_income)  # Round amount down to the next whole euro; truncate decimal places
        if assessment:
            taxable_income_round = taxable_income_round / 2

        if taxable_income_round <= 9744:
            ekst = 0
        elif 9745 <= taxable_income_round <= 14753:
            y = (taxable_income_round - 9744) / 10000
            ekst = (995.21 * y + 1400) * y
        elif 14754 <= taxable_income_round <= 57918:
            z = (taxable_income_round - 14753) / 10000
            ekst = (208.85 * z + 2397) * z + 950.96
        elif 57919 <= taxable_income_round <= 274612:
            ekst = 0.42 * taxable_income_round - 9136.63
        elif taxable_income_round >= 274613:
            ekst = 0.45 * taxable_income_round - 17374.99

        ekst = int(ekst)  # round down to nest whole euro

        if assessment:
            ekst = 2 * ekst
        print("ekst: %f" % (ekst))
        return ekst

    @staticmethod
    def calc_average_tax_rate(texable_income, to_pay_tax):
        print("texable incom: %f" % (texable_income))
        print("to pay: %f" % (to_pay_tax))
        print(to_pay_tax / texable_income)
        return to_pay_tax / texable_income
