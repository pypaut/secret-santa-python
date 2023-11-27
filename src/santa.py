import json
import logging
import random


def load_santas(filepath):
    with open(filepath) as user_file:
        file_contents = user_file.read()
    santas = json.loads(file_contents)
    for _, s in santas.items():
        s["gifts"] = 0
    return santas


def select_gifted(santas, nb_gifts):
    logging.info("selecting gifted...")
    for _, s in santas.items():
        potential_santas_names = [
            name
            for name, santa in santas.items()
            if santa["clan"] != s["clan"] and santa["gifts"] < nb_gifts
        ]

        gifted_names = random.sample(potential_santas_names, k=nb_gifts)

        for name in gifted_names:
            santas[name]["gifts"] += 1

        s["gifted"] = gifted_names

    logging.info("gifted ok")
    return santas
