#Version 2.0
#José Miguel Gabela Salazar, 2021

import CS
import Roundabout
import math

print('')
print('Version 2.0')
print('Procesadora de datos expperimentales')

jmgs = True

while jmgs == True:
    
    print('')
    
    # This string determines the real value of the experiment
    vr = input('Hay Valor Real, Si o No? ')
    if vr == 'si':
        vr = True
    elif vr == 'SI':
        vr = True
    elif vr == 'Si':
        vr = True
    elif vr == '1':
        vr = True
    elif vr == 'no':
        vr = False
    elif vr == 'NO':
        vr = False
    elif vr == 'No':
        vr = False
    elif vr == '0':
        vr = False
    else:
        vr = input('Hay Valor Real, Si o No? ')
        if vr == 'si':
            vr = True
        elif vr == 'SI':
            vr = True
        elif vr == 'Si':
            vr = True
        elif vr == '1':
            vr = True
        elif vr == 'no':
            vr = False
        elif vr == 'NO':
            vr = False
        elif vr == 'No':
            vr = False
        elif vr == '0':
            vr = False
        else:
            vr = input('Hay Valor Real, Si o No? ')
            if vr == 'si':
                vr = True
            elif vr == 'SI':
                vr = True
            elif vr == 'Si':
                vr = True
            elif vr == '1':
                vr = True
            elif vr == 'no':
                vr = False
            elif vr == 'NO':
                vr = False
            elif vr == 'No':
                vr = False
            elif vr == '0':
                vr = False

    #this block process all data if there is vr
    if vr == True:
        vr = input('Ingresa el valor real: ')
        media = vr
        media = float(media)

        #This block distributes the recolected data
        reee = 'p'

        num = input('Numero de datos a procesar: ')
        if type(num) == type(reee):
            try:
                num = int(num)
            except:
                while type(num) == type(reee):
                    print('Necesitas al menos 3 datos para obtener respuestas validas y tienen que ser numeros')
                    num = input('Numero de datos a procesar: ')
                    if num == '1':
                        num = int(num)
                    if num == '2':
                        num = int(num)
                    if num == '3':
                        num = int(num)
                    if num == '4':
                        num = int(num)
                    if num == '5':
                        num = int(num)
                    if num == '6':
                        num = int(num)
                    if num == '7':
                        num = int(num)
                    if num == '8':
                        num = int(num)
                    if num == '9':
                        num = int(num)

        if num < 3:
            while num < 3:
                print('Necesitas al menos 3 datos para obtener respuestas validas')
                num = input('Numero de datos a procesar: ')
                num = int(num)

        if num == 3:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')

            CS.cs(d1, d2, d3)
            if CS.cs.cstt < 0:
                CS.cs.cstt = abs(CS.cs.cstt)
            media = round(media, CS.cs.cstt)

        if num == 4:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')

            CS.cs1(d1, d2, d3, d4)
            if CS.cs1.cs1tt < 0:
                CS.cs1.cs1tt = abs(CS.cs1.cs1tt)
            media = round(media, CS.cs1.cs1tt)

        if num == 5:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')
            d5 = input('Dato 5: ')

            CS.cs2(d1, d2, d3, d4, d5)
            if CS.cs2.cs2tt < 0:
                CS.cs2.cs2tt = abs(CS.cs2.cs2tt)
            media = round(media, CS.cs2.cs2tt)

        if num == 6:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')
            d5 = input('Dato 5: ')
            d6 = input('Dato 6: ')

            CS.cs3(d1, d2, d3, d4, d5, d6)
            if CS.cs2.cs2tt < 0:
                CS.cs2.cs2tt = abs(CS.cs2.cs2tt)
            media = round(media, CS.cs3.cs3tt)

        #These blocks process the recolected data
        if num == 3:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)

            def fn(xd, yd, zd):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                fn.rae = xd + yd + zd
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3)

        if num == 4:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)

            def fn(xd, yd, zd, td):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                fn.rae = xd + yd + zd + td
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4)

        if num == 5:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)
            d5 = float(d5)

            def fn(xd, yd, zd, td, opd):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                opd = pow((opd - media), 2)
                fn.rae = xd + yd + zd + td + opd
                fn.rae = fn.rae / (int(num) - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4, d5)

        if num == 6:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)
            d5 = float(d5)
            d6 = float(d6)

            def fn(xd, yd, zd, td, opd, iod):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                opd = pow((opd - media), 2)
                iod = pow((iod - media), 2)
                fn.rae = xd + yd + zd + td + opd + iod
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4, d5, d6)

        # this block rounds the rae
        media = str(media)
        Roundabout.count_sigfigs(media)
        fn.rae = round(float(fn.rae), Roundabout.count_sigfigs.rer)

        media = float(media)

        ir = fn.rae / media
        ir = round(ir, Roundabout.count_sigfigs.rer)
        ipp = ir * 100
        int(ipp)

        print('')
        print('Datos:')
        print('')
        print('Error Aleatorio:', fn.rae)
        print('Incertidumbre Absoluta:', media, '±', fn.rae)
        print('Incertidumbre Relativa:', ir)
        print('Incertidumbre Porcentual:', ipp, '%')
        print('')

    # This block process all data if there is not a vr
    if vr == False:

        # This group of blocks distributes the data recolected
        reee = 'p'

        num = input('Numero de datos a procesar: ')
        if type(num) == type(reee):
            try:
                num = int(num)
            except:
                while type(num) == type(reee):
                    print('Necesitas al menos 3 datos para obtener respuestas validas y tienen que ser numeros')
                    num = input('Numero de datos a procesar: ')
                    if num == '1':
                        num = int(num)
                    if num == '2':
                        num = int(num)
                    if num == '3':
                        num = int(num)
                    if num == '4':
                        num = int(num)
                    if num == '5':
                        num = int(num)
                    if num == '6':
                        num = int(num)
                    if num == '7':
                        num = int(num)
                    if num == '8':
                        num = int(num)
                    if num == '9':
                        num = int(num)

        if num < 3:
            while num < 3:
                print('Necesitas al menos 3 datos para obtener respuestas validas')
                num = input('Numero de datos a procesar: ')
                num = int(num)

        if num == 3:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')

            media = (float(d1) + float(d2) + float(d3)) / int(num)

            CS.cs(d1, d2, d3)
            if CS.cs.cstt < 0:
                CS.cs.cstt = abs(CS.cs.cstt)
            media = round(media, CS.cs.cstt)

        if num == 4:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')

            media = (float(d1) + float(d2) + float(d3) + float(d4)) / int(num)

            CS.cs1(d1, d2, d3, d4)
            if CS.cs1.cs1tt < 0:
                CS.cs1.cs1tt = abs(CS.cs1.cs1tt)
            media = round(media, CS.cs1.cs1tt)

        if num == 5:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')
            d5 = input('Dato 5: ')

            media = (float(d1) + float(d2) + float(d3) + float(d4) + float(d5)) / int(num)

            CS.cs2(d1, d2, d3, d4, d5)
            if CS.cs2.cs2tt < 0:
                CS.cs2.cs2tt = abs(CS.cs2.cs2tt)
            media = round(media, CS.cs2.cs2tt)

        if num == 6:
            d1 = input('Dato 1: ')
            d2 = input('Dato 2: ')
            d3 = input('Dato 3: ')
            d4 = input('Dato 4: ')
            d5 = input('Dato 5: ')
            d6 = input('Dato 6: ')

            media = (float(d1) + float(d2) + float(d3) + float(d4) + float(d5) + float(d6)) / int(num)

            CS.cs3(d1, d2, d3, d4, d5, d6)
            if CS.cs3.cs3tt < 0:
                CS.cs3.cs3tt = abs(CS.cs3.cs3tt)
            media = round(media, CS.cs3.cs3tt)

        #These blocks process the recolected data
        if num == 3:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)

            def fn(xd, yd, zd):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                fn.rae = xd + yd + zd
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3)

        if num == 4:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)

            def fn(xd, yd, zd, td):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                fn.rae = xd + yd + zd + td
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4)

        if num == 5:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)
            d5 = float(d5)

            def fn(xd, yd, zd, td, opd):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                opd = pow((opd - media), 2)
                fn.rae = xd + yd + zd + td + opd
                fn.rae = fn.rae / (int(num) - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4, d5)

        if num == 6:
            d1 = float(d1)
            d2 = float(d2)
            d3 = float(d3)
            d4 = float(d4)
            d5 = float(d5)
            d6 = float(d6)

            def fn(xd, yd, zd, td, opd, iod):
                xd = pow((xd - media), 2)
                yd = pow((yd - media), 2)
                zd = pow((zd - media), 2)
                td = pow((td - media), 2)
                opd = pow((opd - media), 2)
                iod = pow((iod - media), 2)
                fn.rae = xd + yd + zd + td + opd + iod
                fn.rae = fn.rae / (num - 1)
                fn.rae = math.sqrt(fn.rae)
            fn(d1, d2, d3, d4, d5, d6)

        # this block rounds the rae
        media = str(media)                              #media is not defined
        Roundabout.count_sigfigs(media)
        fn.rae = round(float(fn.rae), Roundabout.count_sigfigs.rer)

        media = float(media)

        ir = fn.rae / media
        ir = round(ir, Roundabout.count_sigfigs.rer)
        ipp = ir * 100
        int(ipp)

        print('')
        print('Datos:')
        print('')
        print('Valor Promedio:', media)
        print('Error Aleatorio:', fn.rae)
        print('Incertidumbre Absoluta:', media, '±', fn.rae)
        print('Incertidumbre Relativa:', ir)
        print('Incertidumbre Porcentual:', ipp, '%')
        print('')
        print('')

        jmgs = input('Quieres hacer de nuevo?')
        if jmgs == 'si':
            jmgs = True
        elif jmgs == 'SI':
            jmgs = True
        elif jmgs == 'Si':
            jmgs = True
        elif jmgs == '1':
            jmgs = True
        elif jmgs == 'no':
            jmgs = False
        elif jmgs == 'NO':
            jmgs = False
        elif jmgs == 'No':
            jmgs = False
        elif jmgs == '0':
            jmgs = False
        else:
            jmgs = False

rtrr = input('Listo')
trtt = input('Presiona ENTER para cerrar el programa')
#-------------------------------------------(José Miguel Gabela Salazar, 2021)--------------------------------------------------------
#-----------------------------------------------------(Version 2.0)------------------------------------------------------------------
