from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2
from datetime import datetime
import traceback

class ActionGuardarFeedback(Action):
    def name(self) -> Text:
        return "action_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Detectar la intención para saber si fue "sí" o "no"
        last_intent = tracker.latest_message['intent'].get('name')
        feedback_value = 1 if last_intent == "feedback_yes" else 0

        # Obtener timestamp
        fecha = datetime.now()

        try:
            conn = psycopg2.connect(
                host="localhost",
                database="feedbacks",
                user="postgres",
                password="8520."
            )
            cur = conn.cursor()

            # Insertar en la tabla feedbacks_users
            cur.execute(
                "INSERT INTO feedbacks_users (valor, fecha) VALUES (%s, %s);",
                (feedback_value, fecha)
            )
            conn.commit()

            cur.close()
            conn.close()

            dispatcher.utter_message(text="¡Gracias por tu opinión!")

        except Exception as e:
            error_message = str(e)
            dispatcher.utter_message(text=f"Error al guardar el feedback: {error_message}")
            print(f"Error al conectar a la base de datos: {error_message}")  # Esto imprime en consola/logs


        return []