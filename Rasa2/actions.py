# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
import spacy
#
#
talking_points=[]
action_items=[]
nlp = spacy.load('en_core_web_sm')
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionTalkingPoint(Action):
    def name(self) -> Text:
        return 'action_talking_point'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        talking_points.append(tracker.latest_message.get("text"))
        return []

class ActionActionItem(Action):
    def name(self) -> Text:
        return 'action_action_item'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.latest_message.get("text")
        ##NER
        #owners=[]
        #deadline=[]
        #modify_ents(text)------delete
        
      #if yes: owner owners.append(word)
      # else: print("Specify owner")
      #       owner.append(input_string) 
          
       #if yes: deadline deadline.append(word)
      # else: print("Specify deadliner")
      #       deadline.append(input_string) 

        #print("Owners:",owners)
       
        #print("Deadline",deadline)
        #fields=(owners,deadline)
        #action_items[text]=fields
        action_items.append(text)
        #return out
        return []

#class ValidateActionItemForm(FormValidationAction):
#    def name(self) -> Text:
#        return "validate_action_item_form"
#    async def extract_