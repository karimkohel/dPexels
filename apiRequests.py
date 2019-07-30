# This scripts handles the retrival part of the api

################ IMPORTS ####################

from pypexels import PyPexels
import requests

##############################################

search_urls = list()

############# main ###########################

# function that retrieves list of all urls from api from a giving string
def execute_search(key, string, pages):

    pexels_instance = PyPexels(api_key=key)
    search_results = pexels_instance.search(query=string, per_page=pages)

    while True:
        for image in search_results.entries:
            search_urls.append(image.url)
        if not search_results.has_next:
            break
        search_results = search_results.get_next_page()

#function that downloads images on a certain path
def download_images(urls, path):
    for url in urls:
        img_name = path + url.split('/')[4]
        img = requests.get(url).content
        with open(img_name, 'wb') as image:
            image.write(img)

###############################################