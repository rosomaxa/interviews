import random
import string
import urlparse


class Codec:
    suffix_len = 6
    prefix = 'http://tinyurl.com'
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}

    def encode(self, longUrl):
        code = self.url_to_code.get(longUrl)
        if code:
            return urlparse.urljoin(Codec.prefix, code)

        code = ''.join(random.choice(Codec.alphabet)
                       for _ in range(Codec.suffix_len))

        while code in self.code_to_url:
            code = ''.join(random.choice(Codec.alphabet)
                           for _ in range(Codec.suffix_len))

        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code

        return urlparse.urljoin(Codec.prefix, code)

    def decode(self, shortUrl):
        this_code = shortUrl[-Codec.suffix_len:]
        long_url = self.code_to_url.get(this_code)
        if not long_url:
            raise ValueError()

        return long_url


if __name__ == '__main__':
    codec = Codec()
    url = 'https://leetcode.com/problems/design-tinyurl'
    print codec.encode(url)
    print codec.encode(url)
    print codec.decode(codec.encode(url))
