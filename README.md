# python-tf2-sku


Format items as strings or objects

## What is an SKU

SKU is the abbreviation of stock keeping unit. These SKUs make it possible to represent items as readable strings, and convert them to and from objects.

The SKU can safely be used to identify items, since they contain all information about them.

## Examples

```py
from skufy import SKU

// SKU of a Mann Co. Supply Crate Key - 5021 is the defindex, 6 is the quality
sku = '5021;6'

// Converts the sku string into an item object
item = SKU.fromstring(sku)
/* ->
{
    'defindex': 5021,
    'quality': 6,
    'craftable': true,
    'killstreak': 0,
    'australium': false,
    'festive': false,
    'effect': null,
    'quality2': null,
    'target': null,
    'craftnumber': null
}
*/
```

```py


// Mann Co. Supply Crate Key
item = {
    'defindex': 5021,
    'quality': 6,
    'craftable': true,
    'killstreak': 0,
    'australium': false,
    'festive': false,
    'effect': null,
    'quality2': null,
    'target': null,
    'craftnumber': null
}

// Converts the item object into an sku string
sku = SKU.fromitem(item);
// -> '5021;6'
```
