import requests
from plugin import Plugin


class DummyApiPlugin(Plugin):
    def __init__(self, username, password):
        """
        Initializes the plugin with the given username and password.
        """
        self.username = username
        self.password = password
        self.token = None

    def connectivity_test(self):
        """
        Tests connectivity by trying to authenticate with the provided credentials.
        """
        url = "https://dummyjson.com/auth/login"
        headers = {'Content-Type': 'application/json'}
        body = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            # Store the token for subsequent authenticated requests
            self.token = response.json().get('token')
            return True
        elif response.status_code == 400:
            print("Error: Received status code 400. Invalid credentials.")
        else:
            print(f"Error: Received status code {response.status_code}. Check credentials.")
        return False
    
    def collect(self):
        """
        Collects the necessary evidences from DummyJSON API.
        """
        if not self.token:
            print("Error: No token available. Cannot collect data without authentication.")
            return
        
        evidences = []
        # Append the required evidences to the evidences list
        evidences.append(self.fetch_user_details())
        evidences.append(self.fetch_posts(60))
        evidences.append(self.fetch_posts_with_comments(60))

        return evidences
    
    def fetch_user_details(self):
        """
        Fetches the user details based on the authenticated token.
        """
        url = "https://dummyjson.com/auth/me"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Failed to fetch user details. Status code {response.status_code}")
            return
        
    def fetch_posts(self,num_of_posts):
        """
        Fetches the received number of posts from the system.
        """
        posts_url = f"https://dummyjson.com/posts?limit={num_of_posts}"
        posts_response = requests.get(posts_url)
        
        if posts_response.status_code == 200:
            posts = posts_response.json().get("posts", [])
            return posts
        else:
            print(f"Error: Failed to fetch posts. Status code {posts_response.status_code}")
            return
        
    def fetch_posts_with_comments(self,num_of_posts):
        """
        Fetches the received number of posts with their comments from the system.
        """
        posts = self.fetch_posts(num_of_posts)
        # Insert comments for each post
        for post in posts:
            post_id = post.get("id")
            comments_url = f"https://dummyjson.com/posts/{post_id}/comments"
            comments_response = requests.get(comments_url)
            if comments_response.status_code == 200:
                comments = comments_response.json().get("comments", [])
                post["comments"] = comments
            else:
                print(f"Error: Failed to fetch comments for post {post_id}. Status code {comments_response.status_code}")
                return
        return posts
