import asyncio
from pathlib import Path

from openai import AsyncOpenAI

from utils.encode_media import encode_image


async def get_response_image_file(image, client: AsyncOpenAI, system_prompt, user_prompt, temperature=1.0,
                                  model="gpt-4o"):
    answer = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",
             "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text",
                 "text": user_prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}
                 }
            ]}
        ],
        temperature=temperature,

    )
    return answer.choices[0].message.content


async def get_response_image_url(client: AsyncOpenAI, image_url, system_prompt, user_prompt, temperature=0.0,
                                 model="gpt-4o"):
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": user_prompt},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]}
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content





