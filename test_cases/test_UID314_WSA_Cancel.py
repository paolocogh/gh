import time
import pytest
from smoke.classes.properties import Properties
from smoke.classes.algorithms import GenericAlgoClient
from smoke.classes.helper import AlgoHelper 
from smoke.classes.ims import Ims 

@pytest.mark.smoke
def test_UID314_WSA_Cancel():

    #Data
    algorithm = GenericAlgoClient(Properties.endpoint)
    helper = AlgoHelper()
    ims = Ims()
    image_name = "D117412_HER2SC1_V010_XHER2.bif"
    
    #Get IMS image id
    image_id = ims.get_image_id(image_name)
    
    #Get algorithm information
    response = algorithm.GetAlgorithmInformation()
    algorithm_id = helper.from_response_get_algorithmId(response.decode())
    
    #Delete preexisting analysis  before starting 
    response = algorithm.DeleteAnalysisResult(image_id, algorithm_id)
    print(response.decode())
    
    #Start analysis
    response = algorithm.StartAnalysis(image_id, algorithm_id)
    token = helper.from_response_get_analysisRequestId(response.decode())
    print(response.decode())
    print("token is {}".format(token))

    #Stop analysis
    response = algorithm.StopAnalysis(token)
    print(response.decode())

    #sleep 
    time.sleep(2)

    #GetAnalysisResult and ErrorCode
    try:
        response = algorithm.GetAnalysisResult(token)
    except:
        #todo filter was edited
        assert(response(0) == "500") #this is the server error code
        last_response = algorithm.client.last_received()
        errorCode = helper.from_response_get_errorCode(last_response.plain()) #last_response.plain() is the soap xml
        assert(errorCode == "-5")
