import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=300
)

DOCS_FOLDER = "docs"
documents = []
filenames = []

for filename in os.listdir(DOCS_FOLDER):
    if filename.endswith(".txt"):
        with open(os.path.join(DOCS_FOLDER, filename), "r", encoding="utf-8") as f:
            documents.append(f.read())
            filenames.append(filename)

if not documents:
    print("No documents found in the 'docs' folder.")
    exit(1)

query = input("Enter your query: ").strip()
if not query:
    print("Query cannot be empty.")
    exit(1)

docs_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], docs_embedding)[0]

index = scores.argmax()
score = scores[index]

print("\nQuery:")
print(query)
print("\nMost similar document: {}".format(filenames[index]))
print(documents[index][:500] + ("..." if len(documents[index]) > 500 else ""))
print("\nSimilarity score: {:.4f}".format(score))