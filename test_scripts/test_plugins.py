# pytest plugins
# 1)parallel execution - pytest-xdist
# pip install pytest-xdist
# 2) Reporting - pytest-html
# pip install pytest-html
# 3)handle flakiness - pytest-rerunfailures
# 4) Code coverage -pytest-cov
# pytest --cov=foldername --cov-report=html
# 5)Managing executionorder - pytest-order
# 6) enforcing limits - pytest-timeout


from playwright.sync_api import Page, expect
from Pages.DashboardPOM import DashboardPage
from Pages.LoginPOM import LoginPomPage
# from Constants.URL import base_url
from Utilities.excel_read import NewExcelReader
from Constants import URL
import pytest
import allure

class TestDemo:
     
    @pytest.mark.regression  
    def test_base_login(self,page:Page): #not under POM
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("//button[text()='Sign In']").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
    
    @pytest.mark.order("last")
    @pytest.mark.smoke    
    def test_admin_login_pom(self,page:Page):
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        login=LoginPomPage(page)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        # POM using chaining
        # login.enter_username("admin").enter_password("admin").click_login()

    @pytest.mark.order("first")
    @pytest.mark.smoke
    # @pytest.mark.timeout(8)
    def test_admin_logout(self,page:Page):
        
        page.goto(URL.base_url)
        try:
            # page.wait_for_timeout(8000)
            obj_excelreader=NewExcelReader()
            Username=obj_excelreader.read_excel_cell(3,3)
            Password=obj_excelreader.read_excel_cell(3,4)
            login=LoginPomPage(page)
            obj_dashboard=DashboardPage(page)
            login.enter_username(Username).enter_password().click_login()        
            page.screenshot(path="SCREENSHOTS/Dashboard.png",full_page=True)
            obj_dashboard.click_admin_icon().click_logout_icon()
            page.screenshot(path="SCREENSHOTS/backtologin.png",full_page=True)
            expect(page).to_have_title(" Login | 7rmart supermarket ")

        except Exception:
            allure.attach(
                page.screenshot(),
                name="failedscreenshot1",
                attachment_type=allure.attachment_type.PNG                
                )
            raise

