sales_by_genre = {}
for game in video_game_sales:
    key = game[GENRE]
    value = game[GLOBAL_SALES]
    if key in sales_by_genre:
        sales_by_genre[key] = sales_by_genre[key] + value
    else:
        sales_by_genre[key] = value
print(sales_by_genre)
print()

games_per_publisher = {}
for game in video_game_sales:
    key = game[PUBLISHER]
    if key in games_per_publisher:
        games_per_publisher[key] = games_per_publisher[key] + 1
    else:
        games_per_publisher[key] = 1
print(games_per_publisher)
print()

top_game = {
    'name': video_game_sales[0][NAME],
    'year': video_game_sales[0][YEAR],
    'genre': video_game_sales[0][GENRE],
    'publisher': video_game_sales[0][PUBLISHER],
    'global_sales': video_game_sales[0][GLOBAL_SALES]    
}
for key, value in top_game.items():
    print(f'{key}: {value}')
