import hashlib
import csv
import os

CSV_USUARIOS = 'usuarios.csv'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def registrar_usuario(nombre_usuario, contraseña):
    hash_contraseña = hash_password(contraseña)
    with open(CSV_USUARIOS, 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre_usuario, hash_contraseña])
    print(f"Usuario '{nombre_usuario}' registrado.")


def verificar_login(nombre_usuario, contraseña):
    hash_ingresado = hash_password(contraseña)
    
    with open(CSV_USUARIOS, 'r') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            if row['usuario'] == nombre_usuario:
                if row['hash_contraseña'] == hash_ingresado:
                    print("Inicio de sesión exitoso ✅")
                else:
                    print("Contraseña incorrecta ❌")
                return
    print("Usuario no encontrado ❌")


# Ejemplo de uso
#if __name__ == '__main__':
#    choose = int(input("Qué desea hacer?\n1 = iniciar sesión.\n2 = Registrar cuenta.\n\n"))
#     
#    if choose == 1:
#        username = input("Ingresar nombre de usuario.\n")
#        contra = input("Ingresar contraseña.\n")
#        verificar_login(username, contra)
#    elif choose == 2:
#        username = input("Ingresar nombre de usuario.\n")
#        contra = input("Ingresar contraseña.\n")
#        registrar_usuario(username, contra)
