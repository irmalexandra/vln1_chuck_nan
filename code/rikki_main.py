from logic_layer.LLAPI import LLAPI
from logic_layer.LLVoyages import LLVoyages
from models.Voyage import Voyage
from models.ModelAPI import ModelAPI
from data_layer.DLAPI import DLAPI

newDLAPI = DLAPI()
newMODELAPI = ModelAPI()

newDate = "20-12-2020"
newVoyage = Voyage()
newVoyage.set_destination("Nuuk")
newLLVoy = LLVoyages(newDLAPI, newMODELAPI)

newLLVoy.duplicate_voyage(newVoyage,newDate)