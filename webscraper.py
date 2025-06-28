import requests
from bs4 import BeautifulSoup

# URLを指定
url = "https://www.python.org/"

# ページを取得
response = requests.get(url)
# HTML解析
soup = BeautifulSoup(response.text, "html.parser")

#タイトルを取得
title = soup.title.string

#説明文（meta description）を取得
description_tag = soup.find("meta", attrs={"name": "description"})
description =description_tag["content"] if description_tag else "説明文が見つかりません"

# イベント情報を取得（最大5件）
events = []
event_section = soup.find("div", class_="medium-widget event-widget last")
if event_section:
    event_list = event_section.find_all("li", limit=5)
    for event in event_list:
        event_title = event.find("a").text
        event_date = event.find("time").text
        events.append(f"{event_date}: {event_title}")

#結果を表示
print(f"タイトル: {title}")
print(f"説明文:{description}")
print("イベント情報:")
for event in events:
    print(event)
