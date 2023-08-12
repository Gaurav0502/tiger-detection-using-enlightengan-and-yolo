# Module used for Google Image Search API.
from google_images_search import GoogleImagesSearch

# Modules used for handling environment variables.
from dotenv import load_dotenv
import os

class CollectImages:

    def __init__(self, search_query: str, path_to_save: str, num_images: int):
        load_dotenv()
        self.gis = GoogleImagesSearch(os.getenv("API_KEY"), os.getenv("GC_CX"))
        self.path_to_save = path_to_save
        self.search_query = search_query
        self.num_images = num_images
    
    def __construct_search_query(self):
        self.search_params = {
            'q': self.search_query,
            'num': self.num_images,
        }

    def search_and_download(self):
        self.__construct_search_query()
        self.gis.search(search_params=self.search_params, path_to_dir=self.path_to_save)

data_collector = CollectImages('tiger images by wildlife photographers', './images', 1)
data_collector.search_and_download()