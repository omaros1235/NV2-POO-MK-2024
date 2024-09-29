
import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get()  # Obtener el texto del campo de entrada
    if task:
        listbox_tasks.insert(tk.END, task)  # Añadir la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

# Función para marcar una tarea como completada
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, task + " - Completada")
    except IndexError:
        messagebox.showwarning("No seleccionada", "Por favor, selecciona una tarea.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("No seleccionada", "Por favor, selecciona una tarea.")

# Crear la ventana principal
window = tk.Tk()
window.title("Gestor de Tareas")

# Crear el campo de entrada para nuevas tareas
entry_task = tk.Entry(window, width=40)
entry_task.pack(pady=10)

# Crear la lista de tareas
listbox_tasks = tk.Listbox(window, height=10, width=50)
listbox_tasks.pack(pady=10)

# Añadir los botones para "Añadir Tarea", "Marcar como Completada" y "Eliminar Tarea"
button_add_task = tk.Button(window, text="Añadir Tarea", command=add_task)
button_add_task.pack(pady=5)

button_complete_task = tk.Button(window, text="Marcar como Completada", command=complete_task)
button_complete_task.pack(pady=5)

button_delete_task = tk.Button(window, text="Eliminar Tarea", command=delete_task)
button_delete_task.pack(pady=5)

# Configurar que presionar Enter añada una nueva tarea
window.bind('<Return>', add_task)

# Ejecutar la ventana
window.mainloop()