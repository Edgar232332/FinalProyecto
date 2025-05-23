import pandas as pd
import matplotlib.pyplot  as plt
import streamlit as st
import numpy as np

Cambio = pd.read_csv("Cambio.csv")
Colcap = pd.read_csv("Colcap.csv")
Desempleo = pd.read_csv("Desempleo.csv")
Inflación = pd.read_csv("Inflación.csv")
PIB = pd.read_csv("PIB.csv")


st.title("Análisis Económico y discursivo del gobierno actual")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Introducción", "PIB", "Índice Colcap","Desempleo","TRM", "Inflación"])
with tab1:
    st.header ("Introducción")
    st.text("La siguiente página web tiene como fin realizar un análisis del desempeño economico del gobierno de Gustavo Petro, con los datos conocidos hasta mayo de 2025.")
    st.text("Este análisis se va a realizar teniendo en cuenta los discursos del gobierno Petro, examinando la concordancia de los datos y el relato, con enfásis en las tendencias claves en cada uno de los rubros econónomicos. ")
    st.text("También buscaremos dar una comparación con los indicadores presentados en otros gobiernos cercanos, como lo son las administraciones de Juan Manuel Santos e Ivan Duque.")
    st.text("Las siguientes observaciones no buscan, por otro lado, dar una explicación causal a la razón de que estos indicadores se comporten de cierta manera, por lo que no tendremos en cuenta choques que puedan explicar las fluctuaciones de los indicadores. ")
    st.text("El siguiente trabajo fue realizado por: Maria José Morales, Felipe Castro y Edgar Diaz")
    st.subheader ("Fuentes:")
    st.text("Índices del mercado bursátil colombiano | Banco de la República. (s. f.). https://www.banrep.gov.co/es/glosario/indices-mercado-bursatil-colombiano")
    st.text("Producto interno bruto (PIB) | Banco de la República. (s. f.). https://www.banrep.gov.co/es/glosario/producto-interno-bruto-pib")
    st.text("Tasa de cambio o tasa de cambio representativa del mercado (TRM) | Banco de la República. (s. f.). https://www.banrep.gov.co/es/glosario/tasa-cambio-trm")
    st.text("Tasa de desempleo | Banco de la República. (s. f.). https://www.banrep.gov.co/es/glosario/tasa-desempleo")
    st.text("Cifras, datos e indicadores : crédito público, macroeconomía y deuda - Minhacienda. (s. f.). Minhacienda. https://www.minhacienda.gov.co/cifras-e-indicadores")
    st.text("Palabras presidente Gustavo Petro en la Cumbre de Gobernadores ‘El campo, motor de crecimiento económico desde las regiones’. (s. f.). Presidencia de la República. https://www.presidencia.gov.co/prensa/Paginas/Palabras-presidente-Gustavo-Petro-en-la-Cumbre-de-Gobernadores-El-campo-motor-de-crecimiento-economico-desde-250219.aspx")
    st.text("Alocución de Año Nuevo del presidente Gustavo Petro Urrego para todas y todos los colombianos. (s. f.). Presidencia de la República. https://www.presidencia.gov.co/prensa/Paginas/Alocucion-de-Anio-Nuevo-del-presidente-Gustavo-Petro-Urrego-para-todas-y-to-241231.aspx")
    st.text("Tasa de cambio: Sobre de la revalorización del peso (diciembre,2023) - crédito @petrogustavo. Via X")
