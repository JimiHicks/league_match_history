import settings
import requests
from urllib.parse import urlencode
from summoner_info import get_summoner_info

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
    
def match_results(puuid, match_id, region=settings.DEFUALT_REGION):
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
    match_result = player_info['win']
    return match_result