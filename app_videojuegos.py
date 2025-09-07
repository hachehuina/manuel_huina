import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # escribe tu contraseña si tienes
    database="BD_Videojuegos"
)
cursor = conexion.cursor()

# Funciones
def agregar_videojuego():
    try:
        sql = "INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES (%s, %s, %s, %s, %s)"
        datos = (id_entry.get(), titulo_entry.get(), genero_entry.get(), clasificacion_entry.get(), plataforma_entry.get())
        cursor.execute(sql, datos)
        conexion.commit()
        messagebox.showinfo("Éxito", "Videojuego agregado.")
        mostrar_videojuegos()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_videojuegos():
    lista.delete(0, tk.END)
    cursor.execute("SELECT * FROM Videojuegos")
    for row in cursor.fetchall():
        lista.insert(tk.END, row)

def eliminar_videojuego():
    id_borrar = id_entry.get()
    cursor.execute("DELETE FROM Videojuegos WHERE ID=%s", (id_borrar,))
    conexion.commit()
    messagebox.showinfo("Eliminado", "Videojuego eliminado.")
    mostrar_videojuegos()

def actualizar_videojuego():
    datos = (
        titulo_entry.get(),
        genero_entry.get(),
        clasificacion_entry.get(),
        plataforma_entry.get(),
        id_entry.get()
    )
    sql = "UPDATE Videojuegos SET Titulo=%s, Genero=%s, Clasificacion=%s, Plataforma=%s WHERE ID=%s"
    cursor.execute(sql, datos)
    conexion.commit()
    messagebox.showinfo("Actualizado", "Videojuego actualizado.")
    mostrar_videojuegos()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestor de Videojuegos")

tk.Label(root, text="ID").grid(row=0, column=0)
tk.Label(root, text="Título").grid(row=1, column=0)
tk.Label(root, text="Género").grid(row=2, column=0)
tk.Label(root, text="Clasificación").grid(row=3, column=0)
tk.Label(root, text="Plataforma").grid(row=4, column=0)

id_entry = tk.Entry(root)
titulo_entry = tk.Entry(root)
genero_entry = tk.Entry(root)
clasificacion_entry = tk.Entry(root)
plataforma_entry = tk.Entry(root)

id_entry.grid(row=0, column=1)
titulo_entry.grid(row=1, column=1)
genero_entry.grid(row=2, column=1)
clasificacion_entry.grid(row=3, column=1)
plataforma_entry.grid(row=4, column=1)

tk.Button(root, text="Agregar", command=agregar_videojuego).grid(row=5, column=0)
tk.Button(root, text="Mostrar", command=mostrar_videojuegos).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar_videojuego).grid(row=6, column=0)
tk.Button(root, text="Actualizar", command=actualizar_videojuego).grid(row=6, column=1)

lista = tk.Listbox(root, width=80)
lista.grid(row=7, column=0, columnspan=2)

mostrar_videojuegos()
root.mainloop()
