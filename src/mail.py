import smtplib
import logging


def send_mails(santas, config):
    logging.info("sending mails")

    with smtplib.SMTP(config["smtp"], config["port"]) as server:
        server.starttls()
        server.login(config["address"], config["password"])
        for name, santa in santas.items():
            logging.info(f"sending to {name}...")
            gifted_str = ", ".join(santa["gifted"])
            message = f"""Subject: Secret santa 2023 !

            Bonjour {name},

            Cette année, tu as l'honneur d'offrir à {gifted_str} !
            Garde ce mail précieusement, il ne te sera pas renvoyé.

            Joyeux Noël !

            """.encode(
                "utf-8"
            )
            server.sendmail(config["address"], santa["email"], message)
