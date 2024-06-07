from helpers import  get_summoner_info, get_match_id_by_summoner_puuid, did_player_win_match, win_percentage_of_last_20_games, get_player_champion

game_name = 'Nachomky'
tag_line = 'brnze'

def main(): 
    summoner = get_summoner_info(game_name, tag_line)

    summoner_matches_ids = get_match_id_by_summoner_puuid(summoner['puuid'], 20)

    win = did_player_win_match(summoner['puuid'], summoner_matches_ids[0])

    win_raio = win_percentage_of_last_20_games(game_name, tag_line)

    champion = get_player_champion(summoner['puuid'], summoner_matches_ids[0])

    print(f"Win: {win} Champion Played: {champion} Win ratio over last 20 games: {win_raio}%")

main()
