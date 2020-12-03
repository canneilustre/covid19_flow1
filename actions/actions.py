from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class PUIForm(FormAction):

    def name(self):
        return "PUI_form"

    @staticmethod
    def required_slots(tracker):

        return ["surname", "name", "department", "birthdate", "city_residence", "contact_number", "temperature", "symptoms", "initial_date"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "surname": [
                self.from_entity(entity="surname"),
                self.from_text(intent="inform"),
            ],
             "name": [
                self.from_entity(entity="name"),
                self.from_text(intent="inform"),
            ],
             "department": [
                self.from_entity(entity="department"),
                self.from_text(intent="inform"),
            ],
            "birthdate" [
                self.from_entity(entity="time"),
                self.from_text(intent="inform"),
            ],
            "city_residence" [
                self.from_entity(entity="GPE"),
                self.from_text(intent="inform"),
            ],
            "contact_number" [
                self.from_entity(entity="phone-number"),
                self.from_text(intent="inform"),
            ],
            "temperature" [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="unsure", value=False),
                self.from_text(intent="inform"),
            ],
            "symptoms" [
                self.from_entity(entity="symptoms"),
                self.from_text(intent="inform"),
            ],
            "initial_date" [
                self.from_entity(entity="time"),
                self.from_intent(intent="unsure", value=NA)
                self.from_text(intent="inform"),
            ]
            
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")
        return []