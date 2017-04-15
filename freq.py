import sys

f = open(sys.argv[1],'r')
fw = open(sys.argv[2],'w')

flist = []

for line in f:
    flist = flist + (line.rstrip(' \n')).split(' ')

fdic = {}

for word in flist:
    if word in fdic:
        fdic[word] += 1
    else:
        fdic[word] = 1

counter = 0
for key, value in sorted(fdic.items(), key=lambda x:x[1],reverse = True):
    if counter == 10:
        break
#    print(value, key)
    fw.write('     '+str(value)+' '+key+'\n')
    counter += 1


    
