import os
import requests
import datetime
 
time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
 
markdown_content = f"""
# 📊 全球商业与投资全景情报
> **{time_str} · 云端自动推送**
 
测试成功！链路已打通。后续将在此处接入AI生成的丰富图文内容。
"""
 
key = os.environ.get('SERVERCHAN_KEY')
if not key:
    print("Error: SERVERCHAN_KEY is not set!")
    exit(1)
 
url = f"https://sctapi.ftqq.com/{key}.send"
data = {
    "title": f"📊 全景投资情报 - {time_str}",
    "desp": markdown_content
}
 
response = requests.post(url, data=data)
print(f"Status: {response.status_code}, Response: {response.text}")
 
if response.status_code != 200:
    exit(1)
