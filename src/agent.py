"""Google Agent ADK demo with Ollama ministral-3:14b model."""

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm


def roll_die(sides: int = 6) -> str:
    """Roll a die with the specified number of sides.
    
    Args:
        sides: Number of sides on the die (default: 6)
    
    Returns:
        A string describing the roll result
    """
    import random
    result = random.randint(1, sides)
    return f"You rolled a {result} on a {sides}-sided die!"


def check_prime(number: int) -> str:
    """Check if a number is prime.
    
    Args:
        number: The number to check
    
    Returns:
        A string indicating if the number is prime or not
    """
    if number < 2:
        return f"{number} is not a prime number."
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number (divisible by {i})."
    
    return f"{number} is a prime number!"


def calculate(expression: str) -> str:
    """Evaluate a simple mathematical expression safely.
    
    Args:
        expression: A mathematical expression (e.g., "2 + 2", "10 * 5")
    
    Returns:
        The result of the calculation
    """
    try:
        # Only allow basic math operations for safety
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return "Error: Only basic math operations are allowed."
        
        result = eval(expression)
        return f"The result of '{expression}' is {result}."
    except Exception as e:
        return f"Error calculating '{expression}': {str(e)}"


# Create the root agent with Ollama ministral-3:14b model
# Functions are passed directly to tools - ADK automatically converts them
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b"),
    name="demo_agent",
    description=(
        "A helpful demo agent that can roll dice, check if numbers are prime, "
        "and perform basic calculations."
    ),
    instruction="""
    You are a helpful assistant that can:
    - Roll dice with any number of sides
    - Check if numbers are prime
    - Perform basic mathematical calculations
    
    Be friendly and explain what you're doing when using tools.
    """,
    tools=[
        roll_die,
        check_prime,
        calculate,
    ],
)

