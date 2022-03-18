consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32}
    },
}

plantas = {
    'Quito': ('Coca Codo Sinclair', 'Sopladora'),
    'Guayaquil': ('Coca Codo Sinclair', 'Sopladora'),
    'Loja': ('Sopladora'),
    'Tena': ('Sopladora'),
    'Manta': ('Sopladora')
}

informacion = {
    'Costa': ('Guayaquil', 'Manta'),
    'Sierra': ('Quito', 'Ambato', 'Loja'),
    'Oriente': ('Tena', 'Nueva Loja')
}

def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

def plantas_total():
    for lugar in plantas:
        if ciudad in lugar:
            for lugar in consumo_energia['Coca Codo Sinclair']:
                if lugar == ciudad:
                    total_coca = (sum(consumo_energia['Coca Codo Sinclair']['{}'.format(ciudad)]['consumos']))
                    print('Coca Codo Sinclair presentó: ',total_coca, 'MWh de energía')
                    continue
            for lugar in consumo_energia['Sopladora']:
                if lugar == ciudad:
                    total_sopladora = (sum(consumo_energia['Sopladora']['{}'.format(ciudad)]['consumos']))        
                    print('Sopladora presentó: ',total_sopladora, 'MWh de energía')
        if ciudad not in plantas:
            print ('La ciudad que ingresó no es válida')
            break


        

def recaudacion ():
    ciudades_region = informacion[region]
    total_consumo = 0
    
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region == ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos'])*consumo_energia[planta][ciudad]['tarifa']
    print(region, ':','$', total_consumo)


op = -1
while op != 0:
    print('[1] Total de MWh por planta/ciudad')
    print('[2] Total de MWh de cada plantas por cuidad')
    print('[3] Consultar información de dinero recaudado en una región')
    print('[0] Terminar programa')
    op = int(input('Ingrese opción: '))
    

    while op == 1:
       
        planta = input('Ingrese el nombre de la planta (Coca Codo Sinclair, Sopladora): ')
        ciudad = input('Ingrese el nombre de la ciudad:')

        total = total_consumo_por_planta_ciudad(planta, ciudad)

        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)
        print('\n--Menú Principal--\n')
        break
    while op == 2:
        ciudad =  input('Ingrese el nombre de la ciudad: ')
        plantas_total()
        print('\n--Menú Principal--\n')
        break
    while op == 3:
        region = input('Introduzca el nombre de la región a evalúar: ')
        if region not in informacion.keys():
            print ('La región no se encuentra registrada')
            print('\n--Menú Principal--\n')
            break
        if region in informacion.keys():
            recaudacion()
            print('\n--Menú Principal--\n')
            break
    while op == 0:
        print('\n** Programa finalizado **\n')
        exit()
