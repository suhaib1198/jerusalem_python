class open_browser:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure"

    def open_browser(self):
        try:
            self.driver.get(self.url)
        except:
            print(f'no response : {self.url}')