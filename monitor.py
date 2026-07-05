import time
import smtplib
from email.message import EmailMessage

# --- معلوماتك ---
EMAIL_ADDRESS = "khalilslema2@gmail.com"
# هام جداً: لازمك تعمل App Password من حساب Google متاعك وتحطها هنا
EMAIL_PASSWORD = "rohw txeh npth mcrg" 
# الرصيد الأولي للمقارنة
INITIAL_BALANCE = 1000 

def send_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"خطأ في إرسال الإيميل: {e}")

def check_balance():
    # هنا تحط الـ API Request متاع Deriv باش تجيب الرصيد الحقيقي
    # مثال بسيط:
    current_balance = 1100 
    
    if current_balance >= INITIAL_BALANCE + 100:
        send_alert("تنبيه تداول", f"مبروك! الرصيد زاد وصل لـ {current_balance}$.")
    elif current_balance <= INITIAL_BALANCE - 50:
        send_alert("تنبيه تداول", f"تنبيه: الرصيد نقص وصل لـ {current_balance}$.")

# الحلقة الرئيسية
print("البوت بدأ في المراقبة...")
while True:
    check_balance()
    time.sleep(60) 
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=10000)
  threading.Thread(target=run_web).start()
while True:
    check_balance()
    time.sleep(60)
