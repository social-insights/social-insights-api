import instaloader
import credentials

class User:
    def __init__(self, obj: instaloader.Profile):
        self.username = obj.username
        self.bio = obj.biography
        self.full_name = obj.full_name
        self.id = obj.userid
        self.followers = obj.followers
        self.following = obj.followees
        self.profile_pic_url = obj.profile_pic_url
        self.private = obj.is_private
        
    def get_basic(self):
        return {
            "username": self.username,
            "bio": self.bio,
            "full_name": self.full_name,
            "id": self.id,
            "private": self.private,
        }
        
    def get_all(self):
        return {
            "username": self.username,
            "bio": self.bio,
            "full_name": self.full_name,
            "id": self.id,
            "followers": self.followers,
            "following": self.following,
            "profile_pic_url": self.profile_pic_url,
            "private": self.private,
        }

def get_user_by_username(username):
    L = instaloader.Instaloader()
    L.login(credentials.username, credentials.password)
    profile = instaloader.Profile.from_username(L.context, username)

    u = User(profile)
    return u.get_all()

def get_user_by_id(id):
    L = instaloader.Instaloader()
    L.login(credentials.username, credentials.password)
    profile = instaloader.Profile.from_id(L.context, id)

    u = User(profile)
    return u.get_all()

def get_media_by_username(username):
    L = instaloader.Instaloader()
    L.login(credentials.username, credentials.password)
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.get_posts()._query()