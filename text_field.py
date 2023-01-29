from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class text_class:

    def __init__(self,driver,label,input):
         self.driver = driver
         self.label = label
         self.input = input
         self.setText(self.input)


         try:
            print("")

         except:
            print("")


    def get_path(self):

        try:
            self.field_path = self.driver.find_element(By.XPATH ,f"//label[contains(text(),'{self.label}')]/following-sibling::input")


            return self.field_path
        except:
            self.field_id = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, f"{self.label}")))

            return self.field_id

    def setText(self,input):
        self.get_path().clear()
        self.get_path().send_keys(input)


    def getText(self):
        return self.get_path().get_attribute('value')


    def clear_text(self):
        self.get_path().clear()

    # def fill(self):
        # self.getPath()
        # self.setText()


