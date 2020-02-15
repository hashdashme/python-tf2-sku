# TEMPLATE = {
#     defindex: 0,
#     quality: 0,
#     craftable: true,
#     killstreak: 0,
#     australium: false,
#     festive: false,
#     effect: null,
#     paintkit: null,
#     wear: null,
#     quality2: null,
#     target: null,
#     craftnumber: null,
#     crateseries: null,
#     output: null,
#     outputQuality: null
# }
from json import dump
from creds import steam, steam_password, api_key
from steampy.client import SteamClient, InvalidCredentials
from steampy.models import GameOptions


steam_client = SteamClient(api_key)
try:
    steam_client.login(steam, steam_password, 'Steamguard.txt')
    print("logged in")
except InvalidCredentials:
    print("Invalid credentials")

inventory = steam_client.get_partner_inventory('76561198065349229', GameOptions('440','2'))
items = {}
for item in inventory.values():
    if item['appid'] == 440:
        items[item['market_name']] = item
with open('test_inv.json', 'w') as f:
    dump(items, f)
print('success!')
steam_client.logout