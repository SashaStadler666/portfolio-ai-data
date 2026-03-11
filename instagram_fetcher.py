import requests
import json

def get_instagram_profile(username):
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "x-ig-app-id": "936619743392459"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Could not fetch profile"}

    data = response.json()

    user = data["data"]["user"]

    return {
        "username": user["username"],
        "full_name": user["full_name"],
        "bio": user["biography"],
        "followers": user["edge_followed_by"]["count"],
        "posts": user["edge_owner_to_timeline_media"]["count"],
        "profile_pic": user["profile_pic_url_hd"]
    }


def fetch_all_profiles():
    usernames = [
        "bobtryingtomakeart",
        "shell.lab"
    ]

    profiles = {}

    for username in usernames:
        profiles[username] = get_instagram_profile(username)

    with open("profiles.json", "w") as f:
        json.dump(profiles, f, indent=4)


if __name__ == "__main__":
    fetch_all_profiles()