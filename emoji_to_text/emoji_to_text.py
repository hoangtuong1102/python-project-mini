import emoji

# emoji to text function
def convert_emoji_to_text(text):
    return emoji.demojize(text)

if __name__ == "__main__":
    input_text = input("Enter a text with emoji: ")
    output_text = convert_emoji_to_text(input_text)

    print(output_text)