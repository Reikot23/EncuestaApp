from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['nombre']
    opinion = request.form['opinion']
    return f"<h1>Gracias, {nombre} </h1><p>por tu opinión: {opinion}.</p>"

if __name__ == '__main__':
    app.run(debug=True)