## Script para manejar la calculadora  del Windows.
vApp =App.open("calc")
#Solicitamos toda la fórmula matemática que realizará el script
formula = input(u"Inserte la fórmula a realizar")

## Función que realiza un click al botón de la operación pasada cómo parametro 
def click_boton(operacion):
    lista ={ '+':"1572955279952.png",'-':"1572955289482.png",'*':   "1572955298923.png",'/':   "1572955308197.png",   
            '0':"1572955029914.png",'1':"1572955036597.png",'2':"1572955053174.png",'3':"1572955043596.png",'4':"1572955060741.png",'5':"1572955068421.png",
            '6':"1572955074469.png",'7':"1572955089214.png",'8':"1572955080982.png",'9':"1572955095564.png"}    
    click(lista[operacion])

#Para cada letra que hay en la formula se realizará un tratamiento 
for vSimbolo in formula:
    try:
        click_boton(vSimbolo)
    except KeyError:
        popup (u"La operación solicitada no existe")
    except FindFailed:        
        popup("Imagen no encontrada para valor : "+ vSimbolo)
    except ValueError: 
        popup(u"Imagen ha producido un problema : "+ vSimbolo)            
    except:
        print ("error no identificado al hacer click en la operación", sys.exc_info()[0])
        raise
            
type(Key.ENTER)
        
    
