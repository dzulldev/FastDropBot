import os
import time
import requests
import threading
from yt_dlp import YoutubeDL

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# use env variable for token
TOKEN = os.getenv('BOT_TOKEN')
API_URL = f'https://api.telegram.org/bot{TOKEN}'

DOWNLOAD_DIR = 'downloads'
USERS_FILE = 'users.txt'

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

print("✅ Connected")

# save user id
def save_user(chat_id):
    try:
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w") as f:
                f.write(f"{chat_id}\n")
        else:
            with open(USERS_FILE, "r") as f:
                users = f.read().splitlines()
            if str(chat_id) not in users:
                with open(USERS_FILE, "a") as f:
                    f.write(f"{chat_id}\n")
    except Exception as e:
        print(f"[!] failed to save user: {e}")

# resolve short url
def resolve_url(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=5)
        return r.url
    except Exception as e:
        print(f"[!] url resolve error: {e}")
        return url

# telegram api functions
def get_updates(offset=None):
    params = {'timeout': 30, 'offset': offset}
    response = requests.get(f'{API_URL}/getUpdates', params=params)
    return response.json().get('result', [])

def send_message(chat_id, text):
    requests.post(f'{API_URL}/sendMessage', data={'chat_id': chat_id, 'text': text})

def send_video(chat_id, filepath):
    with open(filepath, 'rb') as f:
        requests.post(f'{API_URL}/sendVideo', files={'video': f}, data={'chat_id': chat_id})

# download video to downloads folder
def download_video(url):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title).30s.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print(f"[!] download failed: {e}")
        return None

# process incoming message
def process_message(message):
    chat_id = message['chat']['id']
    save_user(chat_id)

    if 'text' not in message:
        send_message(chat_id, "send me a link from instagram, tiktok, twitter, or youtube.")
        return

    input_url = message['text'].strip()
    resolved_url = resolve_url(input_url)

    if not any(domain in resolved_url for domain in ["instagram.com", "tiktok.com", "twitter.com", "youtu"]):
        send_message(chat_id, "only instagram, tiktok, twitter, or youtube links are supported.")
        return

    threading.Thread(target=handle_download, args=(chat_id, resolved_url)).start()

# handle download and send
def handle_download(chat_id, url):
    send_message(chat_id, "checking the link...")

    if "tiktok.com" in url and ("photo" in url or "aweme_type=150" in url):
        send_message(chat_id, "sorry, tiktok photo posts are not supported.")
        return

    send_message(chat_id, "downloading...")

    filepath = download_video(url)

    if filepath and os.path.exists(filepath):
        try:
            send_video(chat_id, filepath)
            send_message(chat_id, "here is your video.")
        except Exception as e:
            send_message(chat_id, "failed to send video.")
            print(f"[!] sending error: {e}")
    else:
        send_message(chat_id, "failed to download.")

# bot loop
def main():
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)
        for update in updates:
            last_update_id = update['update_id'] + 1
            if 'message' in update:
                process_message(update['message'])
        time.sleep(1)

if __name__ == '__main__':
    main()
