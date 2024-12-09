#Input Bilangan dalam List
data = [5,4,3,1,9,8,10]
ok = "y" 
while (ok=="y"):
	data.append(input("Masukkan Bilangan: "))
	ok = input("Lanjut? (y/n) : ")
print ("Bilangan dalam array adalah: ",data)

#Insertion Sort
print (data)
d = 1
n=(len(data)-1)
while(d <= n):
	print ("d:",d)
	titip = data[d]
	c=d
	
	while((c>=1) and (data[c-1]>titip)):
		print ("\tC-->",c,"&",data[c])
		print ("\t[C-1]-->",c-1,"&",data[c-1])
		print ("\ttitip:",titip)
		data[c]=data[c-1]
		c = c-1

	data[c]=titip
	print ("D-->",d,"&",data[d])
	d = d+1

print ("Bilangan setelah diurutkan dengan Insertion Sort adalah: ",data)
