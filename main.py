from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=300
)

documents = [
    "",
    
]

query = ""

docs_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], docs_embedding)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print (query)
print (documents [index])
print("similarity score is:", score)

