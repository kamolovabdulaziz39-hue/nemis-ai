import time
import requests
import os
import threading

def ping_server():
    url = os.getenv("RENDER_EXTERNAL_URL", "https://nemis-ai.onrender.com")
    while True:
        try:
            time.sleep(300) # 5 minutes
            requests.get(url)
            print(f"Pinged {url} to keep alive")
        except Exception as e:
            print(f"Ping failed: {e}")

if __name__ == "__main__":
    ping_server()
