from fastapi import APIRouter
from pydantic import BaseModel
from llm import get_chain

router = APIRouter()
chain = get_chain()

class Question(BaseModel):
    text: str

@router.post("/chat")
def chat(q: Question):
    result = chain.invoke({"query": q.text})
    return {"answer": result["result"]}