import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(subject,text):
    my_sender = '3454969108@qq.com'
    my_pass = 'll2002073012'
    my_user = '2169258690@qq.com'
    try:
        msg = MIMEText(text, 'HTML', 'utf-8')
        msg['From'] = formataddr([my_sender, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([my_user, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['笨蛋'] = subject  # 邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.163.com", 995)  # 发件人邮箱中的SMTP服务器，端口是80
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是80
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print('发送成功')
    except Exception as e: # 如果 try 中的语句没有执行
            print('发送失败\t\n')
            print(str(e))

mail('笨蛋','你真的很蠢诶！')