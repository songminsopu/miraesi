import openai
import os
import asyncio

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


openai.api_key = os.getenv('OPENAI_API_KEY')

async def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = await openai.ChatCompletion.acreate(
        model=model,
        messages=messages,
        temperature=0
    )
    # return response.choices[0].message["content"]
    print(response.choices[0].message["content"])

text = f"""
['팔굽혀펴기 100번 윗몸일으키기 100번, 스쿼트 100번.', "내' 직감이 대음 '' 으 그리고 달리기 10km. 이걸 매일 하는 거야!", "위험 신호를 '리고' 있어!'", '아?']
"""

prompt = f"""
다음 작업을 수행하세요:

```으로 구분된 배열 속의 대사를 활용하여 새로운 소설을 작성하세요.

배열: ```{text}```
"""

# response = get_completion(prompt=prompt)
asyncio.run(get_completion(prompt=prompt))
# print(response)