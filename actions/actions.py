# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#***********************************************************************************************************************************************************
#This is a sample database file
action_items = [
    {
        "id": "1",
        #"meeting_id": "1",
        "text": "Complete the presentation",
        "owners": ["1"],
        #"status": "yet to start",
        "deadline": "",
        #"time":"",
    },
    {
        "id": "2",
        #"meeting_id": "1",
        "text": "Join slack channel",
        "owners": ["1","2"],
        "deadline": "",
        #"status": "yet to start",
        #"time":"",
    },
    {
        "id": "3",
        #"meeting_id": "2",
        "text": "Deploy on Docker",
        "owners": ["2"],
        "deadline": "",
        #"status": "yet to start",
        #"time":"",
    },
]

talking_points = [
    {
        "id": "1",
        #"agenda": "General Knowledge",
        "notes":"",
        #"attendees": ["1","2"],
        #"action_items": ["1","2"],
    },
    {
        "id": "2",
        #"agenda": "Delhi Tourism",
        "notes": "",
        #"attendees": ["1"],
        #"action_items": ["3"],
    }
]

#********************************************************************************************************************************************************

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet
#import spacy
#from transformers import SLOW_TO_FAST_CONVERTERS
#import data
from datetime import datetime as dt
from datetime import timedelta as td
#
#
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
class ActionAddTalkingPoint(Action):
    def name(self) -> Text:
        return 'action_add_talking_point'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #talking_points.append(tracker.latest_message.get("text"))
        text=tracker.get_slot('talking_point_text')
        #last_ind=len(data.talking_points)-1
        #id=data.talking_points[last_ind]['id']+1
        id=tracker.get_slot('talking_point_id')
        dict={}
        dict["id"]=id
        dict["notes"]=text
        talking_points.append(dict)
        dispatcher.utter_message("Talking Point added to database!")
        return []

class ActionAddTalkingPoint2(Action):
    def name(self) -> Text:
        return 'action_add_talking_point_2'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #talking_points.append(tracker.latest_message.get("text"))
        text=tracker.get_slot('talking_point_text_2')
        #last_ind=len(data.talking_points)-1
        #id=data.talking_points[last_ind]['id']+1
        id=tracker.get_slot('talking_point_id_2')
        dict={}
        dict["id"]=id
        dict["notes"]=text
        talking_points.append(dict)
        dispatcher.utter_message("Talking Point added to database!")
        return []

class ActionAddActionItem(Action):
    def name(self) -> Text:
        return 'action_add_action_item'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #talking_points.append(tracker.latest_message.get("text"))
        text=tracker.get_slot('action_item_text')
        owner=tracker.get_slot('owner')
        deadline=tracker.get_slot('deadline')
        #last_ind=len(data.action_items)-1
        #id=data.action_items[last_ind]['id']+1
        id=tracker.get_slot('action_item_id')
        dict={}
        dict["id"]=id
        dict["text"]=text
        owners=tracker.get_latest_entity_values("owner")
        owner_list=[]
        for owner in owners:
            owner_list.append(owner)
        dict["owners"]=owner_list
        dict["deadline"]=deadline
        action_items.append(dict)
        dispatcher.utter_message("Action Item added to database!")
        return []

class ActionAddActionItem2(Action):
    def name(self) -> Text:
        return 'action_add_action_item_2'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #talking_points.append(tracker.latest_message.get("text"))
        text=tracker.get_slot('action_item_text_2')
        owner=tracker.get_slot('owner_2')
        deadline=tracker.get_slot('deadline_2')
        #last_ind=len(data.action_items)-1
        #id=data.action_items[last_ind]['id']+1
        id=tracker.get_slot('action_item_id_2')
        dict={}
        dict["id"]=id
        dict["text"]=text
        owners=tracker.get_latest_entity_values("owner")
        owner_list=[]
        for owner in owners:
            owner_list.append(owner)
        dict["owners"]=owner_list
        dict["deadline"]=deadline
        action_items.append(dict)
        dispatcher.utter_message("Action Item added to database!")
        return []

class ActionGetOwner(Action):
    def name(self) -> Text:
        return 'action_get_owner'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #owner=next(tracker.get_latest_entity_values("owner"), None)
        owners=tracker.get_latest_entity_values("owner")
        owner=[]
        for o in owners:
            owner.append(o)
        owner_str = ','.join(map(str, owner))
        str1="Entities detected"+str(owner_str)
        dispatcher.utter_message(str1)
        #owner=tracker.latest_message.get("text")
        dispatcher.utter_message("Owner slot set")
        return [SlotSet(key='owner', value=owner_str),SlotSet(key='owner_2', value=owner_str)]


