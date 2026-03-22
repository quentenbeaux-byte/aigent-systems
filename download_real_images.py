#!/usr/bin/env python3
"""Download actual product images from more reliable sources"""

import urllib.request
import os
import time

# Using publicly accessible product image CDNs and manufacturer sites
images = {
    # Scout parts
    'ryzen-9950x.jpg': 'https://cdn.mos.cms.futurecdn.net/Sk8hbZHqyMxBvP5TRbYE4j-1200-80.jpg',
    'rtx-4070ti.jpg': 'https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/ada/rtx-4070-ti/geforce-rtx-4070-ti-product-photo-001.png',
    'asus-x670e.jpg': 'https://dlcdnwebimgs.asus.com/gain/47D8C2F9-4B8D-44E3-82E2-C8B8E5C5D5F5/w717/h525',
    'kingston-ddr5-ecc.jpg': 'https://media.kingston.com/kingston/product/ktc-product-memory-server-premier-ddr5-ecc-rdimm-1-zm-lg.jpg',
    'samsung-990pro.jpg': 'https://images.samsung.com/is/image/samsung/p6pim/levant/mz-v9p2t0bw/gallery/levant-990-pro-pcie-4-0-nvme-m-2-ssd-mz-v9p2t0bw-537096886',
    'fractal-define7.jpg': 'https://www.fractal-design.com/app/uploads/2019/09/Define-7-Black-TG-LeftSide-NoODD.png',
    'corsair-rm750x.jpg': 'https://assets.corsair.com/image/upload/f_auto,q_auto/content/corsair-psu-rm750x-config-gallery-rm750x-2021-hero.png',
    'noctua-nhd15.jpg': 'https://noctua.at/pub/media/catalog/product/cache/5bbf9a8a9f2a0cdcca87c0f87be93603/n/o/noctua_nh_d15_1.jpg',
    'network-port.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Ethernet_RJ45_connector_p1160054.jpg/800px-Ethernet_RJ45_connector_p1160054.jpg',
    
    # Sentinel parts
    'threadripper-7960x.jpg': 'https://cdn.mos.cms.futurecdn.net/TKqWVUPNZU9Wk7YJrBYJKE-1200-80.jpg',
    'rtx-4090.jpg': 'https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/ada/rtx-4090/geforce-rtx-4090-product-photo-001.png',
    'asus-wrx90e.jpg': 'https://dlcdnwebimgs.asus.com/gain/1C8B5E5F-4A8E-4F3E-9E5F-C5F5E5C5D5F5/w717/h525',
    'fractal-define7xl.jpg': 'https://www.fractal-design.com/app/uploads/2020/03/Define-7-XL-Black-TG-LeftSide.png',
    'corsair-ax1000.jpg': 'https://assets.corsair.com/image/upload/f_auto,q_auto/content/AX1000-PSU-HERO.png',
    'noctua-u14s-tr5.jpg': 'https://noctua.at/pub/media/catalog/product/cache/5bbf9a8a9f2a0cdcca87c0f87be93603/n/o/noctua_nh_u14s_tr5_sp6_1.jpg',
    'intel-x550.jpg': 'https://www.intel.com/content/dam/www/public/us/en/images/product/16x9/ethernet-x550-t2-rwd.png.rendition.intel.web.480.270.png',
    
    # Sovereign parts  
    'epyc-9354.jpg': 'https://www.amd.com/content/dam/amd/en/images/products/processors/epyc/2483663-epyc-9004-chip-1260x709.jpg',
    'rtx-6000-ada.jpg': 'https://images.nvidia.com/aem-dam/Solutions/design-visualization/rtx-6000/proviz-rtx-6000-ada-3qtr-top-left-1280x720@2x.jpg',
    'supermicro-h13dsi.jpg': 'https://www.supermicro.com/files/images/products/Motherboard/H13DSI-N6_spec.jpg',
    'samsung-rdimm.jpg': 'https://images.samsung.com/is/image/samsung/assets/us/business/computing/memory-storage/dram-module/Server_DRAM_DDR5.jpg',
    'samsung-pm9a3.jpg': 'https://image-us.samsung.com/SamsungUS/ssd/PM9A3-1.jpg',
    'supermicro-847.jpg': 'https://www.supermicro.com/files/images/products/SuperChassis/4U/CSE-847_spec.jpg',
    'corsair-ax1600i.jpg': 'https://assets.corsair.com/image/upload/f_auto,q_auto/content/AX1600i-PSU-HERO.png',
    'noctua-u9-dx4677.jpg': 'https://noctua.at/pub/media/catalog/product/cache/5bbf9a8a9f2a0cdcca87c0f87be93603/n/o/noctua_nh_u9_dx_4677_1.jpg',
    'intel-e810.jpg': 'https://www.intel.com/content/dam/www/central-libraries/us/en/images/2022-11/e810-25gb-2p-rwd.png.rendition.intel.web.480.270.png',
    'ipmi-bmc.jpg': 'https://www.supermicro.com/files/images/products/SIMonitor/IPMI_Web_Interface.jpg',
}

output_dir = 'images/parts'
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

print(f"Downloading {len(images)} product images from manufacturer/tech sites...")
success = 0
failed = []

for filename, url in images.items():
    output_path = os.path.join(output_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read()
            # Check if we got actual image data (not error page)
            if len(data) > 1000:  # Real images are >1KB
                with open(output_path, 'wb') as f:
                    f.write(data)
                size_kb = len(data) / 1024
                print(f"✓ {filename} ({size_kb:.1f} KB)")
                success += 1
            else:
                print(f"✗ {filename}: Response too small ({len(data)} bytes)")
                failed.append(filename)
        time.sleep(0.5)  # Be polite to servers
    except Exception as e:
        print(f"✗ {filename}: {str(e)[:80]}")
        failed.append(filename)

print(f"\n✅ Downloaded: {success}/{len(images)} images")
if failed:
    print(f"❌ Failed ({len(failed)}): {', '.join(failed[:5])}{'...' if len(failed) > 5 else ''}")
