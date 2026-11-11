from playwright.sync_api import Page,expect
from Utilities.json_read import ReadJson
from Pages.LoginPOM import LoginPomPage
from Constants.URL import base_url

class TestReadJson:
    def test_read_json(self,page:Page):
        page.goto(base_url)
        page.wait_for_timeout(3000)
        obj_readjson  = ReadJson()
        jsondata=obj_readjson.read_jsonfile()
        user1=jsondata["Username"]
        pass1=jsondata["Password"]
        obj_login=LoginPomPage(page)
        obj_login.enter_username(user1).enter_password(pass1).click_login()
        expect(page).to_have_url(page.url)