class ActionGetDeadline(Action):
    def name(self) -> Text:
        return 'action_get_deadline'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #deadline=tracker.latest_message.get("text")
        time=tracker.get_slot('time')
        deadline={}
        #grain=tracker.get_slot('time')['grain']
        #deadline["from"] =time["from"].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        #deadline["to"] = time["to"].strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        #deadline['from']= dt.strptime(time['from'], "%Y-%m-%dT%H:%M:%S.%f%z")
        #deadline['to']= dt.strptime(time['to'], "%Y-%m-%dT%H:%M:%S.%f%z")
        #deadline["to"] = dt.strptime(str(time["to"]), "%Y-%m-%dT%H:%M:%S.%f%z")
        #deadline["from"] = dt.strptime(str(time["from"]), "%Y-%m-%dT%H:%M:%S.%f%z")
        #dispatcher.utter_message("Deadline slot set")
        if(type(time) is dict):
            if (time["to"]!=None):
                deadline["to"] = dt.strptime(str(time["to"]), "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%H:%M:%S %d %b %Y")
            if (time["from"]!=None):
                deadline["from"] = dt.strptime(str(time["from"]), "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%H:%M:%S %d %b %Y")
            return [SlotSet(key='deadline', value=deadline),SlotSet(key='deadline_2', value=deadline)]
        elif(time!=None):
            time=dt.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%H:%M:%S %d %b %Y")
            return [SlotSet(key='deadline', value=time),SlotSet(key='deadline_2', value=time)]
        else:
            return [SlotSet(key='deadline', value=time),SlotSet(key='deadline_2', value=time)]

        #return [SlotSet(key='deadline', value=time),SlotSet(key='deadline_2', value=time)]

class ActionGetActionItemText(Action):
    def name(self) -> Text:
        return 'action_get_action_item_text'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.latest_message.get("text")
        dispatcher.utter_message("Action Item Text slot set")
        return [SlotSet(key='action_item_text', value=text)]

class ActionGetActionItemId(Action):
    def name(self) -> Text:
        return 'action_get_action_item_id'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_ind=len(action_items)-1
        id=int(action_items[last_ind]['id'])+1
        dispatcher.utter_message("Action Item id updated!")
        return [SlotSet(key='action_item_id', value=str(id)),SlotSet(key='action_item_id_2',value=str(id))]


class ActionGetTalkingPointText(Action):
    def name(self) -> Text:
        return 'action_get_talking_point_text'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text=tracker.latest_message.get("text")
        dispatcher.utter_message("Talking Point Text slot set")
        return [SlotSet(key='talking_point_text', value=text)]

class ActionGetTalkingPointId(Action):
    def name(self) -> Text:
        return 'action_get_talking_point_id'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        last_ind=len(talking_points)-1
        id=int(talking_points[last_ind]['id'])+1
        dispatcher.utter_message("Talking point id updated!")
        return [SlotSet(key='talking_point_id', value=str(id)), SlotSet(key='talking_point_id_2', value=str(id))]


class ActionResetSlots(Action):
     def name(self) -> Text:
            return "action_reset_slots"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("All slots have been reset")

         return [AllSlotsReset()]

class DisplayTalkingPoints(Action):
    def name(self) -> Text:
        return 'display_talking_points'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for talking_point in talking_points:
            id_str="Id : "+talking_point['id']
            text_str="Notes : "+talking_point['notes']
            dispatcher.utter_message(id_str)
            dispatcher.utter_message(text_str)

class DisplayActionItems(Action):
    def name(self) -> Text:
        return 'display_action_items'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for action_item in action_items:
            id_str="Id : "+action_item['id']
            text_str="Text : "+action_item['text']
            str1=""
            for owner in action_item['owners']:
                str1+=owner+" , "
            owner_str="Owners : "+str1
            deadline_str="Deadline : "+str(action_item['deadline'])
            time_str="Time : "+str(tracker.get_slot('time'))
            dispatcher.utter_message(id_str)
            dispatcher.utter_message(text_str)
            dispatcher.utter_message(owner_str)
            dispatcher.utter_message(deadline_str)
            dispatcher.utter_message(time_str)

