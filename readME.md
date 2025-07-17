# Document Similarity Tool

A simple Python application that finds the most similar document to a given query using OpenAI embeddings and cosine similarity.

## Overview

This tool reads text documents from a `docs/` folder and uses OpenAI's text embeddings to find which document is most similar to a user-provided query. It leverages the power of semantic search to understand meaning beyond exact keyword matching.

## Features

- **Semantic Search**: Uses OpenAI's text-embedding-3 for understanding document meaning
- **Cosine Similarity**: Calculates similarity scores between query and documents
- **Simple Interface**: Interactive command-line interface for easy querying
- **Batch Processing**: Automatically processes all `.txt` files in the docs folder

## Prerequisites

- Python 3.7+
- OpenAI API key

## Example

```
Enter your query: nature and wildlife

Query:
nature and wildlife

Most similar document: 1.txt
The forest hums with life beneath the golden rays of dawn. Every leaf whispers secrets to the wind.

Similarity score: 0.8234
```

## How It Works

1. **Document Processing**: Reads all `.txt` files from the `docs/` folder
2. **Embedding Generation**: Converts documents and query into 300-dimensional vectors using OpenAI's embedding model
3. **Similarity Calculation**: Uses cosine similarity to find the most similar document
4. **Results Display**: Shows the best match with its similarity score

## Project Structure

```
document-similarity/
├── main.py              # Main application script
├── requirements.txt     # Python dependencies
├── readME.md            # This file
├── .env                # Environment variables (create this)
└── docs/               # Document folder
    ├── 1.txt
    ├── 2.txt
    ├── 3.txt
    ├── 4.txt
    ├── 5.txt
    └── 6.txt
```

## Dependencies

- `langchain-openai`: OpenAI integration for embeddings
- `scikit-learn`: Cosine similarity calculations
- `python-dotenv`: Environment variable management
- `openai`: OpenAI API client

## Notes

- Requires an active OpenAI API key
- API usage will incur costs based on OpenAI's pricing
- The tool processes documents in memory, so very large files may impact performance
- Similarity scores range from 0 to 1, where higher scores indicate greater similarity