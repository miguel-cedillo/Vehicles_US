# 🚗💨 USA Vehicles Market Analysis | Dashboard Interactivo

> **Analizando el mercado automotriz de EE.UU. a través de una experiencia web dinámica, accesible e interactiva.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly Express](https://img.shields.io/badge/Plotly_Express-5.0%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/plotly-express/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

---

## 📌 Descripción del Proyecto

El proyecto **USA Vehicles Market Analysis** es una aplicación web interactiva desarrollada para la exploración visual de datos del mercado de vehículos usados en los Estados Unidos. 

La herramienta permite a compradores, vendedores y analistas de datos investigar patrones clave de precios, relaciones de depreciación por kilometraje y tiempo de permanencia de los anuncios en el mercado, transformando un conjunto de datos estático (`vehicles_us.csv`) en una plataforma intuitiva de toma de decisiones.

### 🔑 Funcionalidades Clave

* **Visualización Dinámica:** Generación de histogramas y gráficos de dispersión bajo demanda mediante botones interactivos.
* **Filtros por Casilla de Verificación (`st.checkbox`):** Control modular para superponer análisis de variables como días de publicación o año del modelo.
* **Procesamiento Eficiente:** Carga diferida y almacenamiento en caché de datos para un rendimiento rápido en el navegador.

---

## 🛠️ Tecnologías Utilizadas

Este proyecto utiliza el stack fundamental de Data Science y desarrollo web ligero en Python:

* **[Python 3.9+](https://www.python.org/):** Lenguaje base para el tratamiento y manipulación de datos.
* **[Pandas](https://pandas.pydata.org/):** Limpieza, imputación de valores nulos y transformación de series temporales.
* **[Plotly Express](https://plotly.com/python/plotly-express/):** Creación de gráficos vectoriales interactivos con capacidad de *zoom*, *pan* y tarjetas *hover*.
* **[Streamlit](https://streamlit.io/):** Framework para el despliegue del panel de control interactivo en entorno web sin necesidad de escribir HTML/CSS.

---

## ⚙️ Instrucciones de Instalación en Local

Sigue estos pasos ordenados para clonar el proyecto y ejecutar la aplicación en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/tu-repositorio-vehiculos.git
   cd tu-repositorio-vehiculos
   ```

2. **Crear y activar un entorno virtual (Recomendado):**
   * En macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instalar las dependencias del proyecto:**
   Asegúrate de tener el archivo `requirements.txt` en la raíz e instala los paquetes necesarios:
   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar la aplicación de Streamlit:**
   ```bash
   streamlit run app.py
   ```

5. **Acceder a la aplicación:**
   Abre tu navegador e ingresa a la dirección local predeterminada: `http://localhost:8501`.

---

## 📂 Estructura del Repositorio

```text
├── data/
│   └── vehicles_us.csv      # Dataset principal de anuncios de vehículos
├── app.py                   # Código principal de la aplicación Streamlit
├── notebooks/
│   └── EDA_vehicles.ipynb   # Anotaciones y análisis exploratorio inicial
├── .gitignore               # Archivos excluidos del control de versiones
├── README.md                # Documentación del proyecto
└── requirements.txt         # Lista de dependencias del proyecto
```

---

## 📬 Contacto y Colaboración

Desarrollado como parte del portafolio de análisis exploratorio e ingeniería de interfaces de datos. ¡Feedback y contribuciones son siempre bienvenidos!

* **GitHub:** [@miguel-cedillo](https://github.com/miguel-cedillo)

