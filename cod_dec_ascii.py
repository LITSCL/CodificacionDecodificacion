#Cadena de texto original.
texto_original: str = "Hola, esto es un ejemplo de codificacion ASCII."

#Codificar la cadena en ASCII.
texto_codificado: bytes = texto_original.encode("ascii")

#Decodificar la cadena desde ASCII.
texto_decodificado: str = texto_codificado.decode("ascii")

#Imprimir la cadena original y la decodificada.
print("Cadena original:", texto_original)
print("Cadena decodificada:", texto_decodificado)

print()

def mostrar_secuencia_ascii(texto) -> None:
    #Codificar el texto en ASCII para obtener la secuencia de bytes.
    texto_codificado: bytes = texto.encode("ascii")

    #Mostrar la secuencia de bytes en ASCII.
    secuencia_ascii: str = " ".join(str(byte) for byte in texto_codificado)
    print("Cadena en secuencia ASCII:", secuencia_ascii)
        
mostrar_secuencia_ascii(texto_original)