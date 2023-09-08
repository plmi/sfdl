#!/usr/bin/env python3


class CommandGenerator:
    def create_wget_command(self, url: str) -> str:
        return f'wget --reject --no-parent --recursive {url}'
