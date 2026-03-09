import random

ideas = [
"Discipline beats motivation",
"Small actions create massive success",
"Your habits design your future",
"Fear disappears when you start",
"Consistency builds unstoppable power"
]

def generate_script():
    return "\n".join(random.sample(ideas,3))