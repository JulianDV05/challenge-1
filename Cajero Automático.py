Saldo = 1000000
while True:
    print(" MENÚ: ")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opción= int(input("Digíte una opción del menú: "))
    
    print()
    
    if opción==1:
        extra = float(input("Cuánto dinero desea ingresar: "))
        Saldo = Saldo+extra
        print("Dinero en la cuenta: $",Saldo)
    elif opción==2:
        Retirar = float(input("Cuánto dinero desea retirar: "))
        if Retirar>Saldo:
            print("No tiene fondos sufiscientes")
        elif Retirar<10000:
            print("Error con la cantidad ingresada")
        else:
            if Retirar%10000==0:
                Saldo -= Retirar
                billetes=[50000,20000,10000]
                resto=Retirar
                if resto<=50000:
                    for i in range (len(billetes)):
                        b=resto//billetes[i]
                        if b>0:
                            if resto//billetes[i]==2:
                                print("\nRetirando 2, billetes de 10000 pesos")
                                resto=0.0
                            else:
                                print(f"\nRetirando {b}, billetes de {billetes[i]} pesos")
                                resto=resto%billetes[i]
                else:
                    print("\nRetirando 2.0, billetes de 20000 pesos")
                    print("Retirando 1.0, billetes de 10000 pesos")
                    resto=resto-50000
                    for i in range (len(billetes)):
                        b=resto//billetes[i]
                        if b>0:
                            print(f"Retirando {b}, billetes de {billetes[i]} pesos")
                            resto=resto%billetes[i]

                print("Dinero en la cuenta: $",Saldo)
            else:
                print("Error con la cantidad ingresada")
    elif opción==3:
        print("Dinero en la cuenta: $",Saldo)
    elif opción==4:
        print("Hasta luego")
        break
    else:
        print("Error, digíte un número válido: ")
    
    print()