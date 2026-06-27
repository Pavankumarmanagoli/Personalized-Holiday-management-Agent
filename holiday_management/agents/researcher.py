from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.groq_model import model_client

researcher_agent = AssistantAgent(
    name="Holiday_Researcher",
    description="A Holiday researcher agent that helps users research about their holiday destinations.",
    model_client=model_client,
    system_message=(
        "You are a holiday researcher. Add only concise destination facts, "
        "attraction notes, local culture context, and travel tips that improve "
        "the current plan. When your research notes are complete, end with TERMINATE."
    )
)
