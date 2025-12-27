"""CKM Syndrome Multi-Specialist Consultation Package.

This package implements a Cardio-Kidney-Metabolic (CKM) Syndrome multi-specialist
consultation pattern using Google's Agent Development Kit (ADK).

Modules:
- agent: Main orchestration and root agent
- intake_agent: User intake flow (guided intake and paste mode)
- specialists: Cardiologist, Nephrologist, Diabetologist agents
- mediator: Synthesis agent with Consultation Snapshot output
- output_templates: Standard output formats and templates
- utils: Utility functions
"""

from .agent import root_agent, ckm_panel, specialists_parallel, ckm_board, specialists_board
from .intake_agent import intake_agent, WELCOME_MESSAGE
from .specialists import cardiologist_agent, nephrologist_agent, diabetologist_agent
from .mediator import mediator_agent
from .output_templates import (
    CONSULTATION_SNAPSHOT_TEMPLATE,
    PERIOP_MEDICATION_TABLE_TEMPLATE,
    STANDARD_PERIOP_MEDICATIONS,
    generate_consultation_snapshot,
    format_medication_table,
)

__all__ = [
    # Main agents
    "root_agent",
    "ckm_panel",
    "ckm_board",  # Backwards compatibility
    "specialists_parallel",
    "specialists_board",  # Backwards compatibility
    "intake_agent",
    "mediator_agent",
    # Specialist agents
    "cardiologist_agent",
    "nephrologist_agent",
    "diabetologist_agent",
    # Templates and utilities
    "WELCOME_MESSAGE",
    "CONSULTATION_SNAPSHOT_TEMPLATE",
    "PERIOP_MEDICATION_TABLE_TEMPLATE",
    "STANDARD_PERIOP_MEDICATIONS",
    "generate_consultation_snapshot",
    "format_medication_table",
]
