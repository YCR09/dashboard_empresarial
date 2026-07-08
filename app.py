import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from dotenv import load_dotenv
import os

from analisis_comercial import comercial
from analisis_ventas import ventas
from analisis_financiero import finanzas
from simulacion_financiera import simulacion
from datos import datos
from informes import informes

st.set_page_config(page_title="Dashboard Empresarial", page_icon="📊", layout="wide")


load_dotenv()

PASSWORD = st.secrets["PASSWORD"]

#PASSWORD = os.getenv("PASSWORD")
#df=datos()

# estado login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# pantalla login
if not st.session_state.authenticated:
    st.write("⚖️ **Información Legal (Disclaimer) y Exención de Responsabilidad**")
    st.caption(
        "**Aviso:** Esta herramienta es un simulador con fines exclusivamente informativos, ilustrativos y educativos."
        "Los resultados, cálculos y proyecciones presentados son estimaciones basadas en los datos introducidos por el usuario y en fórmulas financieras estándar;"
        "por lo tanto, no garantizan resultados futuros, rendimientos ni el éxito comercial de ninguna operación. "
        "El uso de este simulador no constituye ni sustituye la asesoría financiera, contable, fiscal o legal profesional."
        " Cada negocio posee variables únicas y riesgos particulares. El desarrollador de esta herramienta no se hace responsable por pérdidas,"
        " daños o decisiones comerciales tomadas por el usuario basadas en la información generada por este sistema."
    )

    st.title("📈 Dashboard Ejecutivo Empresarial 2026 ")

    st.title("🔒 Acceso privado")

    password = st.text_input(
        "Contraseña",
        type="password"
    )

    if st.button("Entrar"):

        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")

    st.stop()

def main():
    with st.sidebar:
        seleccion = option_menu(
            menu_title="Menú Principal", 
            options=[ "Análisis Comercial", "Análisis Ventas", "Análisis Financiero", "Simulación Financiera", "Informes", "Información"], 
            icons=["briefcase", "graph-up-arrow", "calculator", "activity", "archive", "cloud-upload"], # Nombre de iconos de Bootstrap
            menu_icon="house", 
            default_index=0,
        )
    st.write("⚖️ **Información Legal (Disclaimer) y Exención de Responsabilidad**")
    st.caption(
        "**Aviso:** Esta herramienta es un simulador con fines exclusivamente educativos.  "
        "Los resultados, cálculos y proyecciones presentados son estimaciones basadas en los datos introducidos por el usuario y en fórmulas financieras estándar;"
        "  por lo tanto, **no garantizan resultados futuros, rendimientos, ni el éxito comercial de ninguna operación.** "
        "El uso de este simulador no constituye, ni sustituye **la asesoría financiera, contable, fiscal o legal profesional.**"
        " Cada negocio posee variables únicas y riesgos particulares. **El desarrollador de esta herramienta no se hace responsable por pérdidas,"
        " daños o decisiones comerciales tomadas por el usuario basadas en la información generada por este sistema.**"
    )

    # Lógica para renderizar el contenido según el menú seleccionado
    if seleccion == "Análisis Comercial":
        #st.title("Bienvenido al Inicio")
        comercial()
    elif seleccion == "Análisis Ventas":
        #st.title("Panel de Gráficos")
        ventas()
    elif seleccion == "Análisis Financiero":
        #st.title("Finanzas")
        finanzas()
    elif seleccion == "Simulación Financiera":
        #st.title("Simulación Financiera")
        simulacion()
    elif seleccion == "Informes":
        st.title("Informe Ejecutivo  📑")
        st.caption("P R Ó X I M A M E N T E  . . .")
        #informes()
    elif seleccion == "Información":
        datos()
        #st.title("Ajustes del Sistema")

    # botón cerrar sesión
    if st.sidebar.button("🚪 Cerrar sesión"):

        st.session_state.authenticated = False

        st.rerun()

        st.write("Datos listos para analizar")
        st.dataframe(df)

if __name__ == "__main__":
    main()
