class DashboardPage:
   def __init__(self,page):
      self.page=page
      self.admin_icon=page.locator("//a[@data-toggle ='dropdown']")
      self.logout_icon=page.locator("//a[@class='dropdown-item']").nth(1)
      self.more_info_link=page.locator("//a[@class='small-box-footer']").nth(1)  
   def click_admin_icon(self):
      self.admin_icon.click()
      return self
   def click_logout_icon(self):
      from Pages.LoginPOM import LoginPomPage # circular import
      self.logout_icon.click()
      return LoginPomPage(self.page)
   def click_moreinfo_icon(self):
      #placeholder for importingthirdPOM
      from Pages.AdminHomePOM import AdminHomePage
      self.more_info_link.click()
      return AdminHomePage(self.page)
      