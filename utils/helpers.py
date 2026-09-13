import subprocess, platform


def clear_screen() -> None:
	"""Unsurprisingly, should clear the terminal screen; works on both POSIX and Windows!!1!"""

	command: str = ("clear" if (platform.system() != "Windows") else "cls")
	subprocess.run(command, shell=True)

	return (None)


def ask_yes_no(question: str) -> bool:
	"""
	Asks the user a simple yes or no question.

	Args:
		question (str): The question to display to the user.

	Returns:
		bool: 'True' if the user answered with "y" or "yes", 'False' otherwise.
	"""

	answer: str = input(question + " (y/N): ").strip().lower()
	return (answer in ["y", "yes"])
