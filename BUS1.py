import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_total():
   
    distance = entry_distance.get()
    seat_type = seat_type_var.get()
    ac = ac_var.get()
    total_cost = 0.0

    try:
        distance = float(distance)
        total_cost += distance * 10
        
        if seat_type == 2:  
            total_cost += 50  

        if ac == 1:  
            total_cost += 100  
        
        entry_total_cost.delete(0, tk.END)
        entry_total_cost.insert(tk.END, f"Rs. {total_cost:.2f}")
        
        
        sgst = total_cost * 0.09  
        cgst = total_cost * 0.09  
        entry_sgst.delete(0, tk.END)
        entry_sgst.insert(tk.END, f"Rs. {sgst:.2f}")
        entry_cgst.delete(0, tk.END)
        entry_cgst.insert(tk.END, f"Rs. {cgst:.2f}")

    except ValueError:
        entry_total_cost.delete(0, tk.END)
        entry_total_cost.insert(tk.END, "Invalid Input")


def generate_receipt():
    name = entry_name.get()
    mobile = entry_mobile.get()
    email = entry_email.get()
    route = combo_route.get()
    distance = entry_distance.get()
    total_cost = entry_total_cost.get()
    sgst = entry_sgst.get()
    cgst = entry_cgst.get()

    # Create a receipt window
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")
    receipt_window.geometry("400x400")
    receipt_window.config(bg="lightgray")

    receipt_text = f"** Receipt **\n\n"
    receipt_text += f"Name: {name}\n"
    receipt_text += f"Mobile: {mobile}\n"
    receipt_text += f"Email: {email}\n"
    receipt_text += f"Route: {route}\n"
    receipt_text += f"Distance: {distance} KM\n"
    receipt_text += f"SGST: {sgst}\n"
    receipt_text += f"CGST: {cgst}\n"
    receipt_text += f"Total Cost: {total_cost}\n"
    receipt_text += "\nThank you for choosing our service!"

    receipt_label = tk.Label(receipt_window, text=receipt_text, justify=tk.LEFT, padx=10, pady=10, bg="lightgray")
    receipt_label.pack()

# Function to reset the form
def reset_form():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_distance.delete(0, tk.END)
    entry_sgst.delete(0, tk.END)
    entry_cgst.delete(0, tk.END)
    entry_total_cost.delete(0, tk.END)
    combo_route.set('')
    seat_type_var.set(1)
    ac_var.set(0)
    journey_type_var.set(1)
    return_journey_var.set(False)

# Function to update distance based on selected route
def update_distance(event):
    route = combo_route.get()
    if route in routes:
        entry_distance.delete(0, tk.END)
        entry_distance.insert(tk.END, str(routes[route]))

# Sample data for routes
routes = {
    "Route A": 100,
    "Route B": 200,
    "Route C": 300,
}

# Main window setup
root = tk.Tk()
root.title("Bus Booking System")
root.geometry("800x400")
root.config(bg="lightgray")  # Set the main window background color

# Parent Frame for Customer Details, Booking Details, and Charges
frame_parent = tk.Frame(root, bg="lightgray")
frame_parent.pack(pady=10)

# --------- 1. Customer Info Box ---------
frame_customer = tk.LabelFrame(frame_parent, text="Customer Details", padx=10, pady=10, bg="lightgray")
frame_customer.grid(row=0, column=0, padx=10, sticky="nsew")

tk.Label(frame_customer, text="Name", bg="lightgray").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_customer)
entry_name.grid(row=0, column=1)

tk.Label(frame_customer, text="Mobile", bg="lightgray").grid(row=1, column=0, sticky="w")
entry_mobile = tk.Entry(frame_customer)
entry_mobile.grid(row=1, column=1)

tk.Label(frame_customer, text="Email", bg="lightgray").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_customer)
entry_email.grid(row=2, column=1)

