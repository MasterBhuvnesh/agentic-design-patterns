from colorama import Fore, Style, init

init(autoreset=True)

def show_response(response, show_reasoning=True, show_usage=True):
    print(Fore.CYAN + Style.BRIGHT + "\n RESPONSE " + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 40)
    print(response.content)

    if show_reasoning and (reasoning := response.additional_kwargs.get("reasoning_content")):
        print("\n")
        print(Fore.MAGENTA + Style.BRIGHT + "REASONING" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 40)
        print(reasoning)

    if show_usage and (usage := response.usage_metadata):
        print(Fore.GREEN + Style.BRIGHT + "TOKENS " + Style.RESET_ALL)
        print(Fore.GREEN + "-" * 40)
        print(
            f"Input: {usage['input_tokens']} | "
            f"Output: {usage['output_tokens']} | "
            f"Total: {usage['total_tokens']}"
            ,end="\n"
        )
