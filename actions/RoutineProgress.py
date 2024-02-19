from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from .Exercise import *


class ActionRoutineProgress(Action):
    def name(self) -> Text:
        return "action_progresar_rutina"

    @staticmethod
    def format_routine(day: int, day_separation_min: int, day_separation_max: int, exercises: List[Text], sets: List[int], reps: List[int]) -> Text:
        formatted_routine = "Dia {}\n".format(day)

        for i in range(day_separation_min, day_separation_max):
            formatted_routine += "{}x{}x{}\n".format(sets[i], reps[i], exercises[i])

        formatted_routine += "\n"

        return formatted_routine

    @staticmethod
    def search_exercise(exercise: Text) -> Dict[Text, Any]:
        for mp in movement_patterns.keys():
            mp_exercises = movement_patterns[mp]["exercises"]

            if exercise in mp_exercises:
                return mp_exercises[exercise]

        return {}

    @staticmethod
    def transform_routine(day_separation_min: int, day_separation_max: int, exercises: List[Text], sets: List[int], reps: List[int]):
        for i in range(day_separation_min, day_separation_max):
            exercise_i = exercises[i]
            exercise_info = ActionRoutineProgress.search_exercise(exercise_i)

            if exercise_info["max_reps"] == reps[i]:
                sets[i] += 1
                reps[i] = exercise_info["min_reps"]
            else:
                reps[i] += 1

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        # Obtener los valores de todos los slots
        slots = tracker.current_slot_values()

        day = int(slots[DAY])
        exercises = slots[EXERCISES]
        sets = slots[SETS]
        reps = slots[REPS]
        day_separation_min = slots[DAY_SEPARATION][day - 1]

        if day >= len(slots[DAY_SEPARATION]):
            day_separation_max = len(exercises)
        else:
            day_separation_max = slots[DAY_SEPARATION][day]

        ActionRoutineProgress.transform_routine(day_separation_min, day_separation_max, exercises, sets, reps)
        formatted_routine = ActionRoutineProgress.format_routine(day, day_separation_min, day_separation_max, exercises, sets, reps)
        dispatcher.utter_message(formatted_routine)

        return [SlotSet(SETS, sets), SlotSet(REPS, reps)]
