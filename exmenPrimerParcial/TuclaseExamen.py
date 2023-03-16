
def arithmetic_arranger(listaNumeros, showAns=False):
   
        # Verificamos que no haya más de 5 operaciones
        if len(listaNumeros) > 5:
            return "Error: Too many problems."
        else:

            primera_linea = ""
            segunda_linea = ""
            linea_punteada = ""
            linea_respuesta = ""
            for lista in listaNumeros:

                a = lista.split()  # El split sin argumentos separa por espacios, ya sean 1,2,3 o más

                primero = a[0]  # El primer elemento es el primero
                segundo = a[2]  # El terceer elemento es el segundo
                operador = a[1]  # El segundo elemento es el operador

                # Verificamos que los números si sean numeros
                if not primero.isnumeric() or not segundo.isnumeric():
                    return "Error: Numbers must only contain digits."

                # Verificamos la longitud de los numeros
                if len(primero) > 4 or len(segundo) > 4:
                    return "Error: Numbers cannot be more than four digits."

                # Validamos los operadores y realizamos las operaciones
                if operador == '+':
                    respuesta = int(primero) + int(segundo)
                elif operador == '-':
                    respuesta = int(primero) - int(segundo)
                else:
                    return "Error: Operator must be '+' or '-'."

                # Poner espacios
                # La funcion max nos da el mayor de los dos numeros
                ancho = (max(len(segundo), len(primero)))
                ancho = ancho+2  # Añadimos 2 espacios, 1 para el operador y el otro para el espacio entre el operador y el numero más largo

                # rjust nos alinea a la derecha y rellena los espacios el valor que le pasemos "ancho"
                primera_linea += str(primero).rjust(ancho)
                # Se pone -1 ya que solo debe haber un espacio entre el operador y el numero
                segunda_linea += operador + str(segundo).rjust(ancho - 1)
                # Se multiplica el caracter "-" por el ancho para que se repita el caracter el numero de veces que sea el ancho
                linea_punteada += "-" * ancho
                linea_respuesta += str(respuesta).rjust(ancho)

                # Agregamos 4 espacios entre listaas
                if len(listaNumeros) >= 1:
                    primera_linea += "    "
                    segunda_linea += "    "
                    linea_punteada += "    "
                    linea_respuesta += "    "

                # Si nos mandan un true mostramos las respuestas y si no, solo mostramos los listaas sin las respuestas
                if showAns == True:
                    arranged_listaNumeros = (primera_linea.rstrip() + "\n" +
                                            segunda_linea.rstrip() + '\n' +
                                            linea_punteada.rstrip() + '\n' +
                                            linea_respuesta.rstrip())
                else:
                    arranged_listaNumeros = (primera_linea.rstrip() + "\n" +
                                            segunda_linea.rstrip() + '\n' +
                                            linea_punteada.rstrip())

        return arranged_listaNumeros