import requests
from dotenv import load_dotenv
import os

load_dotenv()

database_id = os.environ.get("NOTION_DATABASE")
notion_api = os.environ.get("NOTION_API")

url = "https://api.notion.com/v1/pages"

payload = {
    "parent": {
        "type": "database_id",
        "database_id": f"{database_id}"
    },
    "properties": {
        "Name": {
            "title":
            [
                {
                    "type": "text",
                    "text": {"content": "The title"}
                }
            ]
        }
    }
}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
    "Authorization": f"{notion_api}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
