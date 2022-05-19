import random
from tkinter import *


class Passgen:
    length = 20
    numbers = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = ',;.:!?()/\\-_•'
    password = ''

    def __init__(self, length=None):
        self.length = length

    def length(self, length):
        self.length = length

    def new(self):
        for x in range(self.length):
            rnd = random.randint(1, 7)
            if rnd == 1 or rnd == 2:
                self.password += random.choice(self.lowercase_letters)
            elif rnd == 3 or rnd == 4:
                self.password += random.choice(self.uppercase_letters)
            elif rnd == 5 or rnd == 6:
                self.password += random.choice(self.numbers)
            elif rnd == 7:
                self.password += random.choice(self.special_characters)

        return self

    def get_password(self):
        return Password(self.password)


class Password:
    def __init__(self, password):
        self.password = password

    def get_string(self):
        return self.password

    def copy_to_clipboard(self):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.password)
        r.update()
        r.destroy()
