import lambdaprompt


@lambdaprompt.prompt
def hello(name: str):
    return "Hello {name}!"


lambdaprompt.GPT3Prompt(
    """Write a personalized greeting to {{ name }}.
Write it in the tone of {{ tone }}.
""",
    name="greeting",
)
