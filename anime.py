class Anime:
    def __init__(self, title: str, score: float, genres: list, recommendations: list):
        self.title = title
        self.score = score
        self.genres = genres
        self.recommendations = recommendations

    def print(self):
        print("Title: " + self.title)
        print("Score: " + str(self.score))
        print("Genres: " + str(self.genres))
        print("Shows like it: " + str(self.recommendations))
