from agno.agent import Agent
from agno.models.ollama import Ollama


def simple_agent():
    simple_agent = Agent(
        name="Simple Agent",
        model=Ollama(id="llama3.1"),
        instructions=[
            "Be polite and respectful.",
            "Provide accurate and relevant information.",
            "Be short and consise.",
        ],
        markdown=True,
    )
    simple_agent.print_response(
        """Can you provide an update on the current state of human civilization?""",
        stream=True,
    )
