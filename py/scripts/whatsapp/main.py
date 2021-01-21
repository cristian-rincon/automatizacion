import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


description = "Send messages using whatsapp web and python."
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)


class WhatsappBotHandler():

    def __init__(self):
        self.description = description

    def send_message(self, user, msg):
        """
        Send one message to a group or person.
        """
        try:

            user_path = f'//span[@title="{user}"]'
            user = wait.until(
                EC.presence_of_element_located((By.XPATH, user_path)))
            user.click()
            msg_path = '//div[@class="_1awRl copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
            msg_box = wait.until(
                EC.presence_of_element_located((By.XPATH, msg_path)))
            # msg += '\n _this is a system generated message_'
            msg_box.send_keys(msg + Keys.ENTER)
        except Exception as e:
            print(e)
            self.end_process()

    def end_process(self):
        """
        Close browser function.
        """
        driver.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--cli", help="Get information from cli.", action="store_true")
    args = parser.parse_args()

    if args.cli:
        print("Cli mode on")
        user = input('Enter the name of user or group : ')
        msg = input('Enter your message : ')
        wsp_bot = WhatsappBotHandler()

        wsp_bot.send_message(user, msg)
