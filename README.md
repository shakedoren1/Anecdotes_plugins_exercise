## DummyApiPlugin
This project provides a DummyApiPlugin class that interacts with the DummyJSON API to authenticate, collect user details, posts, and comments.

### Features
**Authentication:** Connect to the DummyJSON API using provided credentials. <br>
**Data Collection:** Fetch user details, posts, and comments. <br>
**Error Handling:** Handle various error scenarios such as invalid credentials or failed data retrieval.

### Running instructions
Simply running main.py. <br>
In the current state it will connect using <br>
username: emilys, password: emilyspass (which are valid credentials) <br>
and run the function collect(). <br>
To see the output of the function it is possible to uncomment the rest of the code in main(). This code demonstrate the actions of both check_connectivity() and collect() by trying to connect with valid and invalid credentials and printing the returned values.

### Functions
*connectivity_test(self)-* Tests connectivity by trying to authenticate with the provided credentials. <br>
Returns: (bool) True if authentication is successful, False otherwise. <br><br>

*collect(self)-* Collects the necessary evidences from DummyJSON API. <br>
Returns: (list) List of collected evidences. <br><br>

*fetch_user_details(self)-* Fetches the user details based on the authenticated token. <br>
Returns: (dict) User details if successful, None otherwise. <br><br>

*fetch_posts(self,num_of_posts)-* Fetches the received number of posts from the system. <br>
Parameters: (int) Number of posts to fetch. <br>
Returns: (list) List of posts if successful, None otherwise. <br><br>

*fetch_posts_with_comments(self,num_of_posts)-* Fetches the received number of posts with their comments from the system. <br>
Parameters: (int) Number of posts to fetch. <br>
Returns: (list) List of posts with comments if successful, None otherwise. <br><br>