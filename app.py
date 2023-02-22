from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

elements = driver.find_elements(By.ID, 'video-title')

# for e in elements:
#     print(e.text)

with open("recommended_videos.txt", "w", encoding="utf8") as f:
    for e in elements:
        f.write(e.text + "\n")

driver.quit()