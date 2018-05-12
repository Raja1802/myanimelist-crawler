# How to use

This script can be used to download anime dataset from [**Myanimelist**](https://myanimelist.net/) using an unofficial MyAnimeList REST API, [**Jikan**](https://jikan.me/docs).

#### Column metadata:

* animeID: id of anime as in anime url [https://myanimelist.net/anime/<span style="color:red">**1**</span>](https://myanimelist.net/anime/1)
* name: title of anime
* premiered: premiered on. default format (season year) 
* genre: list of genre
* type: type of anime (example TV, Movie etc) 
* episodes: number of episodes
* studios: list of studio
* source: source of anime (example original, manga, game etc) 
* scored: score of anime
* scoredBy: number of member scored the anime
* members: number of member added anime to their list

#### Syntax
```
python getAnime.py starting_index ending_index [output_file.csv]
```


#### Demo:

![](../demo/getAnime.gif)

MyAnimeList does not use its last parameter in URL, the name.
E.G. for action animes, https://myanimelist.net/anime/genre/1/<literally anything>
works, so to get url, we can keep only id of the genre, same for studio, producers and so on.

Creating anime ids list from user ratings:
```
python3 createAnimeListFromUsers.py
```