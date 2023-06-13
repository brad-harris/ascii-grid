#
# configs: dictionary
#   width: int
#   label: str
#   alignment: enum
# rows: dictionary
#   keys are config label, value is string for that column
#
def ascii_grid(configs, rows, header):
    print('\n')
    grid_width = len(configs) + 1
    for config in configs:
        grid_width += config['width']
    print('{text:^{width}}'.format(text=header, width=grid_width))


    header_top_border = '\u250f'
    header_labels = '\u2503'
    header_bottom_border = '\u2521'
    for config in configs:
        header_top_border += '{text:\u2501^{width}}\u2533'.format(text='', width=config['width'])
        header_labels += '{text:{align}{width}}\u2503'.format(text=config['label'], align=config['alignment'], width=config['width'])
        header_bottom_border += '{text:\u2501^{width}}{border}'.format(text='', width=config['width'], border='\u253b' if len(rows) == 0 else '\u2547')
    header_top_border = header_top_border[:-1] + '\u2513'
    header_bottom_border = header_bottom_border[:-1] + '\u2529'
    print(header_top_border)
    print(header_labels)
    print(header_bottom_border)

    for row in rows:
        row_text = '\u2502'
        row_border = '\u2514' if row == rows[-1] else '\u251c'
        for config in configs:
            label = config['label']
            row_text += '{text:{align}{width}}\u2502'.format(text=row[label], align=config['alignment'], width=config['width'])
            row_border += '{text:\u2500^{width}}{border}'.format(text= '', width=config['width'], border='\u2534' if row == rows[-1] else '\u253c')
        print(row_text)
        print(row_border[:-1] + ('\u2518' if row == rows[-1] else '\u2524'))
