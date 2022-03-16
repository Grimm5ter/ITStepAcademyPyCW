import tkinter as tk


# def start_demo(): Функциональная версия
#
#     root = tk.Tk()
#
#
#
#
#
#     root.mainloop()

class DemoApp(tk.Tk): #Версия через класс
    def __init__(self, *args, **kwargs):
        super(DemoApp, self).__init__(*args, **kwargs)
        self.__lbl = tk.Label(self, text="Слово.")
        self.__lbl.pack()

    def run(self):
        self.mainloop()



if __name__ == '__main__':
    # start_demo()

    app = DemoApp()
    app.run()
