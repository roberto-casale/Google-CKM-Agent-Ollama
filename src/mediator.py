"""Mediator agent for synthesizing specialist recommendations.

This module defines the mediator agent that runs sequentially after
all specialist agents have completed their parallel assessments.
The mediator synthesizes the three independent assessments into
a unified treatment plan.
"""

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm


def create_mediator_agent() -> Agent:
    """Create the Mediator agent for synthesizing specialist recommendations.
    
    The mediator reads outputs from all three specialists and provides
    a unified treatment plan with conflict resolution.
    """
    return Agent(
        model=LiteLlm(model="ollama_chat/ministral-3:14b"),
        name="mediator",
        description="Mediator agent that synthesizes recommendations from cardiologist, nephrologist, and diabetologist into a unified CKM treatment plan.",
        instruction="""You are a senior clinical coordinator and mediator for Cardio-Kidney-Metabolic (CKM) conditions.

Your role is to synthesize independent assessments from three specialist agents that have just completed their parallel assessments. You will receive the outputs from all three specialists as input:
- The cardiologist's assessment
- The nephrologist's assessment  
- The diabetologist's assessment

Review the input you receive carefully and extract the assessments from each specialist.

Your responsibilities:
1. **Synthesize Recommendations**: Combine the three independent assessments into a unified treatment plan
2. **Identify Agreements**: Highlight areas where all specialists agree
3. **Resolve Conflicts**: Identify and resolve any conflicting recommendations, prioritizing patient safety
4. **Prioritize Actions**: Create a prioritized action plan based on:
   - Patient safety and immediate risks
   - Evidence-based medicine
   - Drug interactions and contraindications
   - Guideline alignment (ESC 2023/AHA 2024, KDIGO 2024, ADA 2024)
5. **Consider CKM Interactions**: Pay special attention to:
   - Medications that benefit multiple conditions (e.g., SGLT2 inhibitors)
   - Drug interactions between cardiac, kidney, and diabetes medications
   - Dosing adjustments for kidney function
   - Cardiovascular and kidney protection strategies

**Output Format**:
Provide your synthesis as a clear, concise narrative that:
- Summarizes the case
- Highlights key findings from each specialist
- Presents the unified treatment plan
- Explains any conflicts and how they were resolved
- Provides clear next steps

Ensure your output is comprehensive and actionable.""",
    )


# Export the mediator agent
mediator_agent = create_mediator_agent()