with tab2:
    st.header ("PIB trimestral, crecimiento anual")
    PIBfig  = plt.figure(figsize=(10, 5))
    plt.plot(PIB["Periodo(TX de AAAA)"][0:3], PIB['Crecimiento PIB real, Trimestral, base: 2015'][0:3], color='black')
    plt.plot(PIB["Periodo(TX de AAAA)"][2:35], PIB['Crecimiento PIB real, Trimestral, base: 2015'][2:35], color='red', label='Juan Manuel Santos')
    plt.plot(PIB["Periodo(TX de AAAA)"][34:51], PIB['Crecimiento PIB real, Trimestral, base: 2015'][34:51], color='blue', label='Ivan Duque')
    plt.plot(PIB["Periodo(TX de AAAA)"][50:], PIB['Crecimiento PIB real, Trimestral, base: 2015'][50:], color='purple', label='Gustavo Petro')
    fechas = PIB["Periodo(TX de AAAA)"]
    plt.xticks(ticks=fechas[::8], rotation=45)

    plt.title('Crecimiento del PIB trimestral')
    plt.xlabel('Año')
    plt.ylabel('% de Crecimiento')
    plt.legend()
    plt.grid(True)
    PIBfig.savefig("PIBfig.png")
    st.pyplot(PIBfig)
    

    PIBfig2= plt.figure(figsize=(10, 5))
    plt.plot(PIB["Periodo(TX de AAAA)"][50:], PIB['Crecimiento PIB real, Trimestral, base: 2015'][50:], color='purple', label='Gustavo Petro')
    fechas2 = PIB["Periodo(TX de AAAA)"][50:]
    plt.xticks(ticks=fechas2[::], rotation=45)

    plt.title('Crecimiento del PIB trimestral')
    plt.xlabel('Periodo')
    plt.ylabel('% de Crecimiento')
    plt.legend()
    PIBfig2.savefig("PIBfig2.png")
    plt.grid(True)
    st.pyplot(PIBfig2)

    st.subheader ("\'Crecimiento económico\'")
    st.text("\'En octubre, segundo punto, el DANE reportó un crecimiento de 2,9% real de la economía. Veníamos de cero. Estamos creciendo, efectivamente, en Colombia -y de una manera que me interesa muchísimo- porque lo propusimos en la campaña electoral.\' -Gustavo Petro")
    st.text("Comparativamente, el periodo Petro ha sido mucho menos convulso para el PIB que el periodo de Duque, esto debido a los efectos de la pandemia, pero se ha podido ver afectado de igual manera por la recuperación de esta,con una disminución del crecimiento, acercandose más a los niveles estructurales.")
    st.text("En el periodo Santos se mantuvo un crecimiento estable entre el 3% y 5%, si bien las cifras de Petro han sido menores, se presenta un ligero repunte hacia el 2024, con tasas de crecimiento cercanas al 2-3%.")
    st.text("En el gobierno Petro colombia comenzó teniendo una desaceleración del crecimiento de la economía, posiblemente debido al final de la reactivación economica, y, desde un pico negativo de decrecimiento, ha mantenido cifras estables, similares a las de periodos pre-pandemia. Pero la tendencia si es de crecimiento, por lo que el enfoque del presidente es acertado.")
with tab3:
    st.header ("Índice Colcap")
    Colfig= plt.figure(figsize=(10, 5))

    plt.plot(Colcap["Periodo(MMM DD, AAAA)"][0:147], Colcap["Índice COLCAP"][0:147], color='black')
    plt.plot(Colcap["Periodo(MMM DD, AAAA)"][146:2098], Colcap["Índice COLCAP"][146:2098], color='red', label='Juan Manuel Santos')
    plt.plot(Colcap["Periodo(MMM DD, AAAA)"][2097:3059], Colcap["Índice COLCAP"][2097:3059], color='blue', label='Ivan Duque')
    plt.plot(Colcap["Periodo(MMM DD, AAAA)"][3058:], Colcap["Índice COLCAP"][3058:], color='purple', label='Gustavo Petro')
    fechas3 = (Colcap["Periodo(MMM DD, AAAA)"])
    plt.xticks(ticks=fechas3[::248], rotation=45)

    plt.title('Variación indice Colcap')
    plt.xlabel('Año')
    plt.ylabel('Valor del índice en puntos')
    plt.legend()
    plt.grid(True)
    Colfig.savefig("Colfig.png")
    st.pyplot(Colfig)

    Colfig2= plt.figure(figsize=(10, 5))
    plt.plot(Colcap["Periodo(MMM DD, AAAA)"][3058:], Colcap["Índice COLCAP"][3058:], color='purple', label='Gustavo Petro')
    fechas4 = (Colcap["Periodo(MMM DD, AAAA)"])[3058:]
    plt.xticks(ticks=fechas4[::67], rotation=45)

    plt.title('Variación indice Colcap')
    plt.xlabel('Año')
    plt.ylabel('Valor del índice en puntos')
    plt.legend()
    plt.grid(True)
    Colfig2.savefig("Colfig2.png")
    st.pyplot(Colfig2)

    st.text("El presidente Petro no ha abordado el índice Colcap especificamente en ninguno de sus discursos. Pero en la grafica podemos apreciar como estos no recibieron con mucho entusiasmo su elección en el cargo, por lo que se inicio con un índice incluso por debajo de los 1100 puntos.")
    st.text("Pero repunta con una tendencia a la subida, superando los 1600 puntos hacia 2025, con niveles similares a los pre-pandemia, y un pico mayor al del periodo Duque. Se puede concluir que los mercados, si bien reticentes inicialmente al actual presidente, fueron adaptandose a este y han presentado una importante recuperación.")
