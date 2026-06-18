import os
from auth import create_driver, inject_cookies
from scraper import get_course_name, get_lessons
from downloader import get_m3u8, download_video
from utils import sanitize, load_progress, save_progress


def run_downloader(course_url, cookies):
    progress = load_progress()

    driver = create_driver()

    print("Injetando cookies...")
    inject_cookies(driver, cookies)

    print("Abrindo curso...")
    driver.get(course_url)

    input("Faça login (se precisar) e pressione ENTER...")

    course_name = sanitize(get_course_name(driver))
    print(f"Curso encontrado: {course_name}")

    course_path = os.path.join("downloads", course_name)
    os.makedirs(course_path, exist_ok=True)

    lessons = get_lessons(driver)

    print(f"{len(lessons)} aulas encontradas")

    if len(lessons) == 0:
        print("Nenhuma aula encontrada.")
        driver.quit()
        return

    total = len(lessons)

    for index, lesson in enumerate(lessons, start=1):
        print(f"\n[{index}/{total}] {lesson['title']}")

        if lesson["url"] in progress["completed"]:
            print("Já baixado, pulando...")
            continue

        driver.get(lesson["url"])

        input("Quando o vídeo carregar, pressione ENTER...")

        m3u8 = get_m3u8(driver)

        if not m3u8:
            print("M3U8 não encontrado")
            continue

        filename = f"{index:02d} - {sanitize(lesson['title'])}.mp4"
        output = os.path.join(course_path, filename)

        print("Baixando vídeo...")
        download_video(m3u8, output)

        progress["completed"].append(lesson["url"])
        save_progress(progress)

        percent = (index / total) * 100
        print(f"Progresso: {percent:.1f}%")

    driver.quit()
    print("\nDownload finalizado.")