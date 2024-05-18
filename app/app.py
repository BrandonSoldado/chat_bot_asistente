from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import psycopg2
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'your_secret_key'

def obtener_nombre_usuario(telefono):
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM usuario WHERE telefono = %s", (telefono,))
    nombre = cur.fetchone()
    cur.close()
    conn.close()
    return nombre[0] if nombre else ""

@app.route("/webhook", methods=["POST"])
def webhook():
    message_body = request.form.get("Body")  
    from_number = request.form.get("From")
    to_number = request.form.get("To") 
    nombre = obtener_nombre_usuario(from_number)
    if(nombre!=""):
        respuesta = "¡Hola! "+nombre + " Soy el asistente de servicios de elevadores. Estoy aquí para ayudarte contus consultas y solicitudes relacionadas con los elevadores. Puedo ayudarte a solicitar servicios de mantenimiento,monitorear el estado de los elevadores en tiempo real, programar horarios de operación y mucho más. ¿En qué puedo ayudarte hoy?"
    else:
        respuesta = "usuario no existe!"
    
    print(f"El mensaje fue enviado a: {from_number}")  
    print(respuesta)
    resp = MessagingResponse()
    resp.message(respuesta)
    return str(resp)


  
if __name__=='__main__':
    app.run(debug=True, port=5000)
