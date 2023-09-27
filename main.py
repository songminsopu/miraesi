import openai
import os
import asyncio

from dotenv import load_dotenv, find_dotenv

from pororoOcr import PororoOcr

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

    return response.choices[0].message["content"]
    

ocr = PororoOcr()

image_path = input("Enter image path: ")
ocr_lst = ocr.run_ocr(image_path, debug=False)

lst_text = ""

for idx, text in enumerate(ocr_lst, 1):
    # lst_text += f"{idx}. {text}\n"
    lst_text += f"{text}\n"

prompt = f"""
다음 작업을 수행하세요:

```
{lst_text}```

```로 구분된 텍스트를 분석하여 창의적인 뒷이야기를 500자로 구체적이고, 자연스럽게 작성하세요.
그리고 작성중에 어색한 문장이나 단어라고 생각되면 고치세요.

다음 형식을 사용하세요:
{{
    title: <소설의 제목>
    content: <소설의 내용>
}}
"""

# prompt = f"""
# 다음 작업을 수행하세요:

# {lst_text}

# 위에 순서대로 나열된 대사를 분석하여 이 이야기의 결말을 대사와 비슷한 말투와 500자로 자연스럽게 작성하세요.
# 그리고 작성중에 어색한 문장이나 단어라고 생각되면 고치세요. 

# 다음 형식을 사용하세요:
# {{
#     title: <소설의 제목>
#     content: <[소설의 내용]>
# }}
# """

print(prompt)

# response = get_completion(prompt=prompt)
result = asyncio.run(get_completion(prompt=prompt))
print(result)