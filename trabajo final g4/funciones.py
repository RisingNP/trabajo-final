import datetime

def validar_alfa(objeto):
    while True:
        alf = input(f"Ingrese {objeto}: ")
        if alf.replace(' ' , '').isalpha():
            return alf
        else:
            print("Error... no ingrese números... reintentando")

def validar_int(objeto):
    while True:
        int_ = input(f"Ingrese {objeto}: ")
        if int_.isnumeric():
            return int(int_)
        else:
            print("Error: No ingrese letras, ingrese un valor numérico... reintentando...")

def date_():
    while True:
        try:
            dia = int(input("Ingrese el dia en que se realizo la prueba: "))
            mes = int(input("Ingrese el mes en que se realizo la prueba: "))
            año = int(input("Ingrese el año en que se realizo la prueba: "))

            fecha = datetime.date(año , mes , dia).strftime("%Y-%m-%d")
            return(fecha)

        except ValueError:
            print("Ha introducido alguna información de la fecha incorrectamente, intente de nuevo")

def buscar_user_txt(dir , user):
    with open(f'{dir}' , mode='r', encoding='utf8') as file:
        data = file.readlines()
    esta = False
    for i in data:
        if user in i:
            esta = True
    if esta == True:
        return True
    if esta == False:
        return False

def cambiar_contraseña_txt():

    with open('admin/login.txt' , mode= 'r', encoding= 'utf8') as file:
        data = file.readlines()

    while True:  

        user_to_update = input('Ingrese el usuario del cual desea cambiar la contraseña')
        esta = buscar_user_txt('admin/login.txt',user_to_update)
        for i in data:
            if user_to_update in i.replace('\n',''):
                new_password = input('ingrese la nueva contraseña').replace(' ','')
                a = i.replace(' ','').replace('\n','').split(':')
                a[1] = a[1].replace(a[1],new_password)
                updated_user = f'{a[0]} : {a[1]}\n'
                idx = data.index(i)
                data[idx] = updated_user
                with open('admin/login.txt' , mode= 'w', encoding= 'utf8') as file:
                    None
                with open('admin/login.txt' , mode= 'a', encoding= 'utf8') as file:
                    for j in data:
                        file.write(j)
        if esta == True:
            break
        elif esta == False:
            print('El usuario ingresado no existe en los registros... regresando al menú de gestión de usuarios...\n','-'*15)
            break    

def ingresar_usuario_txt():
    while True:
        new_username = input('ingrese el nuevo usuario: ').replace(' ' , '')
        verificar = buscar_user_txt('admin/login.txt' , new_username)
        if verificar == True:
            print('este usuario ya está en la base de datos... intente de nuevo')
        elif verificar == False:
            break
    new_password = input('ingrese la contraseña del nuevo usuario: ').replace(' ' , '')
    new_user = f'{new_username} : {new_password}\n'
    with open('admin/login.txt' , mode= 'a' , encoding= 'utf8') as file:
        file.write(new_user)

def mostrar_usuarios_txt():
    with open('admin/login.txt' , mode= 'r', encoding= 'utf8') as file:
            data = file.readlines()
    for i in data:
        data_print = i.replace('\n' , '').split(':')
        print(f'''Usuario: {data_print[0]} 
contraseña: {data_print[1]}\n''' , '-'*20)

def eliminar_user_txt():
    with open('admin/login.txt' , mode= 'r', encoding= 'utf8') as file:
        data = file.readlines()
    while True:
        user_to_delete = input('ingrese el usuario que desea eliminar')
        verificar = buscar_user_txt('admin/login.txt',user_to_delete)
        
        for i in data:
            if user_to_delete in i.replace('\n',''):
                a = i.replace(' ','').replace('\n','').split(':')
                idx = data.index(i)
                data.pop(idx)
                with open('admin/login.txt' , mode= 'w', encoding= 'utf8') as file:
                    None
                with open('admin/login.txt' , mode= 'a', encoding= 'utf8') as file:
                    for j in data:
                        file.write(j)

        if verificar == False:
            print('el usuario ingresado no existe en los registros... regresando al menú de gestión de usuarios')
            break
        elif verificar == True:
            break