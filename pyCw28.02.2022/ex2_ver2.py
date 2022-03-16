import tkinter as tk


def start_demo():

    root = tk.Tk()
    lbl = tk.Label(root, text="Слово.")
    lbl.pack()





    root.mainloop()

# class DemoApp(tk.Tk): #Версия через класс
#     def __init__(self, *args, **kwargs):
#         super(DemoApp, self).__init__(*args, **kwargs)
#
#     def run(self):
#         self.mainloop()



if __name__ == '__main__':
    start_demo()

    # app = DemoApp()
    # app.run()
