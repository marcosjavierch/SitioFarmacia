from flask import Flask, render_template, request, redirect, session
import ctrl_bd

app = Flask(__name__)

#definicion de rutas.

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/acercade.html')
def acercade():
    return render_template('acercade.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/productos.html')
def productos():
    return render_template('productos.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/control.html')
def control():
    pacientes = ctrl_bd.consultar_paciente()
    return render_template('control.html', pacientes=pacientes)


@app.route('/register.html')
def register():
   return render_template('register.html')

#method POST
@app.route('/registro', methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    ctrl_bd.agregar_empleado(nombre, correo, contrasena)
    return redirect('login.html')

#method POST-LOGIN
@app.route('/controluser', methods=["POST"])
def controluser():
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    ctrl_bd.consultar_empleado(correo, contrasena)
    return redirect('control.html')


@app.route("/guardar_paciente", methods=["POST"])
def guardar_paciente():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    celular = request.form["celular"]
    ctrl_bd.agregar_paciente(nombre, apellido, correo, direccion, celular)
    return redirect("/control.html")

@app.route("/eliminar_paciente", methods=["POST"])
def eliminar_paciente():
    ctrl_bd.eliminar_paciente(request.form["id"])
    return redirect("/control.html")

@app.route("/editar_paciente/<int:id>")
def editar_paciente(id):
    paciente = ctrl_bd.obtener_paciente_por_id(id)
    return render_template("editarpaciente.html", paciente=paciente)


@app.route("/actualizar_paciente", methods=["POST"])
def actualizar_paciente():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    celular = request.form["celular"]
    ctrl_bd.actualizar_paciente(nombre, apellido, correo, direccion, celular, id)
    return redirect("/control.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)