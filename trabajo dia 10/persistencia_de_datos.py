import re
from pathlib import Path

RUTA_BASE = Path(r"C:\Users\Usuario\Documents\c4 estudio\ejercicios.py\archivos")
ARCHIVO_ENTRADA = RUTA_BASE / "mbox.txt"
ARCHIVO_SALIDA = RUTA_BASE / "mensajes_enviados.txt"


def leer_correos(archivo: Path):
    correos = []

    with archivo.open("r", encoding="utf-8") as fh:
        for linea in fh:
            if linea.startswith("From:"):
                coincidencia = re.search(r"From:\s*(\S+@\S+)", linea)
                if coincidencia:
                    correos.append(coincidencia.group(1).strip())

    return correos


def enviar_mensajes(correos):
    mensajes = []

    for correo in reversed(correos):
        mensaje = f"{correo} enviado [ok]"
        mensajes.append(mensaje)
        print(mensaje)

    with ARCHIVO_SALIDA.open("w", encoding="utf-8") as archivo:
        for mensaje in mensajes:
            archivo.write(mensaje + "\n")


if __name__ == "__main__":
    correos = leer_correos(ARCHIVO_ENTRADA)
    enviar_mensajes(correos)