from fastapi import APIRouter
from typing import Optional
import traceback
from pydantic import BaseModel

from ..tools.ai_manager import get_ai_res_with_context
from ..tools.chroma import get_context


ai_res_router = APIRouter()

class AIRes(BaseModel):
    topics: list
    user_msg: str
    conv_history: Optional[list] = None

@ai_res_router.post("/ai_res_with_context")
async def ai_res(data: AIRes):
    try:
        # Get the context (docs) from db
        context = get_context(
            topics=data.topics, 
            text=data.user_msg
        )

        # Get ai response
        ai_res = get_ai_res_with_context(
            conv_his=data.conv_history, 
            context=context, 
            user_msg=data.user_msg
        )

        # Return the response
        return {"ai_res": ai_res}
    except Exception as e:
        print(e)
        traceback.print_exc()
        return {"msg": "Server error"}, 500