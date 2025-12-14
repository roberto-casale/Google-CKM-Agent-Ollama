"""CKM Multi-Agent Board Pattern - Main Orchestration.

This module orchestrates the multi-agent tumor board pattern for
Cardio-Kidney-Metabolic (CKM) conditions:
1. Three specialist agents run in parallel
2. Mediator agent synthesizes recommendations sequentially
3. Root agent handles input parsing and delegation
"""

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import ParallelAgent, SequentialAgent
from .specialists import (
    cardiologist_agent,
    nephrologist_agent,
    diabetologist_agent,
)
from .mediator import mediator_agent


# Create parallel agent for specialist assessments
specialists_parallel = ParallelAgent(
    name="specialists_board",
    description="Parallel assessment by cardiologist, nephrologist, and diabetologist for CKM conditions.",
    sub_agents=[cardiologist_agent, nephrologist_agent, diabetologist_agent],
)

# Create sequential agent: parallel specialists → mediator
ckm_board = SequentialAgent(
    name="ckm_board",
    description="CKM multi-specialist tumor board: parallel specialist assessment followed by mediator synthesis.",
    sub_agents=[
        specialists_parallel,  # Step 1: Parallel assessment
        mediator_agent,        # Step 2: Synthesis
    ],
)

# Create root agent that handles input parsing and delegates to the board
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b"),
    name="ckm_root_agent",
    description="Root agent for CKM multi-agent board pattern. Accepts patient cases and coordinates specialist assessments.",
    instruction="""You are the coordinator for a Cardio-Kidney-Metabolic (CKM) multi-specialist tumor board.

Your responsibilities:
1. **Accept Input**: Accept patient cases as free-form text case descriptions.

2. **Normalize Input**: Ensure the input is clear and complete for the specialist agents to understand.

3. **Delegate to Board**: Delegate the case to the ckm_board sub-agent, which will:
   - Run three specialist agents in parallel (cardiologist, nephrologist, diabetologist)
   - Have the mediator agent synthesize their recommendations

4. **Format Output**: Present the final recommendations in a clear, actionable format.

When you receive input:
- Use the input as-is but ensure it's clear and complete
- Always delegate the case to the ckm_board sub-agent
- Present the mediator's synthesis clearly to the user

Be professional, clear, and ensure all relevant clinical information is passed to the specialist board.""",
    sub_agents=[ckm_board],
)

