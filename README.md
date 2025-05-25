ICT LAB 7
(READ ME)

Gym Management System:
This is a basic Gym Management System website built using Flask, HTML, and CSS. It includes pages for Home, About, Services, Gallery, and Contact, along with simulated user registration and login functionality..Displays a welcome message and gym highlights.Provides details about the gym's mission, team, and facilities.Showcases membership plans and services.
Features
•	Static Pages: Home, About Us, Services, Gallery, Contact Us
•	User Authentication: Register, Login, Logout using Flask sessions
•	Session Management: Keeps users logged in during the session
•	Basic Form Handling: User input handling on login, registration, and contact forms
•	Template Inheritance: Uses a base HTML template for consistent layout
•	Styling: Simple CSS styling for layout and navigation




How It Works
•	User data is stored in a Python dictionary (users) to simulate a database (for demonstration only).
•	Registration checks for duplicate usernames before adding a new user.
•	Login authenticates users by matching username and password in the dictionary.
•	Logged-in users see a "Logout" link; logged-out users see "Login" and "Register" links.
•	Uses Flask’s session to store the logged-in username securely, protected by a randomly generated secret key.
•	HTML templates use Jinja2 templating for dynamic content and navigation.


1. Install Flask if you haven’t already: (install using `pip install Flask`)
2. Navigate to the project directory.
3. Run the Flask application.
 4. Open the website in your browser

* This project uses Flask to manage routes and serve dynamic content.
* HTML files are located in the `templates` folder, and CSS files are in the `static` folder.


MADE BY:
Muhammad Baloch
