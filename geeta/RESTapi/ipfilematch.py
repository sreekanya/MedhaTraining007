with open('winelist2.csv') as f1:
    lineset = set(f1)
with open('winelist2.csv') as f2:
    lineset.difference_update(f2)
with open('winelist2-2.csv', 'w') as out:
    for line in lineset:
        out.write(line)
	print line