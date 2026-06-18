from selenium.webdriver.common.by import By


def get_course_name(driver):
    return driver.find_element(By.TAG_NAME, "h2").text


def get_lessons(driver):
    lessons = []
    elements = driver.find_elements(By.TAG_NAME, "a")

    seen = set()

    for el in elements:
        href = el.get_attribute("href")

        if not href:
            continue

        if "/aula/" not in href:
            continue

        if href in seen:
            continue

        seen.add(href)

        title = el.text.strip()

        if not title:
            continue

        lessons.append({
            "title": title,
            "url": href
        })

    return lessons