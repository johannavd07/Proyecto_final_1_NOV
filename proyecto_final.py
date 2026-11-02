import json


# =========================================================
# CARGAR PACIENTES
# =========================================================

def cargar_pacientes():

    with open("pacientes.json", "r") as archivo:

        pacientes = json.load(archivo)

    return pacientes


# =========================================================
# GUARDAR PACIENTES
# =========================================================

def guardar_pacientes(pacientes):

    with open("pacientes.json", "w") as archivo:

        json.dump(
            pacientes,
            archivo,
            indent=4
        )


# =========================================================
# 1. REGISTRAR PACIENTE
# =========================================================

def registrar_paciente(pacientes):

    print("\n--- REGISTRAR PACIENTE ---")


    # IDENTIFICADOR ÚNICO

    while True:

        id_paciente = input(
            "Ingrese el identificador del paciente: "
        ).upper()


        repetido = False


        for paciente in pacientes:

            if paciente["id"] == id_paciente:

                repetido = True


        if repetido == True:

            print(
                "Ese identificador ya está registrado."
            )

        else:

            break


    # NOMBRE

    nombre = input(
        "Ingrese el nombre completo: "
    )


    # EDAD

    edad = int(
        input("Ingrese la edad: ")
    )


    while edad < 1 or edad > 120:

        print(
            "La edad debe estar entre 1 y 120 años."
        )

        edad = int(
            input("Ingrese nuevamente la edad: ")
        )


    # SEXO

    sexo = input(
        "Ingrese el sexo: "
    ).upper()


    # CORRECCIÓN VISUAL

    while True:

        respuesta = input(
            "¿Usa corrección visual? (si/no): "
        ).lower()


        if respuesta == "si":

            usa_correccion = True

            break


        elif respuesta == "no":

            usa_correccion = False

            break


        else:

            print(
                "Debe responder si o no."
            )


    # CREAR DICCIONARIO

    nuevo_paciente = {

        "id": id_paciente,

        "nombre": nombre,

        "edad": edad,

        "sexo": sexo,

        "usa_correccion": usa_correccion
    }


    # AGREGAR A LA LISTA

    pacientes.append(
        nuevo_paciente
    )


    # GUARDAR EN JSON

    guardar_pacientes(
        pacientes
    )


    print(
        "Paciente registrado correctamente."
    )


# =========================================================
# 2. CONSULTAR PACIENTE
# =========================================================

def consultar_paciente(pacientes):

    print("\n--- CONSULTAR PACIENTE ---")


    id_buscar = input(
        "Ingrese el identificador del paciente: "
    ).upper()


    encontrado = False


    for paciente in pacientes:

        if paciente["id"] == id_buscar:

            print(
                "ID:",
                paciente["id"]
            )

            print(
                "Nombre:",
                paciente["nombre"]
            )

            print(
                "Edad:",
                paciente["edad"]
            )

            print(
                "Sexo:",
                paciente["sexo"]
            )

            print(
                "Usa corrección visual:",
                paciente["usa_correccion"]
            )


            encontrado = True

            break


    if encontrado == False:

        print(
            "El paciente no está registrado."
        )


# =========================================================
# 3. MOSTRAR PACIENTES REGISTRADOS
# =========================================================

def mostrar_pacientes(pacientes):

    print(
        "\n--- PACIENTES REGISTRADOS ---"
    )


    if len(pacientes) == 0:

        print(
            "No hay pacientes registrados."
        )


    else:

        for paciente in pacientes:

            print(
                paciente["nombre"]
            )


# =========================================================
# 4. BUSCAR PACIENTES CON CORRECCIÓN VISUAL
# =========================================================

def buscar_correccion(pacientes):

    print(
        "\n--- PACIENTES CON CORRECCIÓN VISUAL ---"
    )


    encontrados = 0


    for paciente in pacientes:

        if paciente["usa_correccion"] == True:

            print(
                paciente["nombre"]
            )

            encontrados += 1


    if encontrados == 0:

        print(
            "No hay pacientes que utilicen corrección visual."
        )


# =========================================================
# 5. GENERAR ESTADÍSTICAS
# =========================================================

def generar_estadisticas(pacientes):

    print(
        "\n--- ESTADÍSTICAS DE LA JORNADA ---"
    )


    if len(pacientes) == 0:

        print(
            "No hay pacientes registrados."
        )


    else:

        total_pacientes = len(
            pacientes
        )


        suma_edades = 0

        cantidad_correccion = 0


        for paciente in pacientes:

            suma_edades += paciente["edad"]


            if paciente["usa_correccion"] == True:

                cantidad_correccion += 1


        edad_promedio = (
            suma_edades / total_pacientes
        )


        print(
            "Número total de pacientes:",
            total_pacientes
        )

        print(
            "Edad promedio:",
            edad_promedio
        )

        print(
            "Cantidad de pacientes que utilizan corrección visual:",
            cantidad_correccion
        )


# =========================================================
# MENÚ PRINCIPAL
# =========================================================

def menu():

    print("\n===================================")

    print("        SISTEMA OPTOGESTIÓN")

    print("===================================")

    print("1. Registrar paciente")

    print("2. Consultar paciente")

    print("3. Mostrar pacientes registrados")

    print("4. Buscar pacientes con corrección visual")

    print("5. Generar estadísticas")

    print("6. Salir")


    opcion = input(
        "\nSeleccione una opción: "
    )


    return opcion


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

pacientes = cargar_pacientes()


while True:

    opcion = menu()


    if opcion == "1":

        registrar_paciente(
            pacientes
        )


    elif opcion == "2":

        consultar_paciente(
            pacientes
        )


    elif opcion == "3":

        mostrar_pacientes(
            pacientes
        )


    elif opcion == "4":

        buscar_correccion(
            pacientes
        )


    elif opcion == "5":

        generar_estadisticas(
            pacientes
        )


    elif opcion == "6":

        guardar_pacientes(
            pacientes
        )

        print(
            "\nSaliendo del programa."
        )

        break


    else:

        print(
            "Opción no válida."
        )