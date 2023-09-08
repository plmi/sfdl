#!/usr/bin/env python3

import os


class ClipboardService:
    @staticmethod
    def to_clipboard(value: str) -> None:
        command: str = f'echo {value} | xclip -sel clipboard'
        os.system(command)
