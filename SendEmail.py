from email.mime.text import MIMEText
import smtplib
mailto_list = ["XXX@qq.com"]  #目标邮箱
mail_host = "smtp.163.com"
mail_user = "XXX@163.com"#发送方
mail_pass = "xxxx"  #163邮箱smtp生成的密码
def send_mail(to_list, sub, content):
    me = "LogServer"+"<"+mail_user+">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user, mail_pass)
    for i in range(0,10):
        server.sendmail(me, to_list, msg.as_string())
    server.close()
if __name__ == '__main__':
        send_mail(mailto_list, '爬虫邮件', '爬虫邮件')