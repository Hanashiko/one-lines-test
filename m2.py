def valid_length(user_input: str) -> str:
	if len(user_input) > 10:
		return "Yes case"
	else:
		return "No case"

def valid_length(user_input: str) -> str:
	return "Yes case" if len(user_input) > 10 else "No case"

def valid_length(user_input: str) -> bool:
	return len(user_input) > 10