
"""
    Format items as string or objects
"""


class SKU:
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
    """
    Convert SKU to object

    Input format:
    <varchar>;<varchar>

    Output format:
    Template above
    """
    @staticmethod
    def fromstring(sku):
        item = {}
        parts = sku.split(';')
        if len(parts) > 0:
            if isinstance(parts[0], str):
                item['defindex'] = int(parts[0])
                del parts[:1]
        if len(parts) > 0:
            if isinstance(parts[0], str):
                item['quality'] = int(parts[0])
                del parts[:1]
        for i in range(len(parts)):
            attribute = parts[i].replace('-', '')
            attribute = str(attribute)
            if attribute == 'uncraftable':
                item['craftable'] = False
            elif attribute == 'australium':
                item['australium'] = True
            elif attribute == 'untradable':
                item['untradable'] = True
            elif attribute == 'festive':
                item['festive'] = True
            elif attribute == 'strange':
                item['quality2'] = 11
            elif attribute.startswith('kt'):
                item['killstreak'] = int(attribute[2:])
            elif attribute.startswith('u'):
                item['effect'] = int(attribute[1:])
            elif attribute.startswith('td'):
                item['target'] = int(attribute[2:])
            elif attribute.startswith('n'):
                item['craftnumber'] = int(attribute[1:])
            elif attribute.startswith('c'):
                item['crateseries'] = int(attribute[1:])
            elif attribute.startswith('od'):
                item['output'] = int(attribute[2:])
            elif attribute.startswith('oq'):
                item['outputquality'] = int(attribute[2:])

        item = SKU.matchtemplate(item)

        return item

    """
        Match the generated item to the template
    """
    @staticmethod
    def matchtemplate(item, template=template):
        for attribute in template:
            if attribute not in item:
                item[attribute] = template[attribute]
            else:
                pass
        return item

    """
        Convert object to SKU

        Input format:
        Template above

        Output format:
        <varchar>;<varchar>
    """
    @staticmethod
    def fromitem(item):

        sku = '{};{}'.format(item['defindex'], item['quality'])

        if not item['craftable']:
            sku += ';uncraftable'
        if item['australium']:
            sku += ';australium'
        if item['festive']:
            sku += ';festive'
        if item['untradable']:
            sku += ';untradable'
        if item['quality2'] is not None:
            sku += ';{}'.format(item['quality2'])
        if item['killstreak'] != 0:
            sku += ';ks-{}'.format(item['killstreak'])
        if item['effect'] is not None:
            sku += ';u={}'.format(item['effect'])
        if item['target'] is not None:
            sku += ';td-{}'.format(item['target'])
        if item['craftnumber'] is not None:
            sku += ';n{}'.format(item['craftnumber'])
        if item['crateseries'] is not None:
            sku += ';c{}'.format(item['crateseries'])
        if item['output'] is not None:
            sku += ';od{}'.format(item['output'])
        if item['outputquality'] is not None:
            sku += ';oq{}'.format((item['outputquality']))

        return sku


