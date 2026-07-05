# smrtdesk.js 完整对比报告 — 2026-07-05 17:13

## 文件概览
- 文件大小: 2380 行
- PRODUCTS 中唯一 ASIN 数量: **89** 个
- 主分类: 5 个 (Office Furniture / Beds / Kitchen & Dining / Camping / Electronics)

---

## 第一轮修改（15:16~16:05 — 子分类按品类拆分）

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| 品类映射表包含所有主分类 | Office Furniture, Beds, Kitchen&Dining, Camping, Electronics | ✅ 5个主分类全部在 CATEGORIES 中 | ✅ |
| Office Furniture 子分类 | Standing Desk, Office Chairs, Storage Cabinets, Storage Shelves, Conference&Reception, Office Accessories | ✅ 6个子分类 | ✅ |
| Beds 子分类 | Single Beds, Bunk Beds, Loft Beds, Storage Metal Bed Frames | ✅ 4个子分类 | ✅ |
| Kitchen & Dining 子分类 | Kitchen Storage Furniture, Food Storage Container, Kitchen Organizer, Small Accessories, Cookware & Grilling | ✅ 5个子分类 | ✅ |
| Camping 子分类 | Tents & Shelters, Sleeping Gear, Camp Furniture, Camp Cooking, Camping Lighting, Safety & Tools, Accessories | ✅ 7个子分类 (但通过CAT_SLUG_ALIAS路由) | ✅ |
| Electronics 子分类 | Cell Phones, Computers, Audio, Cameras, Wearable, Car, Office, Smart Home, Gaming, Portable | ✅ 10个子分类 | ✅ |
| SUBCATEGORIES 映射表 | 所有子分类都有parentSlug指向主分类 | ✅ 26个条目，parent+parentSlug均正确 | ✅ |
| 子分类按 slug 过滤产品 | CAT_SLUG_ALIAS机制 + getSlugs() | ✅ 存在，Slug别名映射到产品的categorySlug | ✅ |
| 面包屑层级正确 | Home > 主分类 > 子分类 | ✅ 代码第2245-2250行，父分类+名称正确获取 | ✅ |
| 页面标题/描述与菜单名称一致 | title = cat.name + " - Expert Tested \| SmrtDesk" | ✅ 动态绑定 cat.name | ✅ |

**第一轮结论: ✅ 全部保留**

---

## 第二轮修改（16:05~16:23 — 子分类链接和产品）

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| Bunk Beds 链接 → slug `bunk-bed` | 子分类链接指向 `category.html?slug=bunk-bed` | ⚠️ 链接正确生成，但路由有BUG（见下方详细） | ⚠️ |
| Kitchen Storage Furniture 链接 → slug `kitchen-storage-organizer` | 子分类链接 | 同上方路由BUG | ⚠️ |
| Tents & Shelters 链接 → slug `camping-outdoors` | 子分类链接 | 同上方路由BUG | ⚠️ |
| Camping 6个子分类有产品 | 各有产品 | 见下方详细分析 | ⚠️ |
| Electronics 5个子分类有产品 | 各有产品 | 见下方详细分析 | ⚠️ |

### 🚨 关键路由BUG

**当前代码中 CATEGORIES 主分类的 key 与子分类的 slug 冲突：**

- `CATEGORIES["bunk-bed"]` = Beds（主分类） → `subcategories[1]` = `{ name: "Bunk Beds", slug: "bunk-bed" }` ← 冲突！
- `CATEGORIES["kitchen-storage-organizer"]` = Kitchen & Dining（主分类） → `subcategories[0]` = `{ name: "Kitchen Storage Furniture", slug: "kitchen-storage-organizer" }` ← 冲突！
- `CATEGORIES["camping-outdoors"]` = Camping（主分类） → `subcategories[0]` = `{ name: "Tents & Shelters", slug: "camping-outdoors" }` ← 冲突！

