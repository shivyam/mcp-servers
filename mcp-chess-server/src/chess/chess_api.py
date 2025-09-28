import requests

CHESS_API_BASE_URL = "https://api.chess.com/pub"

headers= {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}
def get_player_profile(username):
    """Fetches the profile of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_player_stats(username):
    """Fetches the stats of a chess player by username."""
    url = f"{CHESS_API_BASE_URL}/player/{username}/stats"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()