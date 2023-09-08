#!/usr/bin/env python3

class Upload:
    def __init__(self, host: str, username: str, password: str, port: int,
                 description: str, uploader: str, default_path: str,
                 bulk_folder_path: str, package_name: str, encrypted: bool):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.description = description
        self.uploader = uploader
        self.default_path = default_path
        self.bulk_folder_path = bulk_folder_path
        self.package_name = package_name
        self.encrypted = encrypted

    def __str__(self):
        return f'Host: {self.host}\n' \
               f'Username: {self.username}\n' \
               f'Password: {self.password}\n' \
               f'Port: {self.port}\n' \
               f'Description: {self.description}\n' \
               f'Uploader: {self.uploader}\n' \
               f'Default Path: {self.default_path}\n' \
               f'Bulk Folder Path: {self.bulk_folder_path}\n' \
               f'Package Name: {self.package_name}\n' \
               f'Encrypted: {self.encrypted}'

    def get_ftp_link(self) -> str:
        return f'ftp://{self.username}:{self.password}@{self.host}' \
            + f':{self.port}{self.default_path}{self.bulk_folder_path}'
