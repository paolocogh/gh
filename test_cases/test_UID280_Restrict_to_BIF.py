import time
import pytest
from smoke.classes.plugins import _AttributePlugin
from smoke.classes.properties import Properties
from smoke.classes.algorithms import GenericAlgoClient
from smoke.classes.helper import AlgoHelper 


@pytest.mark.smoke
def test_UID280_Restrict_to_BIF():

    algorithm = GenericAlgoClient(Properties.endpoint)
    helper = AlgoHelper()
    
    """
    Get magnification: 
            <supportedImageFormats>
                <data>BIF</data>
            </supportedImageFormats>
    """
    response = algorithm.GetAlgorithmInformation()
    supportedImageFormats = helper.from_response_get_XML_text(response.decode(),".//supportedImageFormats/data")[0]
    assert(supportedImageFormats == "BIF")