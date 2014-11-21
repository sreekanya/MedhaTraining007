import smtplib

#smtplib.SMTP_SSL([465,[]])
#server = smtplib.SMTP('smtp.gmail.com',465)
toaddrs  = 'appigeeta@gmail.com'
#server.login("gitapatel245","python245")
msg ="Hi....using smtp"

#Gmail Login
#
username = 'gitapatel245'
password = 'python245'

#Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:465')
server.starttls()

server.sendmail(fromaddr, toaddrs, msg)
server.quit()
# this script is giving sign-in block email to sender...not working go to SendMailSmtp
