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
# div = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
div = driver.find_elements(By.CLASS_NAME, "Tile-module_tile__3ayIZ")
time.sleep(1)
possible.append("loath")
# main()
for i in range(6):
    current_word = possible[0]
    driver.find_element(By.TAG_NAME, "body").send_keys(current_word, Keys.ENTER)
    # time.sleep(4)
    # time.sleep(3)
    time.sleep(3)
    print(i)
    start = (i * 5)
    end = (i * 5 + 5)
    print(start, end)
    count = 0
    for element in div[start:end]:
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
            if letter not in lettersNotIn:
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
# divs = div.find_elements(By.TAG_NAME, "div")
# for i in range(6):
#     driver.find_element(By.TAG_NAME, "body").send_keys(current_word, Keys.ENTER)
#     main()
#     time.sleep(5)
#     # print(possible)
#     for j in range(5):
#         state = div[j + i].get_attribute("data-state")
#         letter = div[j + i].text.lower()
#         print(state, letter, j)
#         if state == "present":
#             if letter not in lettersIn:
#                 lettersIn.append(letter)
#             # if letter not in known_to_be_wrong[j - (5 * i)]:
#             if letter not in known_to_be_wrong[j]:
#                 known_to_be_wrong[j].append(letter)
#         elif state == "absent":
#             if letter not in lettersNotIn:
#                 lettersNotIn.append(letter)
#             if letter not in known_to_be_wrong[j]:
#                 known_to_be_wrong[j].append(letter)
#         elif state == "correct":
#             if letter not in lettersIn:
#                 lettersIn.append(letter)
#             known_to_be_right[j] = letter


print(lettersIn)
print(lettersNotIn)
print(known_to_be_right)
print(known_to_be_wrong)


# html_str = div.get_attribute('innerHTML')
# bs = BeautifulSoup(html_str, 'lxml')

# print(div)

# driver.find_element(By.NAME, "q").send_keys("javatpoint")
# time.sleep(1)
# driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(30)
driver.close()

print("sample test case successfully completed")


