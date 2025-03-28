import re
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from service.llm_service import LLMQueryAgent  

router = APIRouter()
llm_agent = LLMQueryAgent()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
async def generate_sql_and_explanation(request: QueryRequest):
    """
    Generates an SQL query and an explanation.
    """
    try:
        sql_query, explanation = llm_agent.generate_query_and_explanation(request.query)

        sql_query = re.sub(r"```(\w+)?", "", sql_query).strip()  
        sql_query = sql_query.replace("\n", " ") 

        return {
            "sql_query": sql_query,
            "explanation": explanation.strip() 
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