with tab4: 
    st.header ("Tasa de desempleo")
    Desfig= plt.figure(figsize=(10, 5))

    plt.plot(Desempleo["Periodo(MMM, AAAA)"][:8], Desempleo["Tasa de desempleo - total nacional"][:8], color='black')
    plt.plot(Desempleo["Periodo(MMM, AAAA)"][7:104], Desempleo["Tasa de desempleo - total nacional"][7:104], color='red', label='Juan Manuel Santos')
    plt.plot(Desempleo["Periodo(MMM, AAAA)"][103:152], Desempleo["Tasa de desempleo - total nacional"][103:152], color='blue', label='Ivan Duque')
    plt.plot(Desempleo["Periodo(MMM, AAAA)"][151:], Desempleo["Tasa de desempleo - total nacional"][151:], color='purple', label='Gustavo Petro')
    fechas5 = (Desempleo["Periodo(MMM, AAAA)"])
    plt.xticks(ticks=fechas5[::13], rotation=45)

    plt.title('Desempleo')
    plt.xlabel('Año')
    plt.ylabel('Tasa mensual de desempleo(%)')
    plt.legend()
    plt.grid(True)
    Desfig.savefig("Desfig.png")
    st.pyplot(Desfig)

    Desfig2= plt.figure(figsize=(10, 5))
    plt.plot(Desempleo["Periodo(MMM, AAAA)"][151:], Desempleo["Tasa de desempleo - total nacional"][151:], color='purple', label='Gustavo Petro')
    fechas6 = (Desempleo["Periodo(MMM, AAAA)"])[151:]
    plt.xticks(ticks=fechas6[::5], rotation=45)

    plt.title('Desempleo')
    plt.xlabel('Año')
    plt.ylabel('Tasa mensual de desempleo(%)')
    plt.legend()
    plt.grid(True)
    Desfig2.savefig("Desfig2.png")
    st.pyplot(Desfig2)

    st.subheader("\'Caida\'")
    st.text("\'Por eso es que el desempleo cayó a 8,2% en la última medición de noviembre, que significa, ni más ni menos, sin ningún boom petrolero ni carbonero, como sí existió en el año 2013-14, la menor tasa de desempleo desde el año 2016 en Colombia\' - Gustavo Petro")
    st.text("Comparando los últimos tres mandatos, tenemos que, en el mandato de Juan Manuel Santos, la tasa de desempleo mostró una reducción sostenida, pasando de alrededor del 15% al 8%, este fue un periodo en donde existió una recuperación gradual del mercado laboral. En contraste, Iván Duque enfrentó uno de los picos más altos de desempleo, con una tasa cercana al 22% en 2020, debido al impacto de la pandemia. Algo a resaltar es que logró tener una recuperación parcial en los años siguientes, sin embargo, terminó su gobierno con una tasa muy elevada, la cual Gustavo Petro recibió y ha podido mantener una tendencia decreciente, con tasas entre 9% y 13%, alcanzando incluso 8,2% en noviembre de 2024, el nivel más bajo desde 2016.")
    st.text("La tendencía en el gobierno Petro es de una caída con cierta estacionalidad (subidas y bajadas regulares), por lo que es apropiado la tendencia manifestada por el presidente, si bien no es una caída constante.")
