from Crypto.Cipher import AES

def decrypt_AES(bvp, tzgyvikvok, krx, efetv):
    cipher = AES.new(bvp, AES.MODE_GCM, efetv)
    plaintext = cipher.decrypt_and_verify(tzgyvikvok, krx)
    return plaintext
