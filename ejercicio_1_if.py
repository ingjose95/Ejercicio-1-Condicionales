print('Programa para preguntar edad de usuario')

mayorEdad = 18 #la mayoria de edad puede ser disntinta en cada pais

edadUsuario = int(input('Ingrese su edad: '))

if edadUsuario >= mayorEdad:

    print('El usuario es mayor de edad.')

else:

    print('El usuario no es mayor de edad.')