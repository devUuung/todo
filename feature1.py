import requests

url = "https://api.notion.com/v1/databases/cbaba5e4327b46a38d7af82abf7d29ab"

payload = {"properties": "이름"}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
    "Authorization": "Bearer secret_6tcCZwI8UChaAKW9BGYY33ZBQPZg2aoFlGxxj4VuEGI"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)
