# Sistema Optogestión

## Descripción <3

Sistema Optogestión es un programa desarrollado en Python para un centro universitario de atención optométrica.

Su objetivo es permitir el registro, almacenamiento, consulta y procesamiento básico de la información de pacientes atendidos durante jornadas visuales.

El programa funciona mediante consola y presenta un menú principal que permanece disponible hasta que el usuario selecciona la opción de salir.

## Funcionalidades

El programa permite:

1. Registrar un nuevo paciente.
2. Consultar un paciente mediante su identificador.
3. Mostrar los nombres de todos los pacientes registrados.
4. Buscar los pacientes que utilizan corrección visual.
5. Generar estadísticas básicas de la jornada:
   - Número total de pacientes.
   - Edad promedio de los pacientes.
   - Cantidad de pacientes que utilizan corrección visual.
6. Salir del programa.

## Información almacenada

Para cada paciente se registran los siguientes datos:

- Identificador único.
- Nombre completo.
- Edad.
- Sexo.
- Uso de corrección visual.

Los pacientes se almacenan mediante una lista de diccionarios.

## Almacenamiento de datos

La información se conserva en el archivo:

`pacientes.json`

El programa utiliza el módulo `json` de Python para leer y guardar los registros.

El archivo contiene seis registros de pacientes utilizados para comprobar el funcionamiento del sistema.

## Archivos del proyecto

`proyecto_final.py`  
Contiene el código principal del programa.

`pacientes.json`  
Contiene los registros de los pacientes.

`README.md`  
Contiene la descripción general del proyecto y las instrucciones para ejecutarlo.

## Conceptos utilizados

Durante el desarrollo del programa se utilizaron conceptos trabajados en Programación I, entre ellos:

- Variables.
- Listas.
- Diccionarios.
- Condicionales `if`, `elif` y `else`.
- Ciclos `for` y `while`.
- Funciones.
- Parámetros.
- `return`.
- Archivos JSON.
- `json.load()`.
- `json.dump()`.

## Instrucciones de ejecución

1. Tener Python instalado en el computador.
2. Tener `proyecto_final.py` y `pacientes.json` dentro de la misma carpeta.
3. Abrir la carpeta del proyecto en Visual Studio Code.
4. Ejecutar el archivo `proyecto_final.py`.
5. Seleccionar una de las opciones disponibles en el menú.
6. Para finalizar el programa, seleccionar la opción `6. Salir`.

## Proyecto académico

Proyecto Final — Programación I  
Programa de Optometría