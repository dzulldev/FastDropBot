# 🎬 Telegram Video Downloader Bot

A simple and lightweight Telegram bot that lets you download videos from **Instagram**, **TikTok**, **Twitter**, and **YouTube** — right from your chat.

---

## ✨ Features
- 🔗 Supports direct video links from:
  - Instagram
  - TikTok
  - Twitter
  - YouTube
- 🚀 Fast and lightweight
- 🧠 Smart URL resolver (handles short links)
- 🗂️ Saves unique user IDs (basic logging)
- 🔐 Safe token handling using environment variables

---

## 📦 Requirements
- Python 3.x
- Pip packages:
  - `requests`
  - `yt-dlp`

Install with:
```bash
pip install requests yt-dlp

🚀 Getting Started

1. Export your bot token:



export BOT_TOKEN=your_telegram_bot_token

2. Run the bot:



python bot.py

> 💡 Make sure your bot is started on Telegram and has permission to receive messages.




---

📁 Output

All downloaded videos will be saved in the downloads/ folder before being sent back to the user.


---

🔒 Security Tip

Never hardcode your token inside the script. Always use environment variables like this project does:

TOKEN = os.getenv('BOT_TOKEN')


---

☕ Author

Made with ❤️ by [YourNameHere]
