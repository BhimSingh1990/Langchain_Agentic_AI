# Using Langchain for Agents
def RAG(question):
    import  os
    from dotenv import load_dotenv
    load_dotenv()
    # Load environment variables from .env file
    API_KEY = os.getenv("GOOGLE_API_KEY")
    from langchain.chat_models import init_chat_model

    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    query = input("Ask me anything ")
    response = model.invoke(query)
    return response.content

RAG("What is Langchain?")
