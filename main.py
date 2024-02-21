from fastapi import FastAPI,UploadFile,File
from decouple import config
from openai import OpenAI

app=FastAPI()
api_key=config('OPEN_API_KEY')
client = OpenAI(api_key=api_key)

@app.get("/")
async def transcribe_audio():
    try:
        audio_file= open("Recording (2).m4a","rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
        text=transcript.text
        return text

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000)