with tab5:
    st.header ("Tasa de cambio")
    Camfig= plt.figure(figsize=(10, 5))

    plt.plot(Cambio["Periodo(MMM DD, AAAA)"][:219], Cambio["Tasa Representativa del Mercado (TRM)"][:219], color='black')
    plt.plot(Cambio["Periodo(MMM DD, AAAA)"][218:3141], Cambio["Tasa Representativa del Mercado (TRM)"][218:3141], color='red', label='Juan Manuel Santos')
    plt.plot(Cambio["Periodo(MMM DD, AAAA)"][3142:4602], Cambio["Tasa Representativa del Mercado (TRM)"][3142:4602], color='blue', label='Ivan Duque')
    plt.plot(Cambio["Periodo(MMM DD, AAAA)"][4601:], Cambio["Tasa Representativa del Mercado (TRM)"][4601:], color='purple', label='Gustavo Petro')
    fechas7 = (Cambio["Periodo(MMM DD, AAAA)"])
    plt.xticks(ticks=fechas7[::375], rotation=45)


    plt.title('Tasa de cambio')
    plt.xlabel('Año')
    plt.ylabel('TRM en COP')
    plt.legend()
    plt.grid(True)
    Camfig.savefig("Camfig.png")
    st.pyplot(Camfig)

    Camfig2= plt.figure(figsize=(10, 5))
    plt.plot(Cambio["Periodo(MMM DD, AAAA)"][4601:], Cambio["Tasa Representativa del Mercado (TRM)"][4601:], color='purple', label='Gustavo Petro')
    fechas8 = (Cambio["Periodo(MMM DD, AAAA)"])[4601:]
    plt.xticks(ticks=fechas8[::100], rotation=45)

    
    plt.title('Tasa de cambio')
    plt.xlabel('Año')
    plt.ylabel('TRM en COP')
    plt.legend()
    plt.grid(True)
    Camfig2.savefig("Camfig2.png")
    st.pyplot(Camfig2)

    st.subheader("\'Revalorización\'")
    st.text("\'La revalorización que tiene hoy el peso colombiano, bueno para unas cosas, mala para desatar exportaciones productivas, tiene origen en que nuestra tasa de interés cada vez es mayor en términos reales frente al mundo.\' - Presidente Gustavo Petro")
    st.text("Durante el mandato de Juan Manuel Santos, el peso colombiano se caracterizó por su estabilidad y fortaleza, manteniendo su valor cerca de los $2000, durante su primer mandato (2010-2014),en un entorno global más benigno y con políticas económicas que generaban confianza. Su unica alza, efecto del fenómeno del Niño, fue en 2016, llegando cerca de los $3500, pero cerrando su mandato con una baja entre los $2500 y los $3000. Por el contrario, el gobierno de Gustavo Petro ha enfrentado una mayor volatilidad,sin una tendencia definida, lo cual refleja la sensibilidad de los mercados ante sus propuestas de transformación estructural y la incertidumbre interna. Manteniéndose entre los $3500 y los $5000.")
    st.text("En comparación, el gobierno de Ivan Duque mostró una devaluación progresiva, impulsada en gran parte por factores externos como la pandemia y la caída del precio del petróleo, empezo cerca de los $3000 y termino cerca de los $4500, que aunque es un alza bastante significativa, tiene razones validas e inevitables, que hubiesen afectado a cualquier gobierno. Petro, por su parte, ha gobernado en un contexto de mayores tasas de interes reales frente al mundo, lo que según sus propias palabras ha contribuido a una “revalorización del peso colombiano”, este se ve reflejado ya que empezando su mandato existía una tasa de cambio de $5000, pero ha logrado mantenerla debajo de $4500, este fenómeno que él mismo reconoce como una espada de doble filo: beneficiosa en algunos aspectos, pero perjudicial para el impulso de exportaciones productivas. Esta tensión entre estabilidad cambiaria y competitividad exportadora refleja el complejo balance que debe gestionar la política económica actual.")
    st.text("La tendencia de revalorización manaifestada por el presidente Petro no es acertada ya que la depreciación de la moneda comparado con otros periodos es bastante alta. Si bien la tendencia en 2023 fue de bajada de la tasa de cambio, desde el segundo semestre de 2024 se ha observado una depreciación que muestra una tendencia contaria a la revalorización manifestada por el presidente.")
