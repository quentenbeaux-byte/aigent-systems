#!/bin/bash
# Create simple SVG placeholders for each product

cd images/parts

cat > placeholder.jpg << 'EOF'
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="300" fill="#1e293b"/>
  <text x="200" y="150" font-family="Arial, sans-serif" font-size="20" fill="#64748b" text-anchor="middle">Component Image</text>
</svg>
EOF

# Copy placeholder for all components
for img in ryzen-9950x.jpg rtx-4070ti.jpg asus-x670e.jpg kingston-ddr5-ecc.jpg samsung-990pro.jpg fractal-define7.jpg corsair-rm750x.jpg noctua-nhd15.jpg network-port.jpg threadripper-7960x.jpg rtx-4090.jpg asus-wrx90e.jpg fractal-define7xl.jpg corsair-ax1000.jpg noctua-u14s-tr5.jpg intel-x550.jpg epyc-9354.jpg rtx-6000-ada.jpg supermicro-h13dsi.jpg samsung-rdimm.jpg samsung-pm9a3.jpg supermicro-847.jpg corsair-ax1600i.jpg noctua-u9-dx4677.jpg intel-e810.jpg ipmi-bmc.jpg; do
  cp placeholder.jpg "$img"
done

echo "Created $(ls -1 *.jpg | wc -l) placeholder images"
