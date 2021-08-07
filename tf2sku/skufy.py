
"""
    Format items and api results as string or objects
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
        'paint_kit': None,
        'wear': None,
        'quality2': None,
        'target': None,
        'craft_number': None,
        'crate_series': None,
        'output': None,
        'output_quality': None
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

            elif attribute.startswith('pk'):
                item['paint_kit'] = int(attribute[2:])

            elif attribute.startswith('w'):
                item['wear'] = int(attribute[1:])

            elif attribute.startswith('td'):
                item['target'] = int(attribute[2:])

            elif attribute.startswith('n'):
                item['craft_number'] = int(attribute[1:])

            elif attribute.startswith('c'):
                item['crate_series'] = int(attribute[1:])

            elif attribute.startswith('od'):
                item['output'] = int(attribute[2:])

            elif attribute.startswith('oq'):
                item['output_quality'] = int(attribute[2:])

        item = SKU.matchtemplate(item)

        return item

    """
        Match the generated item or any dictionary to the template
        This will add missing fields, but won't remove unnecessary ones
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

        if not item['tradable']:
            sku += ';untradable'

        if item['quality2'] is not None:
            sku += ';{}'.format(item['quality2'])

        if item['killstreak'] != 0:
            sku += ';kt-{}'.format(item['killstreak'])

        if item['effect'] is not None:
            sku += ';u-{}'.format(item['effect'])

        if item['wear'] is not None:
            sku += ';w{}'.format(item['wear'])
         
        if item['paint_kit'] is not None:
            sku += ';pk{}'.format(item['paint_kit'])

        if item['target'] is not None:
            sku += ';td-{}'.format(item['target'])

        if item['craft_number'] is not None:
            sku += ';n{}'.format(item['craft_number'])

        if item['crate_series'] is not None:
            sku += ';c{}'.format(item['crate_series'])

        if item['output'] is not None:
            sku += ';od-{}'.format(item['output'])

        if item['output_quality'] is not None:
            sku += ';oq-{}'.format((item['output_quality']))

        return sku

    """
        Format single item from:
        http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001
        into SKU
    """
    @staticmethod
    def fromapi(item):

        sku = '{};{}'.format(item['defindex'], item['quality'])

        # Check if item has any additional details

        if 'attributes' in item:
            for attribute in item['attributes']:

                # Check for unusual effect

                if attribute['defindex'] == 134:
                    sku += ';u{}'.format(attribute['float_value'])

                # Check if item is unusual & strange simultaneously

                if attribute['defindex'] == 214 and item['quality'] == 5:
                    sku += ';strange'

                # Check craft number

                if attribute['defindex'] == 229:
                    sku += ';n{}'.format(attribute['value'])

                # Check if it's australium

                if attribute['defindex'] == 2027 and attribute['float_value'] == 1:
                    sku += ';australium'

                # Check crate number

                if attribute['defindex'] == 187:
                    sku += ';c{}'.format(attribute['float_value'])

                # Check killstreak tier

                if attribute['defindex'] == 2025:
                    if attribute['float_value'] == 1:
                        sku += ';kt-1'
                    elif attribute['float_value'] == 2:
                        sku += ';kt-2'
                    elif attribute['float_value'] == 3:
                        sku += ';kt-3'

                # Check target item for non fabricators and non chemistry sets

                if attribute['defindex'] == 2012:
                    sku += ';td-{}'.format(attribute['float_value'])

                # Check if festive

                if attribute['defindex'] == 2053 and attribute['float_value'] == 1:
                    sku += ';festive'

                # Check killstreak tier, only for fabricators

                if attribute['defindex'] == 2000:
                    if 'attributes' in attribute:
                        for subattribute in attribute['attributes'][0]:
                            if attribute['attributes'][0][subattribute] == 2025:
                                if attribute['attributes'][0]['float_value'] == 2:
                                    sku += ';kt-3'
                                elif attribute['attributes'][0]['float_value'] == 1:
                                    sku += ';kt-2'

                # Check target item, output item and output quality

                if 2000 < attribute['defindex'] <= 2009 and attribute['is_output'] is True:
                    for subattribute in attribute['attributes']:
                        if subattribute['defindex'] == 2012:
                            sku += ';td-{}'.format(subattribute['float_value'])
                    sku += ';od-{};oq-{}'.format(attribute['itemdef'], attribute['quality'])

        # Check if item is craftable

        if 'flag_cannot_craft' in item:
            if item['flag_cannot_craft']:
                sku += ';uncraftable'

        # Check if item is tradable

        if 'flag_cannot_trade' in item:
            if item['flag_cannot_trade']:
                sku += ';untradable'
        return sku
