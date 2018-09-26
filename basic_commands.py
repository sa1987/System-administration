#difference between fabric, os and sys package in python




import os
#get current directory
cur_dir=os.getcwd()

os.mkdir('/tmp/test')

os.chdir('/tmp/test')

os.rename('/tmp/test' , '/tmp/test1')

os.rmdir('/tmp/test1')
 
os.listdir() 
import sys

sys.stderr.write('This is stderr text\n')  #output will be in red colour
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

#sys.argv can be used to pass other laguage scripts
###python script
code= "import sys \nprint ('file name:', str(sys.argv[0]))\nprint ('Number of arguments:', len(sys.argv), 'arguments.')\nprint ('Argument List:', str(sys.argv))"
writeFile=open('sysargv.py', 'w')
writeFile.write(code)
writeFile.close()

#bash shell

#python test1.py hello heelo2 hle

sys.argv = ['sysargv.py' , 'hello']
exec(open('sysargv.py').read())

append = "\nadd me too :)\n"
writeFile=open('sysargv.py', 'a')
writeFile.write(append)
writeFile.close()


fileContent = open('sysargv.py', 'r').read()
print(fileContent)




## write to a file



 #difference between fabric, os and sys package in python




import os
#get current directory
cur_dir=os.getcwd()

os.mkdir('/tmp/test')

os.chdir('/tmp/test')

os.rename('/tmp/test' , '/tmp/test1')

os.rmdir('/tmp/test1')
 
os.listdir() 
import sys

sys.stderr.write('This is stderr text\n')  #output will be in red colour
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

#sys.argv can be used to pass other laguage scripts
###python script
code= "import sys \nprint ('file name:', str(sys.argv[0]))\nprint ('Number of arguments:', len(sys.argv), 'arguments.')\nprint ('Argument List:', str(sys.argv))"
writeFile=open('sysargv.py', 'w')
writeFile.write(code)
writeFile.close()

#bash shell

#python test1.py hello heelo2 hle

sys.argv = ['sysargv.py' , 'hello']
exec(open('sysargv.py').read())

append = "\nadd me too :)\n"
writeFile=open('sysargv.py', 'a')
writeFile.write(append)
writeFile.close()


fileContent = open('sysargv.py', 'r').read()
print(fileContent)

fileContent = open('sysargv.py', 'r').readlines()
print(fileContent)



## write to a file


##subprocess : We can communicate with shell and get update 

import subprocess

subprocess.call('uname -a' , shell=True)
out=subprocess.check_output('echo "hello"' , shell=True)
print(out)



subprocess.call("python sysargv.py  'will it work?'" , shell=True)

 
 
 
