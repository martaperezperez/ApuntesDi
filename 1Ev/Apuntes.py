"""Imos facer o repaso des tipos basicos de Python"""
"""Faremos un resumo, que vai ser moi similar os tipode de "Java" salvo algunhas excepcion"""

#Números
#Cadea de texto
#Valores booleanos

cdea="Un texto"
numero=0o25 #0x para numeros hexadecimales, 0o para numeros octales
booleano= True
print(type(booleano()))

print(type(numero()))
print(numero)

reaise=3e-15
print(type(coplexo()))

"""Repaso dos operadores loxicos mais comuns"""

#+_*/

#negacion -

op= numero**2 #exponente
op= numero//2 #division enteira
op2= numero/2 #division con decimais
resto= numero % 2 #modulo

print(type(op()))
print(type(op2()))
print(type(resto()))

"""Operadores a nivel de bit"""

print(3&4)
print(3|4)
print(3^5)
print(3)
print(3>>1)
print(3<<1)

"""Cadeas"""

c1="hola"
c2="adeus"

print(c1+c2)
print(c1+4)

"""Operaciones booleanas"""

print(True and False)
print(True or False)
print(not True)

print(5==6)
print(5!=6)
print(5<6)

"""Lista"""

l=[1,2,3,4,8,-3]
l=list()

print(type(l()))

l2=[1,2,3,True,"Elemento",[5,6,False]]

print(l[4][1])
print(l2[4][2])
l[-3]=999
l[2]=111

print(l)
print([1:4])
print(l[1:5:2])
print(l[:3])
print(l[1:])
print(l[1::2])

l=[0:2]=["uns","novos","elemento","no","Lista"]
print(l)

"""Duplas"""
t=(a,2,3,"dupla",[1,2,3,True])
#t[1]=8#Las duplas no son editables, con esta linea daria error

t2=1,3,2,0,"outra tabla"
t3=1,
print(type(t3))
t[4][2]=100
print(t)
#t[2][3]="x"
t[3]="outra cousa"
print(t)
c="abcdefghijklmnñopqrstuvwxyz"
print(c[2:8])
print(c[1:15:8])

"""Diccionarios"""

d="un";1,
   "dos";2,
    "tres";3,
    4;"cuatro",
    5;"cinco",
    "Vermello";0xff0000,
    "Amarelo";0xfff00,
    "Verde";0x000ff,
    "Azul";0x0000f,

print(d["dous"])
print(d[5])


"""Funciones"""
def nomeFuncion(parametro,parametro2):

    print("Fai algo con" + parametro)
    print("Outra cousa" + parametro2)
    return1

    nomeFuncion(1,"Outro")

    """
    JAVA CONDICIONALES
    if(condicion){
    instruccion1;
    instruccion2;
    ...;
    }else{
    instruccion1;
    instruccion2;
        }
        """

    """PYTHON CONDICIONALES"""

    var = 0

    if var == 2:
        print("AJAJSJDADJFj")
        print("AJAJSJDADJFj")
        if var == 1:
            print("AJAJSJDADJFj")
        else:
            print("miawela")
    else:
        print("AJAJSJDADJFj")
        print("AJAJSJDADJFj")

    """int variable = (condicion) ? valor1: valor2;"""

    variable = "pan" if var % 2 == 0 else "Impar"

    """WHILE"""

    numero = 0
    while numero < 30:
        print("Numero: " + str(numero))
        numero += 1

    while True:
        numero += 1
        print("Numero: " + str(numero))
        if numero == 30:
            break

    """FOR"""

    coleccion = [1, 2, 3, 4, 5, 9]

    for numero in coleccion:
        print(numero)

        """for(i=0;i<5;i++)"""

    for i in range(5):
        print(i)

        d= {1: "un",
            2:"dous",
            3: "tres"}
        for valor in d.values():
            print(valor)
____________________________________________

def nomefuncion(parametro1, parametro2):
    """En esta parte
    facemos a descripcion-documentacion da funcion
    """

    print(parametro1)



def funcion2(parametro1=2, parametro2="Manuel"):
    """En esta funcion imos darlle valores os parametros por defecto
    
    """
    print(parametro1)
    print(parametro2)

def funcionNumeroParametrosVariable(parametro1,prametro2,*outros):
    """Funcion con número de parámetros variable"""

    print(parametro1)
    print(parametro2)
    for parametro in outros:
        print(parametro)

funcionNumeroParametrosVariable(1,2,3,4,5)


def funcionNumeroParametrosVariableConIdentificador(nome, dni, **outros):
    print("Nome: " + nome)
    print("Dni: " + dni)
    for elemento in outros.keys():
        print(elemento + " " + outros[cave])

funcionNumeroParametrosVariableConIdentificador("Manuel", "33333S", Edade=34, Sexo="Home")

def funcionretornarvariosvalores(x,y):

    """As funciones en python poden retornar mais dun valor"""

    return x*2,y*2,2

a,b,c=funcionretornarvariosvalores(5,3)

#print(t[0])

print(b)
print(c)



Z = [c * n for n in x for c in y if n > 1]
"""La linea de arriba es lo mismo que:"""

print(Z)

Z = []
for n in x:
    for c in y:
        if n > 1:
            Z.append(n * c)

"""Xeradores"""

x = (n**2 for n in l)

print(type(l5))
print(type(x))
print(l5)
print(x)
lista = list(x)
print(lista)
for elemento in x:
    print(elemento)

"""Decoradores"""

def meu_decorador(funcion):
    def nova (*args):
        print("Chamada a funcion ", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nova

meu_decorador(saudar)("en")

def saudar2():
    print("Ola")

meu_decorador(saudar2)()











