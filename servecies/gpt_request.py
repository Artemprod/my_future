from openai import AsyncOpenAI



async def get_response_image_file(image, client: AsyncOpenAI, system_prompt, user_prompt, temperature=1.8,

                                  top_p=0.9,
                                  presence_penalty=0.9,
                                  frequency_penalty=0.9,
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
        max_tokens=1000,
        temperature=temperature,
        top_p=top_p,
        presence_penalty=presence_penalty,
        frequency_penalty =frequency_penalty

    )
    return answer.choices[0].message.content


async def get_response_image_url(client: AsyncOpenAI, image_url, system_prompt, user_prompt, temperature=1.0,
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
