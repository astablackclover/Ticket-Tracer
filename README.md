A simple Ticket Management System built using Flask, where users can submit support tickets and administrators can view and respond to them.

**Features**
**User and Admin Authentication**: Users and admins can log in with predefined credentials.
**Ticket Submission**: Users can submit tickets detailing their issue, including user ID, department, and description of the problem.
**Admin Dashboard**: Admins can view all submitted tickets and respond to them.
**Session Management**: User sessions are managed securely, and different user types (admin and regular user) are directed to appropriate pages.
**Ticket Notification**: Users are notified when their tickets are responded to by an admin.

**Project Structure**
**app.py**: Main Flask application handling routes, login, and ticket management.
**templates**: Contains the HTML templates for login, ticket submission, and admin dashboard.
**login.html**: Login page for both users and admins.
**ticket.html**: Ticket submission page for users.
**admin.html**: Admin dashboard to view and respond to tickets.

**Technologies Used**
**Flask**: Micro web framework for Python.
**HTML/CSS**: For front-end design and layout.
**Python**: Backend logic and session handling.
