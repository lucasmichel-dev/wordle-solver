import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from word_finder import check_done
from word_finder import get_current_word
from word_finder import main
from word_finder import remove_wrong_word

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.nytimes.com/games/wordle/index.html")
time.sleep(1)
driver.find_element(By.ID, "pz-gdpr-btn-accept").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74").click()
time.sleep(1)
div = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
time.sleep(1)
body = driver.find_element(By.TAG_NAME, "body")

for i in range(6):
    successful = False
    done = False
    if done:
        break
    while not successful:
        current_word = get_current_word()
        body.send_keys(current_word, Keys.ENTER)
        time.sleep(3)
        if check_done():
            done = True
            break
        count = 0
        correct = set()
        present = set()
        absent = set()
        for element in div[(i * 5):(i * 5 + 5)]:
            time.sleep(1)
            state = element.get_attribute("data-state")
            letter = element.text.lower()
            print(state, letter)
            if state in ["correct", "present", "absent"]:
                successful = True
            if state == "correct":
                correct.add(letter + ":" + str(count))
            elif state == "present":
                present.add(letter + ":" + str(count))
            elif state == "absent":
                absent.add(letter)
            else:
                remove_wrong_word(current_word)
                for j in range(5):
                    body.send_keys(Keys.BACKSPACE)
                break
            count += 1
        main(correct, present, absent)


print("wordle solving successfully completed")
time.sleep(30)
driver.close()
