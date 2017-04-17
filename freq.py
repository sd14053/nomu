import sys,re


argv = sys.argv
f = open(argv[1])
l = f.read()
r = l.replace("\n"," ")
g = r.replace("\w","")
tango = g.split(" ")
dic = dict()
for i in tango:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
for k, v in sorted(dic.items(), key=lambda x:x[1]):
    print(k,v)

