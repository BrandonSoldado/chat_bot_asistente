from flask import Flask, request, session, make_response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import psycopg2
from psycopg2 import OperationalError, Error
from flask import jsonify
import prompt
from groq import Groq


app = Flask(__name__)

def obtener_preguntas_usuario(usuario_id):
    try:
        conn = psycopg2.connect(
            dbname="ChatBot",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432",
            options="-c client_encoding=utf8"
        )
        cur = conn.cursor()
        cur.execute("SELECT Pregunta FROM pregunta_usuario WHERE usuarioid = %s", (usuario_id,))
        preguntas = cur.fetchall()
        cur.close()
        conn.close()
        preguntas_lista = [pregunta[0] for pregunta in preguntas]  # Extrae solo las preguntas de los resultados
        preguntas_string = ', '.join(preguntas_lista)  # Une las preguntas en un solo string separado por comas
        print(preguntas_string)
        return preguntas_string
        
    except (OperationalError, Error) as e:
        print(f"Error al obtener preguntas del usuario: {e}")
        return ""

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

def obtener_id_usuario(telefono):
    conn = psycopg2.connect(
        dbname="ChatBot",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432",
        options="-c client_encoding=latin1"
    )
    cur = conn.cursor()
    cur.execute("SELECT id FROM usuario WHERE telefono = %s", (telefono,))
    id = cur.fetchone()
    cur.close()
    conn.close()
    return id[0] if id else -1


try:
    client = Groq(api_key="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")
except Exception as e:
    print(f"Error al crear el cliente Groq: {e}")

def enviar_mensaje(mensaje,preguntas):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt.prompt_chat_bot+prompt.prompt_bbdd+", previamente te di estas preguntas: "+preguntas+", esta es mi pregunta actual: "+mensaje
            }
        ],
        temperature=0.5,
        max_tokens=3000
    )
    return response.choices[0].message.content




def insertar_pregunta(pregunta, fecha, hora, usuario_id):
    try:
        conn = psycopg2.connect(
            dbname="ChatBot",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432",
            options="-c client_encoding=utf8"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO pregunta_usuario (pregunta, fecha, hora, usuarioid) VALUES (%s, %s, %s, %s)", (pregunta, fecha, hora, usuario_id))
        conn.commit()
        cur.close()
        conn.close()
        print("Pregunta insertada correctamente.")
    except (OperationalError, Error) as e:
        print(f"Error al insertar pregunta: {e}")



def enviar_mensaje2(nombre):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt.mensaje_bienvenida+nombre
            }
        ],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content



@app.route("/webhook", methods=["POST"])
def webhook():
    message_body = request.form.get("Body")
    from_number = request.form.get("From")
    to_number = request.form.get("To")
    nombre = obtener_nombre_usuario(from_number)
    if message_body.lower() == "confirm":
        respuesta = enviar_mensaje2(nombre) 

    else:
        if nombre:
            id_usuario = obtener_id_usuario(from_number)
            insertar_pregunta(message_body,"2024-05-28","12:00:00",id_usuario)
            respuesta = enviar_mensaje(message_body,obtener_preguntas_usuario(id_usuario))
        else:
            respuesta = "Usuario no existe!"

    print(f"El mensaje fue enviado a: {from_number}")
    print(message_body)
    
    resp = MessagingResponse()
    resp.message(respuesta)
    return str(resp)




  
if __name__=='__main__':
    app.run(debug=True, port=5000)
    