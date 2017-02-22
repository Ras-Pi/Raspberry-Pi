# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 发送邮件
def sendEmail(smtpserver,username,password,sender,receiver,subject,msghtml):
    msg = MIMEText(msghtml, 'plain', 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    server = smtplib.SMTP(smtpserver, 25)
    server.set_debuglevel(1)
    server.login(username, password)
    server.sendmail(sender, [receiver], msg.as_string())
    server.quit()

#检查网络连通性
def check_network():
    while True:
        try:
            result=urllib.urlopen('http://www.baidu.com').read()
            print result
            print "Network is Ready!"
            break
        except Exception , e:
            print e
            print "Network is not ready,Sleep 5s..."
            time.sleep(5)
    return True

#获取本级制定接口的ip地址
def get_ip_address():
    s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr

if  __name__ == '__main__' :
    check_network()
    ipaddr= get_ip_address()
    sendEmail("邮件服务器地址，例如：smtp.163.com",'发送者的邮箱地址','发送者的邮箱密码','发送者邮箱','接收者邮箱','IP Address of Raspberry PI',ipaddr)
