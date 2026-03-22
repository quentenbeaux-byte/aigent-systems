// Parts database for Scout, Sentinel, and Sovereign tiers
const partsData = {
    scout: {
        name: "Scout",
        price: "$2,835-$3,035",
        parts: [
            {
                category: "CPU",
                name: "AMD Ryzen 9 9950X",
                description: "16-core, 32-thread processor with 5.7GHz boost",
                image: "images/parts/ryzen-9950x.jpg"
            },
            {
                category: "GPU",
                name: "NVIDIA RTX 4070 Ti",
                description: "12GB GDDR6X, 7680 CUDA cores, excellent 1440p/4K performance",
                image: "images/parts/rtx-4070ti.jpg"
            },
            {
                category: "Motherboard",
                name: "ASUS Pro WS X670E-ACE",
                description: "AMD X670E chipset with ECC memory support, premium workstation features",
                image: "images/parts/asus-x670e.jpg"
            },
            {
                category: "RAM",
                name: "64GB DDR5 ECC (2x32GB)",
                description: "Kingston Server Premier 5600MHz ECC memory",
                image: "images/parts/kingston-ddr5-ecc.jpg"
            },
            {
                category: "Storage",
                name: "2x 2TB Samsung 990 Pro NVMe (RAID-1)",
                description: "PCIe 4.0 drives in mirrored configuration for data protection",
                image: "images/parts/samsung-990pro.jpg"
            },
            {
                category: "Case",
                name: "Fractal Design Define 7",
                description: "Mid-tower with sound dampening, excellent thermals and cable management",
                image: "images/parts/fractal-define7.jpg"
            },
            {
                category: "PSU",
                name: "Corsair RM750x 750W Gold",
                description: "80+ Gold certified, fully modular, 10-year warranty",
                image: "images/parts/corsair-rm750x.jpg"
            },
            {
                category: "CPU Cooler",
                name: "Noctua NH-D15",
                description: "Dual-tower design, whisper-quiet operation, premium cooling",
                image: "images/parts/noctua-nhd15.jpg"
            },
            {
                category: "Network",
                name: "2.5GbE Onboard",
                description: "Integrated 2.5 Gigabit Ethernet on motherboard",
                image: "images/parts/network-port.jpg"
            }
        ]
    },
    sentinel: {
        name: "Sentinel",
        price: "$7,330-$7,930",
        parts: [
            {
                category: "CPU",
                name: "AMD Threadripper 7960X",
                description: "24-core, 48-thread HEDT processor with massive PCIe lanes",
                image: "images/parts/threadripper-7960x.jpg"
            },
            {
                category: "GPU",
                name: "NVIDIA RTX 4090",
                description: "24GB GDDR6X, 16384 CUDA cores, flagship AI/gaming performance",
                image: "images/parts/rtx-4090.jpg"
            },
            {
                category: "Motherboard",
                name: "ASUS Pro WS WRX90E-SAGE",
                description: "TRX50 workstation board with 7x PCIe 5.0 slots, 10GbE networking",
                image: "images/parts/asus-wrx90e.jpg"
            },
            {
                category: "RAM",
                name: "128GB DDR5 ECC (4x32GB)",
                description: "Kingston Server Premier 5600MHz registered ECC memory",
                image: "images/parts/kingston-ddr5-ecc.jpg"
            },
            {
                category: "Storage",
                name: "4x 4TB Samsung 990 Pro NVMe (RAID-5)",
                description: "12TB usable capacity with parity protection",
                image: "images/parts/samsung-990pro.jpg"
            },
            {
                category: "Case",
                name: "Fractal Design Define 7 XL",
                description: "Full tower or Supermicro 4U rackmount chassis option",
                image: "images/parts/fractal-define7xl.jpg"
            },
            {
                category: "PSU",
                name: "Corsair AX1000 1000W Gold",
                description: "80+ Gold certified, fully modular, Corsair Link monitoring",
                image: "images/parts/corsair-ax1000.jpg"
            },
            {
                category: "CPU Cooler",
                name: "Noctua NH-U14S TR5-SP6",
                description: "Threadripper-optimized tower cooler with premium NF-A15 fan",
                image: "images/parts/noctua-u14s-tr5.jpg"
            },
            {
                category: "Network",
                name: "Dual Intel X550 10GbE NICs",
                description: "Dual-port 10 Gigabit Ethernet adapter with SR-IOV support",
                image: "images/parts/intel-x550.jpg"
            }
        ]
    },
    sovereign: {
        name: "Sovereign",
        price: "$19,400-$20,600",
        parts: [
            {
                category: "CPU",
                name: "Dual AMD EPYC 9354",
                description: "2x 32-core processors (64 cores total), 128 PCIe 5.0 lanes",
                image: "images/parts/epyc-9354.jpg"
            },
            {
                category: "GPU",
                name: "NVIDIA RTX 6000 Ada",
                description: "48GB GDDR6 ECC, 18176 CUDA cores, professional workstation GPU",
                image: "images/parts/rtx-6000-ada.jpg"
            },
            {
                category: "Motherboard",
                name: "Supermicro H13DSI-NT",
                description: "Dual socket SP5 board with 24 DDR5 slots, dual 10GbE, IPMI",
                image: "images/parts/supermicro-h13dsi.jpg"
            },
            {
                category: "RAM",
                name: "256GB DDR5 ECC RDIMM (8x32GB)",
                description: "Samsung registered ECC memory, 4800MHz",
                image: "images/parts/samsung-rdimm.jpg"
            },
            {
                category: "Storage",
                name: "8x 8TB Samsung PM9A3 NVMe (RAID-6)",
                description: "48TB usable enterprise NVMe with dual-parity protection",
                image: "images/parts/samsung-pm9a3.jpg"
            },
            {
                category: "Case",
                name: "Supermicro 4U CSE-847",
                description: "Rackmount chassis with 36 hot-swap drive bays, redundant cooling",
                image: "images/parts/supermicro-847.jpg"
            },
            {
                category: "PSU",
                name: "Dual Corsair AX1600i 1600W Platinum",
                description: "Redundant 80+ Platinum PSUs with Corsair Link monitoring",
                image: "images/parts/corsair-ax1600i.jpg"
            },
            {
                category: "CPU Cooler",
                name: "2x Noctua NH-U9 DX-4677",
                description: "Compact 92mm tower coolers optimized for dual-socket servers",
                image: "images/parts/noctua-u9-dx4677.jpg"
            },
            {
                category: "Network",
                name: "Dual Intel E810 25GbE NICs",
                description: "Dual-port 25 Gigabit Ethernet with PCIe 4.0 interface",
                image: "images/parts/intel-e810.jpg"
            },
            {
                category: "Management",
                name: "IPMI with BMC",
                description: "Dedicated baseboard management controller for remote management",
                image: "images/parts/ipmi-bmc.jpg"
            }
        ]
    }
};
