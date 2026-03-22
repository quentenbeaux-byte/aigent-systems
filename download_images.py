#!/usr/bin/env python3
"""Download product images for Aigent Systems parts list"""

import urllib.request
import os

# Product image URLs (using direct links to manufacturer/retailer product images)
images = {
    # Scout parts
    'ryzen-9950x.jpg': 'https://m.media-amazon.com/images/I/51pN3dF6GHL._AC_SL1080_.jpg',
    'rtx-4070ti.jpg': 'https://m.media-amazon.com/images/I/81KGZ8W9nVL._AC_SL1500_.jpg',
    'asus-x670e.jpg': 'https://m.media-amazon.com/images/I/81m5v+jNHlL._AC_SL1500_.jpg',
    'kingston-ddr5-ecc.jpg': 'https://m.media-amazon.com/images/I/51xBT0z3rDL._AC_SL1000_.jpg',
    'samsung-990pro.jpg': 'https://m.media-amazon.com/images/I/81FPO8kZzTL._AC_SL1500_.jpg',
    'fractal-define7.jpg': 'https://m.media-amazon.com/images/I/71s3DsYfMUL._AC_SL1500_.jpg',
    'corsair-rm750x.jpg': 'https://m.media-amazon.com/images/I/61OKgIEfFbL._AC_SL1000_.jpg',
    'noctua-nhd15.jpg': 'https://m.media-amazon.com/images/I/81u3RYfHMBL._AC_SL1500_.jpg',
    'network-port.jpg': 'https://m.media-amazon.com/images/I/51+2XCHvHuL._AC_SL1200_.jpg',
    
    # Sentinel parts
    'threadripper-7960x.jpg': 'https://m.media-amazon.com/images/I/51GyYXWgusL._AC_SL1000_.jpg',
    'rtx-4090.jpg': 'https://m.media-amazon.com/images/I/81WJHVTP4JL._AC_SL1500_.jpg',
    'asus-wrx90e.jpg': 'https://m.media-amazon.com/images/I/91vJyHDKjyL._AC_SL1500_.jpg',
    'fractal-define7xl.jpg': 'https://m.media-amazon.com/images/I/71MqUexwGzL._AC_SL1500_.jpg',
    'corsair-ax1000.jpg': 'https://m.media-amazon.com/images/I/51G5YhzqdgL._AC_SL1000_.jpg',
    'noctua-u14s-tr5.jpg': 'https://m.media-amazon.com/images/I/61wrVLPgbBL._AC_SL1500_.jpg',
    'intel-x550.jpg': 'https://m.media-amazon.com/images/I/61zj3MbOcPL._AC_SL1500_.jpg',
    
    # Sovereign parts  
    'epyc-9354.jpg': 'https://m.media-amazon.com/images/I/51sFCB5u3fL._AC_SL1000_.jpg',
    'rtx-6000-ada.jpg': 'https://m.media-amazon.com/images/I/61MFNH8B-JL._AC_SL1500_.jpg',
    'supermicro-h13dsi.jpg': 'https://m.media-amazon.com/images/I/71iyGcfLdZL._AC_SL1500_.jpg',
    'samsung-rdimm.jpg': 'https://m.media-amazon.com/images/I/61YV7iuhZWL._AC_SL1500_.jpg',
    'samsung-pm9a3.jpg': 'https://m.media-amazon.com/images/I/61kO8r6zqvL._AC_SL1500_.jpg',
    'supermicro-847.jpg': 'https://m.media-amazon.com/images/I/61cKMK2zcDL._AC_SL1500_.jpg',
    'corsair-ax1600i.jpg': 'https://m.media-amazon.com/images/I/71gKWUeVyBL._AC_SL1500_.jpg',
    'noctua-u9-dx4677.jpg': 'https://m.media-amazon.com/images/I/71Jn3KWCJEL._AC_SL1500_.jpg',
    'intel-e810.jpg': 'https://m.media-amazon.com/images/I/61L+M3WVDLL._AC_SL1500_.jpg',
    'ipmi-bmc.jpg': 'https://m.media-amazon.com/images/I/61ZYTp+BOUL._AC_SL1500_.jpg',
}

output_dir = 'images/parts'
os.makedirs(output_dir, exist_ok=True)

# Set user agent to avoid being blocked
headers = {'User-Agent': 'Mozilla/5.0'}

print(f"Downloading {len(images)} product images...")
success = 0
failed = []

for filename, url in images.items():
    output_path = os.path.join(output_dir, filename)
    if os.path.exists(output_path):
        print(f"✓ {filename} (already exists)")
        success += 1
        continue
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            with open(output_path, 'wb') as f:
                f.write(data)
        print(f"✓ {filename}")
        success += 1
    except Exception as e:
        print(f"✗ {filename}: {str(e)}")
        failed.append(filename)

print(f"\nCompleted: {success}/{len(images)} images downloaded successfully")
if failed:
    print(f"Failed: {', '.join(failed)}")
