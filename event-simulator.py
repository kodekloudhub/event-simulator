import time
import random
import logging
import os
from logging.config import dictConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

users = ["USER1", "USER2", "USER3", "USER4"]

events = ["logged in", "logged out", "is viewing page1", "is viewing page2", "is viewing page3"]

# Special message to print at regular interval
special_message = {
    5: "USER5 Failed to Login as the account is locked due to MANY FAILED ATTEMPTS.",
    8: "{0} Order failed as the item is OUT OF STOCK."
}


PRINT_SPECIAL_MESSAGE = "PRINT_SPECIAL_MESSAGE" in os.environ and os.environ["PRINT_SPECIAL_MESSAGE"] or True
OVERRIDE_USER = "OVERRIDE_USER" in os.environ and os.environ["OVERRIDE_USER"] or "USER7"
LOG_HANDLERS = "LOG_HANDLERS" in os.environ and os.environ["LOG_HANDLERS"] or "file,console"

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/log/app.log',
            'maxBytes': 5242880,
            'backupCount': 3,
            'formatter': 'default'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }},
    'root': {
        'level': 'INFO',
        'handlers': LOG_HANDLERS.split(",")
    }
})

i = 0

while True:
    r1 = random.randint(0, len(users)-1)
    r2 = random.randint(0, len(events)-1)
    message = "{0} {1}".format(users[r1], events[r2])
    logging.info(message)
    time.sleep(1)

    i = i + 1

    if PRINT_SPECIAL_MESSAGE != "FALSE":
        for key in special_message:
            mod_5 = i % key
            if mod_5 == 0:
                logging.warning(special_message[key].format(OVERRIDE_USER))

