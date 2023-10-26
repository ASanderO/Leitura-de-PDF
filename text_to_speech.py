import asyncio
from deepgram import Deepgram
from docx import Document
import json

DEEPGRAM_API_KEY = 'e9312877e73293d229ed0e89fffc093ca7e420dd'
TEXT_TO_SPEAK = 'Seu texto aqui'

document = Document('saida.docx')
text_to_speak = ' '.join([paragraph.text for paragraph in document.paragraphs])

async def main():
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    response = await asyncio.create_task(
        deepgram.text_to_speech(text_to_speak, language='pt')
    )

    with open('output_audio.wav', 'wb') as audio_file:
        audio_file.write(response)

    print('Texto do arquivo "saida.docx" convertido em áudio e salvo em output_audio.wav')

try:
    asyncio.run(main())
except Exception as e:
    print(f'Erro: {e}')