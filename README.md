# Expense Tracker

#### Video Demo: https://youtu.be/PWj1a-WccXY

#### GitHub: https://github.com/sahilbansall/CS50-final-project

#### Description:

Expense Tracker is a simple web-based application that helps users record and manage their daily expenses. I created this project as my CS50x final project to apply concepts that I learned during the course, including Python, SQL, HTML, CSS, and JavaScript.

The main purpose of the application is to provide a simple way to keep track of spending. Instead of writing expenses manually, the user can enter an expense into the application and store it in a SQLite database. The dashboard then displays the saved expenses and calculates the total amount spent.

## Features

* Add a new expense.
* Enter the expense title, amount, category, and date.
* View all saved expenses on the dashboard.
* Automatically calculate total spending.
* Display the total number of expenses.
* Search for expenses using the search box.
* Delete an expense when it is no longer needed.
* Store expense information in a SQLite database.
* Use a responsive interface for different screen sizes.

## How It Works

When the application starts, Flask runs the Python backend and connects the web pages with the SQLite database.

The home page displays all expenses stored in the database. It also calculates the total amount of all expenses using an SQL `SUM` query.

When the user selects "Add Expense", the application opens a form where the user can enter the expense title, amount, category, and date. After submitting the form, Flask receives the information and inserts the information into the SQLite database. The user is then redirected back to the dashboard, where the new expense appears in the list.

The search feature is implemented using JavaScript. As the user types into the search box, JavaScript checks the text of each expense row and hides rows that do not match the search text.

The delete feature sends a request to Flask with the ID of the selected expense. Flask then removes that record from the SQLite database and returns the user to the dashboard.

## Files

### `app.py`

This is the main Python file of the application. It creates the Flask application, defines the routes, connects to the SQLite database, adds expenses, displays expenses, calculates total spending, and deletes expenses.

### `templates/index.html`

This is the main dashboard page. It displays the total spending, number of expenses, search box, and expense table. It also provides buttons for adding and deleting expenses.

### `templates/add.html`

This page contains the form used to add a new expense. The form collects the expense title, amount, category, and date.

### `static/style.css`

This file contains the CSS used to design the application. It controls the layout, cards, buttons, table, form, spacing, and responsive design.

### `static/script.js`

This JavaScript file provides the client-side search functionality. It filters the expense table as the user types in the search box.

### `requirements.txt`

This file lists the Python package required to run the application. The project uses Flask.

### `expenses.db`

This is the SQLite database used to store expense records. The database contains an `expenses` table with fields for the ID, title, amount, category, and date.

## Design Choices

I decided to use Flask because it provides a simple way to build a web application with Python. Flask was sufficient for this project without requiring a more complicated framework.

I chose SQLite because it is lightweight and does not require a separate database server. It is suitable for a small application and allowed me to practice SQL database operations.

I kept the interface simple so users can quickly add and review their expenses. I also included a search feature using JavaScript to make finding a particular expense easier.

The application does not require a complicated account system because the main purpose of this project is expense recording and management. Keeping the scope small allowed me to focus on the core functionality.

## Technologies Used

* Python
* Flask
* SQLite
* SQL
* HTML
* CSS
* JavaScript

## Running the Application

To run the application locally, install the required package:

```bash
pip install -r requirements.txt
```

Then start the Flask application:

```bash
python app.py
```

The application can then be opened in a web browser at:

```text
http://127.0.0.1:5000
```

## Conclusion

Expense Tracker is a small but complete web application that demonstrates how different programming concepts can work together. Python and Flask handle the backend, SQLite stores the data, HTML creates the structure of the pages, CSS provides the visual design, and JavaScript adds interactive searching.

Building this project helped me understand how a web application receives user input, stores information in a database, retrieves that information, and displays it back to the user.

## AI Assistance

AI assistance was used during development to help explain Flask concepts, debug errors, and improve the structure and styling of the project. The code was reviewed, tested, and modified as needed while building the application.
