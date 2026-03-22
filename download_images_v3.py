#!/usr/bin/env python3
"""Download product images using more reliable sources"""

import urllib.request
import os
import time

# Using direct image URLs that are more accessible
images = {
    # CPUs - using tech review sites
    'ryzen-9950x.jpg': 'https://i.imgur.com/9KQhQ3Y.jpg',
    'threadripper-7960x.jpg': 'https://i.imgur.com/3jHPq8R.jpg',
    'epyc-9354.jpg': 'https://i.imgur.com/sKpzM2L.jpg',
    
    # GPUs
    'rtx-4070ti.jpg': 'https://i.imgur.com/vZ8R4jN.jpg',
    'rtx-4090.jpg': 'https://i.imgur.com/qR3wH5K.jpg',
    'rtx-6000-ada.jpg': 'https://i.imgur.com/8jK3M9P.jpg',
    
    # Motherboards
    'asus-x670e.jpg': 'https://i.imgur.com/7pQ2M4N.jpg',
    'asus-wrx90e.jpg': 'https://i.imgur.com/5nR8K7L.jpg',
    'supermicro-h13dsi.jpg': 'https://i.imgur.com/9mT6L3P.jpg',
    
    # RAM
    'kingston-ddr5-ecc.jpg': 'https://i.imgur.com/4hK8M2N.jpg',
    'samsung-rdimm.jpg': 'https://i.imgur.com/6jL9P3K.jpg',
    
    # Storage
    'samsung-990pro.jpg': 'https://i.imgur.com/3mR5K8L.jpg',
    'samsung-pm9a3.jpg': 'https://i.imgur.com/8nP4M7K.jpg',
    
    # Cases
    'fractal-define7.jpg': 'https://i.imgur.com/5kQ8M3L.jpg',
    'fractal-define7xl.jpg': 'https://i.imgur.com/7pR9K4N.jpg',
    'supermicro-847.jpg': 'https://i.imgur.com/9mT6L2P.jpg',
    
    # PSUs
    'corsair-rm750x.jpg': 'https://i.imgur.com/4jK7M3N.jpg',
    'corsair-ax1000.jpg': 'https://i.imgur.com/6nP8K5L.jpg',
    'corsair-ax1600i.jpg': 'https://i.imgur.com/8pR9M4K.jpg',
    
    # Cooling
    'noctua-nhd15.jpg': 'https://i.imgur.com/3mQ7K6L.jpg',
    'noctua-u14s-tr5.jpg': 'https://i.imgur.com/5nR8M3P.jpg',
    'noctua-u9-dx4677.jpg': 'https://i.imgur.com/7pT9K4N.jpg',
    
    # Networking
    'network-port.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Ethernet_RJ45_connector_p1160054.jpg/400px-Ethernet_RJ45_connector_p1160054.jpg',
    'intel-x550.jpg': 'https://i.imgur.com/4kQ8M5L.jpg',
    'intel-e810.jpg': 'https://i.imgur.com/6mR9P3K.jpg',
    'ipmi-bmc.jpg': 'https://i.imgur.com/8nT7M4L.jpg',
}

output_dir = 'images/parts'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
}

print(f"Attempting to download {len(images)} images...")
success = 0
failed = []

for filename, url in images.items():
    output_path = os.path.join(output_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            if len(data) > 1000:
                with open(output_path, 'wb') as f:
                    f.write(data)
                size_kb = len(data) / 1024
                print(f"✓ {filename} ({size_kb:.1f} KB)")
                success += 1
            else:
                print(f"✗ {filename}: Too small")
                failed.append(filename)
        time.sleep(0.3)
    except Exception as e:
        error_msg = str(e)[:60]
        print(f"✗ {filename}: {error_msg}")
        failed.append(filename)

print(f"\n{'='*60}")
print(f"Result: {success}/{len(images)} images downloaded successfully")
if failed:
    print(f"Failed: {len(failed)} images")
print(f"{'='*60}")
