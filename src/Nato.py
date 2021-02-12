from tkinter import *


class Nato:
    # NATO alphapet siehe: https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
    CONST_LETTERS = ['a', 'ä', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r',
                     's', 'ß', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    CONST_WORDS = ['alpha', 'alpha umlaut', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india',
                   'juliett', 'kilo', 'lima', 'mike', 'november', 'oscar', 'oscar umlaut', 'papa', 'quebec', 'romeo',
                   'sierra', 'eszett', 'tango', 'uniform', 'uniform umlaut', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu',
                   'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Dash']

    def __init__(self, master):
        self.Subwindow = Toplevel(master)
        self.Subwindow.title("NATO Alphabet buchstabieren")
        self.Subwindow.geometry('400x400')

        Label(self.Subwindow, text="This eingeben:").pack(fill="both")

        # User input
        self.inputText1 = Text(self.Subwindow, height=10)
        self.inputText1.pack()
        self.inputText1.bind('<Return>', self.keyboard_trigger)
        self.inputText1.bind('<space>', self.keyboard_trigger)

        # Button to trigger manuelly
        Button(self.Subwindow, text="bestätigen", font=('arial', 10, 'normal'), bg='#F0F8FF',
               command=self.trigger_nato).pack()

        # Output with nato alphabet
        self.outputText1 = Text(self.Subwindow, height=10)
        self.outputText1.config(state='disabled')
        self.outputText1.pack()

    def keyboard_trigger(self, event):
        self.trigger_nato()

    def trigger_nato(self):
        userInput = self.inputText1.get('1.0', END)
        result_list = Nato.nato(userInput)
        result_text = ""
        for word in result_list:
            result_text = result_text + " " + word

        self.outputText1.config(state='normal')
        self.outputText1.delete('1.0', END)
        self.outputText1.insert('1.0', result_text)
        self.outputText1.config(state='disabled')

    @staticmethod
    def nato(user_input):
        user_input_list = list(user_input)
        result = list()
        for tile in user_input_list:
            result.append(Nato.find_word(tile))
        return result

    @staticmethod
    def find_word(letter):
        if (letter == ".") or (letter == '\n') or (letter == '?') or (letter == '!') or (letter == ',') or (
                letter == ':'):
            return letter
        for item in zip(Nato.CONST_LETTERS, Nato.CONST_WORDS):
            if item[0] == letter:  # letter is lowercase or number
                return item[1]
            elif item[0] == letter.lower():  # letter is uppercase
                return item[1].capitalize()
        return ' '
