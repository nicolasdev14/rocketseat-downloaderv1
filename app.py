import tkinter as tk
from tkinter import messagebox
import threading
from main import run_downloader

def start_download():
    course_url = entry_course.get()
    adonis = entry_adonis.get()
    skylab = entry_skylab.get()

    if not course_url or not adonis or not skylab:
        messagebox.showerror(
            "Erro",
            "Preencha todos os campos"
        )
        return

    cookies = [
        {
            "name": "adonis-session",
            "value": adonis,
            "domain": ".rocketseat.com.br"
        },
        {
            "name": "skylab_next_access_token",
            "value": skylab,
            "domain": ".rocketseat.com.br"
        }
    ]

    print("Curso:", course_url)
    print("Cookies carregados")

    # aqui chama o main downloader
    run_downloader(course_url, cookies)


root = tk.Tk()
root.title("Rocketseat Downloader")
root.geometry("700x400")

tk.Label(root, text="URL do curso").pack()
entry_course = tk.Entry(root, width=80)
entry_course.pack()

tk.Label(root, text="adonis-session").pack()
entry_adonis = tk.Entry(root, width=80)
entry_adonis.pack()

tk.Label(root, text="skylab access token").pack()
entry_skylab = tk.Entry(root, width=80)
entry_skylab.pack()

btn = tk.Button(
    root,
    text="Iniciar Download",
    command=lambda: threading.Thread(
        target=start_download
    ).start()
)
btn.pack(pady=20)

root.mainloop()