import vdf
import json
from json import dump
import requests
from creds import api_key
d = vdf.load(open('tf2_schema.txt'))
b = json.load(open('test_inv.json'))

qualities = {}
items = {}
effects = {}
for item in d['items_game']['qualities']:
    if d['items_game']['qualities'][item]['value'] == '5':
        qualities['unusual'] = d['items_game']['qualities'][item]['value']
    elif d['items_game']['qualities'][item]['value'] == '1':
        qualities['genuine'] = d['items_game']['qualities'][item]['value']
    else:
        qualities[item] = d['items_game']['qualities'][item]['value']

print(qualities)
for item in d['items_game']['items']:
    if d['items_game']['items'][item]['name'] == 'Decoder Ring':
        items['Mann Co. Supply Crate Key'] = item
    else:
        items[d['items_game']['items'][item]['name']] = item
#print(items)

for item in d['items_game']['attribute_controlled_attached_particles']['other_particles']:
    effects[d['items_game']['attribute_controlled_attached_particles']['other_particles'][item]['system']] = item
for item in d['items_game']['attribute_controlled_attached_particles']['cosmetic_unusual_effects']:
    fixed = d['items_game']['attribute_controlled_attached_particles']['cosmetic_unusual_effects'][item]['system'].split('_')
    fixed = '_'.join(fixed[1:])
    effects[fixed] = item
    print(d['items_game']['attribute_controlled_attached_particles']['cosmetic_unusual_effects'][item])
for item in d['items_game']['attribute_controlled_attached_particles']['weapon_unusual_effects']:
    pass
for item in d['items_game']['attribute_controlled_attached_particles']['killstreak_eyeglows']:
    pass
for item in d['items_game']['attribute_controlled_attached_particles']['taunt_unusual_effects']:
    pass
