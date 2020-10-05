

Mes = {
    'ENERO' : 1,
    'FEBRERO' : 2,
    'MARZO' : 3,
    'ABRIL' : 4,
    'MAYO' : 5,
    'JUNIO' : 6,
    'JULIO' : 7,
    'AGOSTO' : 8,
    'SEPTIEMBRE' : 9,
    'OCTUBRE' : 10,
    'NOVIEMBRE' : 11,
    'DICIEMBRE' : 12
}

dia = int(input('Ingresa únicamente el número del día de tu nacimiento (entero): '))
mes = int(input('Ingresa el número del mes de tu cumpleaños:  '))

if (mes == Mes['MARZO'] and dia >= 21) or (mes == Mes['ABRIL'] and dia <= 20):
    print("aries")
elif (mes == Mes['ABRIL'] and dia >= 21) or (mes == Mes['MAYO'] and dia <= 20):
    print("tauro")
elif (mes == Mes['MAYO'] and dia >= 21) or (mes == Mes['JUNIO'] and dia <= 21):
    print("geminis")
elif (mes == Mes['JUNIO'] and dia >= 22) or (mes == Mes['JULIO'] and dia <= 22):
    print("cancer")
elif (mes == Mes['JULIO'] and dia >= 23) or (mes == Mes['AGOSTO'] and dia <= 22):
    print("leo")
elif (mes == Mes['AGOSTO'] and dia >= 23) or (mes == Mes['SEPTIEMBRE'] and dia <= 22):
    print("virgo")
elif (mes == Mes['SEPTIEMBRE'] and dia >= 23) or (mes == Mes['OCTUBRE'] and dia <= 22):
    print("libra")
elif (mes == Mes['OCTUBRE'] and dia >= 23) or (mes == Mes['NOVIEMBRE'] and dia <= 22):
    print("escorpio")
elif (mes == Mes['NOVIEMBRE'] and dia >= 23) or (mes == Mes['DICIEMBRE'] and dia <= 21):
    print("sagitario")
elif (mes == Mes['DICIEMBRE'] and dia >= 22) or (mes == Mes['ENERO'] and dia <= 20):
    print("capricornio")
elif (mes == Mes['ENERO'] and dia >= 21) or (mes == Mes['FEBRERO'] and dia <= 18):
    print("acuario")
elif (mes == Mes['FEBRERO'] and dia >= 19) or (mes == Mes['MARZO'] and dia <= 20):
    print("piscis")