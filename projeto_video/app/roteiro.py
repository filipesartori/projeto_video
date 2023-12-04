from openai import OpenAI


def roteiro(tema):
    with open('/workspaces/projeto_video/projeto_video/app/openai_key.txt', 'r') as file:
        api_key = file.read().strip()

    client = OpenAI(api_key=api_key)  
        
    input_text = 'Crie um roteiro para um vídeo no YouTube sobre' + tema + ', apenas com o que será dito pelo apresentador, sem instruções, sem tags de indetificação de dialogo, apenas um texto a ser falado'
        
    response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text},
            ]
        )
    
    output_text = response.choices[0].message.content
    print(output_text)
    
    return output_text
