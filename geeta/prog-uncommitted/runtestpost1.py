# trying to post
import urllib2_file
import urllib2

data = {'name': 'value',
        'file':  open('/etc/services')
       }
urllib2.urlopen('http://site.com/script_upload.php', data)

data1=