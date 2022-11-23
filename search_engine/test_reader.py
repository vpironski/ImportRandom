import os, io

file = open('search_engine/file.txt','r')
print (file.readlines())
for i in file.readlines():
    # print ("Entered For\n")
    print (i)

topology_list = file.readlines()
print (topology_list)
file.close()
