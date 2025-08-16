from fastapi import APIRouter
from typing import Optional
import traceback

from ..tools.ai_manager import get_ai_res_with_context
from ..tools.chroma import get_context

ai_res_router = APIRouter()

@ai_res_router.post("/ai_res_with_context")
async def ai_res(topics: list, user_msg: str, conv_history: Optional[list] = None):
    try:
        # Get the context (docs) from db
        context = get_context(topics, user_msg)

        # Get ai response
        ai_res = get_ai_res_with_context(conv_history, context, user_msg)

        # Return the response
        return {"ai_res": ai_res}
    except Exception as e:
        print(e)
        traceback.print_exc()
        return {"msg": "Server error"}, 500