from supabase import Client
from datetime import datetime

def get_client():
    return Client(
        # TODO: Find another way to save this stuff
        supabase_url="https://qrvjjjgsxrciauibjpmq.supabase.co",
        supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFydmpqamdzeHJjaWF1aWJqcG1xIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE2MjIxNywiZXhwIjoyMDEwNzM4MjE3fQ.5eZ0gIidXEcNpPmWDtKs5f4cXDvLMYVQGkKN58KLO1I"
    )

def get_most_recent_post():
    client = get_client()
    posts = client.table("Posts").select("*").order("created_at", desc=True).execute()
    if len(posts.data) > 0:
        return posts.data[0]
    else:
        return None

def get_most_recent_post_date():
    post = get_most_recent_post()
    if post:
        return datetime.strptime(post["created_at"].split('T')[0], "%Y-%m-%d")
    else:
        return None

def insert_post(client, post):
    client.table("Posts").insert([post]).execute()