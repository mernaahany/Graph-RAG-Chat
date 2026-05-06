from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain

from config import settings
from graph import get_graph


def get_llm() -> AzureChatOpenAI:
    return AzureChatOpenAI(
        azure_deployment=settings.AZURE_DEPLOYMENT,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_KEY,
        api_version="2024-02-01",
        temperature=0
    )


CYPHER_PROMPT = PromptTemplate(
    input_variables=["schema", "question"],
    template="""
You are an expert Neo4j developer.
Use ONLY the provided schema.

Schema:
{schema}

Question:
{question}

Rules:
- Generate ONLY Cypher query
- Do NOT explain anything
- Do NOT use properties not in schema
- Use correct relationship directions
"""
)

QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant.

Given this data:
{context}

Answer the question clearly and concisely:
{question}
"""
)


def get_chain() -> GraphCypherQAChain:
    return GraphCypherQAChain.from_llm(
        llm=get_llm(),
        graph=get_graph(),
        cypher_prompt=CYPHER_PROMPT,
        qa_prompt=QA_PROMPT,
        verbose=True,
        allow_dangerous_requests=True
    )