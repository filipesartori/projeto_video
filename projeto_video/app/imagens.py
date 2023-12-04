from openai import OpenAI

def imagem(tema):
    with open('/workspaces/projeto_video/projeto_video/app/openai_key.txt', 'r') as file:
        api_key = file.read().strip()

    client = OpenAI(api_key=api_key)

    prompt = 'Gere uma imagem para um video no youtube sobre este tema: ' + tema

    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    print(image_url)
    return image_url