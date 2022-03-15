import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/deactivate/"

SAMPLE_USER = {
    "first_name": "Bill",
    "last_name": "Gates",
    "hobbies": "Surfing",
}

def deactivate_user(user_id):
    url = "%s%s" % (URL, user_id)
    response = requests.put(url)
    if response.status_code == 204:
        print("User deleted")
    else:
        print("User not deleted")




if __name__ == "__main__":
    print("DELETE USER")
    print("-------------")
    user_data = input("Type in the desired user id:")
    deactivate_user(int(user_data))