# Customer Service Management System
The Customer Service Management System is a web application developed using Flask and MySQL, designed to manage customer information, bookings, and administrative tasks. This system allows users to:

Home Page:

Provides an entry point to navigate to various functionalities of the application.
Signup:

Allows new customers to register by providing their name, contact details, email, address, car number, and package information. This data is stored in the MySQL database.
Package Information:

Displays information about available packages.
Admin Login:

Allows administrators to log in using their credentials. Successful login redirects to the user management page.
User Management:

View Users: List all registered customers.
Edit User: Update customer information.
Remove User: Delete customer records from the database.
Search Users: Find specific customers based on their name.
Booking Management:

Book Slot: Allows customers to book a service slot by providing the slot date, slot time, and car number.
View Bookings: Displays a list of all booked slots.
Database Interaction:

The application uses parameterized queries to prevent SQL injection and ensure data security.
Error Handling and Flash Messages:

Provides feedback to users with flash messages for errors and successful operations.
This system aims to streamline customer service operations, making it easier to manage customer information, handle bookings, and provide an intuitive interface for both customers and administrators.