with tab6:
    st.header ("Inflación mensual")
    INFfig= plt.figure(figsize=(10, 5))

    plt.plot(Inflación["Fecha"][:8], Inflación["Inflacion"][:8], color='black')
    plt.plot(Inflación["Fecha"][7:104], Inflación["Inflacion"][7:104], color='red', label='Juan Manuel Santos')
    plt.plot(Inflación["Fecha"][103:152], Inflación["Inflacion"][103:152], color='blue', label='Ivan Duque')
    plt.plot(Inflación["Fecha"][151:], Inflación["Inflacion"][151:], color='purple', label='Gustavo Petro')
    fechas9 = (Inflación["Fecha"])
    plt.xticks(ticks=fechas9[::13], rotation=45)

    plt.title('Inflación')
    plt.xlabel('Año')
    plt.ylabel('Inflación mensual')
    plt.legend()
    plt.grid(True)
    INFfig.savefig("INFfig.png")
    st.pyplot(INFfig)

    INFfig2= plt.figure(figsize=(10, 5))
    plt.plot(Inflación["Fecha"][151:], Inflación["Inflacion"][151:], color='purple', label='Gustavo Petro')
    fechas10 = (Inflación["Fecha"])[151:]
    plt.xticks(ticks=fechas10[::2], rotation=45)

    plt.title('Inflación')
    plt.xlabel('Año')
    plt.ylabel('Inflación mensual')
    plt.legend()
    plt.grid(True)
    INFfig2.savefig("INFfig2.png")
    st.pyplot(INFfig2)
    
    st.subheader("\'Reducción de inflación\'")
    st.text("\'Hemos reducido la inflación, que es el alza de los precios, de un 13% anual, que fue como la encontré con el presidente Duque, a 5% en solo 21 meses, a la mitad, exactamente, o menos de la mitad. La tasa de inflación de alimentos –cómo crecen los precios de la comida, que es lo que más interesa a un colombiano y a una colombiana–, imagínense, la recibí en 22% anual del anterior gobierno.\'")
    st.text("Gracias a las gráficas representadas podemos hacer una comparación entre los últimos tres mandatos en Colombia. Durante el gobierno de Juan Manuel Santos, la inflación se mantuvo relativamente estable, en donde la cifra más alta fue cercana al 9% en 2016, explicado por el fenómeno de El Niño, la devaluación del peso y el aumento en los precios de alimentos. Mientras que, Iván Duque inició su gobierno con una inflación baja (aproximadamente del 3%), lastimosamente a partir del 2021 tuvo que enfrentar una fuerte escalada que llevó la inflación a estar por encima del 13%. Este aumento se ve justificado debido a los factores globales como la pandemia, la interrupción brusca en las cadenas de suministro y el alza en los precios de energía y alimentos. Por último, tenemos el mandato del actual presidente Gustavo Petro que asumió su puesto teniendo el desafío de disminuir la inflación que estaba en su punto más alto en más de dos décadas con cifras superando el 13%, algo que se debe resaltar es que, a pesar de estar un contexto bastante complejo, este gobierno ha logrado una reducir estas cifras alcanzando niveles entre 6% y 7% en 2024.")
    st.text("Si bien la economía tuvo un comienzo inflacionario bastante alto, se llegó a estabilizar y su tendencia es de una inflación decreciente. Por lo tanto, el presidente Petro está justificado en hablar de reducción de la inflación. ")
