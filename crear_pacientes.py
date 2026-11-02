import json


pacientes = [
    {
        "id": "P001",
        "nombre": "Victor Rivera",
        "edad": 59,
        "sexo": "F",
        "usa_correccion": True
    },
    {
        "id": "P002",
        "nombre": "Sandra Rengifo",
        "edad": 56,
        "sexo": "F",
        "usa_correccion": False
    },
    {
        "id": "P003",
        "nombre": "Lina Rivera",
        "edad": 33,
        "sexo": "F",
        "usa_correccion": True
    },
    {
        "id": "P004",
        "nombre": "Alejandro Rivera",
        "edad": 20,
        "sexo": "M",
        "usa_correccion": True
    },
    {
        "id": "P005",
        "nombre": "Johanna Rivera",
        "edad": 23,
        "sexo": "F",
        "usa_correccion": False
    }
]


with open("pacientes.json", "w") as archivo:

    json.dump(
        pacientes,
        archivo,
        indent=4
    )

    