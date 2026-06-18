from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_course_name(driver):
    title = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1, h2"))
    )
    return title.text


def get_lessons(driver):
    lessons = []

    items = driver.find_elements(By.TAG_NAME, "a")

    for item in items:
        href = item.get_attribute("href")
        title = item.text.strip()

        if href and "/aula/" in href and title:
            lessons.append({
                "title": title,
                "url": href
            })

    return lessons