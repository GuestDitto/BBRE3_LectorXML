etiquetas_busc = ['@MetodoPago', '@Total', '@Moneda', '@SubTotal', '@FormaPago', '@Fecha', '@Serie']    #Lista de etiquetas buscadas de la cabecera de la factura
datos_concepto = ['@ValorUnitario', '@Descripcion', '@Cantidad', '@ClaveUnidad']                        #Lista de etiquetas buscadas de los conceptos
dict_completo = {informacion}['cfdi:Comprobante']                                                       #Obtiene todos los datos de la factura
etiquetas_dict = list(dict_completo.keys())                                                             #Lista de todas las etiquetas de la factura
factura = '{factura_actual}'                                                                            #Nombre de la factura

etiquetas_enc = list(set(etiquetas_dict).intersection(etiquetas_busc))                                  #Lista las etiquetas de la cabecera conforme a las buscadas 

#Genera diccionario de encabezado-dato especifico (No en formato original de la factura)
dict_info = {'Archivo XML':factura}
dict_info.update({'Serie Folio':(dict_completo['@Serie'] + ' ' + dict_completo['@Folio'] if '@Serie' in etiquetas_enc else dict_completo['@Folio'])})
dict_info.update({'RFC Emisor':dict_completo.get('cfdi:Emisor').get('@Rfc')})
dict_info.update({'Nombre Emisor':dict_completo.get('cfdi:Emisor').get('@Nombre')})
dict_info.update({'RFC Receptor':dict_completo.get('cfdi:Receptor').get('@Rfc')})
dict_info.update({'Nombre Receptor':dict_completo.get('cfdi:Receptor').get('@Nombre')})

#Genera diccionario con solo los datos buscados
for k,v in dict_completo.items():
  if k in etiquetas_enc:
    dict_info[k] = v

#Obtiene lista de conceptos de la factura
dict_concepto = dict_completo.get('cfdi:Conceptos').get('cfdi:Concepto')
lista_conceptos = []
conceptos = {}

#Genera lista de diccionarios de los conceptos de la factura con unicamente los datos buscados 
if type(dict_concepto) == type(lista_conceptos):
  for item in dict_concepto:
    for k,v in item.items():
      if k in datos_concepto:
        conceptos[k] = v
    lista_conceptos.append(conceptos.copy())
else:
  for k,v in dict_concepto.items():
    if k in datos_concepto:
      conceptos[k] = v
  lista_conceptos.append(conceptos.copy())

SetVar('conceptos', lista_conceptos)
SetVar('informacion', dict_info)
SetVar('encabezados', etiquetas_enc)
SetVar('encabezados_conceptos', datos_concepto)