import io 

f= open('demoFile.txt','w')#read, write, append, read and write
f.write('123456 < tova shte se dobavi')
f.close


f = open('demoFile.txt','r+')
txt = f.read 
print(txt)

f.seek(3)
f.write('hey')
f.close

f = open('demoFile.txt','r')
txt = f.read
print(txt)