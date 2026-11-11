class AdminHomePage:
    def __init__(self,page):
        self.page=page
        # self.new_user_button=page.get_by_role("link",name=' New')
        self.new_user_button =page.locator("a[class='btn btn-rounded btn-danger']")
        self.username=page.locator("#username")
        self.password=page.locator("#password")
        self.user_type=page.locator("#user_type")
        self.save_button=page.locator("//button[@name='Create']")
        self.success_alert=page.locator("//div[@class='alert alert-success alert-dismissible']")
        self.failure_alert=page.locator("//div[@class='alert alert-danger alert-dismissible']")
        self.search=page.locator("//a[@class='btn btn-rounded btn-primary']")
        self.search_username_field = page.locator("input[name='un']")
        self.search_usertype_field = page.locator("//select[@name='ut']")
        self.search_btn =page.locator("//button[@name='Search']")
        self.table = page.locator("//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]")

    def click_new_button(self):
        self.new_user_button.click()
        return self
    def enter_adminppage_username(self,username):
        self.username.fill(username)
        return self
    def enter_adminppage_password(self,password):
        self.password.fill(password)
        return self
    def select_user_type(self):
        self.user_type.select_option(label="Staff")
        return self
    def click_save_button(self):
        self.save_button.click()
        return self
    
    def click_search(self):
        self.search.click()
        return self    

    def search_username(self,username):
        self.search_username_field.fill(username)
        return self
    
    def search_usertype(self):
        self.search_usertype_field.select_option(label="Admin")
        return self

    def search_result(self):
        self.search_btn.click()
        return self
    def table_result(self):
        res = self.table.text_content()
        print(f'The username available in table is: {res}')
        return self