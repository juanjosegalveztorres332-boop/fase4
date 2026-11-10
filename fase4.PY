from abc import ABC, abstractmethod


# Clase abstracta para las entidades del sistema
class Entidad(ABC):
    def __init__(self, identificador):
        self.identificador = identificador

    @abstractmethod
    def es_valida(self):
        """Cada entidad debe implementar su propia validación."""
        pass


# Entidad concreta de ejemplo
class Cliente(Entidad):
    def __init__(self, identificador, nombre, correo):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo

    def es_valida(self):
        return (
            isinstance(self.nombre, str)
            and bool(self.nombre.strip())
            and isinstance(self.correo, str)
            and "@" in self.correo
        )


# Clase abstracta para los servicios
class Servicio(ABC):
    @abstractmethod
    def crear(self, entidad):
        """Crea o guarda una entidad."""
        pass

    @abstractmethod
    def buscar_por_id(self, identificador):
        """Busca una entidad por su identificador."""
        pass

    @abstractmethod
    def listar(self):
        """Devuelve todas las entidades."""
        pass


# Servicio concreto que guarda clientes en memoria
class ServicioClientes(Servicio):
    def __init__(self):
        self.clientes = []

    def crear(self, cliente):
        if not cliente.es_valida():
            raise ValueError("Los datos del cliente no son válidos.")

        self.clientes.append(cliente)
        return cliente

    def buscar_por_id(self, identificador):
        for cliente in self.clientes:
            if cliente.identificador == identificador:
                return cliente
        return None

    def listar(self):
        return self.clientes.copy()


# Ejemplo de uso
cliente = Cliente(1, "Ana Pérez", "ana@email.com")
servicio = ServicioClientes()

servicio.crear(cliente)

print(cliente.es_valida())           # True
print(servicio.buscar_por_id(1).nombre)  # Ana Pérez
print(len(servicio.listar()))        # 1

import re


class Cliente:
    def __init__(self, identificador, nombre, correo, edad):
        self.identificador = identificador
        self.nombre = nombre
        self.correo = correo
        self.edad = edad

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("El identificador debe ser un entero positivo.")
        self.__identificador = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", valor
        ):
            raise ValueError("El correo no es válido.")
        self.__correo = valor.strip()

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or not 18 <= valor <= 120:
            raise ValueError("La edad debe ser un número entero entre 18 y 120.")
        self.__edad = valor

    def __str__(self):
        return (
            f"Cliente {self.identificador}: {self.nombre}, "
            f"{self.correo}, {self.edad} años"
        )


# Crear y mostrar varios clientes
clientes = [
    Cliente(1, "Ana Pérez", "ana@email.com", 25),
    Cliente(2, "Luis Gómez", "luis@email.com", 32),
]

for cliente in clientes:
    print(cliente)

# Probar las validaciones
try:
    Cliente(3, "Marta Ruiz", "correo-invalido", 20)
except ValueError as error:
    print("Validación correcta:", error)
