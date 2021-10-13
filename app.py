from flask import Flask, render_template, request, flash
import os
from formularios import formEstudiante
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/", methods=['GET', 'POST'])
def home():
    form = formEstudiante()
    
    return render_template("Estudiantes.html", form=form)

@app.route("/estudiante/save", methods=['POST'])
def guardar_estudiante():
    form = formEstudiante()
    
    if request.method =='POST':
        documento = form.documento.data
        nombre = form.nombre.data
        ciclo=form.ciclo.data
        sexo= form.sexo.data
        estado= form.estado.data
        
        try:
            with sqlite3.connect('Estudiantes.db') as con:
                cur=con.cursor() #manipula la conexion a la base de datos
                cur.execute("INSERT INTO estudiantes(documento,nombre,ciclo,sexo,estado) VALUES(?,?,?,?,?)",(documento,nombre,ciclo,sexo,estado))
                con.commit()
                return "Guardado satisfactoriamente"
            
        except Error as e:
            print(e)
    return "No se pudo guardar"
            

if __name__ == '__main__':
    app.run(debug=True, port=8000)