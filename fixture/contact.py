__author__ = 'vlovets'

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('edit.php') and (len(wd.find_elements_by_name('submit')) > 0)):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not ((len(wd.find_elements_by_id('maintable')) > 0) and (len(wd.find_elements_by_name('add')) > 0)):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email", contact.email)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def select_first_contact(self, index):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_fields(contact)
        # submit creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def delete_first_contact(self, index):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        success = True
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        #ok
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit(self, index):
        self.modify_some_contact(0)

    def modify_some_contact(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()
        self.fill_contact_fields(contact)
        # submit creation
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name=entry]'):
                textl = element.find_elements_by_css_selector('td')[1].text
                textf = element.find_elements_by_css_selector('td')[2].text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.contact_cache.append(Contact(firstname=textf, lastname=textl, id=id))
        return list(self.contact_cache)