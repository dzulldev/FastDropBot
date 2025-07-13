# FastDropBot

**FastDropBot** is a simple Telegram bot built in Python that lets users download videos from Instagram, TikTok, YouTube, and Twitter — directly through Telegram chat.

## 📦 Features

- 📥 Download from:
  - Instagram
  - TikTok (short/long URLs)
  - YouTube (video only)
  - Twitter
- 🎞️ Sends the video back in best available quality
- 🧠 Automatically resolves short URLs (e.g., `vt.tiktok.com`)
- 🔒 No watermark, no spam, privacy-respecting
- 💾 Logs unique users automatically (one-time)
- ✅ Can be hosted on Termux with `nohup` or `tmux`
  
## ⚙️ Requirements

- Python 3
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- `ffmpeg` (for YouTube audio/video merge)
- `requests` module
- Telegram bot token (get one via [@BotFather](https://t.me/BotFather))

## 🚀 How to Run

```bash
pip install yt-dlp requests
termux-setup-storage
pkg install ffmpeg
python main.py

Or run in background:

nohup python main.py &
```

## 💬 How to Use

1. Open your Telegram bot
   
3. Send a link from:

Instagram
TikTok
Twitter (X)
YouTube

3. The bot will respond with the downloaded video.

No commands needed — just send the link!

📝 License

MIT License — Free to use, modify, and share
