from random import choice

class Quote:
    def __init__(self, quote, author) -> None:
        self.quote = quote
        self.author = author
        
class Quotes:
    def __init__(self):
        self._quotes = [
            Quote(
                author="1-я Царств 30:8",
                quote="И вопросил Давид Господа, говоря: преследовать ли мне это полчище, и догоню ли их? И сказано ему: преследуй, догонишь и отнимешь."
            ),
            Quote(
                author="Екклесиаст 7:8",
                quote="Конец дела лучше начала его; терпеливый лучше высокомерного."
            ),
            Quote(
                author="Эдуард Деремов",
                quote="«Талантливые люди остаются в стороне не потому, что у них не хватает способностей, а потому что они не имеют решимости продолжать»"
            ),
            Quote(
                author="Эдуард Деремов",
                quote="«Не получилось в 2025 году? Ничего, я поставлю новую цель и добьюсь ее в 2026. Это правильный настрой.»"
            )
        ]
    def get_any(self):
        return choice(self._quotes)
    
quotes = Quotes()