import smtplib
import base64
import os
from email.message import EmailMessage
from openai import OpenAI

LINKS = [{"name": "熊本馬刺しドットコム", "url": "https://kumamoto-basasi.com/ad/FS3901_a.html"}]

def run():
    index = 0
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.images.generate(model="gpt-image-2", prompt="Professional food photography, raw horse meat for dogs", n=1, size="1024x1024")
    
    img_bytes = base64.b64decode(response.data[0].b64_json)
    msg = EmailMessage()
    msg['Subject'] = f"【本日の厳選】{LINKS[index]['name']}"
    msg.set_content(f"今日のイチオシ！\n{LINKS[index]['url']}")
    msg.add_attachment(img_bytes, maintype='image', subtype='jpeg', filename='food.jpg')

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("inurukurumu@gmail.com", os.environ["APP_PASS"])
        server.send_message(msg)

if __name__ == "__main__":
    run()
