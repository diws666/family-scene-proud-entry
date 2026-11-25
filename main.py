import os

# Verified count: 140 characters (140 UTF-8 bytes), one line, no trailing newline.
LINE = "Dad taught the toaster to say good morning. Now it burns one side on purpose, so Mom laughs, and breakfast tastes like a family that stayed."

output_path = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.txt')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)
