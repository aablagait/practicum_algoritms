import random


class MarsURLEncoder:

    def __init__(self):
        self.stored_link = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        number = [chr(i) for i in range(48, 58)]
        alphabet = [chr(i) for i in range(65, 123)]
        symbol = number + alphabet
        hash_str = ''
        for i in range(10):
            hash_str += random.choice(symbol)

        self.stored_link[hash_str] = long_url
        return f'https://ma.rs/{hash_str}'

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        hash_str = short_url.split('https://ma.rs/')[1]
        return self.stored_link[hash_str]

long = 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
link_to_mars = MarsURLEncoder()
print(link_to_mars.encode(long))
print(link_to_mars.stored_link)
print(link_to_mars.decode('https://ma.rs/815513AbY'))
