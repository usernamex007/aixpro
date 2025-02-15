from fastapi import FastAPI, Query
import openai

openai.api_key = "proj_r9YMBSTvFLNZvYUri711aEXW"  # OpenAI से API Key लें

app = FastAPI()

@app.get("/chat")
async def chat(query: str = Query(..., min_length=1)):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )
        return {"data": response.choices[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}
