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
