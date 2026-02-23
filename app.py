"""
ESPECIALIZACION PYTHON FOR ANALYTICS
TRABAJO PRACTICO
AUTOR: LUZ IBAÑEZ
"""

# IMPORTACION DE LIBRERIAS
import streamlit as st
import pandas as pd

# ESTILOS HTML Y CSS (MODO CLARO/OSCURO)
st.markdown(
    """
    <style>

        /* OVERRIDE DEL CONTENEDOR PRINCIPAL DE STREAMLIT */
        .block-container {
            max-width: 95% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        /* VARIABLES DE COLOR PARA AMBOS MODOS */
        :root {
            --text-color-light: #2c3e50;
            --bg-light: #ffffff;
            --box-shadow-light: rgba(0,0,0,0.1);

            --text-color-dark: #ecf0f1;
            --bg-dark: #1e1e1e;
            --box-shadow-dark: rgba(255,255,255,0.1);
        }

        /* MODO CLARO */
        .stApp:not(.dark) {
            --text-color: var(--text-color-light);
            --bg-color: var(--bg-light);
            --shadow-color: var(--box-shadow-light);
        }

        /* MODO OSCURO */
        .stApp.dark {
            --text-color: var(--text-color-dark);
            --bg-color: var(--bg-dark);
            --shadow-color: var(--box-shadow-dark);
        }

        /* TÍTULO PRINCIPAL */
        .main-title {
            font-size: 40px;
            font-weight: 800;
            color: var(--text-color);
            text-align: center;
            margin-top: 20px;
        }

        /* SUBTÍTULOS */
        .sub-title {
            font-size: 22px;
            font-weight: 600;
            color: var(--text-color);
            margin-bottom: 10px;
        }

        /* CAJAS */
        .info-box {
            background-color: var(--bg-color);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px var(--shadow-color);
            margin-bottom: 20px;
            color: var(--text-color);
            width: 100%;
        }

        /* SEPARADOR */
        .divider {
            height: 3px;
            background: #32CD32;
            margin: 25px 0;
            border-radius: 5px;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# CREACION DE MENU
st.sidebar.title("🙋🙋‍♂️ Bienvenido(a)")
interfaz = st.sidebar.selectbox(
    "Elija una opción:",
    [
        "Home 🏡",
        "Ejercicio 1️⃣",
        "Ejercicio 2️⃣",
        "Ejercicio 3️⃣",
        "Ejercicio 4️⃣"
    ]
)

# HOME
if interfaz == "Home 🏡":

    st.write('<h1 class="main-title">Proyecto Aplicado en Streamlit – Fundamentos de Programación</h1>', unsafe_allow_html=True)

    st.image(
        "imagen_home.jpg",
        use_container_width=True
    )

    st.write('<div class="divider"></div>', unsafe_allow_html=True)

    st.write(
        """
        <div class="info-box">
            <p class="sub-title">Datos Generales</p>
            <b>Alumna:</b> Luz de Maria Ibañez Berrospi<br>
            <b>Curso:</b> Especialización en Python for Analytics<br>
            <b>Módulo 1:</b> Python Fundamentals<br>
            <b>Año:</b> 2026
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.write(
        """
        <div class="info-box">
            <p class="sub-title">Objetivo</p>
            Aplicar los conceptos aprendidos en el Módulo 1 (variables, estructuras de datos, control de flujo, 
            funciones, programación funcional y programación orientada a objetos) en el desarrollo de ejercicios 
            prácticos de Finanzas.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write('<div class="divider"></div>', unsafe_allow_html=True)

    st.write(
        """
        <div class="info-box">
            <p class="sub-title">Tecnologías utilizadas</p>
            ✔️ Python<br>
            ✔️ Streamlit<br>
            ✔️ Pandas
        </div>
        """,
        unsafe_allow_html=True
    )


# EJERCICIO 1
elif interfaz == "Ejercicio 1️⃣":
    st.title("Ejercicio 1️⃣")
    st.subheader("Aplicación de: Variables y Condicionales")
    st.write('<div class="divider"></div>', unsafe_allow_html=True)

    #SE OBTIENE EL PRESUPUESTO 
    presupuesto=st.number_input(
        label="**Ingrese el presupuesto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )
    #SE OBTIENE EL GASTO
    gasto=st.number_input(
        label="**Ingrese el gasto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )
    #SE REALIZA Y EVALUA
    if st.button(label="Evaluar"):
        resta=round(presupuesto-gasto,2)
        if gasto<=presupuesto:
            st.success("El gasto se encuentra dentro del presupuesto",icon="✅")           
        else:
            st.warning("El gasto excedió el presupuesto",icon="🚨")            
        st.write(f"**Diferencia:** S/. {resta:.2f}")


#EJERCICIO 2
elif interfaz == "Ejercicio 2️⃣":
    st.title("Ejercicio 2️⃣")
    st.subheader("Aplicación de: Listas y Diccionarios")
    st.write('<div class="divider"></div>', unsafe_allow_html=True)

    # SE CREA LA LISTA VACIA
    if "lista" not in st.session_state:
        st.session_state.lista = []

    st.write("A continuación, ingrese los datos solicitados por cada actividad:")

    #SE OBTIENE EL NOMBRE DE LA ACTIVIDAD
    nombre = st.text_input("**Nombre:**")

    #SE OBTIENE EL TIPO DE ACTIVIDAD
    tipo = st.selectbox(
        "**Tipo:**",
        options=[
            "Gasto fijo",
            "Gasto variable",
            "Gasto financiero",
            "Gasto de emergencia"
        ],
        index=None,
        placeholder="Elija el tipo de actividad ingresada"
    )
    #SE OBTIENE EL PRESUPUESTO
    presupuesto = st.number_input(
        "**Presupuesto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )
    #SE OBTIENE EL GASTO REAL
    gasto_real = st.number_input(
        "**Gasto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )

    #ACCION DEL BOTON: 
    #SE AGREGAN LOS VALORES RECIBIDOS EN UN DICCIONARIO
    if st.button("Agregar"):
        dicc_actividad = {
            "Actividad": nombre,
            "Tipo": tipo,
            "Presupuesto": round(presupuesto, 2),
            "Gasto Real": round(gasto_real, 2)
        }
        #SE AGREGA EL DICCIONARIO EN UNA LISTA
        st.session_state.lista.append(dicc_actividad)
        st.success("Actividad agregada correctamente")

    if st.session_state.lista:
        #SE MUESTRA EN UNA TABLA
        st.dataframe(st.session_state.lista)

        st.write("### Evaluación:")
        #SE RECORRE EN BUCLE Y SE CALCULA LA RESTA
        for actividad in st.session_state.lista:
            presupuesto = actividad["Presupuesto"]
            gasto = actividad["Gasto Real"]
            resta = round(presupuesto - gasto, 2)

            if gasto <= presupuesto:
                st.write(
                    f"Actividad: **{actividad['Actividad']}**"
                )
                st.write(
                    f"Estado: ✅ Dentro del presupuesto (diferencia: **{resta:.2f}**)"
                )
            else:
                st.write(
                    f"Actividad: **{actividad['Actividad']}**"
                )
                st.write(
                    f"Estado: 🚨 Fuera del presupuesto (diferencia: **{resta:.2f}**)"
                )
            st.markdown("---")

#EJERCICIO 3
elif interfaz == "Ejercicio 3️⃣":
    st.title("Ejercicio 3️⃣")
    st.subheader("Aplicación de: Funciones y Programación Funcional")
    st.write('<div class="divider"></div>', unsafe_allow_html=True)
    
    # SE CREA LA LISTA VACIA
    if "lista_actividades" not in st.session_state:
        st.session_state.lista_actividades = []

    #SE OBTIENE EL PRESUPUESTO
    presupuesto = st.number_input(
        label="Ingrese el presupuesto (S/.):", 
        min_value=0.00,
        format="%.2f"
        )

     #SE OBTIENE LA TASA
    tasa = st.number_input(
        label="Ingrese la tasa (%):", 
        min_value=0.00,
        format="%.2f"
        )
    
     #SE OBTIENE LA CANTIDAD DE MESES
    meses = st.number_input(
        label="Ingrese cantidad de meses:", 
        min_value=0,
        step=1
        )

    #FUNCION CALCULAR_RETORNO
    def calcular_retorno(presupuesto, tasa, meses):
        retorno=presupuesto*(tasa/100)*meses
        return retorno

    #ACCION DEL BOTON
    if st.button(label="Calcular retorno"):
        # SE USA MAP Y LAMBDA
        resultado = list(
            map(
                lambda x: calcular_retorno(x[0], x[1], x[2]),
                [(presupuesto, tasa, meses)]
            )
        )
        retorno = resultado[0]

        st.success(f"El retorno calculado es: S/. {retorno:.2f}")

        # SE GUARDA EN LA LISTA LOS VALORES INGRESADOS
        st.session_state.lista_actividades.append({
            "presupuesto": presupuesto,
            "tasa": tasa,
            "meses": meses,
            "retorno": retorno
        })

    # SE MUESTRA LOS REGISTROS
    if st.session_state.lista_actividades:
        st.write("**Registro de presupuestos ingresados:**")

        for i, item in enumerate(st.session_state.lista_actividades, start=1):
            st.write(f"- Presupuesto: S/. {item['presupuesto']:.2f}")
            st.write(f"- Tasa: {item['tasa']}%")
            st.write(f"- Meses: {item['meses']}")
            st.write(f"- **Retorno: S/. {item['retorno']:.2f}**")
            st.markdown("---")



#EJERCICIO 4
elif interfaz == "Ejercicio 4️⃣":
    st.title("Ejercicio 4️⃣")
    st.subheader("Aplicación de: Programación Orientada a Objetos (POO)")
    st.write('<div class="divider"></div>', unsafe_allow_html=True)

    class Actividad:
        #CONSTRUCTOR
        def __init__(self,nombre,tipo,presupuesto,gasto_real):
            self.nombre=nombre
            self.tipo=tipo
            self.presupuesto=presupuesto
            self.gasto_real=gasto_real

        #METODO QUE EVALUA SI EL GASTO_REAL ESTA DENTRO DEL PRESUPUESTO
        def esta_en_presupuesto(self):
            return self.presupuesto<self.gasto_real
        
        #METODO QUE MUESTRA INFORMACIÓN DE LA ACTIVIDAD
        def mostrar_info(self):
            st.write(f"**Nombre:** {self.nombre}")
            st.write(f"**Tipo:** {self.tipo}")
            st.write(f"**Presupuesto:** S/.{self.presupuesto:.2f}")
            st.write(f"**Gasto real:** S/.{self.gasto_real:.2f}")
            resta=round(self.presupuesto-self.gasto_real,2)

            if self.esta_en_presupuesto()==True:
                st.write(f"**Diferencia:** S/. {resta:.2f}")
                st.warning("El gasto excedió el presupuesto",icon="🚨")            
            else:
               st.write(f"**Diferencia:** S/. {resta:.2f}")
               st.success("El gasto se encuentra dentro del presupuesto",icon="✅")

    # SE CREA LA LISTA VACIA
    if "lista_actividades_ej4" not in st.session_state:
        st.session_state.lista_actividades_ej4 = []

    st.write("A continuación, ingrese los datos solicitados por cada actividad:")

    #SE OBTIENE EL NOMBRE DE LA ACTIVIDAD
    nombre_input = st.text_input("**Nombre:**")

    #SE OBTIENE EL TIPO DE ACTIVIDAD
    tipo_input = st.selectbox(
        "**Tipo:**",
        options=[
            "Gasto fijo",
            "Gasto variable",
            "Gasto financiero",
            "Gasto de emergencia"
        ],
        index=None,
        placeholder="Elija el tipo de actividad ingresada"
    )
    #SE OBTIENE EL PRESUPUESTO
    presupuesto_input = st.number_input(
        "**Presupuesto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )
    #SE OBTIENE EL GASTO REAL
    gasto_real_input = st.number_input(
        "**Gasto (S/.):**",
        min_value=0.0,
        format="%.2f"
    )

    #SE REALIZA Y EVALUA
    if st.button(label="Evaluar"):
        #SE CREA UN OBJETO DE LA CLASE ACTIVIDAD
        objeto=Actividad(nombre_input,tipo_input,presupuesto_input,gasto_real_input)

        #SE AGREGA EL OBJETO EN LA LISTA
        st.session_state.lista_actividades_ej4.append(objeto)

    #SE RECORRE LOS ELEMENTOS DE LA LISTA
    if st.session_state.lista_actividades_ej4:
        st.write("**Registro de actividades**")

        for i, actividad in enumerate(st.session_state.lista_actividades_ej4, start=1):
            actividad.mostrar_info()
            st.markdown("---")
    



      