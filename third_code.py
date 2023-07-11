# 4. 操作控端or廳主端，使用開牌查詢搜尋某一張注單，印出注單資訊(不用到細單)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
class Login:
    def __init__(self):
        option = ChromeOptions()
        option.add_experimental_option("detach", True)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.drive = webdriver.Chrome(options=option)
        self.__acc = "qaevans"
        self.__pwd = "evans11"
    def login(self):
        self.drive.get("https://admin.vir777.net/login")
        self.drive.maximize_window()
        # CSS 定位語系下拉選單並點擊繁體
        WebDriverWait(self.drive, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "div.el-select.el-dropdown"))).click()
        WebDriverWait(self.drive, 10).until(
            ec.element_to_be_clickable(
                (By.CSS_SELECTOR, ".el-dropdown-menu.el-popper.lang-menu>:nth-child(1)"))).click()

        account = WebDriverWait(self.drive, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "*[type='text']")))
        account.send_keys(self.__acc)

        passwd = WebDriverWait(self.drive, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "*[type='password']")))
        passwd.send_keys(self.__pwd)
        passwd.send_keys(Keys.ENTER)
class Search:
    def __init__(self, drive):
        self.drive = drive
    def search(self):
        WebDriverWait(self.drive, 10).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, ".item.home>a[href*='bet_query']"))).click()

        game = WebDriverWait(self.drive, 10).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, ".iframe-item")))
        self.drive.switch_to.frame(game)
        WebDriverWait(self.drive, 10).until(ec.presence_of_element_located(
            (By.CSS_SELECTOR, ".nav.nav-tabs>li:nth-child(15)"))).click()

        wagersid = WebDriverWait(self.drive, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#wagersid")))
        wagersid.send_keys("520001025310")
        WebDriverWait(self.drive, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#startsearch"))).click()
    def print_result(self):
        tbody = WebDriverWait(self.drive, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody>.text-center>td")))
        for i, value in enumerate(tbody):
            print(value.text)

if __name__ == '__main__':
    login = Login()

    login.login()

    search = Search(login.drive)

    search.search()
    search.print_result()

    # option = ChromeOptions()
    # option.add_experimental_option("detach", True)
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # drive = webdriver.Chrome(options=option)
    # drive.get("https://admin.vir777.net/login")
    # drive.maximize_window()
    # # XPATH 定位語系下拉選單並點擊繁體
    # # lan_bar = WebDriverWait(drive, 10).until(
    # #     ec.presence_of_element_located((By.XPATH, "//div[@class='el-select el-dropdown']"))).click()
    # # lan_zh = WebDriverWait(drive, 10).until(
    # #     ec.presence_of_element_located(
    # #     (By.XPATH, "//*[@class='el-dropdown-menu el-popper lang-menu']/li[1]"))).click()
    #
    # # account = WebDriverWait(drive, 10).until(
    # #     ec.presence_of_element_located((By.XPATH, "//*[@type='text']")))
    # # account.send_keys("qaevans")
    #
    # # CSS 定位語系下拉選單並點擊繁體
    # WebDriverWait(drive, 10).until(
    #     ec.presence_of_element_located((By.CSS_SELECTOR, "div.el-select.el-dropdown"))).click()
    # WebDriverWait(drive, 10).until(
    #     ec.element_to_be_clickable(
    #         (By.CSS_SELECTOR, ".el-dropdown-menu.el-popper.lang-menu>:nth-child(1)"))).click()
    #
    # account = WebDriverWait(drive, 10).until(
    #     ec.presence_of_element_located((By.CSS_SELECTOR, "*[type='text']")))
    # account.send_keys("qaevans")
    #
    # passwd = WebDriverWait(drive, 10).until(
    #     ec.presence_of_element_located((By.CSS_SELECTOR, "*[type='password']")))
    # passwd.send_keys("evans11")
    # passwd.send_keys(Keys.ENTER)
    #
    # WebDriverWait(drive, 10).until(ec.presence_of_element_located(
    #     (By.CSS_SELECTOR, ".item.home>a[href*='bet_query']"))).click()
    #
    # game = WebDriverWait(drive, 10).until(ec.presence_of_element_located(
    #     (By.CSS_SELECTOR, ".iframe-item")))
    # drive.switch_to.frame(game)
    # WebDriverWait(drive, 10).until(ec.presence_of_element_located(
    #     (By.CSS_SELECTOR, ".nav.nav-tabs>li:nth-child(15)"))).click()
    #
    # wagersid = WebDriverWait(drive, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#wagersid")))
    # wagersid.send_keys("520001025310")
    # WebDriverWait(drive, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "#startsearch"))).click()
    #
    # tbody = WebDriverWait(drive, 10).until(
    #     ec.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody>.text-center>td")))
    # for i, value in enumerate(tbody):
    #     print(value.text)
