from Grid import ascii_grid

configs = [
    {
        'label': 'Round',
        'width': 40,
        'alignment': '<'
    },
    {
        'label': 'Gives',
        'width': 10,
        'alignment': '^'
    },
    {
        'label': 'Takes',
        'width': 10,
        'alignment': '^'
    }
]

rows = [
    {
        'Round': 'Round 1',
        'Gives': 34,
        'Takes': 15
    },
    {
        'Round': 'Round 2',
        'Gives': 2,
        'Takes': 76
    },
    {
        'Round': 'Round 3',
        'Gives': 19,
        'Takes': 21
    },
    {
        'Round': 'Round 4',
        'Gives': 1,
        'Takes': 26
    }
]

ascii_grid(configs, rows, 'Brad\'s Game Night')