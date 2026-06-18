import os
from auth import create_driver, inject_cookies
from scraper import get_course_name, get_lessons
from downloader import get_m3u8, download_video
from utils import sanitize, load_progress, save_progress
def run_downloader(course_url, cookies):


def main():
    progress = load_progress()

    driver = create_driver()

    print("Injetando cookies...")
    inject_cookies(driver, cookies)

    print("Abrindo curso...")
    driver.get(course_url)

    input("Quando carregar tudo, pressione ENTER...")

    course_name = sanitize(get_course_name(driver))
    course_path = os.path.join("downloads", course_name)

    os.makedirs(course_path, exist_ok=True)

    lessons = get_lessons(driver)

    for index, lesson in enumerate(lessons, start=1):
        if lesson["url"] in progress["completed"]:
            print(f"Pulando: {lesson['title']}")
            continue

        print(f"Baixando {lesson['title']}")

        driver.get(lesson["url"])

        input("Espere carregar o vídeo e pressione ENTER...")

        m3u8 = get_m3u8(driver)

        if not m3u8:
            print("m3u8 não encontrado")
            continue

        filename = f"{index:02d} - {sanitize(lesson['title'])}.%(ext)s"
        output = os.path.join(course_path, filename)

        download_video(m3u8, output)

        progress["completed"].append(lesson["url"])
        save_progress(progress)

    driver.quit()
    print("Finalizado.")


if __name__ == "__main__":
    pass