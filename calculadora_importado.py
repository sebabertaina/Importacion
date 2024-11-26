import streamlit as st

def calcular_precio_importado(precio_producto):
    # Constantes de impuestos
    iva = 0.21
    arancel = 0.38

    # Cálculo de impuestos
    if precio_producto <= 400:
        impuestos = precio_producto * iva
    else:
        impuestos_base = 400 * iva
        excedente = precio_producto - 400
        impuestos_excedente = excedente * (arancel + iva)
        impuestos = impuestos_base + impuestos_excedente

    precio_total = precio_producto + impuestos
    return precio_total

def convertir_a_pesos(precio_dolares, tipo_cambio):
    return precio_dolares * tipo_cambio

# Configurar la aplicación Streamlit
st.title("Calculadora de Precio de Producto Importado")

# Entrada para el precio del producto
precio_producto = st.number_input("Ingrese el precio del producto en dólares:", min_value=0.0, step=0.01)

if precio_producto > 0:
    # Calcular precio final en dólares (sin incluir flete)
    precio_final_dolares = calcular_precio_importado(precio_producto)
    st.write(f"El precio final del producto en dólares (sin incluir flete) es: **${precio_final_dolares:.2f}**")

    # Entrada para el costo de flete
    costo_flete = st.number_input("Ingrese el costo del flete en dólares:", min_value=0.0, step=0.01)
    precio_final_con_flete = precio_final_dolares + costo_flete

    if costo_flete > 0:
        st.write(f"El precio final del producto con flete es: **${precio_final_con_flete:.2f}**")

    # Entrada para el tipo de cambio
    tipo_cambio = st.number_input("Ingrese el tipo de cambio actual (dólar a peso):", min_value=0.0, step=0.01)

    if tipo_cambio > 0:
        # Convertir a pesos
        precio_final_pesos = convertir_a_pesos(precio_final_con_flete, tipo_cambio)
        st.write(f"El precio final del producto en pesos es: **${precio_final_pesos:.2f}**")
