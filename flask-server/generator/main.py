# import tkinter as tk
# from tkinter import ttk, Button
import control
control.start_BFSRB()
# window = tk.Tk()
# window.geometry('700x250')
# window.title('Algorithm Selection')

# ttk.Label(window, text="Select an Algorithm :",
#           font=("Times New Roman", 15)).grid(column=0, row=3, padx=10, pady=25)

# n = tk.StringVar()
# alg = ttk.Combobox(window, width=40, textvariable=n)

# alg['values'] = (
#     ' Brute-Force Recursive Backtracking Recursive',
#     ' Genetic Algorithm',
#     ' Monte Carlo Tree Search',
# )

# alg.grid(column=1, row=3)


# def callback():
#     if alg.current() == 0:
#         control.start_BFSRB()
#     elif alg.current() == 1:
#         control.start_geneticAlgorithm()
#     elif alg.current() == 2:
#         control.start_MCTS()
#     window.destroy()


# btn = Button(window, text='Start Algorithm', bd='5', command=callback)

# alg.current(0)
# btn.grid(column=3, row=3)
# window.mainloop()