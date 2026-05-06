from langchain_community.graphs import Neo4jGraph
from config import settings
#from langchain_neo4j import Neo4jGraph

def get_graph() -> Neo4jGraph:
    return Neo4jGraph(
        url=settings.NEO4J_URL,
        username=settings.NEO4J_USER,
        password=settings.NEO4J_PASSWORD
    )