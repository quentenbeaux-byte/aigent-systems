#!/usr/bin/env python3
"""Create nice-looking SVG placeholder images for each component"""

import os

output_dir = 'images/parts'
os.makedirs(output_dir, exist_ok=True)

# Component definitions with names and colors
components = {
    'ryzen-9950x.jpg': ('AMD Ryzen 9 9950X', '#ED1C24', 'CPU'),
    'threadripper-7960x.jpg': ('AMD Threadripper 7960X', '#ED1C24', 'CPU'),
    'epyc-9354.jpg': ('AMD EPYC 9354', '#ED1C24', 'CPU'),
    
    'rtx-4070ti.jpg': ('NVIDIA RTX 4070 Ti', '#76B900', 'GPU'),
    'rtx-4090.jpg': ('NVIDIA RTX 4090', '#76B900', 'GPU'),
    'rtx-6000-ada.jpg': ('NVIDIA RTX 6000 Ada', '#76B900', 'GPU'),
    
    'asus-x670e.jpg': ('ASUS X670E', '#0070C0', 'Motherboard'),
    'asus-wrx90e.jpg': ('ASUS WRX90E', '#0070C0', 'Motherboard'),
    'supermicro-h13dsi.jpg': ('Supermicro H13DSi', '#0070C0', 'Motherboard'),
    
    'kingston-ddr5-ecc.jpg': ('Kingston DDR5 ECC', '#E2231A', 'Memory'),
    'samsung-rdimm.jpg': ('Samsung RDIMM DDR5', '#1428A0', 'Memory'),
    
    'samsung-990pro.jpg': ('Samsung 990 PRO', '#1428A0', 'Storage'),
    'samsung-pm9a3.jpg': ('Samsung PM9A3', '#1428A0', 'Storage'),
    
    'fractal-define7.jpg': ('Fractal Define 7', '#1E293B', 'Case'),
    'fractal-define7xl.jpg': ('Fractal Define 7 XL', '#1E293B', 'Case'),
    'supermicro-847.jpg': ('Supermicro SC847', '#1E293B', 'Case'),
    
    'corsair-rm750x.jpg': ('Corsair RM750x', '#FFD700', 'Power Supply'),
    'corsair-ax1000.jpg': ('Corsair AX1000', '#FFD700', 'Power Supply'),
    'corsair-ax1600i.jpg': ('Corsair AX1600i', '#FFD700', 'Power Supply'),
    
    'noctua-nhd15.jpg': ('Noctua NH-D15', '#8B4513', 'Cooling'),
    'noctua-u14s-tr5.jpg': ('Noctua NH-U14S TR5-SP6', '#8B4513', 'Cooling'),
    'noctua-u9-dx4677.jpg': ('Noctua NH-U9 DX-4677', '#8B4513', 'Cooling'),
    
    'network-port.jpg': ('Gigabit Ethernet', '#4B9CD3', 'Networking'),
    'intel-x550.jpg': ('Intel X550-T2', '#0071C5', 'Networking'),
    'intel-e810.jpg': ('Intel E810-XXV', '#0071C5', 'Networking'),
    'ipmi-bmc.jpg': ('IPMI/BMC', '#6B7280', 'Management'),
}

svg_template = '''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad{idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:0.8" />
      <stop offset="100%" style="stop-color:#1e293b;stop-opacity:0.9" />
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="url(#grad{idx})"/>
  <rect x="20" y="20" width="360" height="260" fill="none" stroke="{color}" stroke-width="2" opacity="0.3"/>
  
  <text x="200" y="100" font-family="Arial, sans-serif" font-size="14" font-weight="bold" 
        fill="#94a3b8" text-anchor="middle" letter-spacing="2">{category}</text>
  
  <text x="200" y="150" font-family="Arial, sans-serif" font-size="20" font-weight="bold" 
        fill="#f8fafc" text-anchor="middle">{name_line1}</text>
  <text x="200" y="175" font-family="Arial, sans-serif" font-size="20" font-weight="bold" 
        fill="#f8fafc" text-anchor="middle">{name_line2}</text>
  
  <circle cx="200" cy="230" r="3" fill="{color}" opacity="0.6"/>
  <circle cx="215" cy="230" r="3" fill="{color}" opacity="0.6"/>
  <circle cx="230" cy="230" r="3" fill="{color}" opacity="0.6"/>
</svg>'''

print(f"Creating {len(components)} enhanced placeholder images...")
created = 0

for filename, (name, color, category) in components.items():
    # Split long names across two lines
    words = name.split()
    if len(words) > 3:
        mid = len(words) // 2
        name_line1 = ' '.join(words[:mid])
        name_line2 = ' '.join(words[mid:])
    else:
        name_line1 = name
        name_line2 = ''
    
    svg_content = svg_template.format(
        idx=created,
        name_line1=name_line1,
        name_line2=name_line2,
        category=category.upper(),
        color=color
    )
    
    output_path = os.path.join(output_dir, filename)
    with open(output_path, 'w') as f:
        f.write(svg_content)
    
    created += 1
    print(f"✓ {filename} ({category})")

print(f"\n✅ Created {created} branded placeholder images")
print("These SVG images will display directly in browsers")
