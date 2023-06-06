import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QAction, QMenuBar, QTableWidget, QTableWidgetItem, QHeaderView, QDesktopWidget
from PyQt5.QtGui import QFont, QColor, QBrush
from PyQt5.QtCore import Qt


class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.data = {}

        # Set the window size to 80% of the screen size
        screen_geometry = QDesktopWidget().screenGeometry()
        self.resize(screen_geometry.width() * 0.8, screen_geometry.height() * 0.8)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.inputLayout = QVBoxLayout()
        self.tableLayout = QVBoxLayout()

        self.layout.addLayout(self.inputLayout)
        self.layout.addLayout(self.tableLayout)

        self.nameInput = QLineEdit()
        self.phoneInput = QLineEdit()
        self.emailInput = QLineEdit()
        self.searchInput = QLineEdit()

        self.addContactBtn = QPushButton("Add Contact")
        self.addContactBtn.clicked.connect(self.add_contact)

        self.removeContactBtn = QPushButton("Remove Contact")
        self.removeContactBtn.clicked.connect(self.remove_contact)

        self.searchContactBtn = QPushButton("Search Contact")
        self.searchContactBtn.clicked.connect(self.search_contact)

        self.showContactsBtn = QPushButton("Show All Contacts")
        self.showContactsBtn.clicked.connect(self.show_contacts)

        self.inputLayout.addWidget(QLabel("Name:"))
        self.inputLayout.addWidget(self.nameInput)
        self.inputLayout.addWidget(QLabel("Phone:"))
        self.inputLayout.addWidget(self.phoneInput)
        self.inputLayout.addWidget(QLabel("Email:"))
        self.inputLayout.addWidget(self.emailInput)
        self.inputLayout.addWidget(self.addContactBtn)
        self.inputLayout.addWidget(self.removeContactBtn)
        self.inputLayout.addWidget(QLabel("Search:"))
        self.inputLayout.addWidget(self.searchInput)
        self.inputLayout.addWidget(self.searchContactBtn)
        self.inputLayout.addWidget(self.showContactsBtn)

        self.contactsTable = QTableWidget()
        self.contactsTable.setColumnCount(3)
        self.contactsTable.setHorizontalHeaderLabels(["Name", "Phone", "Email"])
        self.contactsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableLayout.addWidget(QLabel("Contacts"))
        self.tableLayout.addWidget(self.contactsTable)

        self.setFont(QFont("Arial", 12))

        self.create_menu()

    def create_menu(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("File")

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)

        fileMenu.addAction(exitAction)

    def validate_name(self, name):
        name_pattern = r'^[a-zA-Z]+\s+[a-zA-z]+'
        name_match = re.match(name_pattern, name)
        return name_match

    def validate_phone(self, phone):
        phone_pattern = r'^[0-9]{4}\-[0-9]{7}'
        phone_match = re.match(phone_pattern, phone)
        return phone_match

    def validate_email(self, email):
        email_pattern = r'^[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z]'
        email_match = re.match(email_pattern, email)
        return email_match

    def add_contact(self):
        name = self.nameInput.text()
        phone = self.phoneInput.text()
        email = self.emailInput.text()

        if not name or not phone or not email:
            QMessageBox.warning(self, "Error", "Please enter all fields")
            return

        if name in self.data:
            QMessageBox.warning(self, "Error", "Contact already exists")
            return

        if not self.validate_name(name):
            QMessageBox.warning(self, "Error", "Invalid name format")
            return

        if not self.validate_phone(phone):
            QMessageBox.warning(self, "Error", "Invalid phone format (use ####-#######)")
            return

        if not self.validate_email(email):
            QMessageBox.warning(self, "Error", "Invalid email format")
            return

        self.data[name] = {
            "phone": phone,
            "email": email
        }

        self.nameInput.clear()
        self.phoneInput.clear()
        self.emailInput.clear()

        QMessageBox.information(self, "Success", "Contact added successfully")

    def remove_contact(self):
        name = self.nameInput.text()

        if not name:
            QMessageBox.warning(self, "Error", "Please enter a name to remove")
            return

        if name not in self.data:
            QMessageBox.warning(self, "Error", "Contact does not exist")
            return

        del self.data[name]
        self.nameInput.clear()
        QMessageBox.information(self, "Success", "Contact removed successfully")

    def search_contact(self):
        search_term = self.searchInput.text()

        if not search_term:
            QMessageBox.warning(self, "Error", "Please enter a search term")
            return

        results = []

        for name, contact in self.data.items():
            if search_term in name or search_term in contact["phone"] or search_term in contact["email"]:
                results.append((name, contact["phone"], contact["email"]))

        if not results:
            QMessageBox.information(self, "Search Results", "No contacts found")
        else:
            self.display_contacts(results)

    def display_contacts(self, contacts):
        self.contactsTable.setRowCount(len(contacts))

        for i, (name, phone, email) in enumerate(contacts):
            self.contactsTable.setItem(i, 0, QTableWidgetItem(name))
            self.contactsTable.setItem(i, 1, QTableWidgetItem(phone))
            self.contactsTable.setItem(i, 2, QTableWidgetItem(email))

    def show_contacts(self):
        if not self.data:
            QMessageBox.information(self, "Contacts", "No contacts found")
        else:
            contacts = [(name, contact["phone"], contact["email"]) for name, contact in self.data.items()]
            self.display_contacts(contacts)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    style_sheet = """
    QMainWindow {
        background-color: #f0f0f0;
    }

    QLabel {
        color: #333333;
    }

    QLineEdit {
        padding: 5px;
        border: 1px solid #aaaaaa;
        border-radius: 3px;
    }

    QPushButton {
        padding: 5px 10px;
        border: none;
        border-radius: 3px;
        background-color: #007bff;
        color: white;
    }

    QPushButton:hover {
        background-color: #0056b3;
    }

    QPushButton:pressed {
        background-color: #003c80;
    }

    QTableWidget {
        background-color: white;
        border: 1px solid #cccccc;
        border-radius: 3px;
    }

    QHeaderView::section {
        background-color: #007bff;
        color: white;
    }

    QMessageBox {
        background-color: white;
    }
    """
    window.setStyleSheet(style_sheet)
    window.show()
    sys.exit(app.exec_())
