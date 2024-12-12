import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_registration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_registration1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")

        self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys("Ivan")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']").send_keys("Ivanov")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']").send_keys("test@test.qa")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")


        self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys("Ivan")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']").send_keys("Ivanov")
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']").send_keys("test@test.qa")
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
