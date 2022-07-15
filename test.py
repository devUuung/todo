import requests

url = "https://api.notion.com/v1/pages/02d3c59d639b43cb9d96636ec0892e5b"

payload = {"archived": True}
headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
    "Authorization": "Bearer secret_6tcCZwI8UChaAKW9BGYY33ZBQPZg2aoFlGxxj4VuEGI"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.text)