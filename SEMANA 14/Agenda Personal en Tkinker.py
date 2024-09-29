import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitas instalar tkcalendar (pip install tkcalendar)


# Función para agregar un nuevo evento
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha and hora and descripcion:
        treeview.insert('', 'end', values=(fecha, hora, descripcion))
        entrada_fecha.set_date("")
        entrada_hora.delete(0, tk.END)
        entrada_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = treeview.selection()
    if seleccion:
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
        if confirmacion:
            treeview.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona un evento para eliminar.")


# Función para cerrar la aplicación
def salir():
    ventana.quit()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(padx=10, pady=10)

# Frame para la lista de eventos
frame_lista = tk.Frame(frame_principal)
frame_lista.grid(row=0, column=0, columnspan=3, pady=10)

# Lista de eventos (TreeView)
treeview = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings', height=8)
treeview.column("Fecha", width=100)
treeview.column("Hora", width=100)
treeview.column("Descripción", width=300)

treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")

treeview.pack(side="left")

# Barra de desplazamiento
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=treeview.yview)
scrollbar.pack(side="right", fill="y")
treeview.config(yscrollcommand=scrollbar.set)

# Frame para la entrada de datos
frame_entrada = tk.Frame(frame_principal)
frame_entrada.grid(row=1, column=0, columnspan=3, pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entrada_fecha = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy', width=15)
entrada_fecha.grid(row=0, column=1, padx=10)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=1, column=1, padx=10)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entrada_descripcion = tk.Entry(frame_entrada, width=40)
entrada_descripcion.grid(row=2, column=1, padx=10)

# Frame para los botones
frame_botones = tk.Frame(frame_principal)
frame_botones.grid(row=2, column=0, columnspan=3, pady=10)

# Botones
boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=10)

boton_salir = tk.Button(frame_botones, text="Salir", command=salir)
boton_salir.grid(row=0, column=2, padx=10)

# Iniciar el bucle principal
ventana.mainloop()