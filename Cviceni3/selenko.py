from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_first_recipe(self):
        self.driver.get("http://127.0.0.1:5000/picy")
        text_prvniho_receptu = self.driver.find_element(
            By.XPATH, "//ol/li[1]").text
        self.assertEqual(text_prvniho_receptu, "čoky: 123")
    
    def test_objednani(self):
        self.driver.get("http://127.0.0.1:5000/objednej")
        self.driver.find_element(By.NAME, "nazev").clear()
        self.driver.find_element(By.NAME, "nazev").send_keys("piko")
        self.driver.find_element(By.NAME, "mnozstvi").clear()
        self.driver.find_element(By.NAME, "mnozstvi").send_keys("123")
        self.driver.find_element(By.TAG_NAME, "button").click()
        
    def test_vytvoreni(self):
        self.driver.get("http://127.0.0.1:5000/vytvor")
        self.driver.find_element(By.NAME, "nazev").clear()
        self.driver.find_element(By.NAME, "nazev").send_keys("nova pica")
        self.driver.find_element(By.NAME, "cena").clear()
        self.driver.find_element(By.NAME, "cena").send_keys("1111")
        self.driver.find_element(By.TAG_NAME, "button").click()

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
'''
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")
# print(driver.title)
# assert "Pepes pizza-Home page" in driver.title# Correct
# assert "Pepes pizza-Gay page" in driver.title# Wrong

# driver.find_element(By.LINK_TEXT, "Picy").click()

#h2 = driver.find_element(By.TAG_NAME, "h2").text
#assert h2 == "Nabídka pic"

# driver.back() # <- vrátit se na předchozí stránku

#info_prvni_picy = driver.find_element(By.XPATH, "//ol/li[1]").text
#assert info_prvni_picy == "čoky: 123"

#driver.find_element(By.LINK_TEXT, "Objednej").click()
#driver.find_element(By.NAME, "nazev").clear()
#driver.find_element(By.NAME, "nazev").send_keys("piko")
#driver.find_element(By.NAME, "mnozstvi").clear()
#driver.find_element(By.NAME, "mnozstvi").send_keys("123")
#driver.find_element(By.TAG_NAME, "button").click()

# driver.find_element(By.NAME, "nazev").send_keys(Keys.RETURN) # <- press enter

driver.find_element(By.LINK_TEXT, "Vytvor").click()
driver.find_element(By.NAME, "nazev").clear()
driver.find_element(By.NAME, "nazev").send_keys("nova pica")

driver.find_element(By.NAME, "cena").clear()
driver.find_element(By.NAME, "cena").send_keys("1111")
driver.find_element(By.TAG_NAME, "button").click()


driver.get("http://127.0.0.1:5000/picy")



driver.close()
'''