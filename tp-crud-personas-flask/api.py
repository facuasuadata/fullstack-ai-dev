from flask import Flask, jsonify, request

from models.persona import Persona
from services.persona_service import PersonaService


app = Flask(__name__)

# Una sola instancia, para que los cambios (POST, PUT, DELETE) se mantengan
servicio = PersonaService()


def persona_a_json(persona: Persona) -> dict:
    return {
        "dni": persona.dni,
        "nombre": persona.nombre
    }


@app.get("/personas")
def obtener_personas():
    return jsonify([persona_a_json(p) for p in servicio.obtener_personas()])


@app.get("/personas/<int:dni>")
def obtener_persona(dni):
    persona = servicio.obtener_persona_por_dni(dni)

    if persona is None:
        return jsonify({"error": "Persona no encontrada"}), 404

    return jsonify(persona_a_json(persona))


@app.post("/personas")
def agregar_persona():
    datos = request.get_json()

    try:
        persona = Persona(datos["dni"], datos["nombre"])
    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": f"Datos inválidos: {error}"}), 400

    try:
        servicio.agregar_persona(persona)
    except ValueError as error:
        return jsonify({"error": str(error)}), 409

    return jsonify(persona_a_json(persona)), 201


@app.put("/personas/<int:dni>")
def modificar_persona(dni):
    datos = request.get_json()

    try:
        persona = servicio.modificar_persona(dni, datos["nombre"])
    except (KeyError, TypeError) as error:
        return jsonify({"error": f"Datos inválidos: {error}"}), 400
    except (LookupError, ValueError) as error:
        return jsonify({"error": str(error)}), 400

    return jsonify(persona_a_json(persona))


@app.delete("/personas/<int:dni>")
def eliminar_persona(dni):
    try:
        servicio.eliminar_persona(dni)
    except LookupError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({"mensaje": f"Persona con DNI {dni} eliminada"})


if __name__ == "__main__":
    app.run(debug=True)