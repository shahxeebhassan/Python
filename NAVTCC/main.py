# kivy 
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import TreeView
from kivy.uix.popup import Popup


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactManagerGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ContactManagerGUI, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 10

        self.manager = ContactManager()

        self.name_label = Label(text="Full Name:")
        self.name_entry = TextInput()

        self.email_label = Label(text="Email:")
        self.email_entry = TextInput()

        self.phone_label = Label(text="Phone:")
        self.phone_entry = TextInput()

        self.add_button = Button(text="Add Contact", on_release=self.add_contact)

        self.remove_label = Label(text="Contact Name:")
        self.remove_entry = TextInput()

        self.remove_button = Button(text="Remove", on_release=self.remove_contact)

        self.search_label = Label(text="Search Key:")
        self.search_entry = TextInput()

        self.search_button = Button(text="Search", on_release=self.search_contact)

        self.contact_list = TreeView(size_hint=(1, 1))

        self.show_button = Button(text="Show All Contacts", on_release=self.toggle_contact_list)

        self.add_widget(self.name_label)
        self.add_widget(self.name_entry)
        self.add_widget(self.email_label)
        self.add_widget(self.email_entry)
        self.add_widget(self.phone_label)
        self.add_widget(self.phone_entry)
        self.add_widget(self.add_button)
        self.add_widget(self.remove_label)
        self.add_widget(self.remove_entry)
        self.add_widget(self.remove_button)
        self.add_widget(self.search_label)
        self.add_widget(self.search_entry)
        self.add_widget(self.search_button)
        self.add_widget(self.contact_list)
        self.add_widget(self.show_button)

    def add_contact(self, instance):
        name = self.name_entry.text
        email = self.email_entry.text
        phone = self.phone_entry.text

        if not name or not email or not phone:
            self.show_popup("Error", "Please enter all fields.")
            return

        if not self.validate_email(email):
            self.show_popup("Error", "Please enter a valid email.")
            return

        if not self.validate_phone(phone):
            self.show_popup("Error", "Please enter a valid 11-digit phone number.")
            return

        contact = Contact(name, phone, email)
        self.manager.add_contact(contact)
        self.show_popup("Success", "Contact added successfully!")
        self.clear_entries()
        self.update_contact_list()

    def remove_contact(self, instance):
        name = self.remove_entry.text
        if not name:
            self.show_popup("Error", "Please enter a name to remove.")
            return

        result = self.manager.remove_contact(name)
        if result:
            self.show_popup("Success", f"Contact named {name} removed successfully!")
        else:
            self.show_popup("Error", f"No contact named {name} found.")

        self.clear_entries()
        self.update_contact_list()

    def search_contact(self, instance):
        query = self.search_entry.text
        if not query:
            self.show_popup("Error", "Please enter a query to search.")
            return

        contacts = self.manager.search_contacts(query)
        if contacts:
            result = ""
            for contact in contacts:
                result += f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n\n"
            self.show_popup("Search Results", result)
        else:
            self.show_popup("Error", f"No contacts matching the query '{query}' found.")

        self.clear_entries()

    def update_contact_list(self):
        self.contact_list.clear_widgets()
        contacts = self.manager.contacts
        for contact in contacts.values():
            contact_item = TreeViewLabel(text=contact.name)
            self.contact_list.add_node(contact_item)
            contact_item.add_node(TreeViewLabel(text=contact.phone))
            contact_item.add_node(TreeViewLabel(text=contact.email))

    def clear_entries(self):
        self.name_entry.text = ""
        self.email_entry.text = ""
        self.phone_entry.text = ""
        self.remove_entry.text = ""
        self.search_entry.text = ""

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\d{4}-\d{7}$"
        return re.match(pattern, phone)

    def toggle_contact_list(self, instance):
        if self.contact_list.parent is None:
            self.add_widget(self.contact_list)
        else:
            self.remove_widget(self.contact_list)

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()


class TreeViewLabel(Label):
    pass


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def get_contact(self, name):
        return self.contacts.get(name)

    def search_contacts(self, query):
        matched_contacts = []
        for contact in self.contacts.values():
            if query.lower() in contact.name.lower() or query.lower() in contact.email.lower() or query in contact.phone:
                matched_contacts.append(contact)
        return matched_contacts


class ContactManagerApp(App):
    def build(self):
        return ContactManagerGUI()


if __name__ == "__main__":
    ContactManagerApp().run()
