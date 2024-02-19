from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from thefuzz import fuzz
from unidecode import unidecode
from typing import Any, Text, Dict, List
from .Exercise import *


class ActionExplicarEjercicio(Action):
    def name(self) -> Text:
        return "action_explicar_ejercicio"

    @staticmethod
    def get_exercise_description(exercise: Text) -> Text | None:
        for mp in movement_patterns.keys():
            mp_exercises = movement_patterns[mp]["exercises"]

            if exercise in mp_exercises:
                return mp_exercises[exercise]["description"]

        return None

    @staticmethod
    def search_exercise(exercises: List[Text], exercise: Text) -> Text | None:
        lowered_exercise = unidecode(exercise.lower())
        best_ratio = 0
        best_exercise = None

        for e in exercises:
            lowered_e = unidecode(e.lower())
            match_ratio = fuzz.token_set_ratio(lowered_e, lowered_exercise)

            if match_ratio > best_ratio:
                best_ratio = match_ratio
                best_exercise = e

        return best_exercise

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        # Obtener los valores de todos los slots
        slots = tracker.current_slot_values()

        if slots[ROUTINE_CREATED]:
            exercises = slots[EXERCISES]
            exercise = slots[EXERCISE]

            if exercise is None:
                dispatcher.utter_message("Entendido. Parece que no he logrado identificar el ejercicio al que te refieres. ¿Podrías proporcionar "
                                         "más detalles sobre el nombre del ejercicio o especificar de qué ejercicio te gustaría obtener "
                                         "información? Estoy aquí para ayudarte.")
            else:
                # Esto se hace porque el nombre que da el usuario puede no coincidir totalmente con el que esta almacenado en la base de datos
                exercise_name = ActionExplicarEjercicio.search_exercise(exercises, exercise)

                if exercise_name is None:
                    dispatcher.utter_message("Lamentablemente, no he encontrado información sobre el ejercicio que mencionas en tu rutina actual.")
                else:
                    exercise_description = ActionExplicarEjercicio.get_exercise_description(exercise_name)
                    dispatcher.utter_message(exercise_description)
        else:
            dispatcher.utter_message("Actualmente, no tienes una rutina de entrenamiento generada. Para proporcionarte información detallada sobre "
                                     "un ejercicio, primero necesitamos crear una rutina personalizada para ti.")

        return []
