token = ''  # Bot Token
kwargs = {}  # {'proxy_url': 'socks5h://1.14.5.14:1080'}

data = [
    "信创的创，是泥头车的创",
    "快跑，是四核 2F",
    "信任信创的人，最终底裤都会被创没。",
    "我觉得我们主动去跟华为糊弄鬼的东西过不去，我们应该去 600 号自首",
    "什么事大号手机啊（战术后仰",
    "你想看的那个文档 我也想看",
    "RISCV，比信创更创。",
    "信不信随你，创肯定是创的",
    "“创死人不偿命的新设计”， 简称“创新”",
    "信创 BIOS 也不是什么好玩意",
    "体制外除了群友谁用信创啊（？",
    "相信信创就是在相信鬼",
    "都什么年代了还在折腾传统指令集",
    "GB/T 114514-2022 LoongArch 处理器指令集架构",
    "散热器也要自主（暴论",
    "我以为你对信创这么熟悉，这种事情怎么还想不明白",
    "广告位招租 欢迎各大R̶I̶S̶C̶厂在此投放BOSS直聘",
    "手写不了 VLIW 的话，就大声的用 NOP 掩盖过去罢！",
    "写代码的时候用 NOP delay slot 的话，作为 senior 的生活就结束了罢",
    "？我不是正在自己创自己吗（x",
    "他山之石，可以装进泥头车里运过来",
    "每个 vendor 都平等地有创死用户的机会",
    "相比之下，飞腾的机器没那么创",
    "想  创  人",
    "现有 rv 啥都没有啊（x",
    "对创",
    "软硬件互相创来创去是世界的一部分",
    "你 Robin 姐姐什么时候骗过你.png",
    "喜欢吗，主线内核起不来那种",
    "在创与被创中提升自我！",
    "PLCT 最不缺两样东西，一样是 HiFive Unmatched，另一样是 xyn",
    "OI群里有信创卖：OI-->xyn-->信创\n南大镜像站的黑暗主题叫对立：开源->xyn->音游",
    "集龙书也不能换不锈钢脸盆啊（",
    "景嘉微那个 GPU 是浪费沙子",
    "“我们比申威和飞腾市场做得好是因为他们根本没有销售”",
    "请立即就近寻求精神专科帮助",
    "群友最爱的 MIPS",
    "你感动了龙芯之神，祂决定帮你把电脑变成 3A5000",
    "你感动了 RISC-V 之神，祂决定帮你把电脑变成 HiFive Unmatched",
    "RV 不是美国龙芯么",
    "什么时候能用上群友画的机箱，装着群友设计的主板用着群友流的片",
    "abi：不是你的世界，请重试",
    "能动，不是很创",
    "*存在过特别定制的固件* 一听就很创人（x",
    "你想要的固件 我也想要",
    "信创产品诊疗指南（第n版）.pdf",
    "-“PLCT 是编译的黄埔”\n-“那龙芯就是 CPU 的黄埔”",
    "这信创怎么还能越创越有钱的",
    "让同济的基础设施都变成申威",
    "鲲鹏飞腾最多是泥头车 龙芯也就是个灵车 但是申威那简直就是地狱战舰",
    "你说的对, 毕竟第一代嘛, 难免用力过猛. 你看后面第二代 W515 就用了手机处理器, W525 就直接用机顶盒处理器了. 厂家也在慢慢进步嘛",
    "表面上不创，实际上刚踏出一步下一秒就已经在天上飞？（",
    "我宣布 D2000 是国货之光",
    "在你群我创的也是独树一帜的，你看我明明走在路上可以不被泥头车创，却每次都选择最创的",
    "高通海思多少有点卧龙凤雏的味道",
    "只能说华为的人真的很有创意",
    "Biren 能做出能用的东西的概率远大于信 Vivante 那帮人的",
    "龙芯也是内存条检测器，是正品的点不亮",
    "我也支持 RISC-V 中国分 V",
    "你想要的固件 我也想要"
]

chips = [
    "飞腾 FT-2000+/64",
    "飞腾 S2500",
    "飞腾 FT-1500A/16",
    "飞腾 D2000",
    "飞腾 FT-2000/4",
    "飞腾 FT-1500A/4",
    "飞腾 E2000",
    "飞腾 FT-2000A/2",
    "龙芯 3C5000",
    "龙芯 3A5000",
    "龙芯 3B5000",
    "龙芯 3C5000L",
    "龙芯 3A4000",
    "龙芯 3B4000",
    "龙芯 3A3000",
    "龙芯 3B3000",
    "龙芯 7A1000",
    "龙芯 7A2000",
    "龙芯 2K1000LA",
    "龙芯 2K0500",
    "龙芯 1H",
    "龙芯 1D",
    "龙芯 1C101",
    "龙芯 1C",
    "龙芯 1B",
    "LoongOS",
    "Loongnix",
    "UOS",
    "Deepin",
    "中标麒麟",
    "优麒麟",
    "银河麒麟",
    "开先 KX-6000",
    "开先 KX-5000",
    "开先 ZX-C+",
    "开先 ZX-C",
    "开胜 KH-30000",
    "开胜 KH-20000",
    "开胜 ZX-C+",
    "鲲鹏 920",
    "鲲鹏 916",
    "VisionFive",
    "VisionFive 2",
    "HiFive Unmatched",
    "PINE A64",
    "PINE A64-LTS",
    "ROCK64",
    "ROCKPro64",
    "PINE H64 Model B",
    "Quartz64 Model A",
    "Quartz64 Model B",
    "Pinebook",
    "Pinebook Pro",
    "PinePhone Pro",
    "PinePhone",
    "Star64",
    "PineNote",
    "PineTab",
    "PineTime",
]

pictures = [
    'https://i.imgur.com/FofTqys.jpg',
    'https://i.imgur.com/VvQ3fXS.jpg',
    'https://i.imgur.com/pfgV3G6.jpg',
    'https://i.imgur.com/In0D5kY.jpg',
    'https://i.imgur.com/lUvHtrN.jpg',
    'https://i.imgur.com/JJ0BpE1.jpg',
    'https://i.imgur.com/m4kWPSq.jpg',
    'https://i.imgur.com/PSsrvCq.jpg',
    'https://i.imgur.com/vzzIo5E.jpg',
    'https://i.imgur.com/oLVVUxl.jpg',
    'https://i.imgur.com/mxHXE8v.jpg',
    'https://i.imgur.com/z20Jm7x.jpg',
    'https://i.imgur.com/5tEFdi3.jpg',
    'https://i.imgur.com/VghXKKF.jpg',
    'https://i.imgur.com/2TIXen1.jpg',
    'https://i.imgur.com/iQE4ihW.jpg',
    'https://i.imgur.com/kXirdpc.jpg',
    'https://i.imgur.com/LSbBPcR.jpg',
    'https://i.imgur.com/O77e2IG.jpg',
    'https://i.imgur.com/iyTG7qE.jpg',
]
