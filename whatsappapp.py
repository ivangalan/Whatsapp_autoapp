import pywhatkit as kit
import time
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
mensaje_factura = "Nos ponemos en contacto con usted desde Solarclic Energías Renovables Canarias en relación a su solicitud para que le realicemos un presupuesto de instalación fotovoltaica.\nPuede enviarnos la factura más reciente de la que disponga a este número de teléfono y le haremos un estudio económico y técnico de su instalación y el presupuesto.\nUn saludo.\n"
# Lista para almacenar los registros
registros = []

def agregar_registro():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    
    if nombre and telefono:
        registros.append((nombre, telefono))
        textbox_registros.insert("end", f"{nombre} - {telefono}\n")
        entry_nombre.delete(0, "end")
        entry_telefono.delete(0, "end")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre y un número de teléfono.")

def enviar_mensajes():
    try:
        for nombre, telefono in registros:
            # Obtener la hora y minuto actuales
            hora_actual = time.localtime().tm_hour
            minuto_actual = time.localtime().tm_min

            # Enviar el mensaje con un retraso de 1 minutos
            kit.sendwhatmsg(f"+{telefono}", f"Buenos días, {nombre}.\n{mensaje_factura}", hora_actual, minuto_actual + 1)
            time.sleep(30)  # Esperar 30 segundos para asegurarse de que el mensaje sea enviado

        messagebox.showinfo("Éxito", "Mensajes enviados con éxito")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar los mensajes: {e}")

# Crear la ventana principal
app = ctk.CTk()
app.title("Enviar Mensaje por WhatsApp")
app.geometry("400x500")
app.eval('tk::PlaceWindow . center')

# Crear y colocar los widgets
label_nombre = ctk.CTkLabel(app, text="Nombre:")
label_nombre.pack(pady=10)
entry_nombre = ctk.CTkEntry(app, width=200)
entry_nombre.pack(pady=10)

label_telefono = ctk.CTkLabel(app, text="Número de Teléfono:")
label_telefono.pack(pady=10)
entry_telefono = ctk.CTkEntry(app, width=200)
entry_telefono.pack(pady=10)

button_agregar = ctk.CTkButton(app, text="Agregar Registro", command=agregar_registro)
button_agregar.pack(pady=10)

textbox_registros = ctk.CTkTextbox(app, height=150, width=300)
textbox_registros.pack(pady=20)

button_enviar = ctk.CTkButton(app, text="Enviar Mensajes", command=enviar_mensajes)
button_enviar.pack(pady=8)

# Iniciar el bucle principal
app.mainloop()
