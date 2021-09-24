from flask import Flask
app = Flast(__name__)


@app.route('/')
def main_page():
    """ This is the main page of the site """
    return 'Hello'


@app.route('/v1/process')
def process():
    pass


def send_sms():
    pass


def check_serial():
    pass


if __name__ == "__main__":
    app.run("localhost", 5000)
