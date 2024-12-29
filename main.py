import markdown
import sys

argv = sys.argv

if len(argv) != 4:
    print("Usage: python main.py markdown <input.md> <output.html>")
    sys.exit(1)

if argv[1] != "markdown":
    print("Usage: python main.py markdown <input.md> <output.html>")
    sys.exit(1)

with open(argv[2], "r") as f:
    markdown_txt = f.read()

# Convert markdown to HTML
html_output = markdown.markdown(markdown_txt, extensions=["tables", "fenced_code"])

with open(argv[3], "w") as f:
    f.write(html_output)
