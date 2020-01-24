import requests
from smoke.classes.properties import Properties

class Ims:
    def __init__(self, ims_ip = Properties.ims_ip, image_folder_path=Properties.ims_image_folder_path):
        self.ip = ims_ip #eg. http://141.167.70.135:85
        self.image_folder_path = image_folder_path #eg. http://141.167.70.135:85/DP200/BP%202.0/HER2/TestData/

    def set_image_folder_path(self, image_folder_path):
        self.image_folder_path = image_folder_path
        #eg. "http://141.167.70.135:85/DP200/BP%202.0/HER2/TestData/

    def get_image_id(self, image_name=None):
        api_request = "?getimageid"
        url = self.image_folder_path + image_name + api_request 
        #eg. "http://141.167.70.135:85/DP200/BP%202.0/HER2/TestData/D117412_HER2SC1_V010_XHER2.bif?getimageid"
        response = requests.get(url)

        return response.text.strip()