from flask import Flask
from threading import Thread

import main

app = Flask('')


@app.route('/')
def home():
    if main.bot_check():
        return "Neuralia is alive, all ok"
    else:
        print("Problems with bot")


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
