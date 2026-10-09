from models.persona import Persona
from repositories.persona_repository import RepositorioPersonas


class PersonaService:
    def __init__(self):
        self.repo = RepositorioPersonas()

    def agregar_persona(self, persona: Persona) -> None:
        if self.repo.obtener_por_dni(persona.dni) is not None:
            raise ValueError("Ya existe una persona con ese DNI.")

        self.repo.guardar(persona)

    def obtener_personas(self) -> list[Persona]:
        return self.repo.obtener_todas()

    def obtener_persona_por_dni(self, dni: int) -> Persona | None:
        return self.repo.obtener_por_dni(dni)

    def modificar_persona(self, dni: int, nombre: str) -> Persona:
        if self.repo.obtener_por_dni(dni) is None:
            raise LookupError("La persona no existe.")

        # Persona es inmutable: se crea una nueva (el modelo valida el nombre)
        persona = Persona(dni, nombre)
        self.repo.actualizar(persona)
        return persona

    def eliminar_persona(self, dni: int) -> None:
        if self.repo.obtener_por_dni(dni) is None:
            raise LookupError("La persona no existe.")

        self.repo.eliminar(dni)