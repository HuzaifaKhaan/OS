import os
# parent sey data send
# child sey data recieve

r,w  = os.pipe()

ret = os.fork()

if ret> 0:
    os.close(r)
    print("parent")
    text = "hello".encode()
    os.write(w,text)
    os.close(w)

else:
    os.close(w)
    print("child")
    cr = os.fdopen(r)
    print(cr.read())



#task 2
# 2 way read write

import os
r1,w1 = os.pipe()
r2,w2 = os. pipe()

# parent w1 sey write kre ga
# parent r2 sey read kre gay

# child r1 sey read kre gay
# child w2 sey write kare gay

pid = os.fork()

if pid>0:
    # sending
    os.close(w2)
    os.close(r1)
    print("parent")
    text = 'hello child'.encode()
    os.write(w1,text)
    # recieveing
    pr = os.fdopen(r2)
    print("child sey aya "+pr.read())

else:
    #recievein
    os.close(r2)
    os.close(w1)
    print("child")
    cr = os.fdopen(r1)
    print(cr.read())
    # sending
    text2 = "wapis hello parent".encod()
    os.write(w2,text)
    os.close(w2)
