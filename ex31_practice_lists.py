return_options = ['crosscourt', 'down the line', 'to the middle']
serve_options_deuce = ['slice out wide', 'slice in body', 'flat down the T']
serve_options_ad = ['slice down the T', 'flat in body', 'flat out wide']

for returning in return_options:
    print(f"You can return here: {returning}")

for serving_deuce in serve_options_deuce:
    print(f"You can serve here: {serving_deuce}")

for serving_ad in serve_options_ad:
    print(f"You can serve here:{serving_ad}")
