import subprocess, platform


def clear_screen() -> None:
	"""Unsurprisingly, should clear the terminal screen; works on both POSIX and Windows!!1!"""

	command: str = ("clear" if (platform.system() != "Windows") else "cls")
	subprocess.run(command, shell=True)

	return (None)


def ask_yes_no(question:str) -> bool:
	"""
	Asks the user a simple yes or no question.

	Args:
		question (str): The question to display to the user.

	Returns:
		bool: 'True' if the user answered with "y" or "yes", 'False' otherwise.
	"""

	answer: str = input(question + " [y/N]: ").strip().lower()
	return (answer in ["y", "yes"])


def ask_file_name(default_name:str="output", extension: str="", invalid_chars:str="<>:\"/\\|?*") -> str:
	"""
	Asks the user for a file name. Typing the extension is optional.

	Args:
		default_name (str, optional): Name to default to. Must NOT include the extension.  Defaults to "output"
		extension (str, optional): Extension to enforce, dot must be included. Empty is accepted. Defaults to "".
		invalid_chars (str, optional): Characters that make a name invalid. Defaults to "<>:\"/\\|?*".
	
	Returns:
		str: The final file name.
	"""

	user_file_name: str = input(f"File name (default: {default_name}): ").strip()

	if ((user_file_name == "") or (any(char in invalid_chars for char in user_file_name))): #Is user_file_name invalid?
		print(f"You have provided an empty or invalid name; \"{default_name}\" will be used.")
		user_file_name = default_name

	elif ((extension != "") and (user_file_name.lower().endswith(extension.lower()))): #Is extension present already or not needed? 
		user_file_name = user_file_name[:-len(extension)]


	return (user_file_name + extension)