**当访问 `category.html?slug=bunk-bed` 时：**
1. 渲染器先查 `CATEGORIES["bunk-bed"]` → 命中 → 返回"Beds"主分类（含 subcategories）
2. `isSubcategory = false` → 展示 Beds 下所有子分类的产品

**所以点击"Bunk Beds"标签后，显示的是全部 Beds 产品（含 Single Beds, Loft Beds 等），而不是仅 Bunk Beds。**

### Camping 产品分析（当前 camping-outdoors = 10个产品）

| ASIN | 产品名 | 露营品类归属 |
|:-----|:------|:----------|
| B0DGXHWWSV | AKNEAR LED Rechargeable Headlamp 99000 High Lumens | 照明 / Headlamp |
| B0DDQB78L2 | Bolosy Oversized XL Camping Chair Heavy Duty 500LBS | 家具 / Chair |
| B0F9FXHF5S | CLIQ ClassiQ 2.0 Portable Camping Chair | 家具 / Chair |
| B00005OU9D | Coleman Classic 2-Burner Propane Gas Camping Stove | 烹饪 / Stove |
| B004J2GUP4 | Coleman Sundome 4-Person Camping Tent with Rainfly | 帐篷 / Tent |
| B09Q2Y62ZM | EchoSmile Instant Pop Up 2-Person Camping Tent | 帐篷 / Tent |
| B0G8JBLM77 | Elegear CumbreX 4 inch Thick Self-Inflating Sleeping Pad | 睡眠 / Pad |
| B0DTFHC4NC | REDCAMP 10'x10' Instant Canopy Tent with Sidewalls | 帐篷 / Canopy |
| B005188T90 | Stanley Adventure Even-Heat Camp Pro Cook Set | 烹饪 / Cook Set |
| B0CXWX4XY3 | VTOY Portable Camping Chair with Canopy Sun Shade | 家具 / Chair |

所有10个产品 categorySlug 都是 `camping-outdoors`（即 Tents & Shelters 子类），所以点击其他露营子分类（Sleeping Gear, Camp Furniture 等）时，CAT_SLUG_ALIAS 会回退到 `camping-outdoors` 显示全部露营产品。

**结论：6个子分类各自的产品分布不均匀 — 全部挤在 camping-outdoors 下。**

### Electronics 产品分析

Electronics 的10个子分类（cell-phones, computers-tablets, audio-headphones, cameras, wearable-tech, car-electronics, office-electronics, smart-home, gaming, portable-devices）—— 当前代码中**没有产品直接使用这些 slug**。它们仅存在于 CAT_SLUG_ALIAS 中做映射：

| Slug | 别名映射 | 实际有产品的 Slug |
|:-----|:---------|:----------------|
| cell-phones → | phone-accessories | phone-accessories (4个) |
| audio-headphones → | phone-accessories | phone-accessories (同上4个) |
| office-electronics → | laptop-accessories | laptop-accessories (5个) |
| smart-home → | smart-home-gadgets | smart-home-gadgets (5个) |
| portable-devices → | laptop-accessories + phone-accessories | 混合 |
| computers-tablets → | laptop-accessories | laptop-accessories (同上5个) |
| cameras → | laptop-accessories | laptop-accessories (同上5个) ⚠️ 不合理 |
| wearable-tech → | phone-accessories + smart-home-gadgets | 混合 |
| car-electronics → | laptop-accessories + phone-accessories | 混合 |
| gaming → | laptop-accessories + phone-accessories | 混合 |

**⚠️ Electronics 的5个子分类（cameras, wearable-tech, car-electronics, gaming, portable-devices）各有产品，但很多映射不合理（如 cameras 映射到 laptop-accessories）。**

---

## 第三轮修改（16:23~16:41 — 四大任务）

### 任务1：主分类链接修复

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| Beds 主分类 slug | 首页导航到Beds页面 | CATEGORIES key = `"bunk-bed"`，name = "Beds" | ✅ |
| Kitchen & Dining 主分类 slug | 首页导航 | CATEGORIES key = `"kitchen-storage-organizer"`，name = "Kitchen & Dining" | ✅ |
| Camping 主分类 slug | 首页导航 | CATEGORIES key = `"camping-outdoors"`，name = "Camping" | ✅ |

