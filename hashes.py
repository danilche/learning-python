import hashlib

s = b"111"
with open('/home/dane/Documents/wrangling/hashes.txt', 'w') as path:
    #my_file = path
    for j in range(100):
    
        x = hashlib.sha256(s).hexdigest()
        s = x.encode('utf-8')
        print(s)
        print(str(s).lstrip("'b").rstrip("'"), file = path)
        #path.write(str(s))
