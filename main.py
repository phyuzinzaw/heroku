from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def apple():
    return render_template('apple.html')

if __name__ == '__main__':
    app.run(debug=True)

