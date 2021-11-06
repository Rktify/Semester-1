Lang = {
    "Go": "A statically typed, compiled programming language designed at Google",
    "Python": "An advanced programming language that is interpreted, object-oriented and built on flexible and robust semantics.",
    "Java": "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible",
    "JavaScript": "The most popular programming language for building interactive websites",
    "HTML": "A standard markup language used to create web pages; it ensures proper formatting of text and images (using tags) so that Internet browsers can display them in the ways they were intended to look."
}

for i in ["Java", "Python", "JavaScript", "Go", "HTML"]:
    print(i, Lang.get(i),sep="\n")
    print()