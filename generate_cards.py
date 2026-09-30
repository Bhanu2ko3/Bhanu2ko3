import os

os.makedirs('projects', exist_ok=True)

projects = [
    {
        'filename': 'projects/go_erp.svg',
        'title': 'CodebroAI GO ERP',
        'subtitle': 'Next-Gen Enterprise Resource Planning',
        'desc1': 'Cloud-native enterprise architecture for multi-tenant',
        'desc2': 'ERP operations, inventory, and analytics.',
        'tech': ['React', 'Supabase', 'PostgreSQL', 'Cloudflare R2'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/smartmenu.svg',
        'title': 'CodebroAI SmartMenu',
        'subtitle': 'Intelligent Digital Dining Platform',
        'desc1': 'Smart QR dining, order automation, kitchen workflow',
        'desc2': '&amp; enterprise inventory synchronization.',
        'tech': ['Next.js', 'Node.js', 'Docker', 'Oracle'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/pdf_service.svg',
        'title': 'CodebroAI PDF Engine',
        'subtitle': 'High-Performance Microservice',
        'desc1': 'FastAPI microservice for high-speed PDF generation,',
        'desc2': 'OCR extraction, and document processing.',
        'tech': ['Python', 'FastAPI', 'Next.js', 'Docker'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/dxesk.svg',
        'title': 'dxesk SaaS Platform',
        'subtitle': 'Scalable Cloud Service Desk',
        'desc1': 'Multi-channel customer support desk platform',
        'desc2': 'with automated ticketing &amp; AWS cloud scaling.',
        'tech': ['React.js', 'Node.js', 'AWS'],
        'status': 'LIVE',
        'cta': 'LAUNCH APP ↗'
    },
    {
        'filename': 'projects/cbis.svg',
        'title': 'CBIS Intelligence',
        'subtitle': 'Threat &amp; Blacklist Analytics Engine',
        'desc1': 'Security intelligence aggregator, IP verification',
        'desc2': 'engine, and automated threat logging system.',
        'tech': ['Java', 'Spring Boot', 'Next.js'],
        'status': 'INTERNAL',
        'cta': 'PRIVATE SYSTEM'
    },
    {
        'filename': 'projects/studio.svg',
        'title': 'CodebroAI Studio',
        'subtitle': 'Official Agency &amp; Digital Studio',
        'desc1': 'Enterprise digital transformation showcase and',
        'desc2': 'high-performance edge web infrastructure.',
        'tech': ['Next.js', 'React', 'Cloudflare'],
        'status': 'LIVE',
        'cta': 'VISIT STUDIO ↗'
    }
]

def generate_svg(p):
    tech_pills = ''
    x_offset = 24
    for t in p['tech']:
        width = len(t) * 8 + 16
        tech_pills += f'<rect x="{x_offset}" y="160" width="{width}" height="22" rx="4" fill="#0d170d" stroke="#00FF00" stroke-width="1" stroke-opacity="0.4"/><text x="{x_offset + width/2}" y="175" fill="#00FF00" font-family="monospace" font-size="11" text-anchor="middle">{t}</text>'
        x_offset += width + 8

    shell_name = p['title'].lower().replace(' ', '_').replace('.', '_').replace('&amp;', 'and')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="250" viewBox="0 0 480 250">
  <rect x="2" y="2" width="476" height="246" rx="10" ry="10" fill="#050805" stroke="#00FF00" stroke-width="1.5" stroke-opacity="0.6"/>
  <path d="M2 12 C2 6.477 6.477 2 12 2 L468 2 C473.523 2 478 6.477 478 12 L478 38 L2 38 Z" fill="#0e160e"/>
  <line x1="2" y1="38" x2="478" y2="38" stroke="#00FF00" stroke-width="1" stroke-opacity="0.3"/>
  
  <circle cx="20" cy="20" r="5" fill="#FF5F56"/>
  <circle cx="36" cy="20" r="5" fill="#FFBD2E"/>
  <circle cx="52" cy="20" r="5" fill="#27C93F"/>
  
  <text x="70" y="24" fill="#00FF00" font-family="'Fira Code', 'Courier New', monospace" font-size="12" font-weight="bold">&gt;_ {shell_name}.sh</text>
  
  <rect x="385" y="10" width="75" height="20" rx="4" fill="#002200" stroke="#00FF00" stroke-width="1"/>
  <text x="422.5" y="24" fill="#00FF00" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">● {p['status']}</text>
  
  <text x="24" y="72" fill="#FFFFFF" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="17" font-weight="bold">{p['title']}</text>
  <text x="24" y="93" fill="#00FF00" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="12" font-weight="600">{p['subtitle']}</text>
  
  <text x="24" y="118" fill="#A0A0A0" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="12">{p['desc1']}</text>
  <text x="24" y="136" fill="#A0A0A0" font-family="'Segoe UI', Ubuntu, sans-serif" font-size="12">{p['desc2']}</text>
  
  {tech_pills}
  
  <rect x="24" y="198" width="130" height="28" rx="5" fill="#00FF00" fill-opacity="0.12" stroke="#00FF00" stroke-width="1"/>
  <text x="89" y="216" fill="#00FF00" font-family="'Fira Code', monospace" font-size="11" font-weight="bold" text-anchor="middle">{p['cta']}</text>
</svg>'''
    
    with open(p['filename'], 'w') as f:
        f.write(svg)
    print(f"Generated {p['filename']}")

for p in projects:
    generate_svg(p)
