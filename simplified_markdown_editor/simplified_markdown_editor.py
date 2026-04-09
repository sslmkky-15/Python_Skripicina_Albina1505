def show_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def main():
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
    special_commands = ['!help', '!done']
    text_buffer = ""

    while True:
        choice = input("Choose a formatter: ")


        if choice == '!help':
            show_help()
            continue
        elif choice == '!done':

            with open("output.md", "w", encoding="utf-8") as f:
                f.write(text_buffer)
            break
        elif choice not in formatters:
            print("Unknown formatting type or command")
            continue


        if choice == 'header':
            while True:
                try:
                    level = int(input("Level: "))
                    if 1 <= level <= 6:
                        break
                    else:
                        print("The level should be within the range of 1 to 6.")
                except ValueError:
                    print("The level should be within the range of 1 to 6.")
            text = input("Text: ")
            text_buffer += f"{'#' * level} {text}\n"

        elif choice == 'link':
            label = input("Label: ")
            url = input("URL: ")
            text_buffer += f"[{label}]({url})"

        elif choice == 'new-line':
            text_buffer += "\n"

        elif choice in ['ordered-list', 'unordered-list']:
            while True:
                try:
                    rows = int(input("Number of rows: "))
                    if rows > 0:
                        break
                    else:
                        print("The number of rows should be greater than zero.")
                except ValueError:
                    print("The number of rows should be greater than zero.")

            for i in range(1, rows + 1):
                row_text = input(f"Row #{i}: ")
                if choice == 'ordered-list':
                    text_buffer += f"{i}. {row_text}\n"
                else:
                    text_buffer += f"* {row_text}\n"

        elif choice == 'plain':
            text = input("Text: ")
            text_buffer += text

        elif choice == 'bold':
            text = input("Text: ")
            text_buffer += f"**{text}**"

        elif choice == 'italic':
            text = input("Text: ")
            text_buffer += f"*{text}*"

        elif choice == 'inline-code':
            text = input("Text: ")
            text_buffer += f"`{text}`"


        print(text_buffer)

if __name__ == "__main__":
    main()