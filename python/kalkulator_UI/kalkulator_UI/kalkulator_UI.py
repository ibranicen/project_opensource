import tkinter as tk
import math

def press_button(value):
    input_usr = input_user.get()
    input_user.delete(0, tk.END)
    input_user.insert(0, input_usr + str(value))

def result():
    try:
        current_input = input_user.get()

        if current_input.startswith("√"):
            index_input = current_input[1:]
            num = float(index_input)

            if num < 0:
                raise ValueError
            
            hasil = math.sqrt(num)

        elif "^" in current_input:
            real_operation = current_input.replace("^", "**")
            hasil = eval(real_operation)    

        else:
            hasil = eval(current_input)

        input_user.delete(0, tk.END)
        input_user.insert(0, str(hasil))

    except:
        input_user.delete(0, tk.END)
        input_user.insert(0, "ERROR")    

def clear():
    input_user.delete(0, tk.END)

app = tk.Tk()
app.title("KALKULATOR PRIBADI IBRANI")
app.config(bg="pink")
app.resizable(False,False)
app.geometry("325x450")

input_user = tk.Entry(app, width=16, font=('Arial', 24), borderwidth=5, justify='right')
input_user.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','√','^','+',
    'C','=','.'
]

line = 1
column = 0

for i in button:
    if i == "=":
        cmd = result
    elif i == "C":
        cmd = clear
    elif i == "√":
        cmd = lambda : press_button("√")
    elif i == "^":
        cmd = lambda : press_button("^")
    else:
        cmd = lambda x = i : press_button(x)        

    tk.Button(app, width=5, height=2, text=i, font=('Arial', 16), command=cmd).grid(row=line, column=column, padx=5, pady=5)

    column +=1
    if column > 3:
        column = 0
        line +=1

app.mainloop()