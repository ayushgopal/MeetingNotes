from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config


train_data = load_data('config.json')
trainer = Trainer(config.load("config_spacy.yaml"))
trainer.train(train_data)
model_directory = trainer.persist('/projects/')
import spacy
nlp = spacy.load('en_core_web_sm')
docx = nlp("I am looking for an Italian Restaurant where I can eat")
for word in docx.ents:
    print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)
from rasa_nlu.model import Metadata,Interpreter
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory)
text="Let's meet tomorrow"
interpreter.parse(text)
