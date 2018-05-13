import requests
from collections import defaultdict
from client_constants import REQUEST_HEADERS, SUCCESS, RESPONSE_KEYS

# solos k/d in data['stats'][season]['kd']['valueDec']
# solos matches in data['stats'][season]['matches']['valueInt']
# duos k/d in data['stats'][][season]['valueDec']
# duos matches in data['stats'][season]['matches']['valueInt']
# squads k/d in data['stats'][season]['valueDec']
# squads matches in data['stats'][season]['matches']['valueInt']

class Client:
    URL = 'https://api.fortnitetracker.com/v1/profile/{platform}/{epic_nickname}'

    def send_request(self, epic_name, platform='pc', season='all'):
        request_url = self.URL.format(epic_nickname=epic_name, platform=platform)
        r = requests.get(request_url, headers = REQUEST_HEADERS)
        
        if r.status_code == SUCCESS:
            data = r.json()
            try:
                keys = RESPONSE_KEYS[season]
                stats = defaultdict(dict)
                for stat, key in keys.items():
                    stats[stat]['kd'] = data['stats'][key]['kd']['valueDec']
                    stats[stat]['matches'] = data['stats'][key]['matches']['valueInt']
                return stats
            except KeyError:
                return None
        return None