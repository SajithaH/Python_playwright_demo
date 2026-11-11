from playwright.sync_api import Page,expect

from Constants import URL
from Pages.LoginPOM import LoginPomPage
from Utilities.excel_read import NewExcelReader
from Pages.AdminHomePOM import AdminHomePage
from Pages.DashboardPOM import DashboardPage
class TestAdminClass:
    def test_add_new_user(self,page:Page):
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        obj_excelreader=NewExcelReader()
        Username=obj_excelreader.read_excel_cell(3,3)
        Password=obj_excelreader.read_excel_cell(3,4)
        login=LoginPomPage(page)
        login.enter_username(Username).enter_password(Password).click_login().click_moreinfo_icon().click_new_button().enter_adminppage_username("admin444").enter_adminppage_password("pwd444").select_user_type().save_button()

    def test_add_user(self,page:Page):
            page.goto(URL.base_url)
            page.wait_for_timeout(3000)
            obj_excelreader=NewExcelReader()
            Username=obj_excelreader.read_excel_cell(3,3)
            Password=obj_excelreader.read_excel_cell(3,4)
            login=LoginPomPage(page)
            obj_dashboard=DashboardPage(page)
            obj_admin_home=AdminHomePage(page)            
            login.enter_username(Username).enter_password(Password).click_login()
            obj_dashboard.click_moreinfo_icon()
            obj_admin_home.click_new_button().enter_adminppage_username("admin555").enter_adminppage_password("pwd555").select_user_type().click_save_button()
            expect(obj_admin_home.failure_alert).to_be_visible()

    def test_search_user(self,page:Page):
         
            page.goto(URL.base_url)
            page.wait_for_timeout(3000)
            obj_excelreader=NewExcelReader()
            Username=obj_excelreader.read_excel_cell(3,3)
            Password=obj_excelreader.read_excel_cell(3,4)
            login=LoginPomPage(page)
            login.enter_username(Username).enter_password(Password).click_login().click_moreinfo_icon().click_search().search_username("anju").search_usertype().search_result().table_result()
            # obj_adminhome=AdminHomePage(page)
            # expect(obj_adminhome.table).to_have_text("anju")
            