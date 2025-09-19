import sys
import time
from datetime import datetime, timedelta
from typing import Optional

from rich import print as rprint
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.prompt import Prompt
from rich.text import Text

console = Console()


def parse_time_input(time_input: str) -> Optional[datetime]:
    """Parse user input for target time. Supports HH:MM format and minutes from now."""
    try:
        # Try parsing as HH:MM format
        if ":" in time_input:
            hour, minute = map(int, time_input.split(":"))
            now = datetime.now()
            target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

            # If the time has passed today, set it for tomorrow
            if target <= now:
                target += timedelta(days=1)
            return target

        # Try parsing as minutes from now
        minutes = int(time_input)
        if minutes <= 0:
            return None
        return datetime.now() + timedelta(minutes=minutes)

    except (ValueError, TypeError):
        return None


def get_cake_ascii() -> str:
    """Generate beautiful ASCII art cake."""
    cake_art = """
    🕯️ 🕯️ 🕯️
      |  |  |
   ███████████
  █████████████
 ███████████████
█████████████████
█████████████████
 ███████████████
  █████████████
   ███████████
    🍰🎂🍰
    """
    return cake_art


def display_celebration():
    """Display celebration with ASCII cake art."""
    console.clear()

    # Create celebration text
    celebration_text = Text("🎉 CAKE TIME! 🎉", style="bold magenta")

    # Get cake ASCII art
    cake_art = get_cake_ascii()

    # Create panels
    celebration_panel = Panel(
        Align.center(celebration_text), style="bright_yellow", border_style="bright_red"
    )

    cake_panel = Panel(
        Align.center(cake_art),
        title="🎂 Your Cake is Ready! 🎂",
        style="bright_cyan",
        border_style="bright_magenta",
    )

    console.print()
    console.print(celebration_panel)
    console.print()
    console.print(cake_panel)
    console.print()

    # Add some sparkles effect
    rprint("[bright_yellow]✨ ⭐ 🌟 ✨ ⭐ 🌟 ✨ ⭐ 🌟 ✨[/bright_yellow]")


def cake_countdown():
    """Main countdown application."""
    console.print(
        Panel(
            "[bold cyan]🎂 Cake Countdown Timer 🎂[/bold cyan]\n"
            "Set your cake timer and watch the countdown!",
            style="bright_blue",
        )
    )

    console.print()
    console.print("[yellow]How would you like to set your cake timer?[/yellow]")
    console.print("[dim]• Enter time as HH:MM (e.g., 14:30 for 2:30 PM)[/dim]")
    console.print("[dim]• Enter minutes from now (e.g., 25 for 25 minutes)[/dim]")
    console.print()

    while True:
        time_input = Prompt.ask("[green]Enter cake time")
        target_time = parse_time_input(time_input)

        if target_time is None:
            console.print("[red]Invalid time format! Please try again.[/red]")
            continue

        # Calculate seconds until target time
        seconds_remaining = int((target_time - datetime.now()).total_seconds())

        if seconds_remaining <= 0:
            console.print(
                "[red]That time has already passed! Please enter a future time.[/red]"
            )
            continue

        break

    console.print(
        f"[green]✅ Cake timer set for {target_time.strftime('%I:%M %p')}[/green]"
    )
    console.print(f"[yellow]⏰ Counting down {seconds_remaining} seconds...[/yellow]")
    console.print()

    # Start countdown
    start_countdown(seconds_remaining, target_time)


def start_countdown(total_seconds: int, target_time: datetime):
    """Start the visual countdown with progress bar."""
    try:
        with Progress(
            TextColumn("[bold blue]🎂 Cake Timer"),
            BarColumn(complete_style="green", finished_style="bright_green"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("•"),
            TextColumn("[cyan]{task.fields[time_left]}"),
            TextColumn("•"),
            TextColumn("[yellow]Until {task.fields[target_time]}"),
            console=console,
        ) as progress:
            task = progress.add_task(
                "countdown",
                total=total_seconds,
                time_left="",
                target_time=target_time.strftime("%I:%M %p"),
            )

            for i in range(total_seconds, 0, -1):
                # Update progress
                progress.update(task, advance=1, time_left=f"{i // 60}m {i % 60}s")
                time.sleep(1)

            # Countdown finished
            progress.update(task, completed=total_seconds)
            time.sleep(0.5)

        # Show celebration
        display_celebration()

    except KeyboardInterrupt:
        console.print("\n[red]⏹️  Cake countdown cancelled![/red]")
        sys.exit(0)


if __name__ == "__main__":
    try:
        cake_countdown()
    except KeyboardInterrupt:
        console.print("\n[red]👋 Goodbye![/red]")
        sys.exit(0)
