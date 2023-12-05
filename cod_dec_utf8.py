#Cadena de texto original.
texto_original: str = "¡Hola, esto es un ejemplo de codificación UTF-8!"

#Codificar la cadena en UTF-8.
texto_codificado: bytes = texto_original.encode("utf-8")

#Decodificar la cadena desde UTF-8.
texto_decodificado: str = texto_codificado.decode("utf-8")

#Imprimir la cadena original y la decodificada.
print("Cadena original:", texto_original)
print("Cadena decodificada:", texto_decodificado)

print()

def mostrar_secuencia_utf8(texto) -> None:
    #Codificar el texto en UTF-8 para obtener la secuencia de bytes.
    texto_codificado: bytes = texto.encode("utf-8")

    #Mostrar la secuencia de bytes en UTF-8.
    secuencia_utf8: str = "\\x" + "\\x".join(format(byte, "02x") for byte in texto_codificado)
    print("Cadena en secuencia UTF-8:", secuencia_utf8)
        
mostrar_secuencia_utf8(texto_original)