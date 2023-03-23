from config import obtener_conexion

def agregar_empleado(nombre, correo, contrasena):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO empleados(nombre, correo, contrasena) values (%s, %s, %s)", 
                       (nombre, correo, contrasena))
    conexion.commit()
    conexion.close()
    
def consultar_empleado(correo, contrasena):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT correo, contrasena FROM empleados WHERE correo = %s AND contrasena = %s", (correo, contrasena))
    conexion.commit()
    conexion.close()
    

    
def actualizar_usuario(nombre, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE empleados SET nombre WHERE id = %s",
                       (nombre, id))
    conexion.commit()
    conexion.close()


def consultar_paciente():
    conexion = obtener_conexion()
    paciente = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido, correo, direccion, celular FROM pacientes")
        paciente = cursor.fetchall()
    conexion.close()
    return paciente

def obtener_paciente_por_id(id):
    conexion = obtener_conexion()
    paciente = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido, correo, direccion, celular FROM pacientes WHERE id = %s", (id,))
        paciente = cursor.fetchone()
    conexion.close()
    return paciente

def agregar_paciente(nombre, apellido, correo, direccion, celular):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO pacientes(nombre, apellido, correo, direccion, celular) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, correo, direccion, celular))
    conexion.commit()
    conexion.close()

def eliminar_paciente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pacientes WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def actualizar_paciente(nombre, apellido, correo, direccion, celular, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE pacientes SET nombre = %s, apellido = %s, correo = %s, direccion = %s, celular = %s WHERE id = %s",
                       (nombre, apellido, correo, direccion, celular, id))
    conexion.commit()
    conexion.close()