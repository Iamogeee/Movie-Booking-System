import tkinter as tk

def bookSingle():
    row = int(row_entry.get()) - 1
    col = int(col_entry.get()) - 1
    if cinema[row][col] == 0:
        cinema[row][col] = 1
        status_label.config(text='Seat booked!')
        update_seats()
    else:
        status_label.config(text='Seat already booked!')

def bookBackrow():
    backrow = len(cinema[-1])
    for i in range(backrow):
        if cinema[-1][i] == 0:
            cinema[-1][i] = 1
            status_label.config(text=f'Seat {i+1} in the back row has been booked')
            update_seats()
            return
    status_label.config(text='No empty seats in the back row')

def update_seats():
    for i, row in enumerate(cinema):
        for j, seat in enumerate(row):
            if seat == 1:
                seats[i][j].config(bg='red')
            else:
                seats[i][j].config(bg='green')

cinema = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0]
]

# Create the main window
window = tk.Tk()
window.title("Ticket Purchase Center")

# Create and configure GUI elements
menu_label = tk.Label(window, text="Ticket Purchase Center", font=('Arial', 14))
menu_label.grid(row=0, column=0, columnspan=2, pady=10)

row_label = tk.Label(window, text="Row (1-5): ")
row_label.grid(row=1, column=0)
row_entry = tk.Entry(window)
row_entry.grid(row=1, column=1)

col_label = tk.Label(window, text="Column (1-8): ")
col_label.grid(row=2, column=0)
col_entry = tk.Entry(window)
col_entry.grid(row=2, column=1)

book_single_btn = tk.Button(window, text="Book Single Seat", command=bookSingle)
book_single_btn.grid(row=3, column=0, columnspan=2, pady=5)

book_backrow_btn = tk.Button(window, text="Book Backrow Seat", command=bookBackrow)
book_backrow_btn.grid(row=4, column=0, columnspan=2, pady=5)

status_label = tk.Label(window, text="", font=('Arial', 12))
status_label.grid(row=5, column=0, columnspan=2, pady=10)

seats = []
for row in range(5):
    seat_row = []
    for col in range(8):
        seat = tk.Label(window, text=f'{row+1}-{col+1}', bg='green', width=5, height=2, relief=tk.RAISED)
        seat.grid(row=row+6, column=col, padx=5, pady=5)
        seat_row.append(seat)
    seats.append(seat_row)

update_seats()

# Start the main event loop
window.mainloop()
