class Image:
    alphabet = {
        ' ': ' ',
        ',': ',',
        '.': '.',
        '!': '!',
        'a': '๐ฐ',
        'b': '๐ฑ',
        'c': '๐ฒ',
        'd': '๐ณ',
        'e': '๐ด',
        'f': '๐ต',
        'g': '๐ถ',
        'h': '๐ท',
        'i': '๐ธ',
        'j': '๐น',
        'k': '๐บ',
        'l': '๐ป',
        'm': '๐ผ',
        'n': '๐ฝ',
        'o': '๐พ',
        'p': '๐ฟ',
        'q': '๐',
        'r': '๐',
        's': '๐',
        't': '๐',
        'u': '๐',
        'v': '๐',
        'w': '๐',
        'x': '๐',
        'y': '๐',
        'z': '๐'

    }

    def output(self, name, theme=None):
        done_str = ''
        # Process

        if theme == 'made_by':
            done_str += '๐ข๐๐๐ ๐๐ฎ '

        for i in name.lower():
            letter = self.alphabet.get('{0}'.format(i))
            done_str += letter

        if theme == 'love':
            done_str = '(ใฃโโกโ)ใฃ {0} โฅ \n'.format(done_str)

        return done_str

