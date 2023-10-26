import sys
import asyncio
from deepgram import Deepgram
import json

DEEPGRAM_API_KEY = 'e9312877e73293d229ed0e89fffc093ca7e420dd'
FILE = 'cume.wav'
MIMETYPE = 'audio/wav'

async def main():
    deepgram = Deepgram(DEEPGRAM_API_KEY)

    if FILE.startswith('http'):
        source = {'url': FILE}
    else:
        audio = open(FILE, 'rb')
        source = {'buffer': audio, 'mimetype': MIMETYPE}

    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                'punctuate': True,
                'language': 'pt'
            }
        )
    )

    words = [
        word['word'] for word in response['results']['channels'][0]['alternatives'][0]['words']
    ]

    transcribed_text = ' '.join(words)

    with open('transcricao.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(transcribed_text)

    print('Transcrição salva em transcricao.txt')
    print(json.dumps(response, indent=4))

try:
    asyncio.run(main())
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = exception_traceback.tb_lineno
    print(f'line {line_number}: {exception_type} - {e}')
