import urllib, os 

class Properties:

    wsdl_location = urllib.parse.urljoin('file:', urllib.request.pathname2url(os.path.abspath(r".\wsdl\ImageAnalysisDefinitions.wsdl")))
    endpoint = 'http://10.21.1.254:9184/imageAnalysis/service/breastpanel/her2ruo'
    ims_ip = "http://141.167.70.135:85"
    ims_image_folder_path = "http://141.167.70.135:85/DP200/BP%202.0/HER2/TestData/"