> ⚠️ 注意：这三个主分类的 CATEGORIES key 分别是 `bunk-bed`、`kitchen-storage-organizer`、`camping-outdoors`——这些 key 与子分类 slug 相同，导致上述路由冲突。

### 任务2：缺失图片

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| Branch Ergonomic Chair Pro (B0C4XMZP9Y) 图片 | `product_images/B0C4XMZP9Y.jpg` | ✅ `product_images/B0C4XMZP9Y.jpg` | ✅ |
| 之前缺图4个产品图片 | 应有正确图片 | ✅ 所有89个产品都有 `product_images/{ASIN}.jpg` 格式图片 | ✅ |
| Product Title 已改为真实产品名 | 真实产品名 | ✅ 所有产品 title 字段都是真实产品名（非 "Product Title"） | ✅ |

### 任务3：搜索功能

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| 搜索结果链接格式 | `product.html?asin=xxx` | ❌ 当前格式是 `product.html?id=xxx`（代码第2360行） | ❌ |
| 搜索框自动填回 | 搜索页读URL参数填回搜索框 | ⚠️ smrtdesk.js 中搜索入口用 `/search.html?s=xxx`，但 smrtdesk.js 本身没有搜索回填逻辑（可能在 search.html 内联？） | ⚠️ |
| 搜索页面返回结果 | 搜索页能从PRODUCTS匹配 | ⚠️ 搜索跳转到 `/search.html?s=xxx`，但 smrtdesk.js 中没有 search.html 的渲染逻辑（product.html 和 category.html 的渲染逻辑在这里） | ⚠️ |

### 任务4：乱码修复

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| 主页无 `�` 乱码字符 | 无乱码 | ✅ 全文搜索无 U+FFFD 字符 | ✅ |

---

## 第四轮修改（16:41~17:02 — 四大任务）

### 任务A：三个分类修复

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| Bunk Beds 只显示双层床 | slug=bunk-bed 仅过滤 bunk-bed 分类产品 | ❌ 路由冲突：`CATEGORIES["bunk-bed"]` = Beds主分类 → 显示全部Beds产品（含Single/Loft/Storage） | ❌ |
| Kitchen Storage Furniture 只显示厨房收纳 | slug=kitchen-storage-organizer 仅过滤 | ❌ 路由冲突：`CATEGORIES["kitchen-storage-organizer"]` = Kitchen&Dining主分类 | ❌ |
| Tents & Shelters 只显示帐篷 | slug=camping-outdoors 仅过滤帐篷 | ❌ 路由冲突：`CATEGORIES["camping-outdoors"]` = Camping主分类 → 显示全部10个露营产品 | ❌ |

**当前 Bunk Bed（categorySlug='bunk-bed'）产品（4个，全是真正的双层床）：**
1. B0DSDXBV89 - BTHFST Bunk Bed Twin Over Twin with Stairs...
2. B00R2OTYR2 - Coaster Home Furnishings Stephan Rustic Metal Full Over Full Bunk Bed
3. B0CMWQMF16 - DHP Twin Over Full Bunk Bed with Ladder and Guardrails
4. B0GS5GJ14G - Jocoevol Metal Bunk Bed Twin Over Twin with Storage Staircase

**当前 Kitchen Storage Furniture（categorySlug='kitchen-storage-organizer'）产品：0个**
→ 该 slug 没有直接产品，全靠 CAT_SLUG_ALIAS 映射

### 任务B：删除无效产品

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| Coleman Brazos 20°F Sleeping Bag | 已删除 | ✅ 不存在于PRODUCTS | ✅ |
| Bonnlo Full Size Bunk Bed | 已删除 | ✅ 不存在于PRODUCTS（仅在topPick的product ID引用中出现） | ✅ |
| 其他10个无效链接产品 | 已删除 | ✅ 全部不存在：Kaximilu/DlandHome/Eyheyl/VECELO/Yookidoo/Jea.Tech/Rainguard/Iroomy/VASAGLE Tree Bookshelf/等 | ✅ |

