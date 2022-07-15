# todo

# 콘솔버전 todo

```py
todoList = []


def main():
    while True:
        print("번호를 입력해주세요. (1. 할일추가 2. 할일보기 3. 할일완료 0. 종로)")
        num = int(input())
        if not num:
            break
        elif num == 1:
            print("할일이 무엇인가요? ")
            todoList.append(input())
        elif num == 2:
            for todo in todoList:
                print(todo)
        elif num == 3:
            print("무슨일을 완료했나요?")
            todoList.remove(input())


if __name__ == "__main__":
    main()

```

# Notion API 기능 추가 (코드 정리 필요)

```py
import requests
from dotenv import load_dotenv
import os

load_dotenv()

database_id = os.environ.get("NOTION_DATABASE")
notion_api = os.environ.get("NOTION_API")


def main():
    while True:
        print("번호를 입력해주세요. (1. 할일추가 2. 할일보기 3. 할일완료 0. 종로)")
        num = int(input())
        if not num:
            break
        elif num == 1:
            url = "https://api.notion.com/v1/pages"
            print("할일이 무엇인가요? ")
            requests.post(
                url,
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
                                        "text": {"content": f"{input()}"}
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
        elif num == 2:
            url = f"https://api.notion.com/v1/databases/{database_id}/query"
            payload = {"page_size": 100}
            headers = {
                "Accept": "application/json",
                "Notion-Version": "2021-08-16",
                "Content-Type": "application/json",
                "Authorization": f"{notion_api}"
            }
            response = requests.post(url, json=payload, headers=headers)
            for result in response.json()["results"]:
                print(result["properties"]["Name"]["title"][0]["plain_text"])
        elif num == 3:
            url = f"https://api.notion.com/v1/databases/{database_id}/query"
            payload = {"page_size": 100}
            headers = {
                "Accept": "application/json",
                "Notion-Version": "2021-08-16",
                "Content-Type": "application/json",
                "Authorization": f"{notion_api}"
            }
            response = requests.post(url, json=payload, headers=headers)
            print("무슨 일을 완료했나요?")
            text = input()
            for result in response.json()["results"]:
                if result["properties"]["Name"]["title"][0]["plain_text"] == text:
                    page_id = result["url"].split("/")[-1].split("-")[-1]
                    url = f"https://api.notion.com/v1/pages/{page_id}"

                    payload = {"archived": True}
                    headers = {
                        "Accept": "application/json",
                        "Notion-Version": "2022-06-28",
                        "Content-Type": "application/json",
                        "Authorization": f"{notion_api}"
                    }

                    response = requests.patch(
                        url, json=payload, headers=headers)


if __name__ == "__main__":
    main()
ㅁ
```

# 기록

- 2022-07-13 콘솔버전 간단한 ToDo앱 구현
- 2022-07-14 Todo앱 NOTION_DB 기능 추가 계획
  - 2022-07-14 NOTION_DB_CREATE 기능 구현
  - 2022-07-15 NOTION_DB_READ 기능 구현
  - 2022-07-15 NOTION_DB_DELETE 기능 구현
