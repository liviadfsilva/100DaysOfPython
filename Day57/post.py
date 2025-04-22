import requests

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.url)
        self.data = self.response.json()
        
    def show_post(self, url_id):
        for i in self.data:
            if i["id"] == url_id:
                return {
                    "title": i["title"],
                    "subtitle": i["subtitle"],
                    "body": i["body"]
                }