import requests
from dotenv import load_dotenv
import os

load_dotenv()

database_id = os.environ.get("NOTION_DATABASE")
notion_api = os.environ.get("NOTION_API")
url = "https://api.notion.com/"


def create(message):
    requests.post(
        url+"v1/pages",
        json={
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
                                "text": {"content": f"{message}"}
                            }
                        ]
                }
            }
        },
        headers={
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
            "Authorization": f"{notion_api}"
        }
    )
    return True


def read():
    response = requests.post(
        url+f"v1/databases/{database_id}/query",
        json={
            "page_size": 100
        },
        headers={
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"{notion_api}"
        }
    )
    return [result["properties"]["Name"]["title"][0]["plain_text"] for result in response.json()["results"]]


def delete(text):
    for result in response.json()["results"]:
        if result["properties"]["Name"]["title"][0]["plain_text"] == text:
            page_id = result["url"].split("/")[-1].split("-")[-1]
    if page_id:
        requests.patch(
            url+f"v1/pages/{page_id}",
            json={
                "archived": True
            },
            headers={
                "Accept": "application/json",
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json",
                "Authorization": f"{notion_api}"
            }
        )
        return True
    else:
        return False
