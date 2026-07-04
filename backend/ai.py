def generate_reply(name: str, message: str):

    user_message = message.lower()

    if "hello" in user_message:
        return f"Hello {name}! Nice to meet you."

    elif "scan" in user_message:
        return "Website scanning is coming soon."

    elif "help" in user_message:
        return "I can help with cybersecurity questions."

    else:
        return "I'm still learning. Ask me something else."