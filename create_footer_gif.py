import math
from PIL import Image, ImageDraw

width = 1000
height = 80
frames_count = 36

frames = []

for f in range(frames_count):
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 1. Top & Bottom glowing accent lines
    draw.line([(0, 2), (width, 2)], fill=(0, 255, 0, 200), width=1)
    draw.line([(0, height - 2), (width, height - 2)], fill=(0, 255, 0, 200), width=1)
    
    # 2. Animated Cyber Sine Wave / Cyberpulse
    points = []
    phase = (f / frames_count) * 2 * math.pi
    for x in range(0, width + 5, 5):
        y = 40 + math.sin(x * 0.02 + phase) * 14 + math.cos(x * 0.04 - phase * 1.5) * 6
        points.append((x, y))
        
    for i in range(len(points) - 1):
        # Outer glow
        draw.line([points[i], points[i+1]], fill=(0, 255, 0, 70), width=4)
        # Inner core
        draw.line([points[i], points[i+1]], fill=(0, 255, 0, 230), width=2)
        
    # 3. Scanning Laser Node
    scan_x = int((f / frames_count) * width)
    scan_y = 40 + math.sin(scan_x * 0.02 + phase) * 14 + math.cos(scan_x * 0.04 - phase * 1.5) * 6
    draw.ellipse([scan_x - 7, scan_y - 7, scan_x + 7, scan_y + 7], fill=(0, 255, 0, 90))
    draw.ellipse([scan_x - 3, scan_y - 3, scan_x + 3, scan_y + 3], fill=(255, 255, 255, 255))
    
    frames.append(img)

# Save transparent GIF
frames[0].save(
    'footer.gif',
    save_all=True,
    append_images=frames[1:],
    duration=45,
    loop=0,
    disposition=2
)
print("Updated footer.gif with cyber pulse wave!")
