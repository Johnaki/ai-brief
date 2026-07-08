	import os
	import requests
	import datetime
	def generate_html():
	    # 这里后续可接入大模型API动态生成内容，现用模板演示
	    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	    html_content = f"""
	    <div style="font-family: sans-serif; max-width: 680px; margin: auto; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
	      <div style="background: #000428; color: #fff; padding: 20px; text-align: center;">
	        <h1 style="margin:0; font-size: 22px;">全球商业与投资全景情报</h1>
	        <p style="margin:5px 0 0; opacity: 0.8;">{time_str} · 云端自动推送</p>
	      </div>
	      <div style="padding: 20px;">
	        <p style="color:#555;">此处为AI实时生成的政经、科技、A股及宏观情报内容。点击下方链接查看完整高清图文页面。</p>
	      </div>
	    </div>
	    """
	    return html_content
	def send_serverchan(html):
	    key = os.environ.get('SERVERCHAN_KEY')
	    if not key:
	        print("未配置SERVERCHAN_KEY")
	        return
	    # Server酱的Markdown支持部分HTML标签渲染，这里直接发送HTML核心内容
	    url = f"https://sctapi.ftqq.com/{key}.send"
	    data = {
	        "title": f"📊 全景投资情报 - {datetime.datetime.now().strftime('%H:%M')}",
	        "desp": html
	    }
	    response = requests.post(url, data=data)
	    print(f"推送结果: {response.json()}")
	if __name__ == "__main__":
	    html = generate_html()
	    send_serverchan(html)
