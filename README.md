# 📝 Sobre o Projeto

O **Rocketseat Downloader** é uma ferramenta desenvolvida em Python para automatizar o download de cursos da Rocketseat.

O objetivo do projeto é facilitar o processo de baixar aulas, organizando automaticamente os arquivos em pastas e permitindo continuar downloads interrompidos.

## 🚀 Tecnologias utilizadas

* **Python** — Lógica principal do sistema
* **Selenium** — Automação do navegador
* **yt-dlp** — Download e conversão dos vídeos
* **Tkinter** — Interface gráfica
* **JSON** — Armazenamento de progresso
* **PyInstaller** — Geração do executável

## 🎯 Funcionalidades

* Login usando cookies da Rocketseat
* Leitura automática das aulas
* Captura automática do arquivo `.m3u8`
* Download automático dos vídeos
* Organização em pastas
* Sistema de retomada de downloads
* Interface gráfica simples

## 📂 Estrutura do Projeto

```bash
rocketseat_downloader/
│
├── app.py
├── main.py
├── auth.py
├── scraper.py
├── downloader.py
├── utils.py
├── progress.json
└── downloads/
```

## 🛠️ Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd rocketseat_downloader
```

Instale as dependências:

```bash
pip install selenium webdriver-manager yt-dlp pyinstaller
```

Execute:

```bash
python app.py
```

Ou use o executável:

```bash
dist/app.exe
```

## 📌 Como usar

1. Abra a plataforma da Rocketseat
2. Pressione **F12**
3. Vá em **Application → Cookies**
4. Copie:

   * `adonis-session`
   * `skylab_next_access_token`
5. Cole no aplicativo
6. Cole a URL do curso
7. Clique em **Iniciar Download**

## 👤 Sobre mim

Olá! Meu nome é **Nicolas**, tenho **15 anos** e estou estudando programação com foco em desenvolvimento de software.

Atualmente estou aprendendo e evoluindo em:

* Python
* Automação
* Web Scraping
* HTML5
* CSS3
* JavaScript
* Git e GitHub

Busco sempre criar projetos bem estruturados, organizados e funcionais, aplicando boas práticas de programação.

## 📬 Contato

📧 [itadori7zxwm@gmail.com](mailto:itadori7zxwm@gmail.com)
📧 [nicolasdev703@gmail.com](mailto:nicolasdev703@gmail.com)
