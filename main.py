from tkinter import *


class Calculadora:
    def __init__(self):
        self.window = Tk()
        self.window.title('Calculadora')
        self.window.resizable(0, 0)

        self.screen_numerico = Entry(self.window, font='arial 30', bg='#aaaeaf', width=13, fg='#e6e6e6')
        self.screen_numerico.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button_1 = Button(self.frame, bg='#fafafa', bd=1, text='1', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_2 = Button(self.frame, bg='#fafafa', bd=1, text='2', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_3 = Button(self.frame, bg='#fafafa', bd=1, text='3', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_mult = Button(self.frame, bg='#fafafa', bd=1, text='x', font='Arial 20', fg='#dfd476',
                               width=4, height=1, command=None)
        self.button_4 = Button(self.frame, bg='#fafafa', bd=1, text='4', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_5 = Button(self.frame, bg='#fafafa', bd=1, text='5', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_6 = Button(self.frame, bg='#fafafa', bd=1, text='6', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_sub = Button(self.frame, bg='#fafafa', bd=1, text='-', font='Arial 20', fg='#dfd476',
                               width=4, height=1, command=None)
        self.button_7 = Button(self.frame, bg='#fafafa', bd=1, text='7', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_8 = Button(self.frame, bg='#fafafa', bd=1, text='8', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_9 = Button(self.frame, bg='#fafafa', bd=1, text='9', font='Arial 20',
                               width=4, height=1, command=None)
        self.button_adi = Button(self.frame, bg='#fafafa', bd=1, text='+', font='Arial 20', fg='#dfd476',
                               width=4, height=1, command=None)
        self.button_clean = Button(self.frame, bg='#fafafa', bd=1, text='C', font='Arial 20',
                                 width=4, height=1, command=None)
        self.button_0 = Button(self.frame, bg='#fafafa', bd=1, text='0', font='Arial 20',
                                 width=4, height=1, command=None)
        self.button_vir = Button(self.frame, bg='#fafafa', bd=1, text=',', font='Arial 20',
                                 width=4, height=1, command=None)
        self.button_total = Button(self.frame, bg='#fafafa', bd=1, text='=', font='Arial 20', fg='#dfd476',
                                 width=4, height=1, command=None)


        self.button_1.grid(row=0, column=0)
        self.button_2.grid(row=0, column=1)
        self.button_3.grid(row=0, column=2)
        self.button_mult.grid(row=0, column=3)

        self.button_4.grid(row=1, column=0)
        self.button_5.grid(row=1, column=1)
        self.button_6.grid(row=1, column=2)
        self.button_sub.grid(row=1, column=3)

        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_adi.grid(row=2, column=3)

        self.button_clean.grid(row=3, column=0)
        self.button_0.grid(row=3, column=1)
        self.button_vir.grid(row=3, column=2)
        self.button_total.grid(row=3, column=3)




        self.window.mainloop()


Calculadora()
