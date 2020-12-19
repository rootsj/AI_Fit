import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import string
import random


def make_code():
    string_pool = string.ascii_letters + string.digits

    code = ""
    for _ in range(8):
        code += random.choice(string_pool)

    return code


def send_code(email_from, email_password, email_to, code):
    # 제목
    subject = '안녕하세요. 요청하신 인증 코드입니다.'

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = subject

    # 본문
    body = []
    body.append(f'안녕하세요. AI-Fit입니다.\n')
    body.append(f'요청하신 인증 코드 보내드립니다.\n')
    body.append(f'인증 코드: {code}\n')
    body.append(f'감사합니다.\n')
    body = ''.join(body)

    msg.attach(MIMEText(body, 'plain'))

    # 보내기
    text = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_from, email_password)
        server.sendmail(email_from, email_to, text)
    except:
        return False
    else:
        return True
    finally:
        server.quit()
