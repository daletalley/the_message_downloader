import os
import re
import requests
from bs4 import BeautifulSoup
 
# Create download folder
DOWNLOAD_FOLDER = "the_message_episodes"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Base URL
BASE_URL = "https://www.thecurrent.org/programs/the-message/"

# How many pages to scan
NUM_PAGES = 32

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


