class Contacto:
    """Define los atributos básicos de un contacto, incluyendo nombre y apellido."""
    def __init__(self, nombre, apellido, telefono1, telefono2, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.mail = mail

    def __str__(self):
        """Retorna una representación amigable del contacto para su despliegue."""
        nombre_completo = f"{self.nombre} {self.apellido}".upper()
        return (f"\n--- Detalle de Contacto: {nombre_completo} ---\n"
                f" Teléfono Principal: {self.telefono1}\n"
                f" Teléfono Secundario: {self.telefono2}\n"
                f" E-mail: {self.mail}")

# ----------------------------------------------------

class Agenda:
    """Gestiona la colección de contactos y provee las funcionalidades de la agenda."""
    def __init__(self):
        # La lista 'contactos'
        self.contactos = []
        self._cargar_contactos_iniciales()

    # --- Método de ayuda para carga inicial  ---
    def agregar_contacto_directo(self, nombre, apellido, telefono1, telefono2, mail):
        """Crea y añade un nuevo contacto sin interacción de usuario."""
        nuevo_contacto = Contacto(nombre, apellido, telefono1, telefono2, mail)
        self.contactos.append(nuevo_contacto)

    # --- Método para inicializar los contactos ---
    def _cargar_contactos_iniciales(self):
        self.agregar_contacto_directo("Juan", "Pérez", "123456789", "987654321", "juan.perez@email.com")
        self.agregar_contacto_directo("María", "García", "555444333", "N/A", "maria.g@email.com")
        self.agregar_contacto_directo("Carlos", "López", "777888999", "111222333", "carlos.l@email.com")


    # --- Método de ayuda para búsqueda  ---
    def _buscar_contacto_por_nombre(self, nombre_buscado):
        """Retorna el objeto Contacto si lo encuentra, o None, buscando por nombre y/o apellido."""
        nombre_buscado_lower = nombre_buscado.lower()

        for contacto in self.contactos:
            nombre_completo = f"{contacto.nombre} {contacto.apellido}".lower()

            if contacto.nombre.lower() == nombre_buscado_lower or \
               contacto.apellido.lower() == nombre_buscado_lower or \
               nombre_completo.startswith(nombre_buscado_lower):
                return contacto
        return None

    # --- Funcionalidad 1: Agregar un contacto  ---
    def agregar_contacto_interactivo(self):
        """Pide los datos (incluyendo apellido) al usuario y añade un nuevo contacto."""
        print("\n--- AGREGAR NUEVO CONTACTO ---")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono1 = input("Teléfono Principal: ").strip()
        telefono2 = input("Teléfono Secundario (opcional, N/A si no aplica): ").strip()
        mail = input("E-mail: ").strip()

        if not nombre or not telefono1:
            print(" El nombre y el teléfono principal son obligatorios.")
            return

        self.agregar_contacto_directo(nombre, apellido, telefono1, telefono2, mail)
        print(f"\n Contacto '{nombre} {apellido}' agregado correctamente.")

    # --- Funcionalidad 2: Buscar y Desplegar  ---
    def desplegar_informacion_interactivo(self):
        """Pide un nombre/apellido al usuario, busca el contacto y despliega su información."""
        print("\n--- BUSCAR Y DESPLEGAR CONTACTO ---")
        nombre_buscado = input("Ingrese el Nombre o Apellido del contacto a buscar: ").strip()

        contacto = self._buscar_contacto_por_nombre(nombre_buscado)

        if contacto:
            print(contacto)
        else:
            print(f"\n Contacto '{nombre_buscado}' no encontrado.")

    # --- Funcionalidad 3: Eliminar un contacto  ---
    def eliminar_contacto_interactivo(self):
        """Pide un nombre/apellido al usuario, busca y elimina el contacto."""
        print("\n--- ELIMINAR CONTACTO ---")
        nombre_a_eliminar = input("Ingrese el Nombre o Apellido del contacto a eliminar: ").strip()

        contacto_a_eliminar = self._buscar_contacto_por_nombre(nombre_a_eliminar)

        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)
            print(f"\n Contacto '{contacto_a_eliminar.nombre} {contacto_a_eliminar.apellido}' eliminado correctamente.")
        else:
            print(f"\n Eliminación fallida. Contacto '{nombre_a_eliminar}' no encontrado.")

    # --- Funcionalidad 4: Listar ---
    def listar_contactos(self):
        """Muestra una lista simple de todos los nombres en la agenda."""
        if not self.contactos:
            print("\nLa agenda está vacía. ¡Agrega tu primer contacto!")
            return

        print("\n--- LISTA ACTUAL DE CONTACTOS ---")
        for i, contacto in enumerate(self.contactos):
            print(f"{i+1}. {contacto.nombre} {contacto.apellido}")
        print("-----------------------------------")

# ----------------------------------------------------

def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n================ AGENDA TELEFÓNICA ================")
    print("1. Agregar nuevo contacto")
    print("2. Buscar y desplegar contacto")
    print("3. Eliminar contacto")
    print("4. Listar todos los contactos")
    print("5. Salir")
    print("=====================================================")

def menu_interactivo():
    """Función principal que ejecuta el menú de la agenda."""

    mi_agenda = Agenda()

    print("¡Bienvenido a tu Agenda de Contactos!")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '1':
            mi_agenda.agregar_contacto_interactivo()
        elif opcion == '2':
            mi_agenda.desplegar_informacion_interactivo()
        elif opcion == '3':
            mi_agenda.eliminar_contacto_interactivo()
        elif opcion == '4':
            mi_agenda.listar_contactos()
        elif opcion == '5':
            print("\n ¡Gracias por usar la Agenda! Saliendo del programa.")
            break
        else:
            print("\n Opción no válida. Por favor, ingrese un número del 1 al 5.")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    menu_interactivo()