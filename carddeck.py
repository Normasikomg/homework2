class CardDeck:

    def __init__(self):
        self.length = 52
        self.index = 0
        self.suit = ['Бубей', 'Пик', 'Червей', 'Крестей']
        self.rank = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'J', 'Q', 'K', 'A']

    def __len__(self):
        return self.length

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suit = self.suit[self.index // len(self.rank)]
            rank = self.rank[self.index % len(self.rank)]
            self.index += 1
            print(suit, rank)

    def __iter__(self):
        return self

a = CardDeck()
while True:
    print(next(a))