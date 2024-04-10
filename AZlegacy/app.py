""" MAain application of the AZlegacy project """

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = "5000"
    app.run(host, port)
