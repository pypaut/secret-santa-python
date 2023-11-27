import logging
import sys


def check_nb_of_gifted(santas, nb_gifted) -> bool:
    logging.info("checking number of gifted...")
    for _, s in santas.items():
        assert len(s["gifted"]) == nb_gifted
    logging.info("check ok")
    return True


def check_nb_appearances_in_gifted(santas, nb_gifted) -> bool:
    logging.info(f"checking each santa appears {nb_gifted} times...")
    name_counter = {(name, 0) for name in santas}
    name_counter = dict(name_counter)
    for _, santa in santas.items():
        for name in santa["gifted"]:
            name_counter[name] += 1

    for name in name_counter:
        if name_counter[name] != nb_gifted:
            print(
                f"error: {name} receives {name_counter[name]} gifts",
                file=sys.stderr,
            )
            return False

    logging.info("check ok")
    return True


def check_nobody_offers_to_same_clan(santas) -> bool:
    logging.info("checking nobody offers to own clan...")
    for name, santa in santas.items():
        for gifted_name in santa["gifted"]:
            if santa["clan"] == santas[gifted_name]["clan"]:
                print(
                    f"error: {name} offers to {gifted_name}", file=sys.stderr
                )
                return False
    logging.info("check ok")
    return True


def launch_checks(santas, nb_gifted) -> bool:
    return (
        check_nb_of_gifted(santas, nb_gifted)
        and check_nb_appearances_in_gifted(santas, nb_gifted)
        and check_nobody_offers_to_same_clan(santas)
    )
