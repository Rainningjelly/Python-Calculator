import tkinter as tk



window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="#2C1810")

expression = ""



display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="#F5EBDD",
    fg="#2C1810",
    insertbackground="#2C1810",
    justify="right",
    bd=0
)

display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)



def validate_input(event):
    allowed_chars = "0123456789+-*/."

    if event.keysym in (
        "BackSpace",
        "Delete",
        "Left",
        "Right",
        "Home",
        "End",
        "Tab"
    ):
        return

    if event.char and event.char not in allowed_chars:
        return "break"


def sync_expression(event=None):
    global expression
    expression = display.get()


def button_click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(0, expression)


def clear():
    global expression

    expression = ""
    display.delete(0, tk.END)


def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, tk.END)
    display.insert(0, expression)


def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

        expression = str(result)

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "ERROR")

        expression = ""




display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)



buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

button_frame = tk.Frame(
    window,
    bg="#3B2417"
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)



clear_button = tk.Button(
    button_frame,
    text="C",
    font=("poppins semibold", 18, "bold"),
    bg="#A47148",
    fg="#FFF8EC",
    bd=0,
    activebackground="#B88965",
    activeforeground="#FFF8EC",
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)



backspace_button = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 18, "bold"),
    bg="#D8C3A5",
    fg="#2C1810",
    bd=0,
    activebackground="#E7D7BF",
    activeforeground="#2C1810",
    command=backspace
)

backspace_button.grid(
    row=0,
    column=2,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)



for row_index, row in enumerate(buttons, start=1):

    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = "#C66B3D"

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#B08968"

        else:
            command = lambda v=value: button_click(v)
            color = "#5C4033"

        button = tk.Button(
            button_frame,
            text=value,
            font=("quicksand medium", 18, "bold"),
            bg=color,
            fg="#FFF8EC",
            bd=0,
            activebackground=color,
            activeforeground="#FFF8EC",
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )



for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)



window.mainloop()