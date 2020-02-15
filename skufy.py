TEMPLATE = {
    'defindex': 0,
    'quality': 0,
    'craftable': True,
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
    Format items as string or objects
"""
class SKU:
    """
    Convert SKU to object

    Input format:
    <varchar>;<varchar>

    Output format:
    Template above
    """
    def fromstring(self, sku):
        parts = sku.split(';')
        item_object = self.TEMPLATE
        if len(parts) > 0:
            print('elo')
            if isinstance(parts[0], str):
                item_object['defindex'] = int(parts[0])
                del parts[:1]
        if len(parts) > 0:
            if isinstance(parts[0], str):
                item_object['quality'] = int(parts[0])
                del parts[:1]
        for i in range(len(parts)):
            attribute = parts[i].replace('-', '')
            attribute = str(attribute)
            print(attribute)
            if attribute == 'uncraftable':
                item_object['craftable'] = False
            elif attribute == 'australium':
                item_object['australium'] = True
            elif attribute == 'festive':
                item_object['festive'] = True
            elif attribute == 'strange':
                item_object['quality2'] = 11
            elif attribute.startswith('kt'):
                item_object['killstreak'] = int(attribute[2:])
            elif attribute.startswith('u'):
                item_object['effect'] = int(attribute[1:])
            elif attribute.startswith('td'):
                item_object['target'] = int(attribute[2:])
            elif attribute.startswith('n'):
                item_object['craftnumber'] = int(attribute[1:])
            elif attribute.startswith('c'):
                item_object['crateseries'] = int(attribute[1:])
            elif attribute.startswith('od'):
                item_object['output'] = int(attribute[2:])
            elif attribute.startswith('oq'):
                item_object['outputquality'] = int(attribute[2:])

        return item_object

    """
        Convert object to SKU

        Input format:
        Template above

        Output format:
        <varchar>;<varchar>
    """
    def fromitem(self, item):

        self.sku = '{};{}'.format(item['defindex'], item['quality'])

        if not item['craftable']:
            self.sku += ';uncraftable'
        if item['australium']:
            self.sku += ';australium'
        if item['festive']:
            self.sku += ';festive'
        if item['quality2'] is not None:
            self.sku += ';{}'.format(item['quality2'])
        if item['killstreak'] != 0:
            self.sku += ';ks-{}'.format(item['killstreak'])
        if item['effect'] is not None:
            self.sku += ';u={}'.format(item['effect'])
        if item['target'] is not None:
            self.sku += ';td-{}'.format(item['target'])
        if item['craftnumber'] is not None:
            self.sku += ';n{}'.format(item['craftnumber'])
        if item['crateseries'] is not None:
            self.sku += ';c{}'.format(item['crateseries'])
        if item['output'] is not None:
            self.sku += ';od{}'.format(item['output'])
        if item['outputquality'] is not None:
            self.sku += ';oq{}'.format((item['outputquality']))

        return self.sku

    def __init__(self, sku=None, item=None):
        self.sku = sku
        self.TEMPLATE = TEMPLATE
        self.item = item
