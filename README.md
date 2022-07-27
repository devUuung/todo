# todo

![ezgif com-gif-maker](https://user-images.githubusercontent.com/87903147/181086375-f52ecbb0-cb5f-4b67-ba21-2484186737fe.gif)

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

# Notion API 기능 추가

```py
import requests
from dotenv import load_dotenv
import os

load_dotenv()

database_id = os.environ.get("NOTION_DATABASE")
notion_api = os.environ.get("NOTION_API")
url = "https://api.notion.com/"

def main():
    while True:
        print("번호를 입력해주세요. (1. 할일추가 2. 할일보기 3. 할일완료 0. 종료)")
        num = int(input())
        if not num:
            break
        elif num == 1:
            print("할일이 무엇인가요? ")
            requests.post(
                url+"v1/pages",
                json =
                {
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
                headers =
                {
                    "Accept": "application/json",
                    "Notion-Version": "2022-06-28",
                    "Content-Type": "application/json",
                    "Authorization": f"{notion_api}"
                }
            )
        elif num == 2:
            response = requests.post(
                url+f"v1/databases/{database_id}/query", 
                json = {
                    "page_size": 100
                }, 
                headers =
                {
                    "Accept": "application/json",
                    "Notion-Version": "2021-08-16",
                    "Content-Type": "application/json",
                    "Authorization": f"{notion_api}"
                }
            )
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
            response = requests.post(
                url+f"v1/databases/{database_id}/query", 
                json = {
                    "page_size": 100
                }, 
                headers = {
                    "Accept": "application/json",
                    "Notion-Version": "2021-08-16",
                    "Content-Type": "application/json",
                    "Authorization": f"{notion_api}"
                }
            )
            print("무슨 일을 완료했나요?")
            text = input()
            for result in response.json()["results"]:
                if result["properties"]["Name"]["title"][0]["plain_text"] == text:
                    page_id = result["url"].split("/")[-1].split("-")[-1]
            if page_id:
                requests.patch(
                    url+f"v1/pages/{page_id}", 
                    json = {
                        "archived": True
                    }, 
                    headers = {
                        "Accept": "application/json",
                        "Notion-Version": "2022-06-28",
                        "Content-Type": "application/json",
                        "Authorization": f"{notion_api}"
                    }
                )
                print("일을 완료했습니다.")
            else:
                print("완료할 일을 찾지 못했습니다.")

if __name__ == "__main__":
    main()
```

# 기록

- 2022-07-13 콘솔버전 간단한 ToDo앱 구현
- 2022-07-14 Todo앱 NOTION_DB 기능 추가 계획
  - 2022-07-14 NOTION_DB_CREATE 기능 구현
  - 2022-07-15 NOTION_DB_READ 기능 구현
  - 2022-07-15 NOTION_DB_DELETE 기능 구현
- 2022-07-26 Todo앱 MVC패턴화
