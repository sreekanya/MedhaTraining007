# sending email using smtp
import smtplib

from_add = 'gitapatel245@gmail.com'
to_add = 'appigeeta@gmail.com'

test_msg = "Hello this is test email sent from script"

uname = 'gitapatel245@gmail.com'
pword = 'python245'

server = smtplib.SMTP_SSL("smtp.gmail.com",465,)
print "starting ssl server"
#server.startssl()
print "logging in with user name & password"
server.login(uname,pword)
print "sending email..."
server.sendmail(from_add,to_add,test_msg)
print "stopping server.."
server.quit()
# script working