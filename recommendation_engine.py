def get_recommendations(user_data):
    gender = user_data.get('gender', 'male')
    weather = user_data.get('weather', 'mild')
    skin_tone = user_data.get('skin_tone', 'medium')
    body_shape = user_data.get('body_shape', 'rectangle')
    occasion = user_data.get('occasion', 'casual')

    # ─── Top Wear ───────────────────────────────────────────
    top_wear_map = {
        ('male', 'hot'):     'Light cotton t-shirt or linen shirt',
        ('male', 'cold'):    'Wool sweater or thick hoodie',
        ('male', 'rain'):    'Waterproof jacket or raincoat',
        ('male', 'mild'):    'Casual shirt or polo',
        ('female', 'hot'):   'Flowy tank top or crop top',
        ('female', 'cold'):  'Turtleneck or knit sweater',
        ('female', 'rain'):  'Waterproof jacket or trench coat',
        ('female', 'mild'):  'Blouse or light cardigan',
    }

    # ─── Bottom Wear ────────────────────────────────────────
    bottom_wear_map = {
        ('male', 'casual'):   'Slim fit jeans or chinos',
        ('male', 'gym'):      'Track pants or shorts',
        ('male', 'office'):   'Formal trousers',
        ('male', 'formal'):   'Suit trousers',
        ('male', 'date'):     'Dark jeans or chinos',
        ('male', 'wedding'):  'Suit trousers or sherwani bottom',
        ('female', 'casual'): 'High waist jeans or skirt',
        ('female', 'gym'):    'Leggings or yoga pants',
        ('female', 'office'): 'Pencil skirt or trousers',
        ('female', 'formal'): 'Elegant trousers or gown',
        ('female', 'date'):   'Midi skirt or fitted jeans',
        ('female', 'wedding'): 'Lehenga or saree or gown',
    }

    # ─── Footwear ────────────────────────────────────────────
    footwear_map = {
        ('male', 'casual'):   'White sneakers or loafers',
        ('male', 'gym'):      'Sports shoes',
        ('male', 'office'):   'Leather oxford shoes',
        ('male', 'formal'):   'Formal black shoes',
        ('male', 'date'):     'Clean sneakers or loafers',
        ('male', 'wedding'):  'Formal shoes or mojaris',
        ('female', 'casual'): 'Sneakers or sandals',
        ('female', 'gym'):    'Running shoes',
        ('female', 'office'): 'Block heels or flats',
        ('female', 'formal'): 'Stilettos or heels',
        ('female', 'date'):   'Strappy heels or ankle boots',
        ('female', 'wedding'): 'Embellished heels or juttis',
    }

    # ─── Accessories ─────────────────────────────────────────
    accessories_map = {
        'casual':  'Casual watch, sunglasses',
        'gym':     'Sports band, gym bag',
        'office':  'Formal watch, leather belt',
        'formal':  'Tie, cufflinks, dress watch',
        'date':    'Minimalist watch, light perfume',
        'wedding': 'Traditional jewelry, clutch bag',
    }

    # ─── Colors by Skin Tone ─────────────────────────────────
    color_map = {
        'fair':   ['Pastels', 'Baby blue', 'Soft pink', 'Lavender'],
        'medium': ['Earth tones', 'Olive green', 'Mustard', 'Coral'],
        'olive':  ['Jewel tones', 'Emerald', 'Burgundy', 'Royal blue'],
        'dark':   ['Bright colors', 'White', 'Red', 'Gold', 'Orange'],
        'warm':   ['Warm tones', 'Orange', 'Yellow', 'Brown'],
        'cool':   ['Cool tones', 'Blue', 'Purple', 'Silver', 'Pink'],
    }

    # ─── Fabric by Weather ───────────────────────────────────
    fabric_map = {
        'hot':  'Cotton, Linen, Chambray',
        'cold': 'Wool, Fleece, Thermal',
        'rain': 'Polyester, Nylon, Waterproof fabric',
        'mild': 'Cotton blend, Denim, Jersey',
    }

    # ─── Styling Tips ────────────────────────────────────────
    tips_map = {
        'hourglass':          'Wear fitted clothes to highlight your curves.',
        'pear':               'Wear darker bottoms and bright tops to balance.',
        'apple':              'Empire waist tops and A-line skirts work great.',
        'rectangle':          'Add layers and belts to create curves.',
        'inverted_triangle':  'Wide leg pants balance your broad shoulders.',
    }

    # ─── Build Result ────────────────────────────────────────
    top = top_wear_map.get((gender, weather),
          top_wear_map.get(('male', weather), 'Comfortable top'))

    bottom = bottom_wear_map.get((gender, occasion),
             bottom_wear_map.get(('male', occasion), 'Comfortable bottom'))

    footwear = footwear_map.get((gender, occasion),
               footwear_map.get(('male', occasion), 'Comfortable shoes'))

    return {
        'explanation':   f"Outfit for {occasion.title()} in {weather.title()} weather",
        'top_wear':      top,
        'bottom_wear':   bottom,
        'footwear':      footwear,
        'accessories':   accessories_map.get(occasion, 'Watch, belt'),
        'colors':        color_map.get(skin_tone, ['Neutral tones']),
        'fabric':        fabric_map.get(weather, 'Cotton'),
        'styling_tips':  tips_map.get(body_shape, 'Wear what makes you confident!'),
    }