# Función para que la inteligencia artificial responda a las preguntas
def responder_pregunta(pregunta):
    respuestas = {
        "¿Cuál es tu nombre?": "Mi nombre es AIbot.",
        "¿Cómo estás?": "Estoy programado para estar siempre bien.",
        "¿Cuál es la capital de Francia?": "La capital de Francia es París.",
        "¿Cuál es la respuesta a la vida, el universo y todo lo demás?": "La respuesta es 42.",
        "Adiós": "¡Hasta luego! ¡Que tengas un buen día!"
    }
    
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "Lo siento, no puedo responder a esa pregunta."

# Función principal para interactuar con la inteligencia artificial
def interactuar_con_ai():
    print("¡Hola! Soy AIMARCHAN, una inteligencia artificial. Puedes hacerme algunas preguntas.")
    
    while True:
        pregunta = input("Tú: ")
        
        if pregunta.lower() == 'adiós':
            print("AIMARCHAN: " + responder_pregunta(pregunta))
            break
        
        print("AIMARCHAN: " + responder_pregunta(pregunta))

# Iniciar la interacción con la inteligencia artificial
interactuar_con_ai()
