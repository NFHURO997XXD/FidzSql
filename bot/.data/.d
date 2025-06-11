# -*- coding:utf8 -*-

# Import Modules
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x68\x74\x72\x2d\x74\x65\x63\x68\x0a\x23\x20\x54\x69\x6d\x65\x20\x3a\x20%s\n\x23\x20\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x0a" % time.ctime()

def banner(): # Program Banner
    print(' \033[1;34m╔═════════════════════════════════╗\n ║  \033[1;36mSimple Python Code Obfuscator  \033[1;34m║\n ║         \033[1;31mBy Tahmid Rayat         \033[1;34m║\n ╚═════════════════════════════════╝\n')

def menu(): # Program Menu
    #print("\x20\x5b\x30\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x0a\x20\x5b\x30\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x0a\x20\x5b\x30\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x30\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x30\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x30\x36\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x30\x37\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x30\x38\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x5a\x6c\x69\x62\x2c\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x30\x39\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x0a\x20\x5b\x31\x30\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x31\x36\x0a\x20\x5b\x31\x31\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x33\x32\x0a\x20\x5b\x31\x32\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x42\x61\x73\x65\x36\x34\x0a\x20\x5b\x31\x33\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x31\x36\x0a\x20\x5b\x31\x34\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x33\x32\x0a\x20\x5b\x31\x35\x5d\x20\x45\x6e\x63\x6f\x64\x65\x20\x4d\x61\x72\x73\x68\x61\x6c\x2c\x5a\x6c\x69\x62\x2c\x42\x36\x34\x0a\x20\x5b\x31\x36\x5d\x20\x53\x69\x6d\x70\x6c\x65\x20\x45\x6e\x63\x6f\x64\x65\x0a\x20\x5b\x31\x37\x5d\x20\x45\x78\x69\x74\n")
    print(""" \033[1;31m[\033[1;37m01\033[1;31m] \033[1;36mEncode Marshal
 \033[1;31m[\033[1;37m02\033[1;31m] \033[1;36mEncode Zlib
 \033[1;31m[\033[1;37m03\033[1;31m] \033[1;36mEncode Base16
 \033[1;31m[\033[1;37m04\033[1;31m] \033[1;36mEncode Base32
 \033[1;31m[\033[1;37m05\033[1;31m] \033[1;36mEncode Base64
 \033[1;31m[\033[1;37m06\033[1;31m] \033[1;36mEncode Zlib,Base16
 \033[1;31m[\033[1;37m07\033[1;31m] \033[1;36mEncode Zlib,Base32
 \033[1;31m[\033[1;37m08\033[1;31m] \033[1;36mEncode Zlib,Base64
 \033[1;31m[\033[1;37m09\033[1;31m] \033[1;36mEncode Marshal,Zlib
 \033[1;31m[\033[1;37m10\033[1;31m] \033[1;36mEncode Marshal,Base16
 \033[1;31m[\033[1;37m11\033[1;31m] \033[1;36mEncode Marshal,Base32
 \033[1;31m[\033[1;37m12\033[1;31m] \033[1;36mEncode Marshal,Base64
 \033[1;31m[\033[1;37m13\033[1;31m] \033[1;36mEncode Marshal,Zlib,B16
 \033[1;31m[\033[1;37m14\033[1;31m] \033[1;36mEncode Marshal,Zlib,B32
 \033[1;31m[\033[1;37m15\033[1;31m] \033[1;36mEncode Marshal,Zlib,B64
 \033[1;31m[\033[1;37m16\033[1;31m] \033[1;36mSimple Encode
 \033[1;31m[\033[1;37m17\033[1;31m] \033[1;36mExit
""")
class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mEncoded File Size \033[1;31m:\033[0;37m %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % " \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mEncode Count \033[1;31m: \033[0;37m"))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n \033[1;31m[\033[1;37m!\033[1;31m] \033[1;31mInvalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" \033[1;31m[\033[1;37m!\033[1;31m] \033[1;31mTypeError : \033[0;37m" + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        #os.system('clear') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mOption \033[1;31m: \033[0;37m"))
        except ValueError:
            sys.exit("\n Invalid Option !")
        
        if option > 0 and option <= 17:
            if option == 17:
                sys.exit("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mThanks For Using this Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            sys.exit('\n \033[1;31m[\033[1;37m!\033[1;31m] \033[1;31mInvalid Option !')
        try:
            file = eval(_input % " \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mFile Name \033[1;31m: \033[0;37m")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSuccessfully Encrypted %s" % file)
        print(" \033[1;31m[\033[1;37m+\033[1;31m] \033[1;34mSaved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
