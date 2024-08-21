from jikanpy import Jikan
import pandas as pd
import time

jikan = Jikan()

# Fetch the top anime
top_anime = jikan.top(type='anime')

# Print the full response to understand its structure
print(top_anime)

# Adjusting based on the actual structure of the response
if 'data' in top_anime:
    for anime in top_anime['data']:
        print(f"Title: {anime['title']}, Score: {anime['score']}")
else:
    print("Unexpected response structure:", top_anime)
