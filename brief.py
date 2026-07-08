import os
import requests
import datetime

time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

html_content = f"""
<div style="font-family: sans-serif; max-width: 680px; margin: auto; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
<div style="background: #000428; color: #fff; padding: 20px; text-align: center;">
<h1 style="margin:0; font-size: 22px;">全球商业与投资全景情报</h1>
<p style="margin:5px 0 0; opacity: 0.8;">{time_str} · 云端自动推送</p>
</div>
<div style="padding: 20px;">
<p style="color:#555;">测试成功！链路已打通。后续将在此处接入AI生成的丰富图文内容。</p>
</div>
</div>
"""

key = os.environ.get('SERVERCHAN_KEY')
if not key:
print("Error: SERVERCHAN_KEY is not set!")
exit(1)

url = f"https://sctapi.ftqq.com/{key}.send"
data = {
"title": f"📊 全景投资情报 - {time_str}",
"desp": html_content
}

response = requests.post(url, data=data)
print(f"Status: {response.status_code}, Response: {response.text}")

if response.status_code != 200:
exit(1)
