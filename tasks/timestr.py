__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = ((seconds % 86400) % 3600) // 60
    seconds = ((seconds % 86400) % 3600) % 60

    time_str = ""
    if days > 0:
        time_str += f"{days:02}d"
    if hours > 0 or days > 0:
        time_str += f"{hours:02}h"
    if minutes > 0 or hours > 0 or days > 0:
        time_str += f"{minutes:02}m"
    if seconds >= 0 or minutes > 0 or hours > 0 or days > 0:
        time_str += f"{seconds:02}s"


    return time_str

print(seconds_to_str(0))
print(seconds_to_str(20))
print(seconds_to_str(60))
print(seconds_to_str(65))
print(seconds_to_str(3700))
print(seconds_to_str(93600))
print(seconds_to_str(864000))

