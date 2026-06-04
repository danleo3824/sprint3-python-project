game_names = []
for games in video_game_sales:
    game_names.append(games[1])
print(game_names)

video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

dataset_info = (len(video_game_sales), 10, 'Video Game Sales') #Using Tuple to allow for changes in values
print(dataset_info)
