from parametros import (PROBABILIDAD_MAX, PROB_BASE_DESENCALLAR, COSTO_DESENCALLAR, \
    COBRO_USO_AVANZADO, COBRO_USO_PRINCIPIANTE, TENDENCIA_ENCALLAR_BUQUE, PONDERADOR_PRINCIPIANTE, \
    TENDENCIA_ENCALLAR_PASAJEROS, PONDERADOR_AVANZADO, TENDENCIA_ENCALLAR_CARGUERO)
from archivos import lista_barcos
import random
from currency_converter import CurrencyConverter 
c = CurrencyConverter()

class Canales:
    try:
        def __init__(
            self,
            nombre,
            dinero,
            largo,
            dificultad
            ):
            self.nombre = nombre
            self.dinero = float(dinero)
            self.gastado = 0
            self.recibido = 0
            self.dificultad = dificultad
            self.cobro = ""
            self.establecer_cobro()
            self.largo = int(largo)
            self.barcos = []
            self.hora = 0
            self.pasaron = 0
            self.encallados = 0
            self.eventos = 0

        def establecer_cobro(self):
            if self.dificultad == "principiante":
                self.cobro = int(COBRO_USO_PRINCIPIANTE)
            elif self.dificultad == "avanzado":
                self.cobro = int(COBRO_USO_AVANZADO)
            else:
                print("Existe un error en la base de datos de canales.csv")
                print("Las dificultades no estan indicadas como 'principiante' o 'avanzado'")
                print("LA INSTANCIA AFECTARA AL FLUJO DEL PROGRAMA")
            return

        def ingresar_barco_al_canal(self, barco):
            self.barcos.append(barco)
            return

        def avanzar_barcos(self):
            se_pueden_mover = []
            lista_barcos = []
            pagos_al_canal = 0
            cobros_al_canal = 0
            for e in self.barcos:
                lista_barcos.append(e)
            sorted(lista_barcos, key=lambda barco : barco.posicion)
            for barco in lista_barcos:
                if barco.encallado == False:
                    se_pueden_mover.append(barco)
                else:
                    for mover_barco in se_pueden_mover:
                        mover_barco.desplazarse()
                        if mover_barco.posicion >= self.largo:
                            pagos_al_canal += self.cobro
                            self.pasaron += 1
                            print(f"> El barco {mover_barco.nombre} ha salido del canal", \
                                f"{self.nombre}")
                            print(f"> El barco {mover_barco.nombre} ha pagado", \
                                f"{self.cobro} USD al canal {self.nombre}")
                            for x in range(len(self.barcos)):
                                if self.barcos[x].nombre == mover_barco.nombre:
                                    self.barcos.pop(x)
                        else:
                            cobro_mantencion = c.convert(mover_barco.mantencion, \
                                mover_barco.moneda, 'USD')
                            cobros_al_canal += cobro_mantencion
                            print(f"> El barco {mover_barco.nombre} ha avanzando hasta ", \
                                f"{mover_barco.posicion}")
                            print(f"> El canal {self.nombre} ha pagado {cobro_mantencion} USD ", \
                                f"al barco {mover_barco.nombre}")
                            self.dinero -= cobro_mantencion
                            if self.dinero <= 0:
                                print(f"> Por el cobro de {cobro_mantencion} USD, tu canal se ha", \
                                    " quedado sin fondos")
                                print(f">>> Finalizando la simulacion")
                                return "ab", "ab"
            return pagos_al_canal, cobros_al_canal

        def desencallar_barcos(self, barco):
            if self.dinero < COSTO_DESENCALLAR:
                print("> No tienes fondos suficientes para desencallar")
                return
            else:
                print(f"> Intentando desencallar a {barco.nombre}")
                if self.dificultad == "principiante":
                    proba_true = PROB_BASE_DESENCALLAR * PONDERADOR_PRINCIPIANTE
                else:
                    proba_true = PROB_BASE_DESENCALLAR * PONDERADOR_AVANZADO
                proba_false = PROBABILIDAD_MAX - proba_true
                resultado_desencallar = random.choices([True, False], weights=(proba_true, \
                    proba_false), k=1)
                if resultado_desencallar:
                    barco.encallado = False
                    print(f"> El {barco.nombre} fue desencallado")
                    self.dinero -= COSTO_DESENCALLAR
                    print(f"> Se realizo un cobro de {COSTO_DESENCALLAR} USD, tu dinero ", \
                        f"es {self.dinero} USD")
                else:
                    print(f"> El {barco.nombre} no pudo ser desencallado")
                return
            

    except ValueError as err:
        print("Existe un error en la base de datos de canales.csv")
        print("Los datos ingresados no corresponden a los valores que deberian tener")
        print("Revise que se ingresen strs, ints y floats cuando corresponda")
        print("INSTANCIA NO GENERADA")

