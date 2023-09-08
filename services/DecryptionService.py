#!/usr/bin/env python3

import base64
import hashlib
from models.Upload import Upload
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


class DecryptionService:
    def __to_md5(self, value: str) -> bytes:
        return hashlib.md5(value.encode('utf-8')).digest()

    def __to_iv(self, value: str) -> bytes:
        return f'{value}\n'.encode('utf-8')[:16]

    def __decrypt_aes_128_cbc(self, iv: bytes, ciphertext: bytes,
                              key: bytes) -> bytes:
        aes = AES.new(key, AES.MODE_CBC, IV=iv)
        return aes.decrypt(ciphertext)

    def __decrypt(self, ciphertext: str, password: str) -> str:
        key: bytes = self.__to_md5(password)
        iv: bytes = self.__to_iv(ciphertext)
        ciphertext: bytes = base64.b64decode(ciphertext)
        plaintext: bytes = self.__decrypt_aes_128_cbc(iv, ciphertext, key)
        plaintext = unpad(plaintext, AES.block_size)
        return plaintext[16:len(plaintext)].decode()

    def decrypt(self, upload: Upload, password: str) -> Upload:
        return Upload(
            self.__decrypt(upload.host, password),
            self.__decrypt(upload.username, password),
            self.__decrypt(upload.password, password),
            upload.port,
            self.__decrypt(upload.description, password),
            self.__decrypt(upload.uploader, password),
            self.__decrypt(upload.default_path, password),
            self.__decrypt(upload.bulk_folder_path, password),
            self.__decrypt(upload.package_name, password),
            upload.encrypted
        )
