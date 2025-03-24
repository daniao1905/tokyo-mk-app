import streamlit as st
from load_data import get_tokyo_routes

st.set_page_config(page_title="Traslados Tokyo MK", layout="centered")
st.title("Calculadora de Precios - Tokyo MK")

routes = get_tokyo_routes()

vehicle = st.selectbox("Selecciona el vehículo", list(routes.keys()))
destination = st.selectbox("Selecciona el destino (salida desde zona céntrica de Tokyo)", list(routes[vehicle].keys()))

time = routes[vehicle][destination]["time"]
base_price = routes[vehicle][destination]["price"]
tax = int(base_price * 0.10)
total = base_price + tax

st.markdown(f"""
### Resultado
- **Vehículo:** {vehicle}  
- **Destino:** {destination}  
- **Tiempo estimado:** {time}  
- **Precio base:** ¥{base_price:,}  
- **Impuestos (10%):** ¥{tax:,}  
- **Total con impuestos:** ¥{total:,}
""")

st.markdown("""
---

### Avisos importantes

- Los precios son aproximados y pueden variar según el tráfico o condiciones del camino.
- Los valores mostrados **no incluyen peajes, estacionamiento ni servicios especiales** (guías turísticos, sillas de bebé, etc.).
- Se recomienda hacer reservas **al menos 3 días antes**.
- Para presupuestos exactos o reservas, contacta con atención al cliente.

### Política de cancelación
- Cancelación 3 días antes (después de las 9:00) → 30%
- Cancelación 2 días antes (después de las 9:00) → 50%
- Cancelación 1 día antes (después de las 9:00) → 100%
""")
