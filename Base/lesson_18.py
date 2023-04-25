import subprocess, io, os

sp = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding='cp866')
s = ' '
while s:
    s = out.readline()
    print(s)


print('+-----------------------------------+')
print('|-             Д / З               -|')
print('+-----------------------------------+')

command = "date /t"
# command to be executed
res = os.system(command)
# res = subprocess.call(command, shell = True)

#the method returns the exit status
print(res)
