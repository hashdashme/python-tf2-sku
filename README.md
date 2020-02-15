# python-tf2-sku


Format items and web api results as strings or objects

## Instalation
``` pip install tf2sku ```

## What is an SKU

SKU is the abbreviation of stock keeping unit. These SKUs make it possible to represent items as readable strings, and convert them to and from objects.

The SKU can safely be used to identify items, since they contain all information about them.

## Examples

```py
from skufy import SKU

# SKU of a Specialized Killstreak Reserve Shooter Kit Fabricator:
	20002 is the defindex, 
	6 is the quality, 
	kt-2 is killstreak tier,
	td-415 is the target item (Reserve Shooter in that case),
	od-6523 is Specialized Reserve Shooter Killstreak Kit,
	oq-6 is the quality of output item
	
sku = '20002;6;kt-2;td-415;od-6523;oq-6'

# Converts the sku string into an item object
item = SKU.fromstring(sku)

item = {
	'defindex': 20002, 
	'quality': 6, 
	'killstreak': 2, 
	'target': 415, 
	'output': 6523, 
	'outputquality': 6, 
	'craftable': True, 
	'tradable': True, 
	'australium': False, 
	'festive': False, 
	'effect': None, 
	'quality2': None, 
	'craftnumber': None, 
	'crateseries': None
}

```

```py


# Specialized Killstreak Reserve Shooter Kit Fabricator
item = {
	'defindex': 20002, 
	'quality': 6, 
	'killstreak': 2, 
	'target': 415, 
	'output': 6523, 
	'outputquality': 6, 
	'craftable': True, 
	'tradable': True, 
	'australium': False, 
	'festive': False, 
	'effect': None, 
	'quality2': None, 
	'craftnumber': None, 
	'crateseries': None
}

# Converts the item object into an sku string
sku = SKU.fromitem(item)
sku = '20002;6;kt-2;td-415;od-6523;oq-6'
```

```py


# Empty dict
item = {}

# Converts the dictionary into item template
template = SKU.matchtemplate(item)
template = {
        'defindex': 0,
        'quality': 0,
        'craftable': True,
        'tradable': True,
        'killstreak': 0,
        'australium': False,
        'festive': False,
        'effect': None,
        'quality2': None,
        'target': None,
        'craftnumber': None,
        'crateseries': None,
        'output': None,
        'outputquality': None
    }
```

```py


# Single item record from TF2 web api (Specialized Killstreak Reserve Shooter Kit Fabricator) 
# This method does not work for chemistry sets, because of TF2 Web Api Error.
item = {
	'id': 8450165216, 
	'original_id': 8450165216, 
	'defindex': 20002, 
	'level': 5, 
	'quality': 6, 
	'inventory': 2147483825, 
	'quantity': 1, 
	'origin': 20, 
	'attributes': 
		[
			{
				'defindex': 2022, 
				'value': 1065353216, 
				'float_value': 1
			}, 
			{
				'defindex': 2000, 
				'is_output': False, 
				'quantity': 1, 
				'quality': 6, 
				'match_all_attribs': True, 
				'attributes': 
					[
						{
							'defindex': 2025, 
							'value': 1065353216, 
							'float_value': 1
						}
					]
			}, 
			{
				'defindex': 2001, 
				'is_output': False, 
				'quantity': 20, 
				'itemdef': 5707, 
				'quality': 6
			}, 
			{
				'defindex': 2002, 
				'is_output': False, 
				'quantity': 4, 
				'itemdef': 5705, 
				'quality': 6
			}, 
			{
				'defindex': 2003, 
				'is_output': False, 
				'quantity': 3, 
				'itemdef': 5704, 
				'quality': 6
			}, 
			{
				'defindex': 2004, 
				'is_output': False, 
				'quantity': 2, 
				'itemdef': 5703, 
				'quality': 6
			}, 
			{
				'defindex': 2005, 
				'is_output': True, 
				'quantity': 1, 
				'itemdef': 6523, 
				'quality': 6, 
				'attributes': 
					[
						{
							'defindex': 2014, 
							'value': 1086324736, 
							'float_value': 6
						}, 
						{'defindex': 2012, 
						 'value': 1137672192, 
						 'float_value': 415
						 }
					]
			}
		]
}

# Converts the record into sku
sku = SKU.fromapi(item)
sku = '20002;6;kt-2;td-415;od-6523;oq-6'
```

Inspired by: https://github.com/Nicklason/node-tf2-sku
