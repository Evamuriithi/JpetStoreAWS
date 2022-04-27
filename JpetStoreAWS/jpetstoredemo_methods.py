from selenium import webdriver # import selenium to the file
from time import sleep
import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import jpetstoredemo_locators as locators
from selenium.webdriver.support.ui import Select # <--- add this import from drop down list
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
# create a chrome drive instance, specify path to chromedriver file
# # this gives a DeprecationWarning
# driver = webdriver.Chrome('chromedriver.exe')

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'--------------------------------------')
    print(f'Test start at: {datetime.datetime.now()}')

    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to moodle App website
    driver.get(locators.jpetstoredemo_url)
    # check that  moodle URL and the home page title are as expected
    driver.get(locators.jpetstoredemo_url)
    if driver.current_url == locators.jpetstoredemo_url and driver.title == locators.jpetstoredemo_home_page_title:
        print(f'We are at JPetShore Demo homepage -- {driver.current_url}')
        print(f'We\'re seeing title message --{driver.title}')
        sleep(0.75)
    else:
        print(f'we\'re not at the JPetStore Demo homepage. Check your code!')


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def sign_up():
    if driver.current_url == locators.jpetstoredemo_url:
        driver.find_element(By.LINK_TEXT, 'Sign In').click()
        sleep(1.25)
        if driver.current_url == locators.jpetstoredemo_login_page_url and driver.title == locators.jpetstoredemo_home_page_title:
            print(f'{locators.app} App Login page is Displayed! Continue to log in.')
            sleep(0.25)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(1.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1.25)
        driver.find_element(By.NAME, 'signon').click()
        sleep(1.25)


def register():
    driver.find_element(By.XPATH, '//a[normalize-space()="Register Now!"]').click()
    sleep(1.25)
    driver.find_element(By.NAME,'username').send_keys(locators.new_username)
    sleep(1.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.password1)
    sleep(1.25)
    driver.find_element(By.NAME, 'repeatedPassword').send_keys(locators.password2)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.firstName').send_keys(locators.first_name)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.lastName').send_keys(locators.last_name)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.email').send_keys(locators.email)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.phone').send_keys(locators.phonenum)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.address1').send_keys(locators.address1)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.address2').send_keys(locators.address2)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.city').send_keys(locators.city)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.state').send_keys(locators.state)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.zip').send_keys(locators.zip_code)
    sleep(1.25)
    driver.find_element(By.NAME, 'account.country').send_keys(locators.country)
    sleep(1.25)
    print(f'************* Register is done*******************')


def profile_information():
    if driver.current_url == locators.jpetstoredemo_url:
        driver.find_element(By.NAME,'account.languagePreference')
    Select(driver.find_element(By.XPATH,'//select[@name="account.languagePreference"]')).select_by_visible_text('japanese')
    sleep(1.25)
    Select(driver.find_element(By.XPATH, '//select[@name="account.favouriteCategoryId"]')).select_by_visible_text('DOGS')
    sleep(1.25)
    driver.find_element(By.CSS_SELECTOR,'input[value="true"][name="account.listOption"]').click()
    #driver.find_element(By.XPATH,'// input[ @ name = "account.listOption")]').click()
    sleep(1.25)
    driver.find_element(By.CSS_SELECTOR, 'input[value="true"][name="account.bannerOption"]').click()
    sleep(1.25)
    #driver.find_element(By.XPATH, '//input[@name="newAccount")]').click()
    sleep(1.25)
    print(f'*********** Save Account Information is done*******************')


# setUp()
# sign_up()
# register()
# profile_information()
# tearDown()