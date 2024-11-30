import pyodbc
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()

CONNECTION_STRING = (
    f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE')};"
    f"UID={os.getenv('DB_USER')};"
    f"PWD={os.getenv('DB_PASSWORD')};"
    f"TrustServerCertificate=yes"
)

def get_connection():
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as e:
        print("[000] Error al conectar con la base de datos:", e)
        return None

def validar_credenciales(usuario, contraseña):
    try:
        conn = get_connection();
        cursor = conn.cursor()
        
        # Consultar el usuario en la base de datos
        query = "SELECT password_hash, id_user FROM [user] WHERE username = ?"
        cursor.execute(query, (usuario))
        
        # Verificar si el usuario existe
        row = cursor.fetchone()
        if row:
            print(row[0])
            print(hashlib.md5(contraseña.encode()).hexdigest().upper())
            if row[0] == hashlib.md5(contraseña.encode()).hexdigest().upper(): 
                return row[1] # el id
            else:
                return False
        else:
            return False
        
    except Exception as e:
        print("[001] Error al validar las credenciales:", e)
        return False
def getWalletUsuario(id_user):
    print("obteniendo billetera de ID: ",id_user)
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("{CALL obtener_info_wallet (?)}", (id_user))
        result = cursor.fetchone()  
    except Exception as e:
        print("[002] Error al validar las credenciales:", e)
        return None
    finally:
        conn.close()

    if result:
        return {
                "id_wallet": result[0],
                "id_user": result[1],
                "amount": result[2],
                "username": result[3],
                "money_name": result[4],
                "money_abbreviation": result[5],
        }
    else:
        return None

def createUSuarioWallet(username, password, nombre, apellidos, id_money):
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("{CALL crear_usuario_con_wallet (?, ?, ?, ?, ?)}", (username, password, nombre, apellidos, id_money))
        conn.commit()
        return True
    except Exception as e:
        print("[003] Error al crear cuenta:", e)
        return False
    finally:
        conn.close()

def getMoney():
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM money");
        result = cursor.fetchall()  
    except Exception as e:
        print("[004] Error: ", e)
        return None
    finally:
        conn.close()

    if result:
        return [{
                "id": row[0],
                "name": row[1],
                "value_relative": row[2],
                "abrev": row[3],
        } 
        for row in result]
    else:
        return None

def searchUsers(strBusqueda):
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("{CALL buscar_usuario3 (?)}", (strBusqueda))
        result = cursor.fetchall()  
    except Exception as e:
        print("[005] Error: ", e)
        return None
    finally:
        conn.close()

    if result:
        return [{
                "id": row[0],
                "username": row[1],
                "nombre": row[2],
                "apellidos": row[3],
                "id_money": row[4],
                "id_wallet": row[5],
        }
        for row in result]
    else:
        return None

