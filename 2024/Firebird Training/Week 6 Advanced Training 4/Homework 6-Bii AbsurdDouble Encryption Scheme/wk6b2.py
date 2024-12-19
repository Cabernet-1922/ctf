from Crypto.Util.Padding import pad, unpad
import os, time
from Crypto.Cipher import AES, DES
import numpy as np
import time
import sqlite3

def des_ofb_encrypt(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_OFB, iv=iv)
    return cipher.encrypt(plaintext)
def des_cbc_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    return cipher.decrypt(ciphertext)
def generate_des_key1(number: int) -> bytes:
    hex_str = f'{number:08x}'.lower()
    return hex_str.encode()
def generate_des_key2(number: int, known_suffix: str) -> bytes:
    hex_str = f'{number:06x}'.lower() + known_suffix
    return hex_str.encode()


known_suffix = "b4"
iv1 = bytes.fromhex("bacd0f4007055b30")
iv2 = bytes.fromhex("67f79b9fd05f8dc7")
message_input = pad(bytes.fromhex("0000"), 8)
enc_msg = bytes.fromhex("37ba042f3d5c5250")
flag = "a18dc72d2a2ee47194a2bd22ef672160006ec4e4876b3d2097de2c15741c0ee570ed1ea528c589c72298df087659c083"

conn = sqlite3.connect('mitm.db')
c = conn.cursor()
# c.execute('DROP TABLE IF EXISTS encryption_results')
c.execute('''CREATE TABLE IF NOT EXISTS encryption_results
                 (key TEXT, ciphertext BLOB)''')

c.execute('''CREATE TABLE IF NOT EXISTS decryption_results
                 (key TEXT, plaintext BLOB)''')

conn.commit()

def process_to_sql(plaintext, iv):
    dec_data = [(generate_des_key2(i, known_suffix),
             des_cbc_decrypt(ciphertext=plaintext, key=(generate_des_key2(i, known_suffix)), iv=iv)) for i in
            range(2 ** 24)]
    query = 'INSERT INTO decryption_results (key, plaintext) VALUES (?,?)'
    c.executemany(query, dec_data)
    conn.commit()
    return dec_data
# process_to_sql(plaintext=enc_msg,iv =iv2)
# print(data)

def extract_decryption_pair():
    c.execute("SELECT plaintext FROM decryption_results")
    rows = c.fetchall()
    data_decryption = np.array(rows, dtype=object)
    data_fixed = data_decryption.astype('S8')
    unique_d = np.unique(data_fixed)
    return unique_d, data_decryption

unique_data = extract_decryption_pair()[0]

def process_des_ofb_batch(thread_id, size, message, iv,uniq):
    start = time.time()
    nums = np.arange(thread_id * (2 ** 24), thread_id * (2 ** 24) + size, dtype=np.uint64)
    hex_vectorized = np.vectorize(lambda x: f'{x:08x}'.encode())
    keys = hex_vectorized(nums)
    encrypt_vectorized = np.vectorize(lambda k: des_ofb_encrypt(message, k, iv))
    ciphertexts = np.unique(encrypt_vectorized(keys))
    arr = np.intersect1d(uniq, ciphertexts)
    return arr , start



for thread in range(0, 32):
    arr,start = process_des_ofb_batch(thread, 2 ** 24, message_input, iv1,unique_data)
    print(
        f"thread_{thread}: arr = {arr}-----[{thread * (2 ** 24)}, {thread * (2 ** 24) + 2 ** 24}] ----- Time spend: {(time.time() - start) / 60}")