def barcos_no_ingresados(canal, instancias):
    if canal.barcos == []:
        return instancias
    else:
        no_en_canal = []
        barcos_en_canal = []
        for barco in canal.barcos:
            barcos_en_canal.append(barco.nombre)
        for barco in instancias:
            if barco.nombre not in barcos_en_canal:
                no_en_canal.append(barco)
        print("> Selecciona como máximo un barco para ingresarlo al canal")
        for x in range(len(no_en_canal)):
            print(f">>> [{x+1}] {no_en_canal[x].nombre}")
        return no_en_canal

def simular_nueva_hora(canal, instancias):
    print("====[ Nueva Hora ]====")
    print(f"> Simulando la hora {canal.hora}")

    #verificar si se pueden ingresar barcos
    for barco in canal.barcos:
        if barco.encallado == True:
            print("> Existe un barco encallado, no pueden ingresar nuevos barcos")
            print("> Avanzando a los barcos que están libres")
            print("> Desplazando a los barcos que se encuentran libres")
            pagos, cobros = canal.avanzar_barcos()
            if pagos == "ab" or cobros == "ab":
                return "inicio"
            else:
                canal.recibido += pagos
                canal.gastado += cobros
            print(f"> El {canal.nombre} gasto {cobros} USD")
            print(f"> El {canal.nombre} recibio {pagos} USD")
            print("> Las posiciones de los barcos en el canal son las siguientes:")
            for e in canal.barcos:
                print(f"> {e.nombre} ubicado en {e.posicion} M desde que entro al canal")
            print("> Considere que los datos se muestran ordenados segun ingresaron al canal")
            canal.hora += 1
            return "acciones"

    #seleccionar barco para ingresar
    barcos_no_canal = barcos_no_ingresados(canal, instancias)
    print("> Selecciona un barco para ingresarlo al canal:")
    for x in range(len(barcos_no_canal)):
        print(f">>> [{x+1}] {barcos_no_canal[x].nombre}")
    print(">>> [0] Ninguno / Volver")
    selec_ingre = input("Ingresa el numero correspondiente: ")

    if selec_ingre == 0:
        return "acciones"
    
    elif errores_seleccion(selec_ingre, len(barcos_no_canal)) == False:
        #ingreso del barco
        barco_ingresado = barcos_no_canal[int(selec_ingre)-1]
        canal.ingresar_barco_al_canal(barco_ingresado)
        print(f"> {barco_ingresado.nombre} ha sido ingresado a {canal.nombre}")
        ingresado = True

        #probabilidad de encallar
        if barco_ingresado.tipo == "Pasajeros":
            tendencia = TENDENCIA_ENCALLAR_PASAJEROS
        elif barco_ingresado.tipo == "Carguero":
            tendencia = TENDENCIA_ENCALLAR_CARGUERO
        else:
            tendencia = TENDENCIA_ENCALLAR_BUQUE
        if canal.dificultad == "principiante":
            ponderador = PONDERADOR_PRINCIPIANTE
        else:
            ponderador = PONDERADOR_AVANZADO
        barco_ingresado.prob_encallar = [tendencia, ponderador]
        proba_true = barco_ingresado.prob_encallar
        proba_false = PROBABILIDAD_MAX - barco_ingresado.prob_encallar
        resultado_encallar = random.choices([True, False], weights=(proba_true, proba_false), k=1)

        #Evento especial
        if resultado_encallar == False:
            print(f"> el barco {barco_ingresado.nombre} NO encalló al ingresar al canal")
            #Ejecutar evento especial barco
        else:
            print(f"> el barco {barco_ingresado.nombre} encalló al ingresar al canal")
            barco_ingresado.encallado = True
            canal.encallados += 1
        
        #Desplazamiento
        print("> Desplazando a los barcos que se encuentran libres")
        pagos, cobros = canal.avanzar_barcos()
        if pagos == "ab" or cobros == "ab":
            return "inicio"
        else:
            canal.recibido += pagos
            canal.gastado += cobros
        print(f"> El {canal.nombre} gasto {cobros} USD")
        print(f"> El {canal.nombre} recibio {pagos} USD")
        print("> Las posiciones de los barcos en el canal son las siguientes:")
        for e in canal.barcos:
            print(f"> {e.nombre} ubicado en {e.posicion} M desde que entro al canal")
        print("> Considere que los datos se muestran ordenados segun ingresaron al canal")
        canal.hora += 1
        return "acciones"
    else:
        return "acciones"

def errores_seleccion(selec, rango):
    if selec.isdigit() == False: 
        print("> Opcion invalida, ingrese solamente los numeros disponibles")
        return True
    elif int(selec) < 0 or int(selec) > rango:
        print("> Opcion invalida, ingrese solamente los numeros disponibles")
        return True
    else:
        return False