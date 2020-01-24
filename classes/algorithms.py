from smoke.classes.properties import Properties
from suds.client import Client as ClientSuds
from suds.sax.attribute import Attribute
from suds.plugin import MessagePlugin

class _AttributePlugin(MessagePlugin):
    """
    Suds plug-in extending the method call with arbitrary attributes.
    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def marshalled(self, context):
        method = context.envelope.getChild('Body')[0]
        for key, item in self.kwargs.items():
            method.attributes.append(Attribute(key, item))

class GenericAlgoClient:

    def __init__(self, endpoint = Properties.endpoint):
        self.headers = {
        "Accept-Encoding": "gzip,deflate",
        "Content-Type": "text/xml;charset=UTF-8",
        "SOAPAction": "\"http://hostname.com/imageAnalysis/GetAlgorithmInformation\"",
        "Connection": "Keep-Alive"
        }
        self.endpoint = endpoint
        self.client = ClientSuds(Properties.wsdl_location, location=self.endpoint, faults=False, retxml=True)
        self.client.set_options(headers=self.headers)

    def DeleteAnalysisResult(self, image_id, algorithmId):
        image = self.client.factory.create('ns1:Image')
        image.imsInfo.url = Properties.ims_ip 
        image.imageId = image_id
        self.client.options.plugins = [_AttributePlugin(algorithmId=algorithmId)]
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/DeleteAnalysisResult\""
        response = self.client.service.DeleteAnalysisResult(image)
        #remove plugin after the request or algorithmId will be populated in subsequent calls
        self.client.options.plugins = []
        return response

    def GetAlgorithmInformation(self):
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/GetAlgorithmInformation\""
        response = self.client.service.GetAlgorithmInformation()
        return response

    def StartAnalysis(self, image_id, algorithmId):
        StartAnalysisImage = self.client.factory.create('ns1:Image')
        StartAnalysisImage.imsInfo.url = Properties.ims_ip 
        StartAnalysisImage.imageId = image_id
        ParameterGroup = self.client.factory.create('ns1:ParameterGroup')
        self.client.options.plugins = [_AttributePlugin(algorithmId=algorithmId)]
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/StartAnalysis\""
        response = self.client.service.StartAnalysis(StartAnalysisImage, ParameterGroup, "true")
        #remove plugin after the request or algorithmId will be populated in subsequent calls
        self.client.options.plugins = []
        return response

    def StopAnalysis(self,analysisRequestId):
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/StopAnalysis\""
        response = self.client.service.StopAnalysis(analysisRequestId)
        return response

    def GetAnalysisProgress(self,analysisRequestId):
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/GetAnalysisProgress\""
        response = self.client.service.GetAnalysisProgress(analysisRequestId)
        return response
    
    def GetAnalysisResult(self,analysisRequestId):
        self.headers["SOAPAction"] = "\"http://hostname.com/imageAnalysis/GetAnalysisResult\""
        response = self.client.service.GetAnalysisResult(analysisRequestId)
        return response

class Her2AlgoClient:
    def __init__(self, name):
        pass
        #TODO: Inherit from GenericAlgoClient