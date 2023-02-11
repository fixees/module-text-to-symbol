class Image:
    alphabet = {
        ' ': ' ',
        ',': ',',
        '.': '.',
        '!': '!',
        'a': '🅰',
        'b': '🅱',
        'c': '🅲',
        'd': '🅳',
        'e': '🅴',
        'f': '🅵',
        'g': '🅶',
        'h': '🅷',
        'i': '🅸',
        'j': '🅹',
        'k': '🅺',
        'l': '🅻',
        'm': '🅼',
        'n': '🅽',
        'o': '🅾',
        'p': '🅿',
        'q': '🆀',
        'r': '🆁',
        's': '🆂',
        't': '🆃',
        'u': '🆄',
        'v': '🆅',
        'w': '🆆',
        'x': '🆇',
        'y': '🆈',
        'z': '🆉'

    }

    def output(self, name, theme=None):
        done_str = ''
        # Process

        if theme == 'made_by':
            done_str += '𝙢𝙖𝙙𝙚 𝙗𝙮 '

        for i in name.lower():
            letter = self.alphabet.get('{0}'.format(i))
            done_str += letter

        if theme == 'love':
            done_str = '(っ◔◡◔)っ {0} ♥ \n'.format(done_str)

        return done_str

