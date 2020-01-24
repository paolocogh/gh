import time
import pytest

from smoke.classes.plugins import _AttributePlugin
from smoke.classes.properties import Properties
from smoke.classes.algorithms import GenericAlgoClient
from smoke.classes.helper import AlgoHelper 
from smoke.classes.ims import Ims 

def test_getAlgorithm2():

    algorithm = GenericAlgoClient()
    helper = AlgoHelper()
    ims = Ims()
    image_name = "D117412_HER2SC1_V010_XHER2.bif"
    #image_folder_path = "/DP200/BP%202.0/HER2/TestData/"

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

    #GetAnalysisProgress
    time.sleep(2)
    response = algorithm.GetAnalysisProgress(token)
    print(response.decode())

    #Poll until 100 percent completed
    helper.polling(algorithm.GetAnalysisProgress,token)

    #GetAnalysisProgress at 100 percent
    response = algorithm.GetAnalysisProgress(token)
    percent_completed = helper.from_response_get_percentCompleted(response.decode())
    print(response.decode())

    #GetAnalysisResult
    response = algorithm.GetAnalysisResult(token)
    print(response.decode())

    #Stop analysis
    #time.sleep(60)
    #response = algorithm.StopAnalysis(token)
    #print(response.decode())

        


