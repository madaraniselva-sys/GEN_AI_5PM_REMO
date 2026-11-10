import os 
import csv
ip = []
http_status = []
mydict = {}

path = "C:\\Users\\manju\\Desktop"
filename = "mylog.log"

with open(os.path.join(path,filename)) as f:
    for each_line in f:
        mylist = each_line . split(" ")
        ip.append(mylist[3]) 
        http_status.append(mylist[8])

    # print(http_status)
    # print(ip)

def frequency(mylist):
    
    for each in mylist:
        if each not in mydict:
            mydict[each] = 1
        else:
            mydict[each] +=1
    return mydict
# print(frequency(http_status))

def write_to_csv(mydict):
    with open(os.path.join(path,"new_csv.csv"),"w",newline = "")as f:
        writer = csv.writer(f)
        writer.writerow(["Sno","http_status","Frequncy"])
        Sno = 1
        for each in mydict:
            writer.writerow([Sno,each,mydict[each]])
            Sno +=1

rest1 = frequency(ip)
rest2 = frequency(http_status )

write_to_csv(rest1)
write_to_csv(rest2)

print("CSV file created successfully")