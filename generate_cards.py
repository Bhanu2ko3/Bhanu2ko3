import os

os.makedirs('projects', exist_ok=True)

projects = [
    {
        'filename': 'projects/go_erp.svg',
        'title': 'CodebroAI GO ERP',
        'subtitle': 'Next-Gen Enterprise Resource Planning',
        'tech': ['React', 'Supabase', 'PostgreSQL', 'Cloudflare R2'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/smartmenu.svg',
        'title': 'CodebroAI SmartMenu',
        'subtitle': 'Intelligent Digital Dining Platform',
        'tech': ['Next.js', 'Node.js', 'Docker', 'Oracle'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/pdf_service.svg',
        'title': 'CodebroAI PDF Engine',
        'subtitle': 'High-Performance Microservice',
        'tech': ['Python', 'FastAPI', 'Next.js', 'Docker'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/dxesk.svg',
        'title': 'dxesk SaaS Platform',
        'subtitle': 'Scalable Cloud Service Desk',
        'tech': ['React.js', 'Node.js', 'AWS'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/cbis.svg',
        'title': 'CBIS Intelligence',
        'subtitle': 'Threat & Blacklist Analytics Engine',
        'tech': ['Java', 'Spring Boot', 'Next.js'],
        'status': 'INTERNAL',
        'cta': 'PRIVATE SYSTEM'
    },
    {
        'filename': 'projects/studio.svg',
        'title': 'CodebroAI Studio',
        'subtitle': 'Official Agency & Digital Studio',
        'tech': ['Next.js', 'React', 'Cloudflare'],
        'status': 'LIVE',
        'cta': 'VISIT STUDIO ↗'
    }
]

def generate_svg(p):
    tech_pills = ''
    x_offset = 20
    for t in p['tech']:
        width = len(t) * 7.5 + 14
        tech_pills += f'<rect x="{x_offset:.1f}" y="98" width="{width:.1f}" height="20" rx="4" fill="#0a140a" stroke="#1b381b" stroke-width="1"/><text x="{x_offset + width/2:.1f}" y="112" fill="#00FF00" font-family="monospace" font-size="10" text-anchor="middle">{t}</text>'
        x_offset += width + 6

    shell_name = p['title'].lower().replace(' ', '_').replace('.', '_').replace('&amp;', 'and')

    # Linux terminal header with Linux window controls (─ □ ✕) on the right and terminal icon prompt on left
    status_bg = "#032003" if p['status'] == 'LIVE' else "#201803"
    status_color = "#00FF00" if p['status'] == 'LIVE' else "#FFBB00"
    status_stroke = "#005500" if p['status'] == 'LIVE' else "#664400"

    title_clean = p['title'].replace('&', '&amp;')
    subtitle_clean = p['subtitle'].replace('&', '&amp;')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="165" viewBox="0 0 480 165">
  <!-- Subtle dark terminal card background & border -->
  <rect x="2" y="2" width="476" height="161" rx="8" ry="8" fill="#070c07" stroke="#1b2d1b" stroke-width="1.5"/>
  
  <!-- Linux Terminal Header Bar -->
  <path d="M2 10 C2 5.57 5.57 2 10 2 L470 2 C474.43 2 478 5.57 478 10 L478 34 L2 34 Z" fill="#0d160d"/>
  <line x1="2" y1="34" x2="478" y2="34" stroke="#1b2d1b" stroke-width="1"/>
  
  <!-- Linux Prompt & Title on Left -->
  <text x="14" y="22" fill="#00FF00" font-family="'Fira Code', 'DejaVu Sans Mono', 'Ubuntu Mono', monospace" font-size="11" font-weight="bold">codebro@linux:~$ ./{shell_name}.sh</text>
  
  <!-- Linux Terminal Window Controls (─ □ ✕) on Right -->
  <g fill="#456645" font-family="sans-serif" font-size="11" font-weight="bold">
    <text x="424" y="21">─</text>
    <text x="440" y="21">□</text>
    <text x="456" y="21">✕</text>
  </g>

  <!-- Status Tag -->
  <rect x="388" y="48" width="72" height="18" rx="4" fill="{status_bg}" stroke="{status_stroke}" stroke-width="1"/>
  <text x="424" y="61" fill="{status_color}" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">● {p['status']}</text>

  <!-- Card Body Content -->
  <text x="20" y="62" fill="#FFFFFF" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="15" font-weight="bold">{title_clean}</text>
  <text x="20" y="80" fill="#00DD00" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="11" font-weight="500">{subtitle_clean}</text>

  <!-- Tech Tags -->
  {tech_pills}

  <!-- Action Button -->
  <rect x="20" y="128" width="125" height="24" rx="4" fill="#00FF00" fill-opacity="0.08" stroke="#00CC00" stroke-opacity="0.6" stroke-width="1"/>
  <text x="82.5" y="144" fill="#00FF00" font-family="'Fira Code', monospace" font-size="10" font-weight="bold" text-anchor="middle">{p['cta']}</text>
</svg>'''
    
    with open(p['filename'], 'w') as f:
        f.write(svg)
    print(f"Generated {p['filename']}")

for p in projects:
    generate_svg(p)

