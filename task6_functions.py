def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]
print(calculate_total_sales(video_game_sales[0]))
print()

def filter_by_genre(data, genre='Platform'):
    matched_genre = []
    for info in data:
        if info[GENRE] == genre:
            matched_genre.append(info)
    return matched_genre
print(filter_by_genre(video_game_sales))
print(filter_by_genre(video_game_sales, 'Test'))

def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"
for game in video_game_sales:
    print(get_summary(game))
