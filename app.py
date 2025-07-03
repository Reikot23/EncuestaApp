from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nombre = request.form['nombre']
    opinion = request.form['opinion']

# Guardar en la base de datos
    conn = sqlite3.connect('encuesta.db')
    c = conn.cursor()
    c.execute ('INSERT INTO respuestas (nombre, opinion) VALUES (?, ?)', (nombre, opinion))
    conn.commit()
    conn.close()

    return f'<h1>Gracias, {nombre} </h1><p>por tu opinión: {opinion}.</p>'

@app.route('/resultados', methods=['GET'])
def ver_resultados():
    conn = sqlite3.connect('encuesta.db')
    c = conn.cursor()
    c.execute('SELECT * FROM respuestas')
    resultados = c.fetchall()
    conn.close()
    return render_template('resultados.html', resultados=resultados)


if __name__ == '__main__':
    app.run(debug=True)