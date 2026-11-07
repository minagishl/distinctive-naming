#!/usr/bin/env python3
"""Draw random source domains and construction methods for a naming session.

LLMs cannot choose at random (Zhao, Du & Wang 2026, "LLMs Are Bad Dice Players"),
so asking a model to "pick four unrelated domains" yields the same few each time.
This script supplies real entropy from the operating system.

Usage:
  python3 pick_seeds.py                 # 4 domains, 4 methods, 3 personas
  python3 pick_seeds.py --domains 1 --methods 0 --personas 0   # redraw one domain
  python3 pick_seeds.py --seed 42       # reproducible draw (for testing only)
"""

import argparse
import random

DOMAINS = [
    # Natural world
    'minerals and rock types', 'landforms and hydrology', 'clouds, winds and weather lore',
    'tides and ocean currents', 'volcanology', 'forestry', 'mosses and lichens',
    'fungi', 'insect behavior', 'bird behavior', 'deep-sea creatures', 'seeds and germination',
    # Food and farming
    'beekeeping', 'shepherding and herding', 'fishing gear and methods', 'rice farming tools',
    'grafting and horticulture', 'fermentation and brewing', 'noodle and bread making',
    'tea processing', 'the spice trade', 'smoking and preserving food',
    'kitchen knives and sharpening',
    # Crafts and trades
    'blacksmithing', 'joinery and woodworking', 'lacquerware', 'indigo dyeing', 'weaving and looms',
    'papermaking', 'bookbinding and printing', 'movable type and typefaces',
    'clockmaking and automata',
    'locks and keys', 'musical instrument parts', 'tuning and acoustics', 'mending and laundering',
    # Built world and travel
    'building components', 'stone walls and earthworks', 'harbors and lighthouses',
    'canals and locks',
    'railway signalling and track maintenance', 'postal history and stamps', 'knots and seamanship',
    'mountaineering and rope work', 'surveying and cartography', 'expedition equipment',
    'balloons and airships', 'early bicycles', 'post towns and old highways', 'lamps and lanterns',
    # Culture and play
    'tea ceremony utensils', 'stationery', 'abacuses and calculating aids',
    'traditional toys and games',
    'festival tools and roles', 'shrine architecture', 'Noh and Kyogen theatre',
    'rakugo storytelling',
    'sumo terminology', 'shogi and go', 'martial-arts terminology',
    'backstage crafts of traditional theatre',
    'stage machinery', 'circus', 'stage magic', 'Japanese sweets', 'kimono and obi', 'footwear',
    # Language
    'Tohoku dialects', 'Kyushu and Okinawan dialects', 'archaic Japanese and waka poetry',
    'craftspeople\'s jargon', 'shop names and family crests',
    'old province names and small place names',
    'Japanese onomatopoeia', 'seasonal words (kigo)', 'traditional color names',
    # Science and technology history
    'history of medical instruments', 'medicinal herbs', 'anatomical terms',
    'spectacles and optics',
    'darkroom photography', 'film projectors', 'astronomical observation techniques',
    'crystallography',
    'early electricity', 'radio and Morse code', 'early computing machines',
    'history of cryptography',
    # Records and markets
    'libraries and cataloguing', 'natural-history specimens', 'archaeology tools',
    'conservation of old documents', 'coins, weights and measures', 'markets and auctions',
    # Everyday life
    'food preparation techniques', 'kitchen tools', 'folk household tools',
    'snow-country winter life',
    'fishing-village life', 'mountain-village life',
]

METHODS = [
    'repurposed real word', 'metaphor (cast the function as something else)',
    'compound (one half from a far domain)', 'blend', 'truncation', 'foreign real word',
    'phrase or imperative', 'person or place name', 'onomatopoeia or mimetic word',
    'coinage from same-family parts',
]


# Ordinary (not famous, not "creative") personas restore knowledge partitioning between
# sessions; they beat celebrity/creative personas in Deng, Brucks & Toubia (2026).
OCCUPATIONS = [
    'ferry mechanic', 'school nurse', 'night-shift baker', 'piano tuner', 'tax accountant',
    'rice farmer', 'museum conservator', 'bus driver', 'beekeeper', 'hospital porter',
    'sign painter', 'fishmonger', 'tatami maker', 'railway track inspector', 'florist',
    'hotel concierge', 'veterinary technician', 'sake brewer', 'carpenter', 'librarian',
    'postal carrier', 'kindergarten teacher', 'forklift operator', 'locksmith',
    'radio station engineer', 'sushi chef', 'dental hygienist', 'surveyor', 'tailor',
    'insurance claims adjuster', 'ski patroller', 'used-book seller', 'lighthouse keeper',
    'convenience-store owner', 'translator', 'municipal gardener', 'pharmacist',
]
PLACES = [
    'a port town in Hokkaido', 'a hill village in Shikoku', 'central Osaka', 'rural Tohoku',
    'an island in Okinawa', 'suburban Saitama', 'a lakeside town in Shiga', 'Lisbon',
    'rural Wales', 'Montreal', 'a Norwegian fjord town', 'Oaxaca', 'Busan', 'Tasmania',
    'a mill town in northern England', 'Taipei', 'the Scottish Highlands', 'Nairobi',
    'small-town Iowa', 'Kraków', 'Valparaíso', 'Chiang Mai', 'a Dutch canal town',
]
LIFE_DETAILS = [
    'collects old maps', 'restores bicycles on weekends', 'keeps a vegetable plot',
    'sings in a local choir', 'raises two teenagers', 'fishes at dawn', 'grows bonsai',
    'just took up pottery', 'cares for an elderly parent', 'plays shogi at a club',
    'writes haiku in a notebook', 'repairs old radios', 'walks the same route every morning',
    'runs a neighborhood festival', 'brews tea from garden herbs', 'trains for marathons',
]


def persona(rng: random.Random) -> str:
    return f'a {rng.choice(OCCUPATIONS)} in {rng.choice(PLACES)} who {rng.choice(LIFE_DETAILS)}'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--domains', type=int, default=4)
    parser.add_argument('--methods', type=int, default=4)
    parser.add_argument('--personas', type=int, default=3, help='one per generation round')
    parser.add_argument('--seed', type=int, help='fixed seed, for testing only')
    args = parser.parse_args()

    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
    if args.domains:
        print('domains:', ' / '.join(rng.sample(DOMAINS, min(args.domains, len(DOMAINS)))))
    if args.methods:
        print('methods:', ' / '.join(rng.sample(METHODS, min(args.methods, len(METHODS)))))
    for i in range(args.personas):
        print(f'persona {i + 1}: {persona(rng)}')


if __name__ == '__main__':
    main()
