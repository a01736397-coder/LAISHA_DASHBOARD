import streamlit as st
import pandas as pd

#conf
st.set_page_config(layout="wide")

#inicializar
if "data" not in st.session_state:
    st.session_state.data = pd.read_csv("datos/exam_data.csv")

df = st.session_state.data

#sidebar
st.sidebar.title("Filtros")

estado = st.sidebar.selectbox("Estado", ["Todos"] + sorted(df["State"].unique()))
categoria = st.sidebar.selectbox("Categoría", ["Todos"] + sorted(df["Category"].unique()))
avance_min = st.sidebar.slider("Avance mínimo (%)", 0, 100, 0)
manager = st.sidebar.selectbox("Manager", ["Todos"] + sorted(df["Manager"].unique()))

#filtros
df_filtrado = df.copy()

if estado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["State"] == estado]

if categoria != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Category"] == categoria]

df_filtrado = df_filtrado[df_filtrado["PercentComplete"] >= avance_min]

if manager != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Manager"] == manager]

#titulo
st.markdown("## Dashboard principal de proyectos")

#kpi
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Proyectos", len(df_filtrado))

with col2:
    st.metric("Promedio avance (%)",
              round(df_filtrado["PercentComplete"].mean(), 1) if not df_filtrado.empty else 0)

with col3:
    st.metric("Managers únicos", df_filtrado["Manager"].nunique())

with col4:
    st.metric("Total presupuesto (k$)",
              f"{round(df_filtrado['BudgetThousands'].sum(), 1)}K")

#tabla
st.dataframe(df_filtrado, use_container_width=True)




