"""Example script demonstrating programmatic usage of the ADK agent."""

from src.agent import root_agent
from google.adk.runners import Runner


def main():
    """Run example interactions with the agent."""
    print("Initializing ADK agent with Ollama ministral-3:14b...")
    print("-" * 60)
    
    # Create a runner
    runner = Runner(root_agent)
    
    # Example 1: Roll a die
    print("\nExample 1: Rolling a 20-sided die")
    print("Query: Roll a 20-sided die")
    response = runner.run("Roll a 20-sided die")
    print(f"Response: {response}")
    
    # Example 2: Check if a number is prime
    print("\nExample 2: Checking if 17 is prime")
    print("Query: Is 17 a prime number?")
    response = runner.run("Is 17 a prime number?")
    print(f"Response: {response}")
    
    # Example 3: Calculate something
    print("\nExample 3: Performing a calculation")
    print("Query: What's 15 * 23?")
    response = runner.run("What's 15 * 23?")
    print(f"Response: {response}")
    
    # Example 4: Combined operation
    print("\nExample 4: Combined operation")
    print("Query: Roll a 12-sided die and check if the result is prime")
    response = runner.run("Roll a 12-sided die and check if the result is prime")
    print(f"Response: {response}")
    
    print("\n" + "-" * 60)
    print("Examples completed!")


if __name__ == "__main__":
    main()

