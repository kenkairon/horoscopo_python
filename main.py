def obtener_signo_zodiacal(mes, dia):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo = 'Acuario'
        descripcion = 'Los acuario son personas amables, inteligentes y llenas de curiosidad por el mundo.'
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = 'Piscis'
        descripcion = 'Los piscis son personas sensibles y emocionales, con una gran capacidad de empatía.'
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo = 'Aries'
        descripcion = 'Los aries son personas valientes, enérgicas y llenas de pasión.'
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo = 'Tauro'
        descripcion = 'Los tauro son personas prácticas y realistas, con un fuerte sentido de la determinación.'
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = 'Géminis'
        descripcion = 'Los géminis son personas curiosas y sociables, con una mente abierta y adaptable.'
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = 'Cáncer'
        descripcion = 'Los cáncer son personas emocionales y sensibles, con una gran capacidad de empatía.'
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = 'Leo'
        descripcion = 'Los leo son personas valientes y apasionadas, con una gran autoconfianza.'
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = 'Virgo'
        descripcion = 'Los virgo son personas meticulosas y perfeccionistas, con una gran atención al detalle.'
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo = 'Libra'
        descripcion = 'Los libra son personas equilibradas y justas, con una gran habilidad para encontrar la armonía.'
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = 'Escorpión'
        descripcion = 'Los escorpio son personas intensas y apasionadas, con una gran profundidad emocional.'
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo = 'Sagitario'
        descripcion = 'Los sagitario son personas aventureras y optimistas, con una gran pasión por la exploración.'
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        signo = 'Capricornio'
        descripcion = 'Los capricornio son personas ambiciosas y determinadas, con una gran capacidad para el trabajo duro.'
    else:
        signo = 'Desconocido'
        descripcion = 'Fecha fuera del rango de signos zodiacales.'

    return signo, descripcion

# Ejemplo de uso:
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))
signo, descripcion = obtener_signo_zodiacal(mes, dia)
print(f"Signo: {signo}")
print(f"Descripción: {descripcion}")
