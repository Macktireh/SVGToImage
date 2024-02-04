from cairosvg import svg2png


# svg_code = open("assets/sugar.svg", 'rt').read()
svg2png(url="assets/sugar.svg",write_to='assets/output.jpg')