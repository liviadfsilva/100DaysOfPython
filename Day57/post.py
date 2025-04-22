import requests

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.url)
        self.data = self.response.json()
        
    #     def home():
    # blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    # blog_response = requests.get(blog_url)
    # blog_data = blog_response.json()
    # return render_template("index.html", posts=blog_data)