from cProfile import label
import tkinter
import tkinter.messagebox

def main():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red','Hello,world!')\
            if flag else ('blue','Goodbye,world!')
        label.config(text)