import streamlit as st
import pandas as pd
import plotly.express as px

#cargamos datos
@st.cache_data
def load_data():
    return pd.read_csv("datos/exam_data.csv")

df = load_data()
##titulo
st.title("Visualizaciones y comparación")
st.markdown("### **Avance vs Presupuesto (k$)**")
st.markdown("---")

##sidebar
st.sidebar.header("Filtros")

#lo de manager
st.sidebar.markdown("**Selecciona Manager**")
managers = st.sidebar.multiselect(
    "",
    options=df["Manager"].unique(),
    default=df["Manager"].unique(),
)

##categoria
st.sidebar.markdown("**Filtra por categoría**")
categorias = st.sidebar.multiselect(
    "",
    options=df["Category"].unique(),
    default=df["Category"].unique(),
)

##filtros
df_filtered = df.copy()
df_filtered = df_filtered[df_filtered["Manager"].isin(managers)]
df_filtered = df_filtered[df_filtered["Category"].isin(categorias)]

##graph
if len(df_filtered) > 0:

    fig = px.scatter(
        df_filtered,
        x="BudgetThousands",
        y="PercentComplete",
        color="State",
        hover_data=["ProjectName", "Manager", "Category"],
    )

    fig.update_layout(
        height=450,    
        width=1200,
        margin=dict(l=20, r=20, t=10, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)
##si no
else:
    st.warning("No hay datos para mostrar con los filtros seleccionados.")
