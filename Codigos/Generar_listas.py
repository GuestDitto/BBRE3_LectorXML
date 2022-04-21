encabezados_conceptos = {encabezados_conceptos} #Encabezados de lista de conceptos
encabezados = list({informacion}.keys())        #Encabezados de cabecera de factura
columnas = {letras_columnas}                    #Lista de referencia de columnas excel
lista_conceptos = []
lista_formato = []
lista_ord = []

#Genera lista ordenada segun columnas en excel
lista_ord.append('Archivo XML') if 'Archivo XML' in encabezados else ''
lista_ord.append('@Fecha') if '@Fecha' in encabezados else ''
lista_ord.append('RFC Emisor') if 'RFC Emisor' in encabezados else ''
lista_ord.append('Nombre Emisor') if 'Nombre Emisor' in encabezados else ''
lista_ord.append('RFC Receptor') if 'RFC Receptor' in encabezados else ''
lista_ord.append('Nombre Receptor') if 'Nombre Receptor' in encabezados else ''
lista_ord.append('Serie Folio') if 'Serie Folio' in encabezados else ''
lista_ord.append('@Moneda') if '@Moneda' in encabezados else ''
lista_ord.append('@FormaPago') if '@FormaPago' in encabezados else ''
lista_ord.append('@MetodoPago') if '@MetodoPago' in encabezados else ''
lista_ord.append('@Total') if '@Total' in encabezados else ''
lista_ord.append('@SubTotal') if '@SubTotal' in encabezados else ''

#Remueve el '@' de los encabezados de la lista de cabecera, genera otra lista
for item in lista_ord:
  if item.startswith('@'):
    lista_formato.append(item.replace('@', ''))
  else:
    lista_formato.append(item)

#Remueve el '@' de los encabezados de la lista de conceptos, genera otra lista
for item in encabezados_conceptos:
  if item.startswith('@'):
    lista_conceptos.append(item.replace('@', ''))
  else:
    lista_conceptos.append(item) 

#Crea diccionarios con la relacion de dato-columna en excel
encabezados = dict(zip(lista_ord, columnas))
lista_dict = [dict(zip(columnas, lista_formato))]
encabezados_conceptos = dict(zip(encabezados_conceptos, columnas[1:]))
lista_conceptos = [dict(zip(columnas[1:], lista_conceptos))]

SetVar('encabezados', encabezados)
SetVar('encabezados_excel', lista_dict)
SetVar('conceptos_encabezados', lista_conceptos)
SetVar('encabezados_conceptos', encabezados_conceptos)