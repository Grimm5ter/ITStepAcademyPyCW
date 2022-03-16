import tkinter as tk


def start_demo():

    root = tk.Tk()
    lbl = tk.Label(root, text="Слово.")
    lbl.grid(columnspan=3, row=0)

    def create_triple_button_frame(base):
        frame = tk.Frame(base)
        btn1 = tk.Button(frame, text="КнопкаA")
        btn1.pack()
        btn2 = tk.Button(frame, text="КнопкаB")
        btn2.pack()
        btn3 = tk.Button(frame, text="КнопкаC")
        btn3.pack()
        return frame

    frame1 = create_triple_button_frame(root)
    frame1.grid(column=1, row=1)
    frame2 = create_triple_button_frame(root)
    frame2.grid(column=2, row=1)
    frame3 = create_triple_button_frame(root)
    frame3.grid(column=3, row=1)



    root.mainloop()

class DemoApp(tk.Tk): #Версия через класс
    def __init__(self, *args, **kwargs):
        super(DemoApp, self).__init__(*args, **kwargs)
        self.__lbl = tk.Label(self, text="Слово.")
        self.__lbl.grid(columnspan=3, row=0) #Раньше был pack()
        self.frame1 = TripleButton()
        self.frame1.grid(column=1, row=1)





    def run(self):
        self.mainloop()

class TripleButton(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(TripleButton, self).__init__(*args, **kwargs)
        #self.frame = tk.Frame() self == tk.Frame
        self.button1 = tk.Button(self, text="КнопкаA")
        self.button1.pack()
        self.button2 = tk.Button(self, text="КнопкаВ")
        self.button2.pack()
        self.button3 = tk.Button(self, text="КнопкаС")
        self.button3.pack()







if __name__ == '__main__':
    start_demo()

    # app = DemoApp()
    # app.run()
