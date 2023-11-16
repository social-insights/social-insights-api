from firebase_functions import https_fn, options
from firebase_admin import initialize_app
from utils import *
import requests
import json

from nltk.sentiment import SentimentIntensityAnalyzer
from PIL import Image
from image_sentiment import predict
import db

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

@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=[
            r"http://localhost:3000",
        ],
        cors_methods=["get", "post"],
    ),
    timeout_sec=120,
)
def get_rating(req: https_fn.Request) -> https_fn.Response:
    text = req.args.get("text")
    # text_type = req.args.get("type")

    sia = SentimentIntensityAnalyzer()
    rating = str(sia.polarity_scores(text)["compound"])

    return https_fn.Response(rating)

@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=[
            r"http://localhost:3000",
        ],
        cors_methods=["get", "post"],
    ),
    timeout_sec=120,
)
def get_image_rating(req: https_fn.Request) -> https_fn.Response:
    image = req.files.get("image")
    # text_type = req.args.get("type")

    # sia = SentimentIntensityAnalyzer()
    # rating = str(sia.polarity_scores(text)["compound"])

    image = Image.open(image)
    res = predict(image)

    return https_fn.Response(res)

@https_fn.on_request(
    cors=options.CorsOptions(
        cors_origins=[
            r"http://localhost:3000",
        ],
        cors_methods=["get", "post"],
    ),
    timeout_sec=120,
)
def update_posts_database(req: https_fn.Request) -> https_fn.Response:
    username = req.args.get("username")
    posts = get_media_by_username(username)
    most_recent_post_date = db.get_most_recent_post_date(username)
    client = db.get_client()
    for post in posts:
        #   TODO: Delete duplicate posts
        if post["date"] < most_recent_post_date:
            continue
        db.insert_post(client, post)

def test():
    username = "nba"
    posts = get_media_by_username(username)
    return posts