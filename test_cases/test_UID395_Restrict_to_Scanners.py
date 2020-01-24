import time
import pytest
from smoke.classes.plugins import _AttributePlugin
from smoke.classes.properties import Properties
from smoke.classes.algorithms import GenericAlgoClient
from smoke.classes.helper import AlgoHelper 
from smoke.classes.ims import Ims 

@pytest.mark.smoke
def test_UID395_Restrict_to_Scanners():

    #Data
    algorithm = GenericAlgoClient(Properties.endpoint)
    helper = AlgoHelper()
    
    #Get magnification: <supportedScanners>VENTANA DP 200</supportedScanners>
    response = algorithm.GetAlgorithmInformation()
    supportedScanners = helper.from_response_get_XML_text(response.decode(),".//supportedScanners/data")[0]
    assert(supportedScanners == "VENTANA DP 200")


