import os
from dotenv import load_dotenv
load_dotenv()
from psychicapi import Psychic, ConnectorId
from langchain.schema import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain

try:
    # Create a document loader for Zendesk. We can also load from other connectors e.g. ConnectorId.gdrive
    psychic = Psychic(secret_key=os.getenv("PSYCHIC_SECRET_KEY"))
    #replace account_id with the value you set while creating a new connection at https://dashboard.psychic.dev/playground
    raw_docs = psychic.get_documents(connector_id=ConnectorId.gdrive, account_id="account_id", chunked=True)
    documents = [
        Document(page_content=doc["content"], metadata={"title": doc["title"], "source": doc["uri"]})
        for doc in raw_docs
    ]

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vdb = Chroma.from_documents(documents, embeddings)
    while True:
        question = input("✨ Ask a question: ")
        chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=vdb.as_retriever())
        answer = chain({"question": question}, return_only_outputs=True)
        print(answer)
        print("")
except Exception as e:
    print(e)
