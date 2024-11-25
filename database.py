import pyodbc
import os
from dotenv import load_dotenv

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
        print("Error al conectar con la base de datos:", e)
        return None

def validar_credenciales(usuario, contraseña):
    try:
        conn = get_connection();
        cursor = conn.cursor()
        
        # Consultar el usuario en la base de datos
        query = "SELECT password, id_user FROM [user] WHERE username = ?"
        cursor.execute(query, (usuario))
        
        # Verificar si el usuario existe
        row = cursor.fetchone()
        if row:
            if row[0] == contraseña: 
                return row[1] # el id
            else:
                return False
        else:
            return False
        
    except Exception as e:
        print("Error al validar las credenciales:", e)
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
        print("Error al validar las credenciales:", e)
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

def get_balance():
    """Obtiene el saldo actual de la billetera."""
    conn = get_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT balance FROM Wallet WHERE id = 1;")
        row = cursor.fetchone()
        return row[0] if row else None
    except Exception as e:
        print("Error al obtener el saldo:", e)
        return None
    finally:
        conn.close()

def update_balance(amount):
    """Actualiza el saldo de la billetera."""
    conn = get_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE Wallet SET balance = balance + ? WHERE id = 1;", (amount,))
        conn.commit()
        return True
    except Exception as e:
        print("Error al actualizar el saldo:", e)
        return False
    finally:
        conn.close()
