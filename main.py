

from re import A


with open("lista.txt","r",encoding="utf8") as f:
    lines = f.readlines()
f.close()

a = []
for i in lines:
    a.append(i.strip())

with open("lista_out.txt","w",encoding="utf8") as f:
    f.write('[')
    for item in a[0:len(a)-1]:
        f.write('"' + item + '";')
    f.write('"' + a[-1] + '"')
    f.write(']')
f.close()
print('Done')



