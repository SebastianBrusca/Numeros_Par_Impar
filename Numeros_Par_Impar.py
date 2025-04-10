import tkinter as tk
from tkinter import messagebox
import csv

# Función para guardar el historial en un archivo CSV
def guardar_historial_en_archivo(historial):
    """Guarda el historial de números ingresados en un archivo CSV"""
    with open('historial_numeros.csv', mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Número'])
        for numero in historial:
            writer.writerow([numero])
    messagebox.showinfo("Historial guardado", "Historial guardado en 'historial_numeros.csv'.")

# Función principal para pedir números y mostrar estadísticas
def pedir_numero_y_comprobar():
    historial = []  # Lista para almacenar el historial de números ingresados
    intentos = 0  # Contador de intentos fallidos
    pares = 0  # Contador de números pares
    impares = 0  # Contador de números impares

    def ingresar_numero(event=None):  # Añadimos el parámetro 'event' para el binding
        nonlocal intentos, pares, impares
        
        try:
            numero = int(entry_numero.get())
            if numero < 1 or numero > 100:
                messagebox.showwarning("Número fuera de rango", "El número debe estar entre 1 y 100. Intenta de nuevo.")
                return

            # Verifica si el número es par o impar
            if numero % 2 == 0:
                resultado = f"El número {numero} es par."
                pares += 1
            else:
                resultado = f"El número {numero} es impar."
                impares += 1

            # Añadimos el número al historial
            historial.append(numero)
            
            # Actualizar la etiqueta de resultado
            label_resultado.config(text=resultado)

            # Actualizar las estadísticas
            actualizar_estadisticas()

            # Limpiar el campo de entrada
            entry_numero.delete(0, tk.END)
            
        except ValueError:
            intentos += 1
            messagebox.showerror("Error de entrada", "¡Eso no es un número válido! Intenta de nuevo.")
            if intentos >= 3:
                messagebox.showerror("Error crítico", "Has fallado demasiadas veces. El programa se cerrará.")
                ventana.quit()

    def actualizar_estadisticas():
        # Actualizar estadísticas (eliminamos el cálculo del promedio)
        total_numeros = len(historial)
        label_estadisticas.config(
            text=f"Total de números: {total_numeros}\nPares: {pares}\nImpares: {impares}"
        )

    def guardar_historial():
        if messagebox.askyesno("Guardar historial", "¿Quieres guardar el historial de números en un archivo CSV?"):
            guardar_historial_en_archivo(historial)

    def reiniciar_historial():
        """Reinicia el historial y las estadísticas"""
        nonlocal historial, pares, impares
        historial = []
        pares = 0
        impares = 0
        label_resultado.config(text="")
        label_estadisticas.config(text="Total de números: 0\nPares: 0\nImpares: 0")
        messagebox.showinfo("Historial reiniciado", "El historial ha sido reiniciado.")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Programa de Números: Par o Impar")
    
    # Establecer el tamaño de la ventana
    ventana.geometry("500x400")
    ventana.resizable(False, False)  # Evitar que la ventana cambie de tamaño

    # Cambiar el color de fondo de la ventana
    ventana.config(bg="#ADD8E6")  # Usamos un color azul claro como fondo
    
    # Crear widgets
    label_instrucciones = tk.Label(ventana, text="Ingresa un número entre 1 y 100:", bg="#ADD8E6")
    label_instrucciones.pack(pady=10)

    entry_numero = tk.Entry(ventana)
    entry_numero.pack(pady=10)

    # Vincular la tecla Enter con la función de ingresar el número
    entry_numero.bind("<Return>", ingresar_numero)

    boton_ingresar = tk.Button(ventana, text="Ingresar Número", command=ingresar_numero)
    boton_ingresar.pack(pady=10)

    label_resultado = tk.Label(ventana, text="", font=("Arial", 14), bg="#ADD8E6")
    label_resultado.pack(pady=10)

    label_estadisticas = tk.Label(ventana, text="Estadísticas: \nTotal de números: 0\nPares: 0\nImpares: 0", font=("Arial", 12), bg="#ADD8E6")
    label_estadisticas.pack(pady=10)

    boton_guardar = tk.Button(ventana, text="Guardar Historial", command=guardar_historial)
    boton_guardar.pack(pady=10)

    boton_reiniciar = tk.Button(ventana, text="Reiniciar Historial", command=reiniciar_historial)
    boton_reiniciar.pack(pady=10)

    # Ejecutar la interfaz gráfica
    ventana.mainloop()

# Ejecutar la función principal
pedir_numero_y_comprobar()


    

