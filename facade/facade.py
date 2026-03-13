"""
Biblioteca de processamento de vídeo com dezenas de classes.
Classes: 
    - VideoFile, 
    - BitrateReader, 
    - AudioMixer, 
    - CodecFactory

Problema: necessidade de estudar e análisar cada classe interagem apenas para converter um arquivo. 
Solução: criar uma classe Facade com un único método que lida internamente com toda orquestração.
"""

# ------ 1. Subsistema COmplexo com classes difíceis de orquestrar  ------ #   

class VideoFile:
    def __init__(self, filename: str):
        self.filename = filename
        print(f"VideoFile: Carregando arquivo '{filename}'.")

class OggCompressionCodec:
    type = "ogg"

class MPEG4CompressionCodec:
    type = "mp4"

class CodecFactory:
    def extract(self, file: VideoFile):
        print("CodecFactory: Extraindo codec do arquivo de origem.")
        return "mp4" # Simplificação para o exemplo

class BitrateReader:
    @staticmethod
    def read(filename: str, source_codec: str):
        print("BitrateReader: Lendo arquivo.")
        return "buffer"

    @staticmethod
    def convert(buffer, destination_codec):
        print("BitrateReader: Escrevendo arquivo no novo formato.")
        return "novo_buffer"

class AudioMixer:
    def fix(self, result):
        print("AudioMixer: Corrigindo faixas de áudio.")
        return "arquivo_final.mp4"
    
# --- 2. Classe Facade que o cliente vai utilizar ---

class VideoConverter:
    """
    Fornece um método simples para a conversão de vídeos,
    lidando com todas as dependências do framework complexo internamente.
    """

    def convert(self, filename :str, format: str) -> str:
        print(f" Iniciando conversão de {filename} para '{format}")
        file = VideoFile(filename)
        source_codec = CodecFactory().extract(file)

        if format == 'mp4':
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)


        final_file = AudioMixer().fix(result)
        print ("Conversão concluída com sucesso!")
        return final_file
    
# --- Cliente ---

if __name__ == "__main__":

    conversor = VideoConverter()
    arquivo_desconhecido = conversor.convert("video_feliz.ogg", "mp4")
    print(f"Resultado salvo em: {arquivo_desconhecido}")