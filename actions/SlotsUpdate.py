from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from thefuzz import fuzz
from unidecode import unidecode
from typing import Any, Text, Dict
from .Exercise import *


class ActionSlotsUpdate(Action):
    def name(self) -> Text:
        return "action_actualizar_slots"

    @staticmethod
    def gauge_progress(condition_progress: Text) -> Text:
        best_ratio = 0
        best_match = "estancamiento"
        progress_synonyms = ("gran", "significativa", "mejora", "aumentar", "notable", "considerable", "mejorado")
        stagnation_synonyms = ("retroceso", "regresion", "no he mejorado", "no he experimentado")
        processed_progress = unidecode(condition_progress.lower())

        for s in progress_synonyms:
            match_ratio = fuzz.token_set_ratio(processed_progress, s)

            if match_ratio > best_ratio:
                best_ratio = match_ratio
                best_match = "progreso"

        for s in stagnation_synonyms:
            match_ratio = fuzz.token_set_ratio(processed_progress, s)

            if match_ratio > best_ratio:
                best_ratio = match_ratio
                best_match = "estancamiento"

        return best_match

    @staticmethod
    def calc_condition(physical_condition: Text, condition_progress: Text) -> Text:
        if condition_progress == "progreso":
            match physical_condition:
                case "baja":
                    return "media"
                case "media":
                    return "alta"

        return physical_condition

    @staticmethod
    def calc_experience(experience: Text, routine_time: Text) -> Text:
        if routine_time == "meses":
            match experience:
                case "nula":
                    return "poca"
                case "poca":
                    return "promedio"
                case "promedio":
                    return "mucha"
        elif routine_time == "años":
            match experience:
                case "nula":
                    return "promedio"
                case "poca" | "promedio":
                    return "mucha"

        return experience

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        # Obtener los valores de todos los slots
        slots = tracker.current_slot_values()

        if slots[ROUTINE_CREATED]:
            physical_condition = slots[PHYSICAL_CONDITION]
            experience = slots[SPORT_EXPERIENCE]
            condition_progress = slots[CONDITION_PROGRESS]
            routine_time = slots[ROUTINE_TIME]

            progress = ActionSlotsUpdate.gauge_progress(condition_progress)
            physical_condition = ActionSlotsUpdate.calc_condition(physical_condition, progress)
            experience = ActionSlotsUpdate.calc_experience(experience, routine_time)

            return [SlotSet(PHYSICAL_CONDITION, physical_condition), SlotSet(SPORT_EXPERIENCE, experience)]

        return []
