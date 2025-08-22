import requests

from .. import PROMPT_MANAGER_SERVICE_URL


def get_ai_res(topics, user_msg, conv_hist=None):
    res = requests.post(
        url=f"{PROMPT_MANAGER_SERVICE_URL}/ai_res_with_context",
        json={
            "topics": topics,
            "user_msg": user_msg,
            "conv_hist": conv_hist
        }
    )
    return res.json().get("ai_res")