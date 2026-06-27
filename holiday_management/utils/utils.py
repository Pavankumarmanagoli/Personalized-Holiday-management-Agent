from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination


def get_termination_condition():
    text_termination = TextMentionTermination("TERMINATE")
    max_messages = MaxMessageTermination(max_messages=3)

    return text_termination | max_messages
