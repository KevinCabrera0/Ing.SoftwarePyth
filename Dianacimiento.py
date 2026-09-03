from datetime import date


def obtener_fecha_actual():
    hoy = date.today()
    return hoy.year, hoy.month, hoy.day


def validar_fecha_nacimiento(a_actual, m_actual, d_actual):
    conterror = 0
    validar = False
    anacio, mnacio, dnacio = 0, 0, 0

    while not validar and conterror < 3:
        print(f"\n{a_actual}/{m_actual}/{d_actual}")
        print("Ingrese su Fecha de Nacimiento (Año, Mes y Día):")
        try:
            anacio = int(input("Año: "))
            mnacio = int(input("Mes: "))
            dnacio = int(input("Día: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            conterror += 1
            print(f"Intento incorrecto {conterror} de 3")
            continue

        validar = True

        if anacio <= 0 or anacio >= a_actual:
            print("Año de Nacimiento Ingresado Inválido")
            validar = False
        else:
            if mnacio == 2:
                if dnacio < 1 or dnacio > 28:
                    print(
                        "Día de Nacimiento Ingresado es Inválido al mes Ingresado"
                    )
                    validar = False
            elif mnacio in [4, 6, 9, 11]:
                if dnacio < 1 or dnacio > 30:
                    print(
                        "Día de Nacimiento Ingresado es Inválido al mes Ingresado"
                    )
                    validar = False
            elif mnacio in [1, 3, 5, 7, 8, 10, 12]:
                if dnacio < 1 or dnacio > 31:
                    print(
                        "Día de Nacimiento Ingresado es Inválido al mes Ingresado"
                    )
                    validar = False
            else:
                print("Mes de Nacimiento Ingresado Inválido")
                validar = False

        if not validar:
            conterror += 1
            print(f"Intento incorrecto {conterror} de 3")

    return validar, anacio, mnacio, dnacio


def calcular_edad(a_actual, m_actual, d_actual, anacio, mnacio, dnacio):
    edad = a_actual - anacio
    if mnacio > m_actual or (mnacio == m_actual and dnacio > d_actual):
        edad -= 1
    return edad


def obtener_signo_zodiacal(mnacio, dnacio):
    if (mnacio == 3 and 21 <= dnacio <= 31) or (
        mnacio == 4 and 1 <= dnacio <= 19
    ):
        return "Aries"
    elif (mnacio == 4 and 20 <= dnacio <= 30) or (
        mnacio == 5 and 1 <= dnacio <= 20
    ):
        return "Tauro"
    elif (mnacio == 5 and 21 <= dnacio <= 31) or (
        mnacio == 6 and 1 <= dnacio <= 20
    ):
        return "Géminis"
    elif (mnacio == 6 and 21 <= dnacio <= 30) or (
        mnacio == 7 and 1 <= dnacio <= 22
    ):
        return "Cáncer"
    elif (mnacio == 7 and 23 <= dnacio <= 31) or (
        mnacio == 8 and 1 <= dnacio <= 22
    ):
        return "Leo"
    elif (mnacio == 8 and 23 <= dnacio <= 31) or (
        mnacio == 9 and 1 <= dnacio <= 22
    ):
        return "Virgo"
    elif (mnacio == 9 and 23 <= dnacio <= 30) or (
        mnacio == 10 and 1 <= dnacio <= 22
    ):
        return "Libra"
    elif (mnacio == 10 and 23 <= dnacio <= 31) or (
        mnacio == 11 and 1 <= dnacio <= 21
    ):
        return "Escorpio"
    elif (mnacio == 11 and 22 <= dnacio <= 30) or (
        mnacio == 12 and 1 <= dnacio <= 21
    ):
        return "Sagitario"
    elif (mnacio == 12 and 22 <= dnacio <= 31) or (
        mnacio == 1 <= dnacio <= 19
    ):
        return "Capricornio"
    elif (mnacio == 1 and 20 <= dnacio <= 31) or (
        mnacio == 2 and 1 <= dnacio <= 18
    ):
        return "Acuario"
    elif (mnacio == 2 and 19 <= dnacio <= 29) or (
        mnacio == 3 and 1 <= dnacio <= 20
    ):
        return "Piscis"
    return "Fecha inválida para el zodiaco"


def mostrar_menu(edad, divi, mnacio, dnacio):
    opc = 0
    while opc != 5:
        print("\n--- Menú ---")
        print("1. Mostrar Edad y Estado")
        print("2. Carta Astral (Signo Zodiacal)")
        print("3. Estado de su Luna")
        print("4. Numeral Astral")
        print("5. Salir")
        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción no válida")
            continue

        if opc == 1:
            estado = (
                "Mayor de Edad" if edad >= 18 else "Menor de Edad"
            )
            print(f"Su edad es: {edad} Años Y usted es {estado}")
            input("Presione Enter para continuar...")
        elif opc == 2:
            signo = obtener_signo_zodiacal(mnacio, dnacio)
            print("Signo Zodiacal\n----------------")
            print(f"Su signo es: {signo}")
            input("Presione Enter para continuar...")
        elif opc == 3:
            print("Tu Luna Astral\n----------------")
            if divi == 2:
                print("Su luna de este año es LUNA LLENA")
            else:
                print("Su luna de este año es LUNA MENGUANTE")
            input("Presione Enter para continuar...")
        elif opc == 4:
            print("Secuencia Astral\n----------------")
            num_astral = round(edad / divi)
            a, b = 1, 1
            secuencia = []
            for _ in range(int(num_astral)):
                secuencia.append(str(a))
                c = a + b
                a = b
                b = c
            print(", ".join(secuencia))
            input("Presione Enter para continuar...")
        elif opc == 5:
            print("Gracias, Buena Suerte")
        else:
            print("Opción no Válida")


def main():
    a_actual, m_actual, d_actual = obtener_fecha_actual()
    validar, anacio, mnacio, dnacio = validar_fecha_nacimiento(
        a_actual, m_actual, d_actual
    )

    if validar:
        edad = calcular_edad(a_actual, m_actual, d_actual, anacio, mnacio, dnacio)
        divi = 2 if edad % 2 == 0 else 3
        mostrar_menu(edad, divi, mnacio, dnacio)
    else:
        print("\nNo Se pudo Mostrar su Edad Astral, Datos Incorrectos")


if __name__ == "__main__":
    main()