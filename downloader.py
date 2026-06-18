import re
import yt_dlp


def get_m3u8(driver):
    logs = driver.get_log("performance")

    for log in logs:
        message = log["message"]

        if ".m3u8" in message:
            match = re.search(r'https://[^"]+\.m3u8', message)

            if match:
                return match.group(0)

    return None


def download_video(m3u8_url, output_path):
    options = {
        "outtmpl": output_path,
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([m3u8_url])