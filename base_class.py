import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from text_field import  text_class
from button_check import  button_class
from  open_browser import  open_browser
from  err_msg import  display_err



@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def websit(driver):
    open = open_browser(driver)
    open.open_browser()




#fail no inputs
def test_form_submission(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver,'שם פרטי',"")
    text_class(driver,'שם משפחה', "")
    text_class(driver,'cellphone', "")
    text_class(driver,'מספר ת.ז.', "")
    text_class(driver,'phone', "")
    text_class(driver,'דוא"ל', "")
    button_class(driver,"cellphone","050")
    button_class(driver, "phone", "02")
    assert test.check_()

# pass all ok
def test_form_submission_1(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver,'שם פרטי',"סוהייב")
    text_class(driver,'שם משפחה', "אבו גנאם")
    text_class(driver,'cellphone', "0000000")
    text_class(driver,'מספר ת.ז.', "208673178")
    text_class(driver,'phone', "3877655 ")
    text_class(driver,'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","051")
    button_class(driver, "phone", "03")
    assert test.check_()




#fail f/l name not in herbrow
def test_form_submission_2(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "ooops")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "0000000")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "3877655 ")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","052")
    button_class(driver, "phone", "04")
    assert test.check_()




#fail f/l name not in herbrow
def test_form_submission_2_1(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "اؤبس")
    text_class(driver, 'cellphone', "0000000")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "3877655 ")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","053")
    button_class(driver, "phone", "08")
    assert test.check_()


#fail cellphone and phone must be seven numbers
def test_form_submission_3(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "123 ")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","054")
    button_class(driver, "phone", "09")
    assert test.check_()


#fail cellphone and phone must be seven numbers
def test_form_submission_3_1(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "123")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","055")
    button_class(driver, "phone", "072")
    assert test.check_()


# fail cellphone and phone must be numbers
def test_form_submission_3_2(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "number")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","056")
    button_class(driver, "phone", "073")
    assert test.check_()


# fail cellphone and phone must be numbers
def test_form_submission_3_3(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "number")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    button_class(driver,"cellphone","057")
    button_class(driver, "phone", "077")
    assert test.check_()


# fail email must be this form a@b.xy
def test_form_submission_4(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "s@s.s")
    button_class(driver,"cellphone","058")
    button_class(driver, "phone", "09")
    assert test.check_()


# fail email must be this form a@b.xy and in english
def test_form_submission_4_1(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "וטט.דש@גגדץגט")
    button_class(driver,"cellphone","059")
    button_class(driver, "phone", "09")
    assert test.check_()


#fail email must be this form a@b.xy and in english
def test_form_submission_4_2(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "וטט.xx@تت")
    button_class(driver,"cellphone","077")
    button_class(driver, "phone", "077")
    assert test.check_()


# fail email must be this form a@b.xy and in english
def test_form_submission_4_3(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "208673178")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "xxxxxxxx")
    button_class(driver,"cellphone","054")
    button_class(driver, "phone", "09")
    assert test.check_()


#fail ID must be in right formula an numbers
def test_form_submission_5(driver):
    websit(driver)
    test = display_err(driver)
    text_class(driver, 'שם פרטי', "סוהייב")
    text_class(driver, 'שם משפחה', "אבו גנאם")
    text_class(driver, 'cellphone', "1234567")
    text_class(driver, 'מספר ת.ז.', "20")
    text_class(driver, 'phone', "1234567")
    text_class(driver, 'דוא"ל', "suhaib@gmail.com")
    text_class(driver, 'מספר ת.ז.', "1")
    time.sleep(2)
    text_class(driver, 'מספר ת.ז.', "20455432333")
    time.sleep(2)
    text_class(driver, 'מספר ת.ז.', "xxxxxxxxx")
    time.sleep(2)
    text_class(driver, 'מספר ת.ז.', "כקככקכקכק")
    time.sleep(2)
    text_class(driver, 'מספר ת.ז.', "ششششششششش")
    time.sleep(2)

    button_class(driver,"cellphone","054")
    button_class(driver, "phone", "09")
    assert test.check_()

    # add a screenshot to the Allure report
    #allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)


