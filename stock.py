sr="aga|ASFDAS|FAGAFSG|"
for i in range(0,2):
	sr=sr[sr.find("|")+1:]
	print sr

print sr[:sr.find("|")]
	