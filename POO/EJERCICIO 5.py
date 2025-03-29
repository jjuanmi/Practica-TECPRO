import datetime
class Empresa:
  def __init__(self,nombre):
    self.nombre = nombre
    self.nro_facturas = 0
    self.facturas_emitidas = []
  
  def facturar(self,cliente):
    self.nro_facturas += 1
    factura = Factura(self.nro_facturas,cliente,datetime.date.today())
    self.facturas_emitidas.append(factura)
    return factura

  def mostrar_factura(self,nro):
    print(f"Nombre de la empresa {self.nombre}")
    factura = self.facturas_emitidas[nro-1]
    factura.mostrar_factura()
    print("\n")

#
class Factura:
  def __init__(self,nro_factura,cliente,fecha):
    self.nro_factura = nro_factura
    self.cliente = cliente
    self.fecha = fecha
    self.nro_detalle = 0
    self.detalles = []
  
  def agregar_producto(self,producto,cantidad):
    self.nro_detalle += 1
    detalle = DetalleFactura(self.nro_detalle,producto,cantidad)
    self.detalles.append(detalle)

  def calcular_costo_total(self):
    costo_total = 0
    for detalle in self.detalles:
      costo_total += detalle.calcular_total()
    return costo_total

  def mostrar_factura(self):
    print(f"Factura nro: {self.nro_factura}")
    print(f"Cliente {self.cliente.mostrar_cliente()}")
    print(self.fecha)
    print(f"Costo total: ${self.calcular_costo_total()}")
    for detalle in self.detalles:
      detalle.mostrar_detalle()
#
class Producto:
  def __init__(self,nombre,precio):
    self.nombre = nombre
    self.precio = precio
  
  def obtener_nombre(self):
    return self.nombre
#
class DetalleFactura:
  def __init__(self,nrodetalle,producto,unidades):
    self.nrodetalle = nrodetalle
    self.producto = producto
    self.unidades = unidades

  def calcular_total(self):
    return (self.producto.precio)*(self.unidades)

  def mostrar_detalle(self):
    print(f"Detalle {self.nrodetalle}: {self.producto.obtener_nombre()}  {self.unidades} unid. Total Item : ${self.calcular_total()}.-")

class Cliente:
  def __init__(self,nombre,cuit):
    self.nombre = nombre
    self.cuit = cuit

  def mostrar_cliente(self):
    print(f"{self.nombre} - cuit {self.cuit}")

# se crea una instancia de empresa
empresa1 = Empresa("Mayorista S.A.")
empresa2 = Empresa("MAXI KIOSCO TORTITA S.A")
# se crean clientes
cliente1 = Cliente("Gilcomat SRL – R.I.","30-12345678-1")
cliente2 = Cliente("Roberto Carlos","20-12332266-0")
# se crean productos
producto1 = Producto("Phillip 20 mentolado",300)
producto2 = Producto("Agua savorizada naranja",100)
producto3 = Producto("Coca Cola 3 lt",600)
producto4 = Producto("Fernet Branca 710 mL",400)
# se guardan las facturas
factura1 = empresa1.facturar(cliente1)
factura2 = empresa1.facturar(cliente2)
factura3 = empresa2.facturar(cliente2)
# se agregan productos
factura1.agregar_producto(producto1,100)
factura1.agregar_producto(producto2,1)
factura2.agregar_producto(producto3,10)
factura3.agregar_producto(producto4,9)
factura3.agregar_producto(producto1,3)
# se muestra las facturas
empresa1.mostrar_factura(1)
empresa1.mostrar_factura(2)
empresa2.mostrar_factura(1)
