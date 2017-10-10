#!/usr/bin/env python3
import socket
import re


class Translator:
    languages = ["English", "Alphabetrium", "Gazorpazorpian",
                 "Numberconian", "Martian", "Unition",
                 "Blitzion", "Chipzion", "Morphian"]
    entries = []

    def __init__(self):
        with open('Translation_84808d70fab3a396670edac9ff73af2d.txt') as f:
            text = f.read()
        lines = text.splitlines()

        self.entries = list(map(lambda x: x.split(' -> '), lines))

    def translate(self, src_lang, dest_lang, text):
        if src_lang == dest_lang:
            return text

        src_index = self.languages.index(src_lang)
        dest_index = self.languages.index(dest_lang)

        translate = []
        for word in text.split(' '):
            for word_list in self.entries:
                orig = word_list[src_index]
                if orig == word:
                    dest = word_list[dest_index]
                    translate.append(dest)

        return ' '.join(translate)


if __name__ == '__main__':
    s = socket.socket()
    s.connect(('prog.chal.gryphonctf.com', 17453))

    translator = Translator()

    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            continue
        print(data)

        if ' text : ' in data:
            match = re.search(r'(.+) text : (.+)$', data, re.MULTILINE)
            src_lang = match.group(1)
            text = match.group(2)
            print('>> DEBUG src_lang:', src_lang)
            print('>> DEBUG text:', text)

        if ' Translation ->' in data:
            match = re.search(r'(.+) Translation ->', data, re.MULTILINE)
            dest_lang = match.group(1)
            print('>> DEBUG dest_lang:', text)

            payload = translator.translate(src_lang, dest_lang, text)
            payload += '\n'
            print(">> DEBUG payload", payload, end='')

            s.send(payload.encode())
            continue

        if 'YOU FAILED' in data or \
           'GCTF{' in data:
            quit()
