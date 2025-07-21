# Problem: Event Attendance - Finding the First Overcrowded Session

# You are managing an online conference with several parallel sessions.
# For each session, you have its [session_name, max_capacity, current_attendees].
# Your goal is to find the first session in your list that has current_attendees
# greater than its max_capacity (meaning it's overcrowded).

# If such a session is found, you should report its name, its current number of attendees,
# its maximum capacity, and its position (index) in the session list.
# If no session is overcrowded, you should report that all sessions are within capacity.

session_data: list = [
    ["AI & Data", 100, 80],
    ["Financial Independence", 500, 490],
    ["Time Freedom", 300, 315],
    ["Happy Coding", 120, 34],
    ["World Travel", 300, 268],
]


def find_first_over_crowded_session(sessions: list) -> str:
    """
    Find the first over crowded session

    Args:
        sessions (list): List of all the sessions and its details

    Returns:
        str: Message about the session
    """
    if len(sessions) == 0:
        return "There is no session."

    for index in range(len(sessions)):
        if sessions[index][1] < sessions[index][2]:
            return (
                f'Session: "{sessions[index][0]}" is overcrowded at position {index}.'
            )
    return "No session is overcrowded"


# When session is over crowded
report1: str = find_first_over_crowded_session(session_data)
print(report1)

# When no session is overcrowded
report2: str = find_first_over_crowded_session(
    [["Problem Solving", 200, 180], ["Cyber Security", 300, 299]]
)
print(report2)

# When there is no session
report3: str = find_first_over_crowded_session([])
print(report3)
