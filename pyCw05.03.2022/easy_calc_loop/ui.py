import functools
import tkinter as tk
from. import core


class EasyCalcFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(EasyCalcFrame, self).__init__(*args, **kwargs)

        self.output_text = tk.StringVar()
        self.output = tk.Entry(self, state=tk.DISABLED, textvariable=self.output_text)
        self.output.grid(columnspan=4, row=0)

        lbl_left_number = tk.Label(self)
        lbl_left_number.grid(columnspan=2 , row=1)

        lbl_right_number = tk.Label(self)
        lbl_right_number.grid(column=2, columnspan=2, row=1)

        self.ent_left_number_text = tk.StringVar()  # что бы сразу извлечь данные из строки и не помещать текст в переменную
        self.ent_left_num = tk.Entry(self, textvariable=self.ent_left_number_text)
        self.ent_left_num.grid(columnspan=2, row=2)

        self.ent_right_number_text = tk.StringVar()
        self.ent_right_num = tk.Entry(self, textvariable=self.ent_right_number_text)
        self.ent_right_num.grid(column=2, columnspan=2, row=2)

        button_data= [
            {
                "text": "+",
                "column": 0,
                "fn": core.do_addition

            },
            {
                "text": "-",
                "column": 1,
                "fn": core.do_subtraction

            },
            {
                "text": "*",
                "column": 2,
                "fn": core.do_multiplication

            },
            {
                "text": "-",
                "column": 3,
                "fn": core.do_division

            },

        ]

        def action(op):
            #взятие значений из полей ввода и потом вычисление
            left_value=self.ent_left_number_text.get()
            right_value=self.ent_right_number_text.get()
            #Вычисление
            result = op(left_value, right_value)
            #Вывод результата
            self.output_text.set(result)
            self.ent_left_number_text.set("")
            self.ent_right_number_text.set("")

        for record in button_data:
            btn = tk.Button(self, text = record["text"])
            btn.grid(column=record["column"], row=3)
            btn.configure(
                command=functools.partial(
                    action,
                    record["fn"]
                )
            )





        # btn_plus.configure(
        #     command=lambda: action(
        #         self.ent_left_number_text.get(),
        #         self.ent_right_number_text.get(),
        #         core.do_addition
        #     )
        # )
        #
        # btn_minus.configure(
        #     command=lambda: action(
        #         self.ent_left_number_text.get(),
        #         self.ent_right_number_text.get(),
        #         core.do_subtraction
        #     )
        # )
        #
        # btn_mul.configure(
        #     command=lambda: action(
        #         self.ent_left_number_text.get(),
        #         self.ent_right_number_text.get(),
        #         core.do_multiplication
        #     )
        # )
        #
        # btn_div.configure(
        #     command=lambda: action(
        #         self.ent_left_number_text.get(),
        #         self.ent_right_number_text.get(),
        #         core.do_division
        #     )
        # )

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        easy_calc_frame = EasyCalcFrame(self)
        easy_calc_frame.pack()

    def run(self):
        self.mainloop()


