import questionary
from rich.console import Console

from features.transactions.transactions import manage_transactions
from features.budgets.budgets import manage_budgets
from features.analytics.analytics import view_analytics

def main():
    """Main function to run the personal finance tracker CLI."""
    console = Console()
    console.print("[bold green]Welcome to your Personal Finance Tracker![/bold green]")

    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "Manage Transactions",
                "Manage Budgets",
                "View Analytics",
                "Exit",
            ],
        ).ask()

        if choice == "Manage Transactions":
            manage_transactions()
        elif choice == "Manage Budgets":
            manage_budgets()
        elif choice == "View Analytics":
            view_analytics()
        elif choice == "Exit":
            console.print("[bold]Goodbye![/bold]")
            break

if __name__ == "__main__":
    main()
