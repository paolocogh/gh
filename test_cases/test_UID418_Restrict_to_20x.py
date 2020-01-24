import time
import pytest
from smoke.classes.plugins import _AttributePlugin
from smoke.classes.properties import Properties
from smoke.classes.algorithms import GenericAlgoClient
from smoke.classes.helper import AlgoHelper 
from smoke.classes.ims import Ims 

@pytest.mark.smoke
def test_UID418_Restrict_to_20x():

    #Data
    algorithm = GenericAlgoClient(Properties.endpoint)
    helper = AlgoHelper()
    
    #Get magnification: <supportedMagnification>20</supportedMagnification>
    response = algorithm.GetAlgorithmInformation()
    supportedMagnification = helper.from_response_get_XML_text(response.decode(),".//supportedMagnification")[0]
    assert(supportedMagnification == "20")