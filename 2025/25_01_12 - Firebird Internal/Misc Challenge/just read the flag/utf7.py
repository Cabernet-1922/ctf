import base64

def utf8_to_utf7(text):
    def enc_(char):
        if char.isalnum():
            return char
        else:
            utf_16 = char.encode('utf-16-be')
            b_64 = base64.b64encode(utf_16).decode('ascii')
            return f'+{b_64.rstrip("=")}-'
    return ''.join(enc_(c) for c in text)

payload = "print(open(\"flag.txt\").read())"
enc_ = utf8_to_utf7(payload)
print(enc_)