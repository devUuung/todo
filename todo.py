import requests
from dotenv import load_dotenv
import os

load_dotenv()

todoList = []
database_id = os.environ.get("NOTION_DATABASE")
notion_api = os.environ.get("NOTION_API")
url = "https://api.notion.com/v1/pages"


def main():
    while True:
        print("번호를 입력해주세요. (1. 할일추가 2. 할일보기 3. 할일완료 0. 종로)")
        num = int(input())
        if not num:
            break
        elif num == 1:
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
            for todo in todoList:
                print(todo)
        elif num == 3:
            print("무슨일을 완료했나요?")
            todoList.remove(input())


if __name__ == "__main__":
    main()
