import os
#import json
import base64
import codecs
#print(os.path.isfile('/home/mitchell/fileServer/dog.jpg'))
#print(os.listdir('/home/mitchell/fileServer'))

#x ={"name":"hey","test":"yes"}
#y = json.dumps(x)
#print(y)

#img_file = open('/home/mitchell/fileServer/dog.jpg', 'rb')
#data = base64.b64encode(img_file.read())
#print(data)

#fh = open("imageToSave.jpg", "wb")
#fh.write(codecs.decode(data,'base64_codec'))
#fh.close()

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

test = strxor("hello", "abcdefghi")
print(test)
test = strxor(test, "abcdefghi")
print(test)


print(chr(1))