> ✅ **12个无效产品全部删除。当前 PRODUCTS 共 89 个产品。**

### 任务C：图片一致性

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| REDCAMP Canopy Tent 图片 | `product_images/B0DTFHC4NC.jpg` | ✅ `product_images/B0DTFHC4NC.jpg` | ✅ |
| Colamy Kirin Office Chair 图片 | `product_images/B0BD7Z94ZQ.jpg` | ✅ `product_images/B0BD7Z94ZQ.jpg`（自己的ASIN） | ✅ |
| 图片一致性（全89个） | 每个产品 image = product_images/{ASIN}.jpg | ✅ 全部产品 image 字段匹配自己的 ASIN | ✅ |

### 任务D：产品内页标题

| 改动项 | 预期 | 当前实际 | 状态 |
|:-------|:-----|:---------|:----:|
| product.html 标题绑定 | 动态从 PRODUCTS 读取 | ✅ `document.title = pageTitle`，其中 `pageTitle = p.title + ' - Expert Review \| SmrtDesk'` | ✅ |
| document.title 设置 | `document.title = pageTitle` (第2097行) | ✅ 动态 | ✅ |

---

## 📊 当前 PRODUCTS 完整列表（89个）

| # | ASIN | 产品名 | 分类 Slug |
|:--|:-----|:------|:----------|
| 1 | B0B27MDKXD | 5 PCS Large Fruit Containers for Fridge | food-storage-container |
| 2 | B0FDQK69GQ | Ailun 3 Pack Screen Protector for iPhone 17 Pro Max | phone-accessories |
| 3 | B0DGXHWWSV | AKNEAR LED Rechargeable Headlamp 99000 High Lumens | camping-outdoors |
| 4 | B088NRLMPV | Anker USB C to USB C Cable, 60W Fast Charging | laptop-accessories |
| 5 | B0B7JL46ZB | Anxxsu Metal Storage Locker, 55" Retro Black | steel-lockers |
| 6 | B0DGHMNQ5Z | Apple AirPods 4 Wireless Earbuds | phone-accessories |
| 7 | B0GJTFXNRX | Apple AirTag (2nd Generation) | phone-accessories |
| 8 | B0DCH8VDXF | Apple EarPods Headphones with USB-C Plug | phone-accessories |
| 9 | B0FKN2SR3L | Babyletto Lido Wave Convertible Low-Profile Bunk Bed | loft-bed |
| 10 | B09JTHT445 | Basics 3-Drawer Lockable Mobile File Cabinet | filing-cabinet |
| 11 | B0CQTPZNV8 | Basics Adjustable Dual Monitor Desk Mount | monitor-stand |
| 12 | B081H3Y5NW | Basics Classic Puresoft PU Padded Mid-Back Office Chair | office-chair |
| 13 | B0D9XYD75W | Basics Vertical File Cabinet, 2-Drawer, Letter Size | vertical-file-cabinet |
| 14 | B0DDQB78L2 | Bolosy Oversized XL Camping Chair Heavy Duty 500LBS | camping-outdoors |
| 15 | B085KBN2DN | Branch Duo Standing Desk | standing-desk |
| 16 | B0C4XMZP9Y | Branch Ergonomic Chair Pro | office-chair |
| 17 | B0DSDXBV89 | BTHFST Bunk Bed Twin Over Twin with Stairs | bunk-bed |
| 18 | B0DZT71QKT | BUTISOW Metal Lockers - 66" 5 Doors | steel-lockers |
| 19 | B0DT3Y1X96 | Castlery Seb Executive Desk | executive-desk |
| 20 | B0F9FXHF5S | CLIQ ClassiQ 2.0 Portable Camping Chair | camping-outdoors |
| 21 | B00R2OTYR2 | Coaster Home Furnishings Stephan Rustic Metal Full Over Full Bunk Bed | bunk-bed |
| 22 | B0BD7Z94ZQ | Colamy Ergonomic Office Chair (Kirin Series) | office-chair |
| 23 | B00005OU9D | Coleman Classic 2-Burner Propane Gas Camping Stove | camping-outdoors |
| 24 | B004J2GUP4 | Coleman Sundome 4-Person Camping Tent with Rainfly | camping-outdoors |
| 25 | B08G53L8B5 | DEVAISE 2 Drawer Metal File Cabinet, Fully Assembled | filing-cabinet |
| 26 | B0989HLF81 | DEVAISE 3 Drawer Mobile File Cabinet, Wood Lateral | filing-cabinet |
| 27 | B0C8HBFNMV | DHP Metal Loft Bed Twin Size with Desk and Bookshelf | loft-bed |
| 28 | B0CMWQMF16 | DHP Twin Over Full Bunk Bed with Ladder and Guardrails | bunk-bed |
| 29 | B09Q2Y62ZM | EchoSmile Instant Pop Up 2-Person Camping Tent | camping-outdoors |
| 30 | B0G8JBLM77 | Elegear CumbreX 4 inch Thick Self-Inflating Sleeping Pad | camping-outdoors |
| 31 | B082MLVXRR | ErGear Dual Monitor Stand Heavy Duty | monitor-stand |
| 32 | B0B41YH9B6 | ErGear Height Adjustable Electric Standing Desk 48x24 | standing-desk |
| 33 | B0FQM6QB48 | ErGear Single Monitor Arm for 13-34 Inch Screens | monitor-stand |
| 34 | B0CG1ZHD74 | Superday Metal Storage Cabinet, 72" Garage | garage-cabinets |
| 35 | B0DJ2XKJJT | FlexiSpot EN1 One-Piece Standing Desk | standing-desk |
| 36 | B081DFLV9K | Freshware Food Storage Containers [50 Set] | food-storage-container |
| 37 | B07Y8BXBX8 | GABRYLLY Ergonomic Office Chair High Back | office-chair |
| 38 | B01LYBQXRH | Gladiator Premier 3-Piece Garage Cabinet Set | garage-cabinets |
| 39 | B07773PQG7 | GORILLA GRIP powerGRIP Drawer Shelf and Cabinet Liner | cabinet-organizer |
| 40 | B0FPM4NYR5 | INTERGREAT Metal Storage Cabinet with Doors, 72" | cabinet-organizer |
| 41 | B0FFSBVFMP | Homhedy Farmhouse Bathroom Storage Cabinet with 2 Doors | cabinet-organizer |
| 42 | B07FLC2YDF | HON 2-Drawer Vertical File Cabinet, Letter Size | vertical-file-cabinet |
| 43 | B07T5SY43L | HUANUO FlowLift—Dual Monitor Stand | monitor-and-monitor-mount |
| 44 | B0GK7FVTR4 | HUANUO FlowLift Pro Monitor Arm for 13-32" Screens | monitor-and-monitor-mount |
| 45 | B07T3KCQ94 | HUANUO FlowLift Single Monitor Mount | monitor-and-monitor-mount |
| 46 | B0CB1FW5FC | INIU 45W Fast Charging Portable Charger 10000mAh | laptop-accessories |
| 47 | B0C4T3RQQC | INTERGREAT Metal Storage Cabinet with Lock, 72" H | cabinet-organizer |
| 48 | B0B283QP2N | iPhone Charger Fast Charging 2 Pack | laptop-accessories |
| 49 | B08ZCTL5HC | Iwell 67" Tall Bathroom Cabinet, 2 Doors & 1 Drawer | cabinet-organizer |
| 50 | B0GS5GJ14G | Jocoevol Metal Bunk Bed Twin Over Twin with Storage | bunk-bed |
| 51 | B0B4K1XH8Y | Kitsure Dish Drying Rack for Kitchen Counter | kitchen-utensils-gadgets |
| 52 | B09YVJN8R7 | Letaya 3 Drawer Mobile File Cabinet with Lock | filing-cabinet |
| 53 | B0C39QL3XY | Letaya Metal Storage Cabinet with Lock, 72" Tall | steel-lockers |
| 54 | B0F8HFLNQG | Lifewit Expandable Silverware Organizer | kitchen-utensils-gadgets |
| 55 | B0GXCJ1QYD | Mixcous Full Over Full Bunk Bed for Adults | heavy-duty-bunk |
| 56 | B0814MM9XV | Muscle Rack 4-Shelf Unit with Sides and Back | storage-shelves |
| 57 | B0C49H4BLG | NewAge Products Bold 3-Piece Garage Cabinet Set | garage-cabinets |
| 58 | B0F5PPDTVR | OPNICE Desk Organizers and Accessories, Dual Monitor Stand | countertop-storage-rack |
| 59 | B09DKH8XDS | Paper Towel Holder Black, Premium Stainless Steel | countertop-storage-rack |
| 60 | B0DPSJP47V | Paper Towel Holder Countertop, Anti Slip Weighted Base | countertop-storage-rack |
| 61 | B0CC27124P | Paper Towel Holder, Self Adhesive Under Cabinet Mount | countertop-storage-rack |
| 62 | B0DTFHC4NC | REDCAMP 10'x10' Instant Canopy Tent with Sidewalls | camping-outdoors |
| 63 | B08BR9HBZ3 | Rubbermaid Brilliance Glass Food Storage Containers Set of 9 | food-storage-container |
| 64 | B079M8FPTW | Rubbermaid Brilliance Tritan Plastic Food Storage Set of 5 | food-storage-container |
| 65 | B01M0QM2O7 | Sauder Select Storage Cabinet, Pantry Cabinet | storage-shelves |
| 66 | B07GNDDNMW | SIHOO M18 Ergonomic Office Chair | office-chair |
| 67 | B09PRGXY3Y | SIKADEER Under Sink Mat Waterproof 34" x 22" | countertop-storage-rack |
| 68 | B0C7L373XM | Simple Houseware Desk Dual Monitor Stand Riser | monitor-and-monitor-mount |
| 69 | B07Q79ZZJ6 | Single LCD Computer Monitor Stand Riser for 13-32 inch | monitor-and-monitor-mount |
| 70 | B0D6SX8VLQ | Premium Smart Speaker with Alexa | smart-home-gadgets |
| 71 | B09B8V1LZ3 | Smart Speaker with Alexa - Vibrant sounding | smart-home-gadgets |
| 72 | B09B2SBHQK | Compact Smart Display with Alexa - 2x bass | smart-home-gadgets |
| 73 | B0BLS3QJTX | Smart Display with Alexa, Spatial Audio | smart-home-gadgets |
| 74 | B0BFC7WQ6R | Smart Alarm Clock with Alexa | smart-home-gadgets |
| 75 | B0FF4KTKZL | SNTD Dish Drying Rack - Space-Saving | kitchen-utensils-gadgets |
| 76 | B005188T90 | Stanley Adventure Even-Heat Camp Pro Cook Set | camping-outdoors |
| 77 | B01H48094C | Sterilite 4-Shelf Cabinet, Lockable Utility Storage | storage-shelves |
| 78 | B0FJQDLXXM | SUPEER 6-Door Metal Storage Locker, 72" | steel-lockers |
| 79 | B0C8MGJD1F | Tallsen Garage Storage Cabinet with Lock, 71" | garage-cabinets |
| 80 | B0FNWM5WW8 | ukeetap Extra Thick Silicone Mat Waterproof 34" x 22" | countertop-storage-rack |
| 81 | B0DNTQ2YNT | Ukeetap Multi-Purpose Pull-Out Storage Organizers | cabinet-organizer |
| 82 | B0BHS4PNPL | UPLIFT V3 Standing Desk | standing-desk |
| 83 | B0BRXQ1DKF | VASAGLE 2-Drawer File Cabinet, Rolling | filing-cabinet |
| 84 | B0FF4STK4S | VASAGLE Storage Cabinet with Drawers, Cloud White | storage-shelves |
| 85 | B009S750LA | VIVO Dual Monitor Desk Mount STAND-V002 | monitor-and-monitor-mount |
| 86 | B0D7P6XKNP | Vtopmart 5 Pack 22oz Glass Storage Containers with Lids | food-storage-container |
| 87 | B0CXWX4XY3 | VTOY Portable Camping Chair with Canopy Sun Shade | camping-outdoors |
| 88 | B094QTGHNZ | WALI Computer Monitor Stand for Desk, Adjustable | monitor-and-monitor-mount |
| 89 | B0DGPZR6P1 | WALI Single Monitor Mount for 13-34 inch Screens | laptop-accessories |

