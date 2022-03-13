import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users/"

SAMPLE_USER = {
    "first_name": "Bill",
    "last_name": "Gates",
    "hobbies": "Surfing",
}
def get_user():
    user_id = input("Type in the desired user id:")
    url = "%s%s" % (URL, user_id)
    response = requests.get(url)
    user = {}
    if response.status_code == 200:
        response_json = response.json()
        user = response_json["user"][0]
        print("User:")
        pprint(user)
    else:
        print("Error while trying to retrieve user.")
    return user.get("id")


def deactivate_user(user_id):
    url = "%s%s" % (URL, user_id)
    response = requests.put(url)
    if response.status_code == 200:
        print("User deleted")
    else:
        print("User not deleted")




if __name__ == "__main__":
    print("DELETE USER")
    print("-------------")
    user_id = get_user()
    deactivate_user(user_id)