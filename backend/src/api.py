from fastapi import FastAPI
from summarization import convert_to_mp3


app = FastAPI()


@app.get("/")
def summarize():
    convert_to_mp3(r"C:\Users\iWaheeb\repos\jawhar-backend\cache\video\input.mp4")
    return "DONE"