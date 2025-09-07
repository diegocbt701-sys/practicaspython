print("Buen Diá, te yudaremos a caucular tu indice de masa corporalr")
nombre= str(input("Introduce Tu Nombre A Continuacion, Si Tienes Dos; Ambos Por Favor "))
if not nombre:
    raise ValueError("No Se Introdujo La Informacion Solicitada")
p_apellido= str(input("Ahora Introduce Tu Primer Apellido Por favor "))
if not p_apellido: 
    raise ValueError("no se introdujo la informacion solicitada")
s_apellido= str(input("Y Ahora Tu Segundo Apellido "))
if not s_apellido:
   raise ValueError("No Se Introdijo La Informacion Solicitada")
x= input("Comencemos con la parte importante")
peso= float(input("Por Favor Introduce Tu Peso "))
if not peso:
    raise ValueError("No Introdujiste Ningun VAlor")
altura= float(input("Ahora Proporcionanos Tu estatura "))
if not altura:
    raise ValueError("No Introdujiste Ningun VAlor")
y= input("Terminemos De Una vez")
imc= float(peso/(altura**2))
print(nombre," ", p_apellido, " ", s_apellido, "Tu Peso Es De ", peso, "Y Yu Altura ", altura," ","Tu Indice De Masa Muscular Es: ", imc)
print("Te Recomendamos Acudir A Tu Medico De Confianza Para Obtener Indicaciones y estar en " \
"Un Buen Estado De SAlud.")
