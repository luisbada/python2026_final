import json

# PUNTO A -----------------------------------------

# excepción personalizada para manejar errores de stock inválido
class StockInvalidoError(Exception):
    pass


class DispositivoEcologico: #clase base para dispositivos ecológicos
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock 

    @property 
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser un valor negativo.")
        self.__stock = valor

    def emitir_ficha_tecnica(self):
        return (f"FICHA COMERCIAL BÁSICA:\n"
                f"Dispositivo: {self.nombre}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Stock disponible: {self.__stock} unidades")


class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre: str, precio: float, stock: int, potencia_w: float, eficiencia: float):
        super().__init__(nombre, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    def emitir_ficha_tecnica(self):
        return (f"FICHA COMERCIAL PANEL SOLAR:\n"
                f"Dispositivo: {self.nombre}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Stock disponible: {self.stock} unidades\n"
                f"Potencia: {self.potencia_w}W\n"
                f"Eficiencia: {self.eficiencia}%")



# PUNTO B -----------------------------------------

class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        datos_serializar = []
        for dispositivo in lista_dispositivos:
            datos_dispositivo = {
                "tipo": "PanelSolar" if isinstance(dispositivo, PanelSolar) else "DispositivoEcologico",
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.stock
            }

            # Si es un Panel Solar, añadimos sus atributos específicos
            if isinstance(dispositivo, PanelSolar):
                datos_dispositivo["potencia_w"] = dispositivo.potencia_w
                datos_dispositivo["eficiencia"] = dispositivo.eficiencia

            datos_serializar.append(datos_dispositivo)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos_serializar, archivo, indent=4, ensure_ascii=False)




# PRUEBA

if __name__ == "__main__":
    catalogo_ecotech = []

    print("--- Cargando catálogo de equipamiento sustentable ---")
    
    # Productos válidos
    try:
        p1 = PanelSolar("Panel Monocristalino Pro", 180.50, 15, 400.0, 21.5)
        catalogo_ecotech.append(p1)
        print("Panel 1 creado con éxito.")
    except StockInvalidoError as e:
        print(f"Error inesperado al crear p1: {e}")

    # Producto con stock inválido
    try:
        print("Intentando configurar panel con stock erróneo (-5)...")
        p2 = PanelSolar("Panel Defectuoso", 120.0, -5, 300.0, 18.0)
        catalogo_ecotech.append(p2)
    except StockInvalidoError as e:
        print(f"❌ Captura controlada exitosa: {e}")

    print("\n--- Mostrando fichas técnicas del catálogo ---")
    for dispositivo in catalogo_ecotech:
        print(dispositivo.emitir_ficha_tecnica())
        print("-" * 40)

    # Exportar a JSON 
    archivo_salida = "catalogo_ecotech.json"
    GestorInventario.guardar_catalogo_json(catalogo_ecotech, archivo_salida)
    print(f"Catálogo de productos válidos exportado correctamente a '{archivo_salida}'.")