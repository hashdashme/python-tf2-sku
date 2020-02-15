# python-tf2-sku


Format items as strings or objects

## What is an SKU

SKU is the abbreviation of stock keeping unit. These SKUs make it possible to represent items as readable strings, and convert them to and from objects.

The SKU can safely be used to identify items, since they contain all information about them.

## Examples

```py
from skufy import SKU

# SKU of a Mann Co. Supply Crate Key - 5021 is the defindex, 6 is the quality
sku = '5021;6'

# Converts the sku string into an item object
item = SKU.fromstring(sku)
"""
item = {
    'defindex': 5021,
    'quality': 6,
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
"""
```

```py


# Mann Co. Supply Crate Key
item = {
    'defindex': 5021,
    'quality': 6,
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

# Converts the item object into an sku string
sku = SKU.fromitem(item)
# sku = '5021;6'
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

Inspired by: https://github.com/Nicklason/node-tf2-sku