class GetId(Action):
    def name(self) -> Text:
        return 'action_get_id'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #id=tracker.latest_message.get("text")
        id=tracker.latest_message.get("entities")
        dispatcher.utter_message(tracker.latest_message.get("entities"))
        return[SlotSet(key="id",value=str(id))]

#class AskField(Action):
    #def name(self) -> Text:
        #return 'action_ask_field'

    #async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(buttons = [
                #{"payload": "/text", "title": "Text"},
                #{"payload": "/owners", "title": "Owners"},
                #{"payload": "/deadline", "title": "Deadline"},
            #])
        #return[]

#class GetField(Action):
    #def name(self) -> Text:
        #return 'action_get_field'

    #async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #field=tracker.latest_message.get("text")
        #return[SlotSet(key="field",value=field)]


class GetNewTalkingPointText(Action):
    def name(self) -> Text:
        return 'action_get_new_talking_point_text'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new=tracker.latest_message.get("text")
        return[SlotSet(key="new_talking_point_text",value=new)]


class EditTalkingPoint(Action):
    def name(self) -> Text:
        return 'action_edit_talking_point'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id=tracker.get_slot('talking_point_id_modify')
        new_notes=tracker.get_slot('new_talking_point_text')
        for t in talking_points:
            if t['id']==str(id):
                t['notes']=str(new_notes)
                dispatcher.utter_message("Talking point edited successfully!")
                return[]

        dispatcher.utter_message("Please enter a valid ID")
        return[SlotSet(key='talking_point_id_modify',value=None)]

class DeleteTalkingPoint(Action):
    def name(self) -> Text:
        return 'action_delete_talking_point'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id=tracker.get_slot('id')
        for t in talking_points:
            if t['id']==str(id):
                talking_points.remove(t)
                dispatcher.utter_message("Talking point deleted successfully!")
                return[]
        dispatcher.utter_message("Please enter a valid ID")
        return[SlotSet(key='id',value=None)]

class AskNewFieldValue(Action):
    def name(self) -> Text:
        return 'action_ask_new_field_value'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        field=tracker.get_slot('field')
        if str(field).lower()=="owners":
            dispatcher.utter_message("Enter new owners")
        elif str(field).lower()=="deadline":
            dispatcher.utter_message("Enter updated deadline")
        elif str(field).lower()=="text":
            dispatcher.utter_message("Enter updated text")
        else:
            dispatcher.utter_message("No such field exists")
        return[]

class GetNewFieldValue(Action):
    def name(self) -> Text:
        return 'action_get_new_field_value'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        new_field_value=tracker.get_slot('field')
        return[SlotSet(key="new_field_value",value=new_field_value)]    

class EditActionItem(Action):
    def name(self) -> Text:
        return 'action_edit_action_item'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id=tracker.get_slot('action_item_id_modify')
        field=tracker.get_slot('field')
        new_field_value=tracker.get_slot('new_field_value')
        for a in action_items:
            if field.lower() not in list(a.keys()):
                dispatcher.utter_message("Please enter a valid field")
                return[SlotSet(key='field',value=None)]
            if field.lower()=="owners":
                owners=tracker.get_latest_entity_values("owner")
                owner_list=[]
                for owner in owners:
                    owner_list.append(owner)
                a[field].clear()
                a[field]=owner_list
                return[]
            if a['id']==str(id):
                a[field.lower()]=str(new_field_value)
                dispatcher.utter_message("Action Item edited successfully!")
                return[]

        dispatcher.utter_message("Please enter a valid ID")
        return[SlotSet(key='action_item_id_modify',value=None)]
        

class DeleteActionItem(Action):
    def name(self) -> Text:
        return 'action_delete_action_item'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id=tracker.get_slot('id')
        for a in action_items:
            if a['id']==str(id):
                action_items.remove(a)
                dispatcher.utter_message("Action Item deleted successfully!")
                return[]
        dispatcher.utter_message("Please enter a valid ID")
        return[SlotSet(key='id',value=None)]

#Action Get New Field Values
#Action Get New Talking Point Values
class ValidateDeadline(Action):
    def name(self) -> Text:
        return 'action_validate_deadline'

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        deadline=tracker.get_slot("deadline")
        deadline_2=tracker.get_slot("deadline_2")
        if(deadline==None or deadline_2==None):
            dispatcher.utter_message("Please provide deadline")
        else:
            dispatcher.utter_message("Deadline was already provided")