import smtplib
from_add='gitapatel245@gmail.com'
to_add='naninice@gmail.com'
test_msg='hi through smtp '
uname='gitapatel245'
pssword='python245'
server=smtplib.SMTP('smtp.gmail.com',465)
server.startssl()
server.login(uname,pssword)
server.sendmail(from_add,to_add,test_msg)
server.quit()
# script not working
