import tkinter as tk 

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#00ace6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

input = tk.Entry(frame, font=40)
input.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Test Button', font=40 )
button.place(relx=0.7, relwidth=0.3, relheight=1)

result_frame = tk.Frame(root, bg='#00ace6', bd=10)
result_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tk.Label(frame, text='Weather App')
# label.pack()

root.mainloop()
