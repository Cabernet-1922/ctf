import os, sys, hashlib
from Crypto.Cipher import AES

def decrypt_file(inp, outp):
    iv = bytes.fromhex("cafef00dbeefc0cccafef00dbeefc0cc")
    name = os.path.basename(inp)[:-4]
    key = hashlib.sha256(name.encode()).digest()
    ct = open(inp, "rb").read()
    pt = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
    pt = pt[:-pt[-1]]
    open(outp, "wb").write(pt)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: decrypt.py <encrypted_file> <output_file>")
        sys.exit(1)
    decrypt_file(sys.argv[1], sys.argv[2])