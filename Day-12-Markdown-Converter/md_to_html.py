import os
import re

def convert_inline(text):
    # Bold **text**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic *text*
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Links [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    return text

def parse_markdown(md_text):
    html_lines = []
    lines = md_text.splitlines()
    in_list = False

    for line in lines:
        line_str = line.strip()

        # Heading 1
        if line_str.startswith("# "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h1>{line_str[2:]}</h1>")
            continue
        
        # Heading 2
        if line_str.startswith("## "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h2>{line_str[3:]}</h2>")
            continue

        # Heading 3
        if line_str.startswith("### "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h3>{line_str[4:]}</h3>")
            continue

        # Unordered List Items (- or *)
        if line_str.startswith("- ") or line_str.startswith("* "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            content = convert_inline(line_str[2:])
            html_lines.append(f"  <li>{content}</li>")
            continue
        elif in_list and line_str == "":
            html_lines.append("</ul>")
            in_list = False

        if line_str == "":
            continue

        # Standard Paragraph
        content = convert_inline(line_str)
        html_lines.append(f"<p>{content}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)

def convert_file(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"\nError: File '{input_file}' not found!\n")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            md_text = f.read()

        html_body = parse_markdown(md_text)
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Converted Document</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; color: #333; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        ul {{ margin-left: 20px; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_html)

        print(f"\nSuccessfully converted '{input_file}' ➔ '{output_file}'!\n")
    except Exception as e:
        print(f"\nError converting file: {e}\n")

def main():
    while True:
        print("MARKDOWN TO HTML CONVERTER")
        print("1. Convert Sample String")
        print("2. Convert File (.md ➔ .html)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            sample_md = "# Welcome\n\nThis is **bold** and *italic* text.\n\n- Task 1\n- Task 2\n\nVisit [GitHub](https://github.com)"
            print("\n--- SAMPLE MARKDOWN ---")
            print(sample_md)
            print("\n--- CONVERTED HTML OUTPUT ---")
            print(parse_markdown(sample_md))
            print()
        elif choice == "2":
            inp = input("Enter input markdown filename (e.g. sample.md): ").strip()
            out = input("Enter output html filename (e.g. index.html): ").strip()
            if inp and out:
                convert_file(inp, out)
            else:
                print("\nFilenames cannot be empty!\n")
        elif choice == "3":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == "__main__":
    main()