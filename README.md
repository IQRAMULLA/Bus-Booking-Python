This Python script implements a Bus Booking System using the tkinter library. The application is a GUI-based tool that helps users calculate travel costs, generate receipts, and manage booking details.

Key Features
Customer Details:

Allows users to input their name, mobile number, and email.
Booking Information:

Select a route from a dropdown menu.
Automatically updates the travel distance based on the selected route.
Options to choose:
Seat Type (Prime or VIP)
AC (Yes or No)
Journey Type (Single or Double Seat)
Return Journey (Checkbox)
Dynamic Cost Calculation:

Calculates the total cost based on the following:
Distance traveled.
Additional charges for VIP seats.
Additional charges for AC services.
Applies SGST (9%) and CGST (9%) on the calculated cost.
Receipt Generation:

Creates a detailed receipt in a new window, including all booking details, total cost, and applicable taxes.
Reset Functionality:

Clears all input fields, returning the form to its default state.
GUI Layout
Customer Details Section:

Collects personal information (Name, Mobile, Email).
Booking Information Section:

Allows selection of the route, seat type, AC option, journey type, and return journey.
Displays the corresponding distance for the selected route.
Charges Details Section:

Displays SGST, CGST, and the total cost.
Buttons Section:

Calculate: Computes the total cost with taxes.
Generate Receipt: Opens a new window with a printable receipt.
Reset: Clears all fields.
Functional Highlights
Dynamic Distance Update:

The update_distance() function updates the travel distance when a route is selected.
Cost Calculation:

The calculate_total() function calculates:
Base fare: Distance (in KM) × ₹10.
Additional charges:
VIP seat: ₹50.
AC service: ₹100.
Taxes: SGST and CGST at 9% each.
Receipt Generation:

The generate_receipt() function creates a receipt in a separate window, summarizing all the booking details.
Reset Functionality:

The reset_form() function resets all input fields and options to their default state.
Technologies Used
Python
tkinter for GUI.
ttk for dropdown menus and enhanced widgets.
Example Scenarios
A user books a 200 KM journey (Route B) with:
VIP seat and AC service.
The total cost is calculated, including applicable SGST and CGST.
A detailed receipt is generated for the booking.
This application demonstrates a user-friendly booking system, ideal for small-scale transportation services or as a learning project to master GUI development with Python.
