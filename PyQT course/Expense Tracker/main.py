from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(550, 500)
        self.setWindowTitle(("Expense Tracker"))

        self.date_box = QDateEdit()
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Expense")
        self.delete_button = QPushButton("Delete Expense")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        header_names = ["Id", "Date", "Category", "Amount", "Description"]
        self.table.setHorizontalHeaderLabels(header_names)

        self.dropdown.addItems(["Food", "Transportation", "Rent", "Shopping", "Movies", "Other"])

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(QLabel("Date:"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category"))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description"))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_button)
        self.row3.addWidget(self.delete_button)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("expense.db")
        if not database.open():
            QMessageBox.critical(None, "Error", "Could not open your database")
            print("MEH")
            sys.exit(1)

        query = QSqlQuery()
        query.exec("""
                            CREATE TABLE IF NOT EXISTS expenses (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT,
                                category TEXT,
                                amount REAL,
                                description TEXT
                            )
                            """)

        self.load_table()

    def load_table(self):
        self.table.setRowCount(0)
        query = QSqlQuery("SELECT * FROM expenses")
        row = 0
        while query.next():
            expense_id = query.value(0)
            date = query.value(1)
            category = query.value(2)
            amount = query.value(3)
            description = query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(expense_id)))
            self.table.setItem(row, 1, QTableWidgetItem(str(date)))
            self.table.setItem(row, 2, QTableWidgetItem(str(category)))
            self.table.setItem(row, 3, QTableWidgetItem(str(amount)))
            self.table.setItem(row, 4, QTableWidgetItem(str(description)))

            row += 1

    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        query = QSqlQuery()
        query.pre


if __name__ in "__main__":
    app = QApplication([])
    main_window = ExpenseApp()
    main_window.show()
    app.exec()
