from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.groq_model import model_client

planner_agent = AssistantAgent(
    name="Holiday_Planner",
    description="A Holiday planner agent that helps users plan their trips.",
    model_client=model_client,
    system_message=(
        "You are a holiday planner. Create a concise, practical trip plan with "
        "day-by-day activities, logistics, and travel tips. Keep the answer short. "
        "When the plan is complete, end with TERMINATE."
    )
)
