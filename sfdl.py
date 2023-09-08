#!/usr/bin/env python3

import argparse
from models.Upload import Upload
from services.SfdlParser import SfdlParser
from services.DecryptionService import DecryptionService
from services.ClipboardService import ClipboardService
from services.CommandGenerator import CommandGenerator


def main():
    parser = argparse.ArgumentParser(description='Parse sfdl files')
    parser.add_argument('file', type=str, help='sfdl file')
    parser.add_argument('password', type=str, help='password')
    args = parser.parse_args()

    sfdl_parser = SfdlParser()
    upload: Upload = sfdl_parser.parse(args.file)

    if upload.encrypted:
        decryption_service: DecryptionService = DecryptionService()
        upload = decryption_service.decrypt(upload, args.password)

    command_generator = CommandGenerator()
    command: str = command_generator.create_wget_command(upload.get_ftp_link())
    ClipboardService.to_clipboard(command)


if __name__ == '__main__':
    main()