# --------- 2. Booking Info Box ---------
frame_booking = tk.LabelFrame(frame_parent, text="Booking Info", padx=10, pady=10, bg="lightgray")
frame_booking.grid(row=0, column=1, padx=10, sticky="nsew")

tk.Label(frame_booking, text="Select Route", bg="lightgray").grid(row=0, column=0, sticky="w")
combo_route = ttk.Combobox(frame_booking, values=list(routes.keys()), state="readonly")
combo_route.grid(row=0, column=1)
combo_route.bind("<<ComboboxSelected>>", update_distance)

tk.Label(frame_booking, text="Distance (KM)", bg="lightgray").grid(row=1, column=0, sticky="w")
entry_distance = tk.Entry(frame_booking)
entry_distance.grid(row=1, column=1)

# Seat Type Selection
tk.Label(frame_booking, text="Seat Type", bg="lightgray").grid(row=2, column=0, sticky="w")
seat_type_var = tk.IntVar(value=1)
tk.Radiobutton(frame_booking, text="Prime", variable=seat_type_var, value=1, bg="lightgray").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_booking, text="VIP", variable=seat_type_var, value=2, bg="lightgray").grid(row=2, column=2, sticky="w")

# AC Option
tk.Label(frame_booking, text="AC", bg="lightgray").grid(row=3, column=0, sticky="w")
ac_var = tk.IntVar(value=0)  # Default: Not selected
tk.Radiobutton(frame_booking, text="Yes", variable=ac_var, value=1, bg="lightgray").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame_booking, text="No", variable=ac_var, value=0, bg="lightgray").grid(row=3, column=2, sticky="w")

# Journey Type Selection
tk.Label(frame_booking, text="Journey Type", bg="lightgray").grid(row=4, column=0, sticky="w")
journey_type_var = tk.IntVar(value=1)  # Default: Single Seat
tk.Radiobutton(frame_booking, text="Single Seat", variable=journey_type_var, value=1, bg="lightgray").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame_booking, text="Double Seat", variable=journey_type_var, value=2, bg="lightgray").grid(row=4, column=2, sticky="w")

# Return Journey Option
tk.Label(frame_booking, text="Return Journey", bg="lightgray").grid(row=5, column=0, sticky="w")
return_journey_var = tk.BooleanVar()
tk.Checkbutton(frame_booking, variable=return_journey_var, bg="lightgray").grid(row=5, column=1, sticky="w")

# --------- 3. Charges Box ---------
frame_details = tk.LabelFrame(frame_parent, text="Charges Details", padx=10, pady=10, bg="lightgray")
frame_details.grid(row=0, column=2, padx=10, sticky="nsew")

tk.Label(frame_details, text="SGST", bg="lightgray").grid(row=0, column=0, sticky="w")
entry_sgst = tk.Entry(frame_details)
entry_sgst.grid(row=0, column=1)
entry_sgst.insert(tk.END, "Rs. 0.00")  # Default SGST value

tk.Label(frame_details, text="CGST", bg="lightgray").grid(row=1, column=0, sticky="w")
entry_cgst = tk.Entry(frame_details)
entry_cgst.grid(row=1, column=1)
entry_cgst.insert(tk.END, "Rs. 0.00")  # Default CGST value

tk.Label(frame_details, text="Total Cost", bg="lightgray").grid(row=2, column=0, sticky="w")
entry_total_cost = tk.Entry(frame_details)
entry_total_cost.grid(row=2, column=1)

# --------- 4. Buttons Box ---------
frame_buttons = tk.Frame(root, bg="lightgray")
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="Calculate", command=calculate_total)
btn_calculate.grid(row=0, column=0, padx=5, pady=5)

btn_receipt = tk.Button(frame_buttons, text="Generate Receipt", command=generate_receipt)
btn_receipt.grid(row=0, column=1, padx=5, pady=5)

btn_reset = tk.Button(frame_buttons, text="Reset", command=reset_form)
btn_reset.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
