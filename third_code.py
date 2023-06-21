# 4. 操作控端or廳主端，使用開牌查詢搜尋某一張注單，印出注單資訊(不用到細單)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    option = ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    drive = webdriver.Chrome(options=option)
    drive.get("https://admin.vir777.net/login")
    drive.maximize_window()
    # XPATH 定位語系下拉選單並點擊繁體
    # lan_bar = WebDriverWait(drive, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@class='el-select el-dropdown']"))).click()
    # lan_zh = WebDriverWait(drive, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[@class='el-dropdown-menu el-popper lang-menu']/li[1]"))).click()

    # account = WebDriverWait(drive, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[@type='text']")))
    # account.send_keys("qaevans")

    # CSS 定位語系下拉選單並點擊繁體
    WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.el-select.el-dropdown"))).click()
    WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".el-dropdown-menu.el-popper.lang-menu>:nth-child(1)"))).click()

    account = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "*[type='text']")))
    account.send_keys("qaevans")

    passwd = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "*[type='password']")))
    passwd.send_keys("evans11")
    passwd.send_keys(Keys.ENTER)

    WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[href='/game/betrecord_search/bet_query']"))).click()
