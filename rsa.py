import random
max_PrimLength = 1000

'''
modulo inverso entre e and phi
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''
maximo con un divisor entre dos numeros
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
si es primo
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    print("n ",n)
    phi = (p-1) * (q-1) 
    print("phi ",phi)
    
    '''choose e coprime to n and 1 > e > phi'''    
    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e=",e," ","phi=",phi)
    d = egcd(e, phi)[1]
    d = d % phi
    if(d < 0):
        d += phi
        
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext


def leermensaje():
    mensajetxt = open("mensajeentrada.txt","r")
    mensaje = mensajetxt.read()
    mensajetxt.close()
    return mensaje

def crearmensaje(mensaje_enviar):
    mensajetxt = open("mensajerecibido.txt","w")
    mensajetxt.write(mensaje_enviar)
    mensajetxt.close()

if __name__ == '__main__':
    public_key,private_key = generate_keyPairs() 
    mensajeentrada = leermensaje()

    print(len(mensajeentrada))
    print("Llave privada",private_key)
    print("Llave publica",public_key)


    key_public = int(input("Ingrese la llave publica: "))
    
    if key_public == public_key[0]:
        print("Encriptando el mensaje del archivo mensajeentrada.")
        ctext = encrypt(mensajeentrada,public_key)
        print(ctext)


        print("Para desencriptar el mensaje, se debe de colocar la llave privada")
        key_private = int(input("Ingrese la llave privada: "))

        if key_private == private_key[0]:
            print("Se ha creado un archivo con el mensaje desencripadto")
            plaintext = decrypt(ctext, private_key)
            crearmensaje(plaintext)
        else:
            print("Llave erronea se cierra el programa")


    else:
        print("Llave erronea se cancela la operacion")


    