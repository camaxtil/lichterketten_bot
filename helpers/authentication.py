import requests, yaml
with open("config.yaml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

def generate_authorization_bearer():
    url = f"https://id.twitch.tv/oauth2/token?client_id={config['client_id']}&client_secret={config['client_secret']}&grant_type=client_credentials"
    r = requests.post(url).json()
    write_authorization_bearer(r["access_token"])
    return r["access_token"]

def write_authorization_bearer(authentication_bearer):
    with open("config.yaml", "w") as file:
        config["authentication_bearer"] = authentication_bearer
        documents = yaml.dump(config, file)