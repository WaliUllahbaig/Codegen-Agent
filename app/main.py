from app.llm.local_llm import OllamaLLM
from app.rag.retriever import CodeRetriever
from app.agent.agent import CodeAgent

def main():
    llm = OllamaLLM(model="qwen2.5-coder:1.5b")
    retriever = CodeRetriever("data/vector_store/index.pkl")

    agent = CodeAgent(llm, retriever)

    task = input("What do you want to build? > ")
    result = agent.run(task)

    print(result)

if __name__ == "__main__":
    main()
