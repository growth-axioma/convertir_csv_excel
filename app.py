import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="CSV a Excel", page_icon="📄")

st.title("Conversor de CSV a Excel 📄➡️📊")

uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file:
    try:
        # Intentar leer CSV con separador automático
        df = pd.read_csv(uploaded_file, sep=None, engine='python')
        st.success("CSV leído correctamente")
        
        # Convertir a Excel
        output = io.BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        output.seek(0)
        
        # Botón para descargar
        st.download_button(
            label="📥 Descargar Excel",
            data=output,
            file_name=uploaded_file.name.replace(".csv", ".xlsx"),
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Error al procesar el CSV: {e}")
