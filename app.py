import os
from flask import Flask
import ldap     # This is where we get the crash

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello():
    return 'If you see this, the LDAP import is working :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
