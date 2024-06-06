from helpers import get_summoner_info, get_match_id_by_summoner_puuid, did_player_win_match, win_percentage_of_last_20_games



def main(): 
    summoner = get_summoner_info(game_name=None, tag_line=None)
    print(summoner)

    summoner_matches_ids = get_match_id_by_summoner_puuid(summoner['puuid'], 20)
    print(summoner_matches_ids)

    win = did_player_win_match(summoner['puuid'], summoner_matches_ids[0])
    print(win)

    win_raio = win_percentage_of_last_20_games(game_name=None, tag_line=None)
    print(win_raio)


main()
