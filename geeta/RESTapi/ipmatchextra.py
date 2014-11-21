proc=subprocess.Popen(['netstat','-an'],
stdout=subprocess.PIPE)
stdoutdata=proc.communicate()[0]
print stdoutdata