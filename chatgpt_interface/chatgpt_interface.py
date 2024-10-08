import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class ChatGPTInterface:
    def __init__(self, profile_path, chat_url, prompts):
        self.profile_path = profile_path
        self.chat_url = chat_url
        self.prompts = prompts

        if not os.path.exists(self.profile_path):
            os.makedirs(self.profile_path)

        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={self.profile_path}")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_chat(self):
        self.driver.get(self.chat_url)
        self.prompt_user_action("Press 'y' after completing login or captcha to continue...")

    def prompt_user_action(self, message):
        print(message)
        while True:
            if input().lower() == 'y':
                break

    def send_prompt(self, prompt):
        chat_input_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#prompt-textarea"))
        )
        chat_input_box.clear()

        for line in prompt.split('\n'):
            chat_input_box.send_keys(line)
            chat_input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        
        # chat_input_box.send_keys(Keys.RETURN)
        chat_input_box.submit()
        time.sleep(2)

    def get_response(self):
        wait_for_button = WebDriverWait(self.driver, 180)
        send_button = wait_for_button.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='fruitjuice-send-button']"))
        )
        
        response_box = wait_for_button.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@data-message-author-role='assistant']//div[contains(@class, 'markdown')])[last()]"))
        )
        return response_box.get_attribute('innerHTML')

    def process_prompts(self):
        responses = []
        for prompt in self.prompts:
            self.send_prompt(prompt)
            response = self.get_response()
            responses.append((prompt, response))
            # print(response)
        return responses

    def save_profile(self):
        self.driver.quit()
        print(f"Profile saved at {self.profile_path}")