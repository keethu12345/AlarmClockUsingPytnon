import tkinter as tk
import pygame

def add_to_display(text):
    entry.insert(tk.END, text)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        clear_display()
        entry.insert(tk.END, str(result))
    except Exception as e:
        clear_display()
        error_description = "Error: " + str(e)
        entry.insert(tk.END, error_description)
        print("Error:", e)
        # Play an error sound
        pygame.mixer.init()
        pygame.mixer.music.load("assets/alarm.mp3")  
        pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for input
entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, command=clear_display, width=5).grid(row=row, column=col)
    elif button == '=':
        tk.Button(root, text=button, command=calculate, width=5).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda text=button: add_to_display(text), width=5).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
