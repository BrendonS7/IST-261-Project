import requests
import json
from bs4 import BeautifulSoup
from anime import Anime
import matplotlib.pyplot as plt
import numpy as np
from gui.gui import GUI


def plot(scores: list, titles: list):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(titles))
    ax.barh(y_pos, scores, align="center")
    ax.set_yticks(y_pos, labels=titles)
    ax.invert_yaxis()
    ax.set_xlabel("Score")
    ax.set_title("Anime Scores")
    plt.show()




def get_anime(url) -> Anime:
    request = requests.get(url)
    j = json.loads(request.text)
    data = j["data"][0]
    title = data["title"]
    score = data["score"]
    genres = [g["name"] for g in data["genres"]]
    genre_str = "Genre(s): "
    for i in range(0, len(genres)):
        if i == (len(genres) - 1):
            genre_str += str(genres[i])
        else:
            genre_str += str(genres[i] + ', ')
    recommended_titles = []
    try:
        recommended_titles = get_recommended_titles(data["url"])
    except:
        pass
    anime = Anime(title, score, genres, recommended_titles)
    anime.print()
    return anime


def get_recommended_titles(url) -> list:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    ul = soup.find("ul", {"data-slide": "7"})
    titles = []
    for li in ul.find_all("li"):
        title = li.get("title")
        titles.append(title)
    return titles


def main():
    url = "https://api.jikan.moe/v4/anime?q="
    inp = input("Please enter a single anime title or a series of anime titles seperated by a \"|\":\n")
    title_list = inp.split("|")
    animes = []
    for title in title_list:
        title = title.strip()
        anime_url = url + title
        try:
            anime = get_anime(anime_url)
            animes.append(anime)
        except:
            print("Anime " + title + "does not exist.")
    scores = [a.score for a in animes]
    titles = [a.title for a in animes]
    #plot(scores, titles)
















if __name__ in {"__main__", "__mp_main__"}:
    main()