---

## 📊 最终总结

### ✅ 已保留（43项）
- 第一轮：全部9项 ✅（品类映射、子分类、面包屑、标题描述）
- 第三轮任务1：3项 ✅（主分类slug正确）
- 第三轮任务2：3项 ✅（Branch Chair图片、所有产品图片、真实标题）
- 第三轮任务4：1项 ✅（无乱码）
- 第四轮任务B：12个无效产品全部删除 ✅
- 第四轮任务C：3项 ✅（图片一致性完美）
- 第四轮任务D：2项 ✅（标题动态绑定）

### ❌ 需要重做（6项）

| 优先级 | 问题 | 影响 |
|:------:|:-----|:-----|
| 🔴 **高** | **路由冲突 BUG**：Bunk Beds / Kitchen Storage Furniture / Tents & Shelters 三个子分类的 slug 与主分类 CATEGORIES key 冲突 | 点击任意这3个子分类标签后，显示的是整个主分类的产品而非仅该子分类 |
| 🟡 中 | **搜索结果链接格式**：当前用 `product.html?id=xxx`，预期应为 `product.html?asin=xxx` | 可能影响搜索页到产品页的跳转（取决于 search.html 的实现） |
| 🟡 中 | **搜索自动回填**：smrtdesk.js 中没有搜索页回填搜索词逻辑 | search.html 可能需要内联脚本处理（需检查 search.html） |
| 🟡 中 | **Camping 子分类产品分布**：10个产品全部 categorySlug=camping-outdoors，其他6个子分类(sleeping-gear, camp-furniture等)无产品但有 CAT_SLUG_ALIAS 回退映射 | 点击 Sleeping Gear 等子分类时通过 alias 回退显示 camping-outdoors 的10个产品，非精确分类 |
| 🟡 中 | **Electronics 子分类映射**：cameras→laptop-accessories、gaming→laptop-accessories 等映射不合理 | 用户可能困惑 |
| 🔴 **高** | **Kitchen Storage Furniture 无直接产品**：slug=kitchen-storage-organizer 的 categorySlug 没有产品，全靠 alias 包含 food-storage-container 等 | Kitchen Storage Furniture 子分类实际显示 Kitchen & Dining 全部产品 |

### 🔧 修复建议（核心修复）

**修复路由冲突的方案：** 在 Category Page Renderer 中，当 `catSlug` 在 CATEGORIES 中找到且 `isSubcategory=false` 时，检查该 slug 是否同时是某个主分类的子分类。如果是，按子分类模式处理。

或者更简单的方案：将 CATEGORIES 中 Beds 的 key 从 `"bunk-bed"` 改为 `"beds"`，Kitchen & Dining 从 `"kitchen-storage-organizer"` 改为 `"kitchen-dining"`，Camping 从 `"camping-outdoors"` 改为 `"camping"`。然后在产品数据中保持现有 categorySlug 不变。这样主分类和子分类的 slug 不再冲突。
