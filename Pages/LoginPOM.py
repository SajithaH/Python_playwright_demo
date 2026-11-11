class LoginPomPage:
    def __init__(self,page):
        self.page=page
        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        self.button= page.locator("//button[text()='Sign In']")

    def enter_username(self,user1):
        self.username.fill(user1)
        return self
    def enter_password(self,password1):
        self.password.fill(password1)
        return self
    def click_login(self):
        from Pages.DashboardPOM import DashboardPage
        self.button.click()
        return DashboardPage(self.page)
