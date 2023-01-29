from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class display_err:
    def __init__(self, driver):
        self.driver = driver

    def check_(self):
        try:
            self.locator = {
                'By': By.XPATH,
                'Value': "//div[contains(@class,'field-errors ng-star-inserted') and @role='alert']"
            }
            self.field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.locator['By'], self.locator['Value'])))
            return False,print("invalid")
        except:
            return True,print("valid")



