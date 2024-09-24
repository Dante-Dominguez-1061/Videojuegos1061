class Videojuego1061:
    id_videojuego = 0
    titulo = ""
    genero = ""
    compañia = ""
    precio = 0.0
    fecha_de_lanzamiento = ""
    stock = 0

def lista_titulos():
    titulos = ["Super Mario Bros","The Legend of Zelda","Pacman","Megaman","Sonic"]
    for x in titulos:
        print(x)

def tupla_generos():
    generos = ("Accion","Aventura","Terror","Rompecabezas","Familiar")
    for x in generos:
        print(x)

def diccionario_producto_precio():
    producto_precio = {
        "Producto":["Super Mario 64","Sonic 3","God of War","Crash Bandicoot","Pacman"],
        "Precio":[400.0,700.0,300.0,600.0,900.0]
    }
    for x,y in producto_precio.items():
        print(x,y)

datos = Videojuego1061()

datos.id_videojuego = 430
datos.titulo = "Mario Bros 3"
datos.genero = "Aventura"
datos.compañia = "Nintendo"
datos.precio = 1400.0
datos.fecha_de_lanzamiento = "12/06/1987"
datos.stock = 17

print("Lista de datos")

def mostrar_datos():
    print(f"ID videojuego: {datos.id_videojuego}")
    print(f"Titulo: {datos.titulo}")
    print(f"Genero: {datos.genero}")
    print(f"Compañia: {datos.compañia}")
    print(f"Precio: {datos.precio}")
    print(f"Fecha de lanzamiento: {datos.fecha_de_lanzamiento}")
    print(f"Stock: {datos.stock}")
    print("\n")

print("\n")
mostrar_datos()
print("Lista de titulos")
lista_titulos()
print("\n")
print("Tupla de generos")
tupla_generos()
print("\n")
print("Diccionario de precios y stock")
diccionario_producto_precio()
print("\n")