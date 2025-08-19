import requests

from .. import PROMPT_MANAGER_SERVICE_URL

def add_topic_name(topic_name):
    res = requests.post(
        url=f"{PROMPT_MANAGER_SERVICE_URL}/add_topic",
        params={"topic": topic_name}
    )
    return res.json()