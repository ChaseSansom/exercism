def resistor_label(colors):
    # resistance digits
    bands = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }
    # tolerance percentages
    tolerances = {
        'grey': 0.05,
        'violet': 0.1,
        'blue': 0.25,
        'green': 0.5,
        'brown': 1,
        'red': 2,
        'gold': 5,
        'silver': 10
    }
    # prefixes
    metric_prefixes = ['', 'kilo', 'mega', 'giga']
    
    # read input
    if len(colors) == 1:
        color = colors[0]
        resistance = bands[color]
        return f'{resistance} ohms'
    else:
        resistances = [bands[color] for color in colors[:-2]]

    if len(colors) > 2:
        multiplier, tolerance = bands[colors[-2]], tolerances[colors[-1]]

    # calculating total resistance
    total = resistances[0]
    for resistance in resistances[1:]:
        total *= 10
        total += resistance
    total *= (10**multiplier)
    while (total >=  1000):
        if total % 1000 == 0:
            total //= 1000
        else:
            total /= 1000
    
    # find prefix to add
    prefix = (multiplier + len(resistances) - 1) // 3
    return f'{total} {metric_prefixes[prefix]}ohms ±{tolerance}%'
            