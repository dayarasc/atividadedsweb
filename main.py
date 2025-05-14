from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('body.html')


@app.route('/Ciencias')
def portugues():
    return render_template('primeiro.html')


@app.route('/Matematica')
def matematica():
    return render_template('segundo.html')


@app.route('/Historia')
def ciência():
    return render_template('terceiro.html')


@app.route('/Ingles')
def geografia():
    return render_template('quarto.html')


if __name__ == '__main__':
    app.run(debug=True)
