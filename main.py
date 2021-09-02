#Version 2.22
#José Miguel Gabela Salazar, 2021

import CS
import Roundabout
import math
import re
import rezero

print('')
print('Version 2.22')
print('Procesadora de datos expperimentales')
print('')

ah = input('Presiona ENTER para empezar ')

jmgs = True
reee = 'p'

while jmgs == True:
    
    print('')
    
    # This string determines the real value of the experiment
    vr = 87
    while vr == 87:
        vr = input('Hay Valor Real, Si o No? ')
        re.rer(vr)
        vr = re.rer.vrr

    #this block process all data if there is vr
    if vr == True:

        media = input('Ingresa el valor real: ')
        while type(media) == type(reee):
            try:
                media = float(media)
            except:
                media = input('Ingresa el valor real: ')

        #This group of blocks distributes the data recolected
        num = input('Numero de datos a procesar: ')
        while type(num) == type(reee):
            try:
                num = int(num)
                while num < 3:
                    print('Necesitas al menos 3 datos para obtener respuestas validas')
                    num = input('Numero de datos a procesar: ')
                    num = str(num)
            except:
                print('Tiene que ser un numero')
                num = input('Numero de datos a procesar: ')                

        print('')
        print('Datos Brutos:')
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

        media = float(media)
        ir = fn.rae / media
        tre = float(ir)
        ter = fn.rae

        fn.rae = round(float(fn.rae), Roundabout.count_sigfigs.rer)
        ir = round(ir, Roundabout.count_sigfigs.rar)
        ipp = ir * 100
        int(ipp)

        print('')
        print('Datos Procesados:')
        print('Valor Promedio:', media)
        print('Error Aleatorio:', fn.rae)
        print('Incertidumbre Absoluta:', media, '±', fn.rae)
        print('Incertidumbre Relativa:', ir)
        print('Incertidumbre Porcentual:', ipp, '%')
        print('')
        print('Datos Procesados sin redondear:')
        print('Error Aleatorio:', ter)
        print('Incertidumbre Relativa:', tre)
        print('')

        #This block is to redo the process if the user wants to
        jmgs = input('Quieres hacer de nuevo? ')
        rezero.sk(jmgs)
        jmgs = rezero.sk.jmgs

    # This block process all data if there is not a vr
    if vr == False:

        #This group of blocks distributes the data recolected
        num = input('Numero de datos a procesar: ')
        while type(num) == type(reee):
            try:
                num = int(num)
                while num < 3:
                    print('Necesitas al menos 3 datos para obtener respuestas validas')
                    num = input('Numero de datos a procesar: ')
                    num = str(num)
            except:
                print('Tiene que ser un numero')
                num = input('Numero de datos a procesar: ')

        if num < 3:
            while num < 3:
                print('Necesitas al menos 3 datos para obtener respuestas validas')
                num = input('Numero de datos a procesar: ')
                num = int(num)

        print('')
        print('Datos Brutos:')
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
        media = str(media)
        Roundabout.count_sigfigs(media)

        media = float(media)
        ir = fn.rae / media
        tre = float(ir)
        ter = fn.rae

        fn.rae = round(float(fn.rae), Roundabout.count_sigfigs.rer)
        ir = round(ir, Roundabout.count_sigfigs.rar)
        ipp = ir * 100
        int(ipp)
        ipp = round(ipp, Roundabout.count_sigfigs.rar)

        print('')
        print('Datos Procesados:')
        print('Valor Promedio:', media)
        print('Error Aleatorio:', fn.rae)
        print('Incertidumbre Absoluta:', media, '±', fn.rae)
        print('Incertidumbre Relativa:', ir)
        print('Incertidumbre Porcentual:', ipp, '%')
        print('')
        print('Datos Procesados sin redondear:')
        print('Error Aleatorio:', ter)
        print('Incertidumbre Relativa:', tre)
        print('')

        jmgs = input('Quieres hacer de nuevo? ')
        rezero.sk(jmgs)
        jmgs = rezero.sk.jmgs

rtrr = input('Listo')
trtt = input('Presiona ENTER para cerrar el programa')

#-------------------------------------------(José Miguel Gabela Salazar, 2021)--------------------------------------------------------
#-----------------------------------------------------(Version 2.22)------------------------------------------------------------------
