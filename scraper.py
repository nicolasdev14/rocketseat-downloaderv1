from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_course_name(driver):
    title = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    return title.text.strip().split("\n")[0]


def get_lessons(driver):
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*"))
    )

    lessons = []
    seen = set()

    elements = driver.find_elements(By.XPATH, "//*[contains(@href, '/aula/')]")

    for el in elements:
        href = el.get_attribute("href")
        title = el.text.strip()

        if href and href not in seen:
            seen.add(href)

            if not title:
                title = f"Aula {len(lessons)+1}"

            lessons.append({
                "title": title,
                "url": href
            })

    return lessons