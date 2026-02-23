from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta productos
@app.route("/productos")
def productos():
    productos = [
        {'nombre': 'Sandalia Playa', 'precio': 20},
        {'nombre': 'Sandalia Casual', 'precio': 30},
        {'nombre': 'Sandalia Deportiva', 'precio': 40}
    ]
    return render_template("productos.html", productos=productos)

# Ruta Acerca de
@app.route("/about")
def about():
    return render_template("about.html")

# Ruta factura
@app.route("/factura")
def factura():
    return render_template("factura.html")

# Ruta clientes
@app.route("/clientes")
def clientes():
    clientes = [
        {'nombre': 'Juan Pérez', 'email': 'juan@correo.com'},
        {'nombre': 'María López', 'email': 'maria@correo.com'}
    ]
    return render_template("clientes.html", clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)