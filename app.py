import streamlit as st # pit install streamlit
import pandas as pd # pip install pandas
import plotly.express as px # pip install plotly.express

# Le ponemos titulo a la pagia

st.set_page_config(page_title = "Excel Plotter")
st.title("Excel Plotter ")
# Colocar subtitulo

st.subheader ("Alimente la pagina con su archivo Excel")

# Codigo para cargar el archivo excel.

uploaded_file = st.file_uploader("Cargar archivo", type=["xlsx", "xls"])
if uploaded_file:
    st.markdown("---")
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.dataframe(df)

# creamos grupos para seleccionar de la base de datos, asi poder graficar.
    groupby_columns = st.selectbox("Que te gustaria analizar?", ("Ship Mode", "Segment", "Category","Sub-Category", "Region" ),)    
    
# Creamos lo grupos, con los datos de salida.
    output_columns = ["Sales", "Profit"]
    df_grouped = df.groupby(by= [groupby_columns], as_index=False)[output_columns].sum()
    
# PLOT DATAFRAME

    fig = px.bar(
        df_grouped,
        x=groupby_columns,
        y="Sales",
        color="Profit",
        color_continuous_scale=["red","yellow","green"],
        template="plotly_dark",
        title=f"<b> Ventas y ganancias por {groupby_columns} </b>")   
    
    st.plotly_chart(fig)


