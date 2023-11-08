from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html',veces=3, color="#9fc5f8")

@app.route('/play/<int:numero>')
def cajas_azules(numero):
        return render_template('index.html', veces=numero, color="#9fc5f8") 

@app.route('/play/<int:numero>/<string:color>')
def cajas_de_colores(numero,color):
        return render_template('index.html', veces=numero, color=color) 

if __name__=="__main__":
    app.run(debug=True)