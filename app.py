import pandas as pd
import plotly.express as px
import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Dashboard de Anuncios de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# ==============================================================================
# TITULO Y SUBTITULO LLAMATIVOS CON EMOJIS
# ==============================================================================
st.title("🚗💨 Cuadro de Mando: Análisis de Vehículos Usados en EE.UU. 🚙📊")
st.caption("🔍 Explora tendencias de precios, kilometraje y características clave del mercado automotriz.")

st.markdown("---")

# ==============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# ==============================================================================
@st.cache_data
def load_data():
    # Cargar los datos desde la ruta especificada
    df = pd.read_csv("data/vehicles_us.csv")
    
    # Limpieza/preparación básica de datos
    df['is_4wd'] = df['is_4wd'].fillna(0.0)
    df['model'] = df['model'].str.title()
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    
    return df

# Cargar el dataframe
car_data = load_data()

# Vista previa opcional de los datos para confirmación
if st.checkbox("👀 Mostrar vista previa del conjunto de datos"):
    st.write("### Vista previa del Dataset", car_data.head(10))

# ==============================================================================
# ENCABEZADO PRINCIPAL DE INTERACCIÓN
# ==============================================================================
st.header("📈 Herramientas de Visualización Interactiva")
st.write("Utiliza las opciones a continuación para generar gráficos personalizados según tus intereses de análisis.")

# ==============================================================================
# SECCIÓN CON BOTONES (Puntos 4 y 5)
# ==============================================================================
st.subheader("🔘 Generación Visual mediante Botones")

col1, col2 = st.columns(2)

with col1:
    # Botón para construir un histograma de precios
    hist_button = st.button("📊 Construir Histograma de Precios")
    
    if hist_button:
        st.write("#### Distribución de Precios de los Vehículos")
        fig_hist = px.histogram(
            car_data, 
            x="price", 
            nbins=30,
            title="Frecuencia de Precios de Vehículos",
            labels={"price": "Precio ($USD)", "count": "Cantidad de Vehículos"},
            color_discrete_sequence=["#0083B0"]
        )
        fig_hist.update_layout(template="plotly_white")
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    # Botón para construir un gráfico de dispersión (Kilometraje vs Precio)
    scatter_button = st.button("📉 Construir Gráfico de Dispersión")
    
    if scatter_button:
        st.write("#### Relación entre Kilometraje y Precio")
        fig_scatter = px.scatter(
            car_data, 
            x="odometer", 
            y="price", 
            color="condition",
            hover_data=["model", "model_year", "fuel"],
            title="Kilometraje (Odometer) vs. Precio por Condición",
            labels={"odometer": "Kilometraje (Millas)", "price": "Precio ($USD)", "condition": "Condición"},
            opacity=0.7
        )
        fig_scatter.update_layout(template="plotly_white")
        st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# ==============================================================================
# SECCIÓN CON CASILLAS DE VERIFICACIÓN / CHECKBOXES (Punto 6)
# ==============================================================================
st.subheader("☑️ Selección mediante Casillas de Verificación")
st.write("Marca las casillas correspondientes para desplegar los gráficos:")

# Casillas de verificación para activar/desactivar visualizaciones
build_histogram = st.checkbox("Mostrar Histograma de Días Publicado")
build_scatter = st.checkbox("Mostrar Gráfico de Dispersión (Año del Modelo vs. Precio)")

if build_histogram:
    st.write("#### Distribución de Días que el Anuncio Permaneció Publicado")
    fig_days = px.histogram(
        car_data, 
        x="days_listed", 
        color="transmission",
        title="Días Publicados según el Tipo de Transmisión",
        labels={"days_listed": "Días Publicado", "count": "Cantidad de Anuncios"},
        barmode="overlay"
    )
    fig_days.update_layout(template="plotly_white")
    st.plotly_chart(fig_days, use_container_width=True)

if build_scatter:
    st.write("#### Año del Modelo vs. Precio por Tipo de Vehículo")
    fig_year_price = px.scatter(
        car_data, 
        x="model_year", 
        y="price", 
        color="type",
        hover_data=["model", "condition"],
        title="Año del Modelo vs. Precio por Tipo",
        labels={"model_year": "Año del Modelo", "price": "Precio ($USD)", "type": "Tipo"},
        opacity=0.7
    )
    fig_year_price.update_layout(template="plotly_white")
    st.plotly_chart(fig_year_price, use_container_width=True)