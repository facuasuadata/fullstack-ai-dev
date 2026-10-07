from models.persona import Persona


class RepositorioPersonas:

    def __init__(self):
        self.__personas: list[Persona] = []
        self.__cargar_datos_prueba()

    def __cargar_datos_prueba(self):
        self.__personas.append(Persona(30111222, "Juan"))
        self.__personas.append(Persona(28333444, "Maria"))
        self.__personas.append(Persona(35555666, "Carlos"))

    def guardar(self, persona: Persona) -> None:
        self.__personas.append(persona)

    def obtener_por_dni(self, dni: int) -> Persona | None:
        for persona in self.__personas:
            if persona.dni == dni:
                return persona

        return None

    def obtener_todas(self) -> list[Persona]:
        return self.__personas.copy()