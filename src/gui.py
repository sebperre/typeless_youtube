from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.overrideredirect(True)

def on_focus_in(e):
    e.widget.config(bg="#4CAF50", fg="white")  # highlight

def on_focus_out(e):
    e.widget.config(bg="SystemButtonFace", fg="black")  # reset

Label(frm, text="Hello World!").grid(column=0, row=0)
Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# # First Row
Q = Button(frm, text="Q", width=2)
Q.grid(column=2, row=3)
W = Button(frm, text="W", width=2)
W.grid(column=3, row=3)
E = Button(frm, text="E", width=2)
E.grid(column=4, row=3)
R = Button(frm, text="R", width=2)
R.grid(column=5, row=3)
T = Button(frm, text="T", width=2)
T.grid(column=6, row=3)
Y = Button(frm, text="Y", width=2)
Y.grid(column=7, row=3)
U = Button(frm, text="U", width=2)
U.grid(column=8, row=3)
I = Button(frm, text="I", width=2)
I.grid(column=9, row=3)
O = Button(frm, text="O", width=2)
O.grid(column=10, row=3)
P = Button(frm, text="P", width=2)
P.grid(column=11, row=3)

# # Second Row
A = Button(frm, text="A", width=2)
A.grid(column=2, row=4)
S = Button(frm, text="S", width=2)
S.grid(column=3, row=4)
D = Button(frm, text="D", width=2)
D.grid(column=4, row=4)
F = Button(frm, text="F", width=2)
F.grid(column=5, row=4)
G = Button(frm, text="G", width=2)
G.grid(column=6, row=4)
H = Button(frm, text="H", width=2)
H.grid(column=7, row=4)
J = Button(frm, text="J", width=2)
J.grid(column=8, row=4)
K = Button(frm, text="K", width=2)
K.grid(column=9, row=4)
L = Button(frm, text="L", width=2)
L.grid(column=10, row=4)

# # Third Row
Z = Button(frm, text="Z", width=2)
Z.grid(column=3, row=5)
X = Button(frm, text="X", width=2)
X.grid(column=4, row=5)
C = Button(frm, text="C", width=2)
C.grid(column=5, row=5)
V = Button(frm, text="V", width=2)
V.grid(column=6, row=5)
B = Button(frm, text="B", width=2)
B.grid(column=7, row=5)
N = Button(frm, text="N", width=2)
N.grid(column=8, row=5)
M = Button(frm, text="M", width=2)
M.grid(column=9, row=5)

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.attributes("-topmost", True)

for btn in [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]:
    btn.bind("<FocusIn>", on_focus_in)
    btn.bind("<FocusOut>", on_focus_out)

Q.focus_set()

root.mainloop()
