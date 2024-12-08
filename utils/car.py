import re

def formalize_car_number(number: str) -> str:
    number = number.upper()
    pattern = r'^([АВЕКМНОРСТУХ])(\d{3})([АВЕКМНОРСТУХ]{2})(\d{2,3})$'
    
    match = re.match(pattern, number)
    if match:
        return f"{match.group(1)}{match.group(2)}{match.group(3)}{match.group(4)}"
    else:
        return ""

