from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest
class Booking:
    def __init__(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:/Selenium/chromedriver.exe")
        driver.get("https://www.goindigo.in/")
        driver.implicitly_wait(10)
    def launch(self):
        driver.find_element_by_xpath("//*[@id='bookFlightTab']/form/div[2]/div[2]/label/label").click()
        driver.find_element_by_xpath("//*[@id='bookFlightTab']/form/div[3]/div[1]/div[2]/div/div/input").click()
        driver.find_element_by_xpath("//*[@id='bookFlightTab']/form/div[3]/div[1]/div[2]/div/div/input").send_keys(
            "Mum",Keys.ENTER)
        driver.find_element_by_xpath(
            "/html/body/div[3]/section/div[2]/div[1]/div/div/div/div[2]/div[1]/form/div[7]/div[4]/label/label").click()
        driver.find_element_by_xpath("//*[@id='bookFlightTab']/form/div[7]/div[6]/button/span[1]").click()
        driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/div[2]/button").click()
        driver.find_element_by_xpath("//*[@id='bookFlightTab']/form/div[7]/div[6]/button/span[1]").click()

    def test_login(self):
        # LoginFields
        driver.maximize_window()
        element = driver.find_element_by_xpath("//a[@title='Login']")
        element.click()
        # UserName
        element = driver.find_element_by_xpath("/html/body/div[56]/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/input")
        element.send_keys("8126079511")
        driver.implicitly_wait(5)
        # PassWord
        element = driver.find_element_by_xpath("//input[@id='mobilePass']")
        element.send_keys("54561220A")
        # ButtonClick
        login = driver.find_element_by_xpath(
            "//button[@type='submit' and @class='btn btn-primary block bold mem-login-button' ]")
        login.click()
        driver.implicitly_wait(10)

    def test_signout(self):
        # Logout
        x=r"//*[@id='navbarSupportedContent']/ul/li[11]/a"
        user = driver.find_element_by_xpath(x)
        user.click()
        driver.implicitly_wait(5)

        logout = driver.find_element_by_xpath(
            "//li[@class='profile-login']//a[@class='header-logout-btn'][contains(text(),'Log out')]")
        logout.click()
    def test_teardown(self):
        driver.quit()
        driver.close()


s = Booking()
s.test_login()
s.test_signout()