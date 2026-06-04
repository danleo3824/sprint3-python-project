for games in video_game_sales:
    if games[GLOBAL_SALES] > 25:
        print(games[NAME], games[GLOBAL_SALES])
print()
pre_2000_count = 0
for years in video_game_sales:
    if years[YEAR] < 2000:
        pre_2000_count = pre_2000_count + 1
print(pre_2000_count)

print()

NASales = 0
JapanSales = 0
for sales in video_game_sales:
    NASales = NASales + sales[NA_SALES]
    JapanSales = JapanSales + sales[JP_SALES]
print(f"North American Sales: ${NASales}M, Japan Sales: ${JapanSales}M")
if NASales > JapanSales:
    print('North American Sales > Japan Sales')
elif JapanSales > NASales:
    print('Japan Sales > North American Sales')
else:
    print('North American Sales = Japan Sales')
print()

nintendo_games = []
for nin in video_game_sales:
    if nin[PUBLISHER] == 'Nintendo':
        nintendo_games.append(nin[NAME])
print(nintendo_games)
print(len(nintendo_games))
