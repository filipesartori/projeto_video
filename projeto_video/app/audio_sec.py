from pydub import AudioSegment

def obter_duracao_em_segundos(caminho_arquivo):
    # Carregar o arquivo de áudio usando o pydub
    audio = AudioSegment.from_file(caminho_arquivo)

    # Obter a duração em milissegundos
    duracao_em_milissegundos = len(audio)

    # Converter a duração para segundos
    duracao_em_segundos = duracao_em_milissegundos / 1000.0

    return duracao_em_segundos