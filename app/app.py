from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import psycopg2
from flask import jsonify









app = Flask(__name__)
app.secret_key = 'your_secret_key'

def marcar_mensaje_enviado():
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )
    cur = conn.cursor()
    cur.execute("UPDATE bandera SET estado1 = 'true' WHERE id = 1")
    conn.commit()
    cur.execute("SELECT estado1 FROM bandera WHERE id = 1")
    condicion = cur.fetchone()[0]
    cur.close()
    conn.close()



def verificar_mensaje_fue_enviado():
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )

    cur = conn.cursor()
    cur.execute("SELECT estado1 FROM bandera WHERE id = 1")
    condicion = cur.fetchone()[0]  
    cur.close()
    conn.close()
    return condicion


def obtener_nombre_usuario(telefono):
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )
    # Crear un cursor para ejecutar consultas
    cur = conn.cursor()
    
    # Ejecutar una consulta SQL para obtener el nombre asociado con el número de teléfono dado
    cur.execute("SELECT nombre FROM usuario WHERE telefono = %s", (telefono,))
    
    # Obtener el resultado de la consulta
    nombre = cur.fetchone()
    
    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()
    
    # Devolver el nombre si se encontró, o una cadena vacía si no se encontró
    return nombre[0] if nombre else ""







def marcar_mensaje_enviado2():
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )
    cur = conn.cursor()
    cur.execute("UPDATE bandera SET estado2 = 'true' WHERE id = 1")
    conn.commit()
    cur.execute("SELECT estado2 FROM bandera WHERE id = 1")
    condicion = cur.fetchone()[0]
    cur.close()
    conn.close()



def verificar_mensaje_fue_enviado2():
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )

    cur = conn.cursor()
    cur.execute("SELECT estado2 FROM bandera WHERE id = 1")
    condicion = cur.fetchone()[0]  
    cur.close()
    conn.close()
    return condicion




@app.route("/webhook", methods=["POST"])
def webhook():
    message_body = request.form.get("Body")
    to_number = request.form.get("To")  # Aquí obtenemos tu número de teléfono
    resp = MessagingResponse()
    resp.message(f"Hello, you said: {message_body}")
    if(verificar_mensaje_fue_enviado()=="false"):
        enviar(to_number)
        marcar_mensaje_enviado()
    print(f"El mensaje fue enviado a: {to_number}")  # Imprime tu número de teléfono

    return str(resp)


@app.route('/enviar')
def enviar(nro_tefeno):
    if(verificar_mensaje_fue_enviado2()=="false"):
        nombre = obtener_nombre_usuario(nro_tefeno+"3")
        print(nombre)
        marcar_mensaje_enviado2()
        if(nombre!=""):
            #account_sid = 'AC0700301559f20ae40bdd55dd06748660'
            #auth_token = '314ad44592ca8d53f6d7891d4b45c042'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Hola '+ nombre +"!",
                to=nro_tefeno
            )
            return 'mensaje enviado'
        else:
            #account_sid = 'AC0700301559f20ae40bdd55dd06748660'
            #auth_token = '314ad44592ca8d53f6d7891d4b45c042'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body="usuario no existe",
                to=nro_tefeno
            )
            return 'mensaje enviado'
    else:
        return 'null'
        


if __name__=='__main__':
    app.run(debug=True, port=5000)
