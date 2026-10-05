import streamlit as st
from transformers import pipeline

# 1. Configuración de la página de Streamlit
st.set_page_config(
    page_title="Circuito Informativo - Automatizador",
    page_icon="📰",
    layout="centered"
)

# 2. Encabezado de la aplicación
st.title("📰 Circuito Informativo")
st.subheader("Panel de Automatización y Análisis de Contenido")
st.markdown("Pega el texto, artículo o reporte de la noticia a continuación para generar un resumen y los puntos clave para tu guion.")

# 3. Área de entrada de datos (Texto de la noticia)
texto_noticia = st.text_area(
    "Contenido o fuente de la noticia:", 
    height=250, 
    placeholder="Pega aquí el artículo, la crónica o la información recopilada..."
)

# 4. Botón de procesamiento
if st.button("🚀 Procesar e iniciar análisis"):
    if texto_noticia.strip() == "":
        st.warning("⚠️ Por favor, ingresa algún texto antes de procesar.")
    else:
        # Mostramos un indicador de carga mientras la IA trabaja
        with st.spinner("🤖 Analizando contextos y redactando puntos clave..."):
            try:
                # Cargamos el modelo de procesamiento de lenguaje natural de Hugging Face
                resumidor = pipeline("text-generation", model="gpt2")
                
                # Generamos el texto ajustando los límites
                resultado = resumidor(
                    texto_noticia, 
                    max_length=150, 
                    do_sample=False
                )
                
                resumen_final = resultado[0]['generated_text']
                
                # 5. Mostrar resultados estructurados para tu video
                st.success("¡Análisis completado con éxito!")
                
                st.markdown("### 📝 Resumen Ejecutivo para el Guion:")
                st.info(resumen_final)
                
                # Opcional: Generación automática de ideas para etiquetas o títulos
                st.markdown("### 💡 Sugerencia rápida:")
                st.write("Puedes usar este resumen como la introducción principal o gancho (hook) para los primeros segundos de tu video en YouTube.")

            except Exception as e:
                st.error(f"Ocurrió un error al procesar el texto: {e}")

# 6. Pie de página institucional
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Sistema interno de automatización - @noticieroci</p>", unsafe_allow_html=True)