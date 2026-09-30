svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="140" height="45" viewBox="0 0 140 45">
  <rect width="140" height="45" rx="3" fill="#000000"/>
  <g transform="translate(14, 12)">
    <path fill="#00FF00" d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z"/>
  </g>
  <text x="78" y="27" fill="#00FF00" font-family="'DejaVu Sans', Verdana, Geneva, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" letter-spacing="1">LINKEDIN</text>
</svg>'''

with open('linkedin.svg', 'w') as f:
    f.write(svg_content)
print("linkedin.svg created successfully!")
