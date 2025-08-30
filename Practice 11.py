# test1=open("test1.txt","r")
# for i in test1:
#     print(i.strip())    
# test1=open("test2.txt","x")
# test1.write("l8")
# test1.close()
# test1=open("test2.txt","a")
# test1.write("\nl8")
namel=[]
numl=[]
# test1=open("names.txt","r")
# for i in test1:
#     print(i)
# test1.close()
count=0
test1=open("names.txt","r")
for i in test1:
    if count%2==0:
        namel.append(i.strip())
    else:
        numl.append(i.strip())
    count=count+1
print(namel)
print(numl)