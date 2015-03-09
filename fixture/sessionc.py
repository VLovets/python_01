__author__ = 'vlovets'


class SessionHelperC:

    def __init__(self, appc):
        self.appc = appc

    def log_in(self, username, password):
        wd = self.appc.wd
        self.appc.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def log_out(self):
        wd = self.appc.wd
        wd.find_element_by_link_text("Logout").click()