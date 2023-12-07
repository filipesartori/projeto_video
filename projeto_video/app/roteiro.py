from openai import OpenAI


def roteiro(tema, console):
    with open('/workspaces/projeto_video/projeto_video/app/openai_key.txt', 'r') as file:
        api_key = file.read().strip()

    client = OpenAI(api_key=api_key)  
        
    input_text = console + tema
    
        
    response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text},
            ]
        )   
    output_text = response.choices[0].message.content
    
    return output_text
