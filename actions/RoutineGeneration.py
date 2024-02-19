import math
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from .Exercise import *


class ActionCrearPlanEntrenamiento(Action):
    def name(self) -> Text:
        return "action_crear_plan_entrenamiento"

    # Given a dictionary of final exercises, the function formats that dictionary to a message the bot will respond
    @staticmethod
    def format_routine(final_exercises: Dict[int, Dict]) -> Text:
        formatted_routine = ""

        for fe in final_exercises.keys():
            formatted_routine += "Dia {}\n".format(fe)

            for e in final_exercises[fe].keys():
                formatted_routine += "{}x{}x{}\n".format(final_exercises[fe][e]["sets"], final_exercises[fe][e]["reps"], e)

            formatted_routine += "\n"

        return formatted_routine

    # Filters the exercises by a max_difficulty parameter
    @staticmethod
    def filter_exercises_by_difficulty(exercises: Dict[str, Any], max_difficulty: int) -> Dict[str, Any]:
        filtered_exercises = {}

        for e in exercises.keys():
            description = exercises[e]

            if description["difficulty"] <= max_difficulty:
                filtered_exercises[e] = description

        return filtered_exercises

    # Filters the exercises by a priority parameter
    @staticmethod
    def filter_exercises_by_priority(exercises: Dict[str, Any], priority: Text) -> Dict[str, Any]:
        filtered_exercises = {}

        for e in exercises.keys():
            description = exercises[e]

            if description["priority"] == priority:
                filtered_exercises[e] = description

        return filtered_exercises

    # Calculates the average number of sets for a given movement pattern and a max_difficulty
    @staticmethod
    def calc_set_range(movement: Dict[str, Any], max_difficulty: int) -> Dict[str, int]:
        if max_difficulty == BEGINNER:
            min_sets = movement["min_beginner_sets"]
            max_sets = movement["max_beginner_sets"]
        elif max_difficulty == INTERMEDIATE:
            min_sets = movement["min_intermediate_sets"]
            max_sets = movement["max_intermediate_sets"]
        else:
            min_sets = movement["min_advanced_sets"]
            max_sets = movement["max_advanced_sets"]

        return {"min_sets": min_sets,
                "max_sets": max_sets}

    # Calculates the age modifier for a certain field
    @staticmethod
    def calc_age_mod(field: str, age: int) -> float:
        for a in reversed(modifiers[field][AGE]):
            if age >= a:
                return modifiers[field][AGE][a]

        return 1.0

    # Calculates the total amount of points of effectiveness in a certain list of exercises
    @staticmethod
    def calc_total_effectiveness(exercises: Dict[str, Any]) -> int:
        total_score = 0

        for e in exercises.keys():
            total_score += exercises[e]["effectiveness"]

        return total_score

    # Modifies the amount from a certain field (sets or reps) given the values of the slots
    @staticmethod
    def mod_field(slots: Dict[Text, Any], field: str, field_amount: int) -> int:
        # Extracts all slots values
        age = int(slots[AGE])
        physical_condition = slots[PHYSICAL_CONDITION].lower()
        sport_experience = slots[SPORT_EXPERIENCE].lower()
        objective = slots[OBJECTIVE].lower()

        # Modifies the set's value
        field_modifiers = modifiers[field]
        field_amount *= ActionCrearPlanEntrenamiento.calc_age_mod(field, age)
        field_amount *= field_modifiers[PHYSICAL_CONDITION][physical_condition]
        field_amount *= field_modifiers[SPORT_EXPERIENCE][sport_experience]
        field_amount *= field_modifiers[OBJECTIVE][objective]

        return field_amount

    # Calculates de amount of sets for a given movement pattern and a max_difficulty
    @staticmethod
    def calc_amount_field(slots: Dict[Text, Any], field_range: Dict[str, Any], field: str) -> int:
        # Calculates the minimum and maximum amount of the field
        min_field = field_range["min_" + field]
        max_field = field_range["max_" + field]

        # Modifies an average amount of the field from the slot's values
        average_field = (min_field + max_field) / 2.0
        average_field = ActionCrearPlanEntrenamiento.mod_field(slots, field, int(average_field))

        # Normalizes the amount of the field
        average_field = max(average_field, min_field)
        average_field = min(average_field, max_field)

        return math.floor(average_field)

    # Calculates the amount of sets a person should do given the amount of repetitions per set that is going to be done
    @staticmethod
    def calc_amount_sets(amount_reps: int) -> int:
        if amount_reps < 6:
            return 5
        elif amount_reps < 9:
            return 4
        elif amount_reps < 25:
            return 3
        else:
            return 2

    # Calculates the amount of days should be done in a weekly basis for the generated routine
    @staticmethod
    def calc_amount_days(difficulty: int, objective: str) -> int:
        days = difficulty + 3

        if objective == "fuerza":
            return days + 1

        return days

    # Selects the chosen exercise from a list with and a score
    @staticmethod
    def sel_chosen_exercise(exercises: Dict[str, Any], chosen_score: int) -> str:
        for e in exercises.keys():
            effectiveness = exercises[e]["effectiveness"]

            if effectiveness >= chosen_score:
                return e
            else:
                chosen_score -= effectiveness

    # Obtains a random exercise from a list of exercises
    @staticmethod
    def get_random_exercise(exercises: Dict[str, Any]) -> str | None:
        if len(exercises) == 0:
            return None

        total_score = ActionCrearPlanEntrenamiento.calc_total_effectiveness(exercises)
        chosen_score = random.randint(1, total_score)

        return ActionCrearPlanEntrenamiento.sel_chosen_exercise(exercises, chosen_score)

    # Obtains the maximum difficulty of exercises the user can do
    @staticmethod
    def get_max_difficulty(sport_experience: str) -> int:
        if sport_experience == "promedio":
            return INTERMEDIATE
        elif sport_experience == "mucha":
            return ADVANCED

        return BEGINNER

    # Initializes the dictionary where the routine is going to be generated
    @staticmethod
    def init_routine_dict(days: int) -> Dict[int, Dict]:
        routine_dict = {}

        for d in range(1, days + 1):
            routine_dict[d] = {}

        return routine_dict

    # Creates a basic routine given the slots that the chatbot provides
    @staticmethod
    def create_basic_routine(slots: Dict[Text, Any]) -> Dict[int, Dict]:
        max_difficulty = ActionCrearPlanEntrenamiento.get_max_difficulty(slots[SPORT_EXPERIENCE])
        days = ActionCrearPlanEntrenamiento.calc_amount_days(max_difficulty, slots[OBJECTIVE])
        final_exercises = ActionCrearPlanEntrenamiento.init_routine_dict(days)
        next_day = 1

        for mp in movement_patterns.keys():
            movement_i = movement_patterns[mp]
            filtered_exercises = ActionCrearPlanEntrenamiento.filter_exercises_by_difficulty(movement_i["exercises"], max_difficulty)
            set_range = ActionCrearPlanEntrenamiento.calc_set_range(movement_i, max_difficulty)
            amount_sets = ActionCrearPlanEntrenamiento.calc_amount_field(slots, set_range, "sets")
            i = 0

            while amount_sets > 0:
                exercise_sets = 0
                i_filtered_exercises = ActionCrearPlanEntrenamiento.filter_exercises_by_priority(filtered_exercises, EXERCISE_PRIORITY[i])

                if len(i_filtered_exercises) > 0:
                    chosen_exercise = ActionCrearPlanEntrenamiento.get_random_exercise(i_filtered_exercises)
                    amount_reps = ActionCrearPlanEntrenamiento.calc_amount_field(slots, i_filtered_exercises[chosen_exercise], "reps")
                    exercise_sets = ActionCrearPlanEntrenamiento.calc_amount_sets(amount_reps)
                    final_exercises[next_day][chosen_exercise] = {"sets": exercise_sets,
                                                                  "reps": amount_reps}
                    next_day = next_day % days + 1

                amount_sets -= exercise_sets
                i += 1

        return final_exercises

    # Sets the exercises, sets and reps slots with the newly generated routine
    @staticmethod
    def set_routine_slots(routine: Dict[int, Dict]) -> List:
        # Generates the different list from the routine
        days = []
        exercises = []
        sets = []
        reps = []

        day_separation = 0

        for day in routine.keys():
            days.append(day_separation)

            for e in routine[day].keys():
                exercises.append(e)
                sets.append(routine[day][e]["sets"])
                reps.append(routine[day][e]["reps"])

            day_separation += len(routine[day])

        return [SlotSet(ROUTINE_CREATED, True), SlotSet(DAY_SEPARATION, days), SlotSet(EXERCISES, exercises), SlotSet(SETS, sets), SlotSet(REPS, reps)]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        # Get the values from all slots
        slots = tracker.current_slot_values()

        routine = ActionCrearPlanEntrenamiento.create_basic_routine(slots)
        formatted_routine = ActionCrearPlanEntrenamiento.format_routine(routine)
        dispatcher.utter_message(formatted_routine)

        return ActionCrearPlanEntrenamiento.set_routine_slots(routine)
