import tkinter as tk
from tkinter import messagebox
import csv
import os


ARCHIVO_UNICO = "registro_estudiantes.csv"
ENCABEZADOS = [
    "Nombre", "RUT", "Sala", "Fecha",
    "Álgebra", "Geometría", "Funciones",
    "Puntaje Ensayo",
    "Horas de Sueño", "Estado de Ánimo", "Estrés",
    "Asistencia"
]

def crear_csv_si_no_existe(nombre, encabezado):
    if not os.path.exists(nombre):
        with open(nombre, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(encabezado)

def guardar_o_actualizar(registro):
    if not os.path.exists(ARCHIVO_UNICO):
        with open(ARCHIVO_UNICO, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
            writer.writeheader()

    datos = []
    actualizado = False

    with open(ARCHIVO_UNICO, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if (fila["Nombre"] == registro["Nombre"] and
                fila["Sala"] == registro["Sala"] and
                fila["Fecha"] == registro["Fecha"]):
                for k, v in registro.items():
                    if v:
                        fila[k] = v
                actualizado = True
            datos.append(fila)

    if not actualizado:
        nueva_fila = {col: "" for col in ENCABEZADOS}
        for k, v in registro.items():
            nueva_fila[k] = v
        datos.append(nueva_fila)

    with open(ARCHIVO_UNICO, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ENCABEZADOS)
        writer.writeheader()
        writer.writerows(datos)

# VENTANAS

def ventana_asistencia():
    win_sala = tk.Toplevel(root)
    win_sala.title("Datos Generales de Asistencia")

    tk.Label(win_sala, text="Sala").pack()
    entry_sala = tk.Entry(win_sala)
    entry_sala.pack()

    tk.Label(win_sala, text="Fecha (YYYY-MM-DD)").pack()
    entry_fecha = tk.Entry(win_sala)
    entry_fecha.pack()

    def abrir_registro_estudiantes():
        sala = entry_sala.get()
        fecha = entry_fecha.get()

        if not sala or not fecha:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa Sala y Fecha.")
            return

        win_sala.destroy()

        def agregar_estudiante():
            nombre = entry_nombre.get()
            rut = entry_rut.get()
            asistencia = asistencia_var.get()

            if not nombre or not rut:
                messagebox.showwarning("Campos Vacíos", "Completa nombre y RUT.")
                return

            registro = {
                "Nombre": nombre,
                "RUT": rut,
                "Sala": sala,
                "Fecha": fecha,
                "Asistencia": asistencia
            }
            guardar_o_actualizar(registro)
            entry_nombre.delete(0, tk.END)
            entry_rut.delete(0, tk.END)

        def finalizar():
            win_estudiantes.destroy()
            messagebox.showinfo("Finalizado", "Asistencia registrada.")

        win_estudiantes = tk.Toplevel(root)
        win_estudiantes.title("Registrar Estudiantes")

        tk.Label(win_estudiantes, text=f"Sala: {sala} | Fecha: {fecha}").pack(pady=5)

        tk.Label(win_estudiantes, text="Nombre del Estudiante").pack()
        entry_nombre = tk.Entry(win_estudiantes)
        entry_nombre.pack()

        tk.Label(win_estudiantes, text="RUT").pack()
        entry_rut = tk.Entry(win_estudiantes)
        entry_rut.pack()

        asistencia_var = tk.StringVar(value="Presente")
        tk.Label(win_estudiantes, text="Asistencia").pack()
        tk.OptionMenu(win_estudiantes, asistencia_var, "Presente", "Ausente", "Justificado").pack()

        tk.Button(win_estudiantes, text="Agregar otro", command=agregar_estudiante, bg="green", fg="white").pack(pady=5)
        tk.Button(win_estudiantes, text="Finalizar", command=finalizar, bg="gray", fg="white").pack(pady=5)

    tk.Button(win_sala, text="Continuar", command=abrir_registro_estudiantes, bg="blue", fg="white").pack(pady=10)


def ventana_ensayo():
    win_fecha = tk.Toplevel(root)
    win_fecha.title("Fecha del Ensayo")

    tk.Label(win_fecha, text="Fecha del Ensayo (YYYY-MM-DD)").pack()
    entry_fecha = tk.Entry(win_fecha)
    entry_fecha.pack()

    def abrir_formulario_estudiantes():
        fecha = entry_fecha.get()
        if not fecha:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una fecha.")
            return

        win_fecha.destroy()

        def agregar_estudiante():
            nombre = entry_nombre.get()
            rut = entry_rut.get()
            puntaje = entry_puntaje.get()

            if not nombre or not rut or not puntaje:
                messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
                return

            registro = {
                "Nombre": nombre,
                "RUT": rut,
                "Fecha": fecha,
                "Puntaje Ensayo": puntaje
            }
            guardar_o_actualizar(registro)
            entry_nombre.delete(0, tk.END)
            entry_rut.delete(0, tk.END)
            entry_puntaje.delete(0, tk.END)

        def finalizar():
            win_estudiantes.destroy()
            messagebox.showinfo("Finalizado", "Puntajes registrados.")

        win_estudiantes = tk.Toplevel(root)
        win_estudiantes.title("Agregar Puntajes de Ensayo")

        tk.Label(win_estudiantes, text=f"Fecha: {fecha}").pack(pady=5)

        tk.Label(win_estudiantes, text="Nombre del Estudiante").pack()
        entry_nombre = tk.Entry(win_estudiantes)
        entry_nombre.pack()

        tk.Label(win_estudiantes, text="RUT").pack()
        entry_rut = tk.Entry(win_estudiantes)
        entry_rut.pack()

        tk.Label(win_estudiantes, text="Puntaje del Ensayo").pack()
        entry_puntaje = tk.Entry(win_estudiantes)
        entry_puntaje.pack()

        tk.Button(win_estudiantes, text="Agregar otro", command=agregar_estudiante, bg="blue", fg="white").pack(pady=5)
        tk.Button(win_estudiantes, text="Finalizar", command=finalizar, bg="gray", fg="white").pack(pady=5)

    tk.Button(win_fecha, text="Continuar", command=abrir_formulario_estudiantes, bg="blue", fg="white").pack(pady=10)


def ventana_controles_animo():
    win_info = tk.Toplevel(root)
    win_info.title("Datos del Control")

    tk.Label(win_info, text="Fecha del Control (YYYY-MM-DD)").pack()
    entry_fecha = tk.Entry(win_info)
    entry_fecha.pack()

    tk.Label(win_info, text="Tipo de Control").pack()
    entry_tipo_control = tk.Entry(win_info)
    entry_tipo_control.pack()

    tk.Label(win_info, text="Nombre del Control").pack()
    entry_nombre_control = tk.Entry(win_info)
    entry_nombre_control.pack()

    def abrir_formulario_estudiantes():
        fecha = entry_fecha.get()
        tipo_control = entry_tipo_control.get()
        nombre_control = entry_nombre_control.get()

        if not fecha or not tipo_control or not nombre_control:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
            return

        win_info.destroy()

        def agregar_estudiante():
            nombre = entry_nombre.get()
            sueno = entry_sueno.get()
            animo = estado_animo_var.get()
            estres = entry_estres.get()

            if not nombre or not sueno or not estres:
                messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
                return

            registro = {
                "Fecha Control": fecha,
                "Tipo Control": tipo_control,
                "Nombre Control": nombre_control,
                "Nombre Estudiante": nombre,
                "Horas de Sueño": sueno,
                "Estado de Ánimo": animo,
                "Estrés": estres
            }
            guardar_o_actualizar(registro)
            entry_nombre.delete(0, tk.END)
            entry_sueno.delete(0, tk.END)
            entry_estres.delete(0, tk.END)

        def finalizar():
            win_estudiantes.destroy()
            messagebox.showinfo("Finalizado", "Datos de controles y ánimo registrados.")

        win_estudiantes = tk.Toplevel(root)
        win_estudiantes.title("Agregar datos de estudiantes")

        tk.Label(win_estudiantes, text=f"Control: {nombre_control} ({tipo_control})").pack(pady=5)
        tk.Label(win_estudiantes, text=f"Fecha: {fecha}").pack(pady=5)

        tk.Label(win_estudiantes, text="Nombre del Estudiante").pack()
        entry_nombre = tk.Entry(win_estudiantes)
        entry_nombre.pack()

        tk.Label(win_estudiantes, text="Horas de sueño promedio").pack()
        entry_sueno = tk.Entry(win_estudiantes)
        entry_sueno.pack()

        tk.Label(win_estudiantes, text="Estado de ánimo").pack()
        estado_animo_var = tk.StringVar(value="Neutro")
        tk.OptionMenu(win_estudiantes, estado_animo_var, "Feliz", "Neutro", "Triste", "Ansioso", "Cansado").pack()

        tk.Label(win_estudiantes, text="Nivel de estrés (1-5)").pack()
        entry_estres = tk.Entry(win_estudiantes)
        entry_estres.pack()

        tk.Button(win_estudiantes, text="Agregar otro", command=agregar_estudiante, bg="orange", fg="black").pack(pady=5)
        tk.Button(win_estudiantes, text="Finalizar", command=finalizar, bg="gray", fg="white").pack(pady=5)

    tk.Button(win_info, text="Continuar", command=abrir_formulario_estudiantes, bg="orange", fg="black").pack(pady=10)


# ====================== VENTANA PRINCIPAL ======================

root = tk.Tk()
root.title("Sistema de Registro PAES")
root.geometry("400x400")

tk.Label(root, text="Sistema PAES", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Registrar Asistencia", command=ventana_asistencia, width=30).pack(pady=10)
tk.Button(root, text="Agregar Puntaje de Ensayo", command=ventana_ensayo, width=30).pack(pady=10)
tk.Button(root, text="Controles por Área + Ánimo", command=ventana_controles_animo, width=30).pack(pady=10)

root.mainloop()
