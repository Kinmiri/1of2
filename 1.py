from Crypto.Cipher import AES

def decrypt_AES(bvp, tzgyvikvok, krx, efetv):
    cipher = AES.new(bvp, AES.MODE_GCM, efetv)
    plaintext = cipher.decrypt_and_verify(tzgyvikvok, krx)
    return plaintext
    
bvp = b':)'
tzgyvikvok = b':)'
krx = b':)'
efetv = b':)'

decrypted_text = decrypt_AES(bvp, tzgyvikvok, krx, efetv)
print(decrypted_text)
