from roteiro import roteiro

def tags(tema):
    tags = roteiro(tema, 'Crie SOMENTE 5 tags que façam viralizar no tiktok e imprima neste formato (1. 2. 3. 4. 5. 6. 7. 8. 9. 10.) sobre este tema:')
    tags = ''.join(char for char in tags if not char.isdigit() and char != '.' and char != '#' and char != ' ')
    lista_resultante = [item.strip() for item in tags.split()]
    
    return lista_resultante
