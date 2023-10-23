from firebase_functions import https_fn, options
from firebase_admin import initialize_app
from utils import *
import requests
import json

from nlp_api import rate_comment, rate_post

initialize_app()


@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=[
            r"http://localhost:3000",
        ],
        cors_methods=["get", "post"],
    ),
    timeout_sec=120,
)
def get_user(req: https_fn.Request) -> https_fn.Response:
    username = req.args.get("username")
    if username:
        user = get_user_by_username(username)
    else:
        id = req.args.get("id")
        if id:
            user = get_user_by_id(id)
        else:
            return https_fn.Response("No username or id provided", status=400)
    return https_fn.Response(json.dumps(user))

# get instagram posts by username
@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=[
            r"http://localhost:3000",
        ],
        cors_methods=["get", "post"],
    ),
    timeout_sec=120,
)
def get_posts(req: https_fn.Request) -> https_fn.Response:
    username = req.args.get("username")
    posts = get_media_by_username(username)
    return https_fn.Response(posts)
def get_rating(req: https_fn.Request) -> https_fn.Response:
    text = req.args.get("text")
    text_type = req.args.get("type")
    rating = None
    if text_type == "post":
        rating = rate_post(text)
    elif text_type == "comment":
        rating = rate_comment(text)
    else:
        return https_fn.Response("Invalid text_type", status=400)

    return https_fn.Response(rating)