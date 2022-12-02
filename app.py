import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from word_finder import lettersIn
from word_finder import lettersNotIn
from word_finder import known_to_be_right
from word_finder import known_to_be_wrong
from word_finder import possible
from word_finder import main

current_word = ""
driver = webdriver.Chrome("/Users/lucas/Projects/SeleniumTest/Browsers/chromedriver")
actions = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.nytimes.com/games/wordle/index.html")
time.sleep(1)
driver.find_element(By.ID, "pz-gdpr-btn-accept").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74").click()
time.sleep(1)
div = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
time.sleep(1)
possible.append("loath")
for i in range(6):
    current_word = possible[0]
    driver.find_element(By.TAG_NAME, "body").send_keys(current_word, Keys.ENTER)
    time.sleep(3)
    count = 0
    for element in div[(i * 5):(i * 5 + 5)]:
        time.sleep(1)
        state = element.get_attribute("data-state")
        letter = element.text.lower()
        print(state, letter, count)
        if state == "empty":
            break
        elif state == "present":
            if letter not in lettersIn:
                lettersIn.append(letter)
            if letter not in known_to_be_wrong[count]:
                known_to_be_wrong[count].append(letter)
        elif state == "absent":
            if letter not in lettersNotIn and letter not in known_to_be_right:
                lettersNotIn.append(letter)
            if letter not in known_to_be_wrong[count]:
                known_to_be_wrong[count].append(letter)
        elif state == "correct":
            if letter not in lettersIn:
                lettersIn.append(letter)
            known_to_be_right[count] = letter
        count += 1
    main()
    if len(possible) == 1:
        break


time.sleep(30)
driver.close()

print("wordle solving successfully completed")


