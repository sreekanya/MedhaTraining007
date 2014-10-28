#/usr/bin/python
import smtplib

To='renuga.suresh@gmail.com'
SUBJECT='send mail using smtp'
TEXT='Here is the Message to be sent'

gmail_sender='abc@gmail.com'
gmail_pwd='xyz'

server.smtplib.SMTP('smtp.gmail.com',587)
server.eclo()
server.starttls()
server.ecloserver.login(gmail_sender,gmail_pwd)

Body='\r\n'.join([
		'TO:%s'%TO,
		'From%s'%gmail_sender,
		'Subject%s'%SUBJECT,
		'',
		TEXT])
try:
	server.sendmail(gmail_sender,[TO],Body)
	print 'email sent'
except:
	print 'error in sending mail'
server.quit()
