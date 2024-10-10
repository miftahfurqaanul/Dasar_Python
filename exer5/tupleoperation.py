favorite_languages = ("Python", "JavaScript", "C++", "Java", "Ruby")

# Print each language in the tuple
for language in favorite_languages:
    print(language)

# Print the length of the tuple
length = len(favorite_languages)
print("Length of the tuple:", length)

# Check if a specific language is in the tuple
target_language = "C#"
if target_language in favorite_languages:
    print(f"{target_language} is in the tuple.")
else:
    print(f"{target_language} is not in the tuple.")