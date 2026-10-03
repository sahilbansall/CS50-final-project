# AI assistance:
# ChatGPT was used to help explain Flask concepts,
# debug errors, and improve the structure and styling of this project.

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "expenses.db"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def index():
    connection = get_db()

    expenses = connection.execute(
        "SELECT * FROM expenses ORDER BY date DESC, id DESC"
    ).fetchall()

    total = connection.execute(
        "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses"
    ).fetchone()["total"]

    connection.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        title = request.form["title"]
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]

        connection = get_db()

        connection.execute(
            """
            INSERT INTO expenses (title, amount, category, date)
            VALUES (?, ?, ?, ?)
            """,
            (title, amount, category, date)
        )

        connection.commit()
        connection.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    connection = get_db()

    connection.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)