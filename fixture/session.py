__author__ = 'vlovets'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def log_in(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def log_out(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()