from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicialiazacion del servidor flask
app= Flask(__name__)

#Configuracion para base de datos
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbcentromedico"
app.secret_key='mysecretkey'

mysql= MySQL(app)



#Declaramos una ruta
#Declaramos ruta index http://localhost:5000
#Ruat se compone de nombre y la funcion
@app.route('/')
def index():
    return render_template('menuadmin.html')

@app.route('/guardarmedico',methods=['POST'])
def guardarmedico():
    if request.method == 'POST':
        rfc= request.form['txtrfc']
        nombre= request.form['txtnombre']
        cedula= request.form['txtcedula']
        correo= request.form['txtcorreo']
        password= request.form['txtpassword']
        rol= request.form['txtrol']
        #print(titulo,artista,año)
        CS = mysql.connection.cursor()
        CS.execute('insert into admedico(rfcmed,nombre,cedula,correo,contraseña,rol) values(%s,%s,%s,%s,%s,%s)',(rfc,nombre,cedula,correo,password,rol))
        mysql.connection.commit()
        

    flash('Album Agregado Correctamente bro')
    return redirect(url_for('index'))


@app.route('/acualizarmedico',methods=['POST'])
def actualizarmedicomedico():
    if request.method == 'POST':
        rfc= request.form['txtrfc']
        nombre= request.form['txtnombre']
        cedula= request.form['txtcedula']
        correo= request.form['txtcorreo']
        password= request.form['txtpassword']
        rol= request.form['txtrol']
        #print(titulo,artista,año)
        CS = mysql.connection.cursor()
        CS.execute('update admedico set nombre = (%s),cedula= (%s),correo= (%s),contraseña= (%s),rol= (%s) where rfcmed=(%s)' )
        mysql.connection.commit()
        

    flash('Album Agregado Correctamente bro')
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('registropaciente.html')

@app.route('/guardarpaciente',methods=['POST'])
def guardarmedico():
    if request.method == 'POST':
        rfc= request.form['txtRFC Médico']
        nombre= request.form['txtNombre del Paciente']
        fecha_nacimiento= request.form['txtFecha de Nacimiento']
        enfermedades= request.form['txtEnfermedades Crónicas']
        alergias= request.form['txtalergias']
        antecendetes= request.form['txtAntecedentes']
        #print(titulo,artista,año)
        CS = mysql.connection.cursor()
        CS.execute('insert into admedico(rfc,nombre,fecha_nacimiento,enfermedades,alergias,antecedentes) values(%s,%s,%s,%s,%s,%s)',(rfc,nombre,fecha_nacimiento,enfermedades,alergias,antecendetes))
        mysql.connection.commit()

@app.route('/eliminar')
def eliminar():
    return "Se elimino el album"

#Lineas que ejecutan el servidor    
if __name__== '__main__':
    app.run(port= 5000, debug=True)