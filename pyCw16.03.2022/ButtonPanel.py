import tkinter as tk



class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)


        self.enter_string = Enter(self)
        self.enter_string.grid(column=1, row=0)

        self.buttons = MinusPlusButtonFrame(self)
        self.buttons.grid(column=1, row=1)

        self.enter_string = Enter(self)
        self.enter_string.grid(column=3, row=0)

        self.buttons = MinusPlusButtonFrame(self)
        self.buttons.grid(column=3, row=0)

        self.enter_string = Enter(self)
        self.enter_string.grid(column=5, row=0)

        self.buttons = MinusPlusButtonFrame(self)
        self.buttons.grid(column=4, row=0)

        self.buttons = MinusPlusButtonFrame(self)
        self.buttons.grid(column=1, row=3)



class MinusPlusButtonFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(MinusPlusButtonFrame, self).__init__(*args, **kwargs)

        self.configure(padx=20, pady=20, bg="#ccc")

        self.btn_plus = tk.Button(self, text="+")
        self.btn_plus.grid(column=1, row=0)

        self.btn_minus = tk.Button(self, text="-")
        self.btn_minus.grid(column=3, row=0)

        self.info = tk.Label(self, bg="white")
        self.info.grid(column=2, columnspan=4, row=3)



class Enter(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Enter, self).__init__(*args, **kwargs)

        self.output_text = tk.StringVar()
        self.entry = tk.Entry(self, justify="center", textvariable=self.output_text)
        self.entry.grid(columnspan=2)




