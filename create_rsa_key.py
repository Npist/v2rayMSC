from Crypto import Random
#from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
#from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

#伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(2048, random_generator)

# master的秘钥对的生成
private_pem = rsa.exportKey()

with open('master-private.pem', 'wb+') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'wb') as f:
    f.write(public_pem)

# # ghost的秘钥对的生成
# private_pem = rsa.exportKey()
# with open('master-private.pem', 'wb') as f:
#     f.write(private_pem)

# public_pem = rsa.publickey().exportKey()
# with open('master-public.pem', 'wb') as f:
#     f.write(public_pem)

message = 'hello ghost, this is a plian text'
cipher_text = ''
with open('master-public.pem', 'rb+') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(bytes(message, "utf-8")))
    print(cipher_text)

text = ''
with open('master-private.pem', 'rb+') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = str(
        cipher.decrypt(base64.b64decode(cipher_text), random_generator),
        "utf-8")
    print(text)

assert text == message, 'decrypt falied'
