from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('land.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/notification')
def notification():
    return render_template('notification.html')

if __name__ == '__main__':
    app.run(debug=True)

