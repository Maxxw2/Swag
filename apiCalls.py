import requests
from pathlib import Path
import time
x = 1

while x > 0:
    time.sleep (1)
    def download_image(url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved to {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")

    def main():
        api_url = "https://inspirobot.me/api?generate=true"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            image_url = response.text.strip()
            script_directory = Path(__file__).resolve().parent
            save_path = script_directory / "downloadedImage.png"

            download_image(image_url, save_path)
        else:
            print(f"Failed to fetch image URL. Status code: {response.status_code}")

    if __name__ == "__main__":
        main()

