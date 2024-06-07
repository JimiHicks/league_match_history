import settings 
import requests
from urllib.parse import urlencode

def get_summoner_info(game_name=None, tag_line=None, region=settings.DEFUALT_REGION):
    if not game_name:
        game_name = input("Summoner Name: ")
    if not tag_line:
        tag_line = input("Summoner Tag: ")

    params = {
        'api_key': settings.API_KEY
    }
    api_url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"

    try: 
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Issue getting summoner data from API: {e}")
        return None


def get_match_id_by_summoner_puuid(puuid, matches_count, region=settings.DEFUALT_REGION):
    params = {
        'api_key': settings.API_KEY,
        'count': matches_count,
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"

    try: 
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Issue getting match_id from puuid: {e}")
        return None
    
def did_player_win_match(puuid, match_id, region=settings.DEFUALT_REGION):
    params = {
        'api_key': settings.API_KEY, 
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try: 
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Issue getting match data from match_id: {e}")
        return None
    
    if puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(puuid)
    else: 
        return None

    player_info = match_data['info']['participants'][player_index]
    return player_info['win'] 

def win_percentage_of_last_20_games(game_name, tag_line, region=settings.DEFUALT_REGION, region_code=settings.DEFUALT_REGION_CODE):
    summoner = get_summoner_info(game_name, tag_line)
    matches = get_match_id_by_summoner_puuid(summoner['puuid'], 20, region)
    
    wins = 0
    for match in matches:
        if did_player_win_match(summoner['puuid'], match):
            wins += 1

    return (wins/len(matches))*100

def get_player_champion(puuid, match_id, region=settings.DEFUALT_REGION):
    params = {
        'api_key': settings.API_KEY, 
    }
    api_url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    try: 
        response = requests.get(api_url, params=urlencode(params))
        response.raise_for_status()
        match_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Issue getting match data from match_id: {e}")
        return None
    
    if puuid in match_data['metadata']['participants']:
        player_index = match_data['metadata']['participants'].index(puuid)
    else: 
        return None

    player_info = match_data['info']['participants'][player_index]
    return player_info['championName'] 