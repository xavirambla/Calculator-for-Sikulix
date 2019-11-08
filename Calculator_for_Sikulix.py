vApp =App.open("calc")
operando1 = input("Inserte el primer operando")
operando2 = input("Inserte el segundo operando")
operacion = input(u"Inserte la operación")

def click_numero(numero):
    listaNums=["1572955029914.png","1572955036597.png","1572955053174.png","1572955043596.png","1572955060741.png","1572955068421.png","1572955074469.png","1572955089214.png","1572955080982.png","1572955095564.png"]
    click(listaNums[int(numero)])

def click_operacion(operacion):
    listaOperaciones ={
            '+':   "1572955279952.png", '-':   "1572955289482.png",  '*':   "1572955298923.png", '/':   "1572955308197.png",
            }
    click(listaOperaciones[operacion])

click_numero(operando1)
click_operacion(operacion)
click_numero(operando2)

type(Key.ENTER)
    

