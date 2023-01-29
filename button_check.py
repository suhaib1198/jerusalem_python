import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class button_class:

    def __init__(self,driver,id,num):
         self.driver = driver
         self.id = id
         self.num = num
         self.fill()


    def get_path_1(self):
        self.p1 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//input[@id='{self.id}']/following-sibling::p-dropdown")))
        self.p1.click()


    def get_path_2(self):
        self.p2 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"//li[@role='option' and @aria-label='{self.num}']")))

        self.p2.click()


    # def get_path_3(self ,i):
    #
    #     self.p3 = WebDriverWait(self.driver, 30).until(
    #         EC.presence_of_element_located((By.XPATH, f"//ul[@role='listbox']//p-dropdownitem['{i}']")))
    #     self.get_path_1()
    #     self.p3.click()



    def fill(self):
        self.get_path_1()
        time.sleep(1)
        self.get_path_2()


