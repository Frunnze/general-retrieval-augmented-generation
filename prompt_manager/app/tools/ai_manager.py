import json

from .. import openai


def get_ai_res_with_context(conv_his, context, user_msg):
    system_prompt = f"""
    ##Role##
    You are an expert in answering questions strictly based on some material.

    ##Task##
    Your task is to answer the user question based on the "Documents" in the "Context" section.
    Also, consider the "Conversation history". Strictly output the answer as specified in "Output" section.

    ##Context##:
    - Documents: ```{context}```
    - Conversation history: ```{conv_his}```

    """

    output = """
    ##Output##
    JSON```
    {
        "answer": string
    }
    ```
    """
    system_prompt += output
    return get_ai_res(system_prompt, user_msg)


def get_ai_res(system_prompt, user_prompt, model="gpt-5-nano"):
    print("get_ai_res", system_prompt, user_prompt)
    res = openai.responses.create(
        model=model,
        input=[
            {
                "role": "assistant",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"User question: {user_prompt}."
            }
        ]
    )
    return get_dict_from_text(res.output_text).get("answer")


def get_dict_from_text(text):
    curl1 = text.find("{")
    curl2 = text.find("}")
    return json.loads(text[curl1:curl2+1])