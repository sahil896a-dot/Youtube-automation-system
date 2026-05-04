"""Beginner-friendly YouTube automation script.

This project:
1) Picks a trending topic in the history niche for a USA audience.
2) Creates a 60-second script with a hook, storytelling, and climax.
3) Saves the result to a text file.
"""

from datetime import datetime
import random


def generate_trending_topic() -> str:
    """Return a history-focused topic that often performs well in the USA."""
    topic_bank = [
        "The untold story of how the Golden Gate Bridge was built",
        "The day the Wright brothers changed America forever",
        "How the Louisiana Purchase doubled the size of the United States",
        "The midnight ride of Paul Revere: what really happened",
        "How Route 66 became the most famous road in America",
    ]
    return random.choice(topic_bank)


def create_60_second_script(topic: str) -> str:
    """Create a short-form script using hook, storytelling, and climax."""
    hook = (
        f"HOOK: What if I told you that '{topic}' changed everyday life in America "
        "in ways most people never notice?"
    )

    storytelling = (
        "\n\nSTORYTELLING: It started with a bold idea, massive risk, and people who "
        "were told it could not be done. Through setbacks, public doubt, and "
        "hard choices, this moment in history slowly turned into a national "
        "turning point. Families talked about it at dinner tables, newspapers "
        "covered every update, and its impact spread from one city to every "
        "corner of the country."
    )

    climax = (
        "\n\nCLIMAX: Then came the breakthrough that proved everyone wrong. In one "
        "powerful moment, history shifted, and America stepped into a new era. "
        "The lesson? Big change often begins with one impossible idea and people "
        "brave enough to chase it."
    )

    outro = "\n\nIf you want more 60-second history stories, follow for the next one."

    return f"Topic: {topic}\n\n{hook}{storytelling}{climax}{outro}"


def save_script_to_file(content: str, filename: str = "generated_youtube_script.txt") -> None:
    """Save generated script text to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Generated on: {datetime.utcnow().isoformat()}Z\n\n")
        file.write(content)


def main() -> None:
    topic = generate_trending_topic()
    script = create_60_second_script(topic)
    save_script_to_file(script)

    print("Done! Your YouTube script has been saved to generated_youtube_script.txt")


if __name__ == "__main__":
    main()
