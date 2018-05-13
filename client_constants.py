KEY = 'REPLACE WITH CUSTOM FORTNITE TRACKER API KEY'
SUCCESS = 200
REQUEST_HEADERS = {
    'TRN-Api-Key' : KEY
}
RESPONSE_KEYS = {
    'all' : {
            'solos' : 'p2',
            'duos' : 'p10',
            'squads' : 'p9'
        },
    'season4': {
            'solos' : 'curr_p2',
            'duos' : 'curr_p10',
            'squads' : 'curr_p9'
        },
    'season3': {
           'solos' : 'prior_p2',
           'duos' : 'prior_p10',
           'squads' : 'prior_p9'
       }
}