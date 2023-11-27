#!/usr/bin/python

import logging
import yaml

from src.check import launch_checks

# from src.mail import send_mails
from src.santa import load_santas, select_gifted


def main():
    logging.basicConfig(level=logging.DEBUG)

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    santas = load_santas(config["santas_file"])

    try:
        santas = select_gifted(santas, config["nb_gifts"])
    except ValueError:
        logging.error("could not finish, start again")
        return

    if not launch_checks(santas, config["nb_gifts"]):
        logging.error("checks did not complete")
        return

    # send_mails(santas, config["mail"])


if __name__ == "__main__":
    main()
