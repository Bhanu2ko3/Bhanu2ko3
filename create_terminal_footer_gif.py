from PIL import Image, ImageDraw, ImageFont

width = 850
height = 175
frames_count = 60

terminal_lines = [
    "root@codebroai:~# ./init_system.sh --mode=production",
    "[+] Initializing CodebroAI Core Subsystems...",
    "[+] Loading AI Automation, Cloud ERP & Security Protocols... [OK]",
    "[+] Verifying System Integrity: 0 Errors // Status: CLEAN",
    "[+] ALL SYSTEMS OPERATIONAL AND SECURE",
    "root@codebroai:~# "
]

try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 12)
    font_bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 12)
except Exception:
    font = ImageFont.load_default()
    font_bold = font

frames = []

# Total typing frames: 40, Hold full screen frames: 20
typing_frames = 40
hold_frames = 20

for frame_idx in range(frames_count):
    img = Image.new('RGBA', (width, height), (5, 8, 5, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Outer Window Border
    draw.rectangle([1, 1, width - 2, height - 2], fill=None, outline=(0, 255, 0, 160), width=1)
    
    # 2. Window Title Bar
    draw.rectangle([2, 2, width - 3, 28], fill=(14, 22, 14, 255))
    draw.line([(2, 28), (width - 3, 28)], fill=(0, 255, 0, 80), width=1)
    
    # Terminal Window Buttons (Red, Yellow, Green)
    draw.ellipse([12, 10, 20, 18], fill=(255, 95, 86, 255))
    draw.ellipse([26, 10, 34, 18], fill=(255, 189, 46, 255))
    draw.ellipse([40, 10, 48, 18], fill=(39, 201, 63, 255))
    
    # Title Bar Text
    draw.text((62, 8), "root@codebroai: ~ (zsh)", fill=(0, 255, 0, 255), font=font_bold)
    draw.text((width - 135, 8), "[SECURE NODE]", fill=(0, 255, 0, 180), font=font)
    
    # 3. Typing Logic
    if frame_idx < typing_frames:
        lines_count = min(len(terminal_lines), int((frame_idx / typing_frames) * len(terminal_lines)) + 1)
    else:
        lines_count = len(terminal_lines)
        
    y_pos = 38
    for line_i in range(lines_count):
        line_text = terminal_lines[line_i]
        
        # If currently typing this line
        if frame_idx < typing_frames and line_i == lines_count - 1 and line_i < len(terminal_lines) - 1:
            line_progress = ((frame_idx * len(terminal_lines) / typing_frames) % 1.0)
            chars = max(1, int(len(line_text) * line_progress))
            display_text = line_text[:chars]
        else:
            display_text = line_text
            
        # Add blinking cursor to active line
        if line_i == lines_count - 1 and (frame_idx // 3) % 2 == 0:
            display_text += " ▋"
            
        # Syntax Highlight
        if display_text.startswith("root@codebroai"):
            draw.text((16, y_pos), display_text, fill=(0, 255, 0, 255), font=font_bold)
        elif "[OK]" in display_text or "CLEAN" in display_text:
            draw.text((16, y_pos), display_text, fill=(0, 255, 130, 240), font=font)
        else:
            draw.text((16, y_pos), display_text, fill=(160, 230, 160, 220), font=font)
            
        y_pos += 20

    frames.append(img)

# Save high FPS GIF
frames[0].save(
    'footer.gif',
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)
print("Perfect Hacking Terminal footer.gif generated!")
