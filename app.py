import streamlit as st
import tempfile 

# Configurar la página
st.set_page_config(page_title="Visualizador de Videos y Código", layout="wide")

# Título
st.title("Bot Interactivo")

# Subir el video
video_file = st.file_uploader("Carga un video", type=["mp4", "mov", "avi", "mkv"])

if video_file is not None:
    st.success("Video cargado con éxito")

    # Guardar el archivo en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_file.read())
        video_path = temp_file.name  # Ruta del archivo guardado

    # Mostrar el video subido
    st.video(video_path)
else:
    st.warning("Esperando un archivo de video.")

# Subir y mostrar código fijo (no editable)
st.subheader("Código Ejemplo")

# Código que se quiere mostrar (ejemplo en Python)
codigo = '''
def saludar(nombre):
    """
    Esta función recibe un nombre y lo imprime en un mensaje de saludo.
    """
    print(f"Hola, {nombre}!")

saludar("Mundo")
'''

# Mostrar el código con resaltado de sintaxis
st.code(codigo, language="python")

st.graphviz_chart('''
    digraph {
        rankdir=TB;  # De arriba hacia abajo
        node [shape=rect, style=filled, fillcolor=lightblue];  # Estilo de los nodos

        // Nodos para los pasos del algoritmo
        start [label="Inicio", shape=circle, width=.25, style=filled, fillcolor=lightgreen];
        input_list [label="Entrada: Lista y número a buscar", shape=box];
        check_start [label="¿Se encontró el número?", shape=diamond, style=filled, fillcolor=yellow];
        found [label="Número encontrado", shape=box, fillcolor=lightgreen];
        not_found [label="Número no encontrado", shape=box, fillcolor=lightcoral];
        end [label="Fin", shape=circle, width=.25, style=filled, fillcolor=lightcoral];

        // Conexiones entre los pasos del algoritmo
        start -> input_list -> check_start;
        check_start -> found [label="Sí"];
        check_start -> not_found [label="No"];
        found -> end;
        not_found -> end;
    }
''')