print(effects)
effect = {
	'1': 'Particle 1',
	'2': 'Flying Bits',
	'3': 'Nemesis Burst',
	'4': 'Community Sparkle',
	'5': 'Holy Glow',
	'6': 'Green Confetti',
	'7': 'Purple Confetti',
	'8': 'Haunted Ghosts',
	'9': 'Green Energy',
	'10': 'Purple Energy',
	'11': 'Circling TF Logo',
	'12': 'Massed Flies',
	'13': 'Burning Flames',
	'14': 'Scorching Flames',
	'15': 'Searing Plasma',
	'16': 'Vivid Plasma',
	'17': 'Sunbeams',
	'18': 'Circling Peace Sign',
	'19': 'Circling Heart',
	'20': 'Map Stamps',
	'28': 'Genteel Smoke',
	'29': 'Stormy Storm',
	'30': 'Blizzardy Storm',
	'31': 'Nuts n\' Bolts',
	'32': 'Orbiting Planets',
	'33': 'Orbiting Fire',
	'34': 'Bubbling',
	'35': 'Smoking',
	'36': 'Steaming',
	'37': 'Flaming Lantern',
	'38': 'Cloudy Moon',
	'39': 'Cauldron Bubbles',
	'40': 'Eerie Orbiting Fire',
	'43': 'Knifestorm',
	'44': 'Misty Skull',
	'45': 'Harvest Moon',
	'46': 'It\'s A Secret To Everybody',
	'47': 'Stormy 13th Hour',
	'55': 'Attrib_Particle55',
	'56': 'Kill-a-Watt',
	'57': 'Terror-Watt',
	'58': 'Cloud 9',
	'59': 'Aces High',
	'60': 'Dead Presidents',
	'61': 'Miami Nights',
	'62': 'Disco Beat Down',
	'63': 'Phosphorous',
	'64': 'Sulphurous',
	'65': 'Memory Leak',
	'66': 'Overclocked',
	'67': 'Electrostatic',
	'68': 'Power Surge',
	'69': 'Anti-Freeze',
	'70': 'Time Warp',
	'71': 'Green Black Hole',
	'72': 'Roboactive',
	'73': 'Arcana',
	'74': 'Spellbound',
	'75': 'Chiroptera Venenata',
	'76': 'Poisoned Shadows',
	'77': 'Something Burning This Way Comes',
	'78': 'Hellfire',
	'79': 'Darkblaze',
	'80': 'Demonflame',
	'81': 'Bonzo The All-Gnawing',
	'82': 'Amaranthine',
	'83': 'Stare From Beyond',
	'84': 'The Ooze',
	'85': 'Ghastly Ghosts Jr',
	'86': 'Haunted Phantasm Jr',
	'87': 'Frostbite',
	'88': 'Molten Mallard',
	'89': 'Morning Glory',
	'90': 'Death at Dusk',
	'91': 'Abduction',
	'92': 'Atomic',
	'93': 'Subatomic',
	'94': 'Electric Hat Protector',
	'95': 'Magnetic Hat Protector',
	'96': 'Voltaic Hat Protector',
	'97': 'Galactic Codex',
	'98': 'Ancient Codex',
	'99': 'Nebula',
	'100': 'Death by Disco',
	'101': 'It\'s a mystery to everyone',
	'102': 'It\'s a puzzle to me',
	'103': 'Ether Trail',
	'104': 'Nether Trail',
	'105': 'Ancient Eldritch',
	'106': 'Eldritch Flame',
	'107': 'Neutron Star',
	'108': 'Tesla Coil',
	'109': 'Starstorm Insomnia',
	'110': 'Starstorm Slumber',
	'111': 'Brain Drain',
	'112': 'Open Mind',
	'113': 'Head of Steam',
	'114': 'The Galactic Gateway',
	'115': 'The Eldritch Opening',
	'116': 'The Dark Doorway',
	'117': 'Ring of Fire',
	'118': 'Vicious Circle',
	'119': 'White Lightning',
	'120': 'Omniscient Orb',
	'121': 'Clairvoyance',
	'122': 'Fifth Dimension',
	'123': 'Vicious Vortex',
	'124': 'Menacing Miasma',
	'125': 'Abyssal Aura',
	'126': 'Wicked Wood',
	'127': 'Ghastly Grove',
	'128': 'Mystical Medley',
	'129': 'Ethereal Essence',
	'130': 'Twisted Radiance',
	'131': 'Violet Vortex',
	'132': 'Verdant Vortex',
	'133': 'Valiant Vortex',
	'134': 'Sparkling Lights',
	'135': 'Frozen Icefall',
	'136': 'Fragmented Gluons',
	'137': 'Fragmented Quarks',
	'138': 'Fragmented Photons',
	'139': 'Defragmenting Reality',
	'141': 'Fragmenting Reality',
	'142': 'Refragmenting Reality',
	'143': 'Snowfallen',
	'144': 'Snowblinded',
	'145': 'Pyroland Daydream',
	'701': 'Hot',
	'702': 'Isotope',
	'703': 'Cool',
	'704': 'Energy Orb',
	'2001': 'Attrib_Particle2001',
	'2002': 'Attrib_Particle2002',
	'2003': 'Attrib_Particle2003',
	'2004': 'Attrib_Particle2004',
	'2005': 'Attrib_Particle2005',
	'2006': 'Attrib_Particle2006',
	'2007': 'Attrib_Particle2007',
	'2008': 'Attrib_Particle2008',
	'3001': 'Showstopper',
	'3003': 'Holy Grail',
	'3004': '\'72',
	'3005': 'Fountain of Delight',
	'3006': 'Screaming Tiger',
	'3007': 'Skill Gotten Gains',
	'3008': 'Midnight Whirlwind',
	'3009': 'Silver Cyclone',
	'3010': 'Mega Strike',
	'3011': 'Haunted Phantasm',
	'3012': 'Ghastly Ghosts',
	'3013': 'Hellish Inferno',
	'3014': 'Spectral Swirl',
	'3015': 'Infernal Flames',
	'3016': 'Infernal Smoke',
	'3017': 'Acidic Bubbles of Envy',
	'3018': 'Flammable Bubbles of Attraction',
	'3019': 'Poisonous Bubbles of Regret',
	'3020': 'Roaring Rockets',
	'3021': 'Spooky Night',
	'3022': 'Ominous Night',
	'3023': 'Bewitched',
	'3024': 'Accursed',
	'3025': 'Enchanted',
	'3026': 'Static Mist',
	'3027': 'Eerie Lightning',
	'3028': 'Terrifying Thunder',
	'3029': 'Jarate Shock',
	'3030': 'Nether Void',
	'3031': 'Good-Hearted Goodies',
	'3032': 'Wintery Wisp',
	'3033': 'Arctic Aurora',
	'3034': 'Winter Spirit',
	'3035': 'Festive Spirit',
	'3036': 'Magical Spirit',
	'22001': 'Attrib_Particle22001',
	'22002': 'Attrib_Particle22002',
	'22003': 'Attrib_Particle22003',
	'22004': 'Attrib_Particle22004',
	'22005': 'Attrib_Particle22005',
	'22006': 'Attrib_Particle22006',
	'22007': 'Attrib_Particle22007',
	'22008': 'Attrib_Particle22008'
}
with open('effects.json', 'w') as f:
	dump(effect, f)

# for item in b:
# 	if item == 'Unusual Brown Bomber':
# 		print(b[item])

# for item in b:
#     for defindex in d['items_game']['items']:
#         if item == d['items_game']['items'][defindex]['name']:
#             print(item + ' {}'.format(defindex))
#         elif item == 'Mann Co. Supply Crate Key' and d['items_game']['items'][defindex]['name'] == 'Decoder Ring':
#             print(item + ' {}'.format(defindex))

# for item in b:
#     print(item)
#     print(b[item])
#     print('\n')
# Schemat itemow tf2
# r = requests.get('http://api.steampowered.com/IEconItems_440/GetSchemaURL/v1?key={}'.format(api_key)).json()
# schema_url = r['result']['items_game_url']
# print(schema_url)
# tf2_schema = requests.get(schema_url).content
# open('tf2_schema.txt', 'wb').write(tf2_schema)
# params = {
# 	'SteamID': '76561198060419855'
# }
# r = requests.get('http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001?key={}'.format(api_key), params=params)
# r = r.json()
# with open('test_inv.json', 'w') as f:
# 	dump(r, f)
for item in b['result']['items']:
	if item['quality'] == 5:
		print(item)


# attributes defindex 134 to efekt a float to szczegolowy efekt