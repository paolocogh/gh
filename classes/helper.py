import xml.etree.ElementTree as ET
import re
import polling2
import logging

class Helper:
    #Helper functions for AlgoHelper. Segrated so only AlgoHelper methods are used at the script level
    def __init__(self):
        pass

    def save_soap_message(self, obj):
        pass

    def soap_to_ElementTree(self, soap_message):
        root = ET.fromstring(soap_message)
        return root

    def get_soap_envelope(self, raw_text):
        soapEnvenlope = re.search(r'<s:Envelope.*s:Envelope>', raw_text)[0]
        return soapEnvenlope

    def ET_get_text(self, root, xpath):
        element = root.findall(xpath)
        element_texts = []
        for i in range(len(element)):
            element_texts.append(element[i].text)
        return element_texts #returns a list

class AlgoHelper:
    #Methods used at script level
    def __init__(self):
        pass

    def from_response_get_XML_text(self, response, xpath):
        helper = Helper()
        soap_envelope = helper.get_soap_envelope(response)
        soap_envelope_xml = helper.soap_to_ElementTree(soap_envelope)
        text = helper.ET_get_text(soap_envelope_xml, xpath)
        return text #? Best practice to return a single item or a list of one that must be indexed 
    
    def from_response_get_algorithmId(self, response):
        algorithm_id = self.from_response_get_XML_text(response, ".//algorithmId")
        return algorithm_id[0]

    def from_response_get_analysisRequestId(self, response):
        analysisRequestId = self.from_response_get_XML_text(response, ".//analysisRequestId")
        return analysisRequestId[0]

    def from_response_get_percentCompleted(self, response):
        percentCompleted = self.from_response_get_XML_text(response, ".//percentCompleted")
        return percentCompleted[0]
    
    def from_response_get_errorCode(self, response):
        errorCode = self.from_response_get_XML_text(response, ".//{http://hostname.com/imageAnalysis/definitions}ErrorCode")
        return errorCode[0]
    
    def is_percentCompleted_100(self, response):
        percentCompleted = self.from_response_get_percentCompleted(response)
        return "100" in percentCompleted
    
    def polling(self,client, analysisRequestId):
        
        polling2.poll(lambda: client(analysisRequestId).decode(), 
                      check_success=self.is_percentCompleted_100,
                      step = 5,             #poll every 5 seconds
                      timeout=600,          #timeout after 5 mins
                      log=logging.INFO)     #logs


