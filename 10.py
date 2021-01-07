name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
dic=dict()
count=0
newl=list()

for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):continue
    line=line.split()
    if not ':' in line[5]: continue
    date=line[5]
    s=date[:2]
    lst.append(s)
slst=sorted(lst)
for w in slst:
    dic[w]=dic.get(w,0)+1

for k,v in dic.items():
    print(k,v)
