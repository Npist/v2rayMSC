from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.Signature import PKCS1_v1_5 as PKCS1_v1_5_sign
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA
import base64


class Rsa:
    def __init__(self,
                 ciper_lib=PKCS1_v1_5_cipper,
                 sign_lib=PKCS1_v1_5_sign,
                 hash_lib=SHA,
                 pub_file=None,
                 pri_file=None,
                 pub_skey=None,
                 pri_skey=None,
                 pub_key=None,
                 pri_key=None,
                 reversed_size=11):

        self.ciper_lib = ciper_lib
        self.sign_lib = sign_lib
        self.hash_lib = hash_lib

        if pub_key:
            self.pub_key = pub_key
        elif pub_skey:
            self.pub_key = RSA.importKey(pub_skey)
        elif pub_file:
            self.pub_key = RSA.importKey(open(pub_file).read())

        if pri_key:
            self.pri_key = pri_key
        elif pri_skey:
            self.pri_key = RSA.importKey(pri_skey)
        elif pri_file:
            self.pri_key = RSA.importKey(open(pri_file).read())

        self.block_reversed_size = reversed_size

    def get_block_size(self, rsa_key):
        try:
            reserve_size = self.block_reversed_size
            key_size = rsa_key.size_in_bits()
            if (key_size % 8) != 0:
                raise RuntimeError('RSA 密钥长度非法')

            if rsa_key.has_private():
                reserve_size = 0

            bs = int(key_size / 8) - reserve_size
        except Exception as err:
            print('计算加解密数据块大小出错', rsa_key, err)
        return bs

    def block_data(self, data, rsa_key):
        bs = self.get_block_size(rsa_key)
        for i in range(0, len(data), bs):
            yield data[i:i + bs]

    def enc_bytes(self, data, key=None):
        text = b''
        try:
            rsa_key = self.pub_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            for dat in self.block_data(data, rsa_key):
                cur_text = cipher.encrypt(dat)
                text += cur_text
        except Exception as err:
            print('RSA加密失败', data, err)
        return base64.b64encode(text)

    def dec_bytes(self, data_raw, key=None):
        text = b''
        try:
            rsa_key = self.pri_key
            if key:
                rsa_key = key

            cipher = self.ciper_lib.new(rsa_key)
            data = base64.b64decode(data_raw)
            for dat in self.block_data(data, rsa_key):
                if type(self.ciper_lib) == PKCS1_OAEP:
                    cur_text = cipher.decrypt(dat)
                else:
                    cur_text = cipher.decrypt(dat, '解密异常')
                text += cur_text
        except Exception as err:
            print('RSA解密失败', data, err)
        return text
