import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.options = Options()
        self.service = Service(driver_path)
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
    
    def closeBrowser(self):
        self.driver.close()
        self.driver.quit()

    def login(self, url, username, password):
        driver = self.driver
        driver.get(url)
        time.sleep(2)
        elm = self.find_web_page_element("id", "verify-bar-close")
        elm.click()
        self.find_web_page_element("xpath", "//*[contains(text(), 'Log in')]").click()
        user_name_elem = self.find_web_page_element("id", "email")
        user_name_elem.clear()
        user_name_elem.send_keys(username)
        passworword_elem = self.find_web_page_element("id", "pass")
        passworword_elem.clear()
        passworword_elem.send_keys(password)
        driver.find_element(By.NAME,'login').click()
        time.sleep(15)
    
    def find_web_page_element(self, identifier, value):
        if identifier == "id":
            element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.ID, value))
                    )
        elif identifier == "xpath":
            element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, value))
                    )
        elif identifier == "name":
            element = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.NAME, value))
                    )
        elif identifier == "partial_link":
            element = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.PARTIAL_LINK_TEXT, value))
                    )
        elif identifier == "class":
            element = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.CLASS_NAME, value))
                    )    
        return element
    
    def get_element_text(self, value):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, value).text
        except Exception as e:
            print(str(e))
            return None
    
    def goto(self, url):
        try:
            self.driver.get(url)
        except:
            self.driver.execute_script("location.reload();")
            self.driver.get(url)
    
    def get_script_data(self, raw_script):
        try:
            script = f'return {raw_script}'
            return self.driver.execute_script(script)
        except Exception as e:
            print(str(e))
    
    def scroll_to_bottom(self):
        old_position = 0
        new_position = None

        while new_position != old_position:
            # Get old scroll position
            time.sleep(1)
            old_position = self.driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                    " window.pageYOffset : (document.documentElement ||"
                    " document.body.parentNode || document.body);"))
            # Sleep and Scroll
            time.sleep(2)
            self.driver.execute_script((
                    "var scrollingElement = (document.scrollingElement ||"
                    " document.body);scrollingElement.scrollTop ="
                    " scrollingElement.scrollHeight;"))
            # Get new position
            new_position = self.driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                    " window.pageYOffset : (document.documentElement ||"
                    " document.body.parentNode || document.body);"))
    
    def take_current_screenshot(self, filename):
        try:
            print("Taking screenshot")
            curr_dir = os.path.dirname(os.path.realpath(__file__))
            filename = f'{filename}.png'
            file_path = os.path.join(curr_dir, "screenshots", filename)
            self.driver.get_screenshot_as_file(file_path)
        except Exception as e:
            # logger.info(f'Error in capturing screenshot, {str(e)}')
            print(f'Error in capturing screenshot, {str(e)}')
