from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


def simple_agent():
    LLM = ChatOllama(model="llama3.1")
    for message_chunk in LLM.stream(
        [
            SystemMessage(content="Be polite and respectful."),
            SystemMessage(content="Provide accurate and relevant information."),
            SystemMessage(content="Be short and consise."),
            HumanMessage(
                content="""Can you provide an update on the current state of human civilization?""", name="Human"
            ),
        ]
    ):
        print(message_chunk.content, end="")
