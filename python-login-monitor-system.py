#Logs

logs=[]
count={}

while True:
	print("1)Login:")
	print("2)Log out:")
	print("3)Exit:")

	ch=input("Choose:")

	if ch=="1":
		ip=input("Enter the ip address:")
		logs.append(ip)

		if ip in count:
			count[ip]+=1
		else:
			count[ip]=1

		if count[ip] >= 5:
			print("Suspicious!")
		else:
			print("Logged in!!")

	if ch=="2":
		ip=input("Enter the ip address:")
		print("Log out!")

	if ch=="3":
		print("Bye")
		break

