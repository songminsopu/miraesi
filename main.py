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

first_prompt = f"""
주어진 문자열 배열을 기반으로 대본을 작성하세요:
{ocr_lst}
"""

print(first_prompt)

result_script = asyncio.run(get_completion(prompt=first_prompt))
print("=" * 100)
print(result_script)