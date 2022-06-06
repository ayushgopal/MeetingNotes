# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import spacy
#
talking_points=[]
action_items={}
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
        owners=[]
        deadline=[]
        #modify_ents(text)------delete
        print(nlp(text).ents)
        for word in nlp(text).ents:
          if word.label_== 'PERSON':
            str1="Is "+str(word)+" the owner? (Y/N)"
            dispatcher.utter_message
            ans=input(str1) #show yes/no buttons
            ans=ans.lower()
            if ans=='y':
              owners.append(word)
            elif ans=='n':
              owner=input("Please specify owner/owners")
              owner=nlp(owner)
              owners.append(owner)
            else: print("Please type Y for yes and N for no")
      #if yes: owner owners.append(word)
      # else: print("Specify owner")
      #       owner.append(input_string) 
          elif word.label_=='TIME' or word.label_=='DATE':
            str2="Is "+str(word)+" the deadline? (Y/N)"
            ans=input(str2)
            ans=ans.lower()
            if ans=='y':
              deadline.append(word)
            elif ans=='n':
              due=input("Please specify deadline")
              due=nlp(due)
              deadline.append(due)
            else: print("Please type Y for yes and N for no")
       #if yes: deadline deadline.append(word)
      # else: print("Specify deadliner")
      #       deadline.append(input_string) 

        print("Owners:",owners)
        print("Deadline",deadline)
        if not owners:
          owner=input("Please specify owner/owners")
          owner=nlp(owner)
          owners.append(owner)
        if not deadline:
          due=input("Please specify deadline")
          due=nlp(due)
          deadline.append(due)

        fields=(owners,deadline)
        action_items[text]=fields
        #return out
        return []
