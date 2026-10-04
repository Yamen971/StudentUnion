from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ضع بياناتك هنا على جهازك فقط
BOT_TOKEN = "8908486402:AAE9L3x_xNP_Le3UhZ0w12RxVAj85yGg9RM"
CHAT_ID = "-1003990005366"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send_message():

    name = request.form.get("name")
    class_name = request.form.get("class_name")
    phone = request.form.get("phone")
    problem = request.form.get("problem")

    message = f"""
📢 رسالة جديدة إلى اتحاد الطلاب
━━━━━━━━━━━━━━━━

👤 الاسم:
{name}

🏫 الفصل / الشعبة:
{class_name}

📱 رقم الهاتف:
{phone}

📝 المشكلة / المقترح:
{problem}

━━━━━━━━━━━━━━━━
أمين الطلاب: يامن ياسر
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    if response.json().get("ok"):

        return """
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">

        <head>
            <meta charset="UTF-8">
            <title>تم الإرسال</title>
        </head>

        <body style="text-align:center; padding:80px; font-family:Arial;">

            <h1>✅ تم إرسال رسالتك بنجاح</h1>

            <p>
                شكرًا لتواصلك مع اتحاد الطلاب.
            </p>

            <a href="/">
                العودة إلى الصفحة الرئيسية
            </a>

        </body>

        </html>
        """

    else:

        print(response.json())

        return """
        <h1>❌ حدث خطأ أثناء الإرسال</h1>
        <p>حاول مرة أخرى.</p>
        """


if __name__ == "__main__":
    app.run(debug=True)
