# 🎧 The Message Episode Downloader

This is a simple, powerful Python script that **automatically downloads full MP3s** of _The Message_ radio show from The Current’s website.

Built for efficiency, flexibility, and clean results.

---

## 🚀 What It Does

- Scans the archive at: https://www.thecurrent.org/programs/the-message  
- Extracts all `.mp3` episode links hidden inside embedded JavaScript  
- Downloads them to a folder named `the_message_episodes`  
- Skips duplicates — no redownloading  
- Default: grabs the **latest 5 pages** of episodes (roughly 20–30 total)
- Optional: change the number of pages to get **all available episodes (up to 31 pages!)**

---

## 🛠️ How to Use

### 1. Clone or Create the Script Folder

```bash
mkdir the_message_downloader
cd the_message_downloader
```

### 2. Create the Script File

```bash
nano main.py
```

Then paste in the full script below 👇

---

## 💾 The Full Script (`main.py`)

```python
import os
import re
import requests
from bs4 import BeautifulSoup

# ✅ Settings
DOWNLOAD_FOLDER = "the_message_episodes"
BASE_URL = "https://www.thecurrent.org/programs/the-message/"
NUM_PAGES = 5  # ⬅️ CHANGE THIS to 31 for ALL episodes

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def extract_and_download():
    downloaded = 0
    for page in range(1, NUM_PAGES + 1):
        print(f"\n📄 Scanning page {page}...")
        url = f"{BASE_URL}{page}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        for script in soup.find_all("script"):
            if "__next_f.push" in script.text and ".mp3" in script.text:
                matches = re.findall(r'https://play\.publicradio\.org/unreplaced_ua/[^\"]+\.mp3', script.text)
                for link in set(matches):
                    filename = link.split("/")[-1]
                    path = os.path.join(DOWNLOAD_FOLDER, filename)

                    if os.path.exists(path):
                        print(f"✅ Already downloaded: {filename}")
                        continue

                    print(f"⬇️  Downloading: {filename}")
                    audio = requests.get(link)
                    with open(path, "wb") as f:
                        f.write(audio.content)
                    downloaded += 1

    print(f"\n✅ Done! Total new files downloaded: {downloaded}")

if __name__ == "__main__":
    extract_and_download()
```

---

## ▶️ Run the Script

```bash
python3 main.py
```

It will:
- Scan the last 5 pages of episodes
- Download new MP3s
- Skip any already-downloaded files

---

## 🔧 Optional Settings

| Setting      | What It Does                        | Default | Notes                           |
|--------------|-------------------------------------|---------|----------------------------------|
| `NUM_PAGES`  | How many pages of shows to scan     | `5`     | Set to `31` to get **everything** |
| `DOWNLOAD_FOLDER` | Where files get saved             | `the_message_episodes` | You can change the folder name |

---

## 🧠 Best Practices

- 🔁 **Run this weekly** to stay up to date (use a cron job or reminder)
- 💾 **Keep your folder backed up** (Dropbox/Drive recommended)
- 🛑 **Never delete episodes manually** — the script skips existing ones so you can just re-run it anytime
- 🧪 Test by setting `NUM_PAGES = 1` if you're just trying it out
- 🎯 Rename or organize episodes further if you want to sync with a music player

---

## 🫶 Made With

- `requests` for fetching web pages and files  
- `beautifulsoup4` for parsing the HTML and JavaScript  
- Raw hustle and simplicity — no bloated dependencies  

---

## 📦 To Install Dependencies

If needed:

```bash
pip3 install requests beautifulsoup4
```

---

## ✅ Final Thoughts

This was built from scratch with real-world testing, smooth setup, and fast results in mind. If you need more features (like:

- a GUI  
- auto `.txt` file of links  
- integration with iTunes or Spotify-style player  
- or a Mac `.app` you can double-click  

Just say the word — we’ll build it.

---

You’re all set. Run it. Own it. 🎙️
