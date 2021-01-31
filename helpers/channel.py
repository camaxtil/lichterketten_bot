import requests, yaml
with open("config.yaml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def get_channel_id():
    url = f"https://api.twitch.tv/kraken/users?login={config['channel']}"
    headers = {"Client-ID": config["client_id"], "Accept": "application/vnd.twitchtv.v5+json"}
    r = requests.get(url, headers=headers).json()
    write_channel_id(r['users'][0]['_id'])
    return r['users'][0]['_id']

def write_channel_id(channel_id):
    with open("config.yaml", "w") as file:
        config["channel_id"] = channel_id
        documents = yaml.dump(config, file)

def change_stream_title(stream_title):
    url = f"https://api.twitch.tv/kraken/channels/{config['channel_id']}"
    data = {"channel[status]": stream_title}
    headers = {"Client-ID": config["client_id"], "Authorization": f"OAuth {config['token'].replace('oauth:', '')}", "Accept": "application/vnd.twitchtv.v5+json"}
    r = requests.put(url, data=data, headers=headers).json()

def change_stream_game(stream_game):
    url = f"https://api.twitch.tv/kraken/channels/{config['channel_id']}"
    data = {"channel[game]": stream_game}
    headers = {"Client-ID": config["client_id"], "Authorization": f"OAuth {config['token'].replace('oauth:', '')}",
               "Accept": "application/vnd.twitchtv.v5+json"}
    r = requests.put(url, data=data, headers=headers).json()

def get_channel_followers():
    print("FAIL?")
    url = f"https://api.twitch.tv/kraken/channels/{config['channel_id']}"
    headers = {"Client-ID": config["client_id"], "Accept": "application/vnd.twitchtv.v5+json"}
    r = requests.get(url, headers=headers).json()
    return r["followers"]



    