class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def paints(self):
        return f' \"{self.title}\" by {self.artist} ({self.year}) hangs in the Louvre.'


paint = Painting(input(), input(), input())
# paint = Painting('Mona Lisa', 'Leonardo da Vinci', '1503')
print(paint.paints())

# paint = Painting('The Fortune Teller', 'Caravaggio', '1600')
# print(paint.paints())
