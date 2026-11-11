
from playwright.sync_api import Page, expect
from Pages.LoginPOM import LoginPomPage
# from Constants.URL import base_url
from Utilities.excel_read import NewExcelReader
from Constants import URL
class TestDemo:
    def test_base_login(self,page:Page): #not under POM
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("//button[text()='Sign In']").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    def test_admin_login_pom(self,page:Page):
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        login=LoginPomPage(page)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()
        # POM using chaining
        # login.enter_username("admin").enter_password("admin").click_login()

    def test_datadriven_login(self,page:Page):
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        obj_excelreader=NewExcelReader()
        Username=obj_excelreader.read_excel_cell(3,3)
        Password=obj_excelreader.read_excel_cell(3,4)
        login=LoginPomPage(page)
        login.enter_username(Username)
        page.wait_for_timeout(3000)
        login.enter_password(Password)
        login.click_login()

    def test_admin_logout(self,page:Page):
        page.goto(URL.base_url)
        page.wait_for_timeout(3000)
        obj_excelreader=NewExcelReader()
        Username=obj_excelreader.read_excel_cell(3,3)
        Password=obj_excelreader.read_excel_cell(3,4)
        login=LoginPomPage(page)
        login.enter_username(Username).enter_password(Password).click_login().click_admin_icon().click_logout_icon()
        expect(page).to_have_title(" Login | 7rmart supermarket ")


    #File upload testcases
    def test_single_file_upload(self,page:Page): 
         page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html") 
         page.wait_for_timeout(3000) 
         file_upload_field = page.locator("#singleFileInput") 
         file_upload_field.scroll_into_view_if_needed() # to scroll to a component 
         file_upload_field.set_input_files("C:\\Users\\user\\Downloads\\employeedata_latest.xlsx") 
         page.wait_for_timeout(3000) 
         page.get_by_role("button",name="Upload Single File").click() 
         page.wait_for_timeout(3000) 
         result = page.locator("#singleFileStatus") 
         msg =result.text_content() 
         expect(result).to_be_visible() 
         expect(result).to_have_text(msg) 
         # here scroll_into_view_if_needed, is used t scroll the page to a said component 
         # here set_input_files, is used to upload a file or image in an  input component with type="file". 
  
    def test_multi_file_upload(self,page:Page): 
         page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html") 
         page.wait_for_timeout(3000) 
         multi_files_upload_field = page.locator("#multipleFilesInput") 
         multi_files_upload_field.scroll_into_view_if_needed() 
         files = ["C:\\Users\\NETCOM\\Downloads\\Playwright\\miscellaneous test cases.txt","C:\\Users\\NETCOM\\Downloads\\JavaScript\\day3- functions.js"] 
         multi_files_upload_field.set_input_files(files) 
         page.get_by_role("button",name='Upload Multiple Files').click() 
         result = page.locator("#multipleFilesStatus") 
         msg = result.text_content() 
         expect(result).to_be_visible() 
         expect(result).to_have_text(msg) 
  
         # for multi file choosing , we should upload a list inside the set_input_files()

    import pytest
    @pytest.mark.parametrize("valid_usernames",["standard_user","locked_out_user",
"problem_user",
"performance_glitch_user",
"error_user",
"visual_user"])
    def test_parametrized_login(self,page:Page,valid_usernames):
        page.goto("https://www.saucedemo.com/") 
        page.wait_for_timeout(3000) 
        page.get_by_placeholder("Username").fill(valid_usernames)
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.locator("#login-button").click()
        