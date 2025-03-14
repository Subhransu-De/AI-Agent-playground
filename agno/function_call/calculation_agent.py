from agno.agent import Agent
from agno.models.ollama import Ollama


def addition_of_numbers(a, b) -> str:
    """Use this function to add two given numbers.

    Args:
        a (int | float): The first number to add.
        b (int | float): The second number to add.

    Returns:
        str: Sum of the given numbers as a string.
    """
    return str(a + b)


def subtraction_of_numbers(a, b) -> str:
    """Use this function to subtract the second number from the first number.

    Args:
        a (int | float): The number to subtract from.
        b (int | float): The number to subtract.

    Returns:
        str: Difference of the given numbers as a string.
    """
    return str(a - b)


def multiplication_of_numbers(a, b) -> str:
    """Use this function to multiply two given numbers.

    Args:
        a (int | float): The first number to multiply.
        b (int | float): The second number to multiply.

    Returns:
        str: Product of the given numbers as a string.
    """
    return str(a * b)


def division_of_numbers(a, b) -> str:
    """Use this function to divide the first number by the second number.

    Args:
        a (int | float): The number to be divided.
        b (int | float): The number to divide by.

    Returns:
        str: Quotient of the given numbers as a string.
    """
    if b == 0:
        return "Error: Division by zero"
    return str(a / b)


def calculation_agent():
    calculation_agent = Agent(
        model=Ollama(id="llama3.1"),
        tools=[
            addition_of_numbers,
            subtraction_of_numbers,
            multiplication_of_numbers,
            division_of_numbers,
        ],
        instructions=[
            "Be polite and respectful.",
            "Do the calculation on the equation given iteratively.",
        ],
        show_tool_calls=True,
        markdown=True,
    )
    calculation_agent.print_response("What is 124 - 45 * 2 / 5?", stream=True)
