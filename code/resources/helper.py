from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

console = Console()
init(autoreset=True)

def show_response(response, show_reasoning=False, show_usage=True):
    print(Fore.CYAN + Style.BRIGHT + "\n RESPONSE " + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 40)
    print(response.content)

    if show_reasoning and (reasoning := response.additional_kwargs.get("reasoning_content")):
        print("\n")
        print(Fore.MAGENTA + Style.BRIGHT + "REASONING" + Style.RESET_ALL)
        print(Fore.MAGENTA + "-" * 40)
        print(reasoning)

    if show_usage and (usage:= response.usage_metadata):
        print("\n")
        table = Table(title="TOKEN USAGE", title_style="bold green")

        table.add_column("METRIC", style="cyan")
        table.add_column("VALUE", justify="right", style="green")

        table.add_row("INPUT", str(usage["input_tokens"]))
        table.add_row("OUTPUT", str(usage["output_tokens"]))
        table.add_row("TOTAL", str(usage["total_tokens"]))

        console.print(table)