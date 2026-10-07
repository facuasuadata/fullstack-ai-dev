from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    _dni: int
    _nombre: str

    def __post_init__(self):
        if self._dni <= 0:
            raise ValueError("El DNI debe ser mayor que 0.")

        if not self._nombre:
            raise ValueError("El nombre no puede estar vacío.")

        if len(self._nombre) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres.")

        if not self._nombre[0].isupper():
            raise ValueError("El nombre debe comenzar con mayúscula.")

        if self._nombre[1:] != self._nombre[1:].lower():
            raise ValueError("El resto del nombre debe estar en minúscula.")

    @property
    def dni(self) -> int:
        return self._dni

    @property
    def nombre(self) -> str:
        return self._nombre