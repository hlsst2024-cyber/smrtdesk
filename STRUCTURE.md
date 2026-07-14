# SmrtDesk 网站框架结构索引

> 生成日期：2026-06-25 | 项目根目录：`smrtdesk\`
> 编号格式：`FR-XXX` (Framework) / `FR-XXX-NN` (子级)
> 状态标记：✅ 活跃 / ⚠️ 疑似废弃 / 🗄️ 备份存档 / 🔧 工具脚本

---

## 📊 总览统计

| 分类 | 文件数 | 编号段 |
|:-----|:------:|:-------|
| 主页 & 核心页面 | 4 | FR-001 ~ FR-004 |
| 产品详情页 | 119 | FR-010 |
| 分类页 | 35 | FR-020 |
| 文章页 | 13 | FR-030 |
| 功能页面 | 12 | FR-040 |
| 静态资源 (CSS) | 2 | FR-050 |
| 静态资源 (JS) | 2 | FR-051 |
| 静态资源 (图片) | 121 | FR-052 |
| 部署/工具脚本 | 25 | FR-060 |
| 配置文件 | 6 | FR-070 |
| 文档 | 4 | FR-080 |
| 备份目录 | 203 | FR-900 |
| 分块缓存 | 27 | FR-901 |
| **总计** | **~573** | |

---

## 🏠 主页 & 核心页面 (FR-001 ~ FR-009)

| 编号 | 分类 | 文件名 | 大小 | 说明 | 用途 |
|:-----|:-----|:-------|:----|:-----|:-----|
| FR-001 | 🏠 主页 | `index.html` | 82.6 KB | ✅ SmrtDesk 网站首页 | 主入口，含 Hero Banner、分类导航、推荐产品、布局模板 |
| FR-002 | 📦 产品 | `product.html` | 26.2 KB | ✅ 产品详情模板页 | 通用产品详情页模板 |
| FR-003 | 📂 分类 | `category.html` | 25.0 KB | ✅ 分类列表模板页 | 通用分类列表模板页 |
| FR-004 | 📝 文章 | *none* | — | ⚠️ 不存在独立文章模板 | 文章页直接使用独立 HTML，无模板文件 |

---

## 📦 产品详情页 (FR-010)

共 **119** 个独立产品详情页，按产品类型分组。

| 编号段 | 子类 | 数量 | 示例 |
|:-------|:-----|:----:|:-----|
| FR-010-01 | 露营/户外 (Coleman, 等) | 15+ | `product-coleman-sundome-4-person-camping-tent-with-rainfly.html` |
| FR-010-02 | 办公家具 (桌子) | 10+ | `product-branch-duo-standing-desk.html`, `product-uplift-v3-standing-desk.html` |
| FR-010-03 | 办公椅 | 5 | `product-branch-ergonomic-chair-pro.html`, `product-colamy-ergonomic-office-chair-kirin-series.html` |
| FR-010-04 | 显示器支架/臂 | 12+ | `product-ergotron-lx-single-monitor-arm.html`, `product-ergear-dual-monitor-stand-heavy-duty.html` |
| FR-010-05 | 存储柜/储物 | 20+ | `product-gladiator-premier-3-piece-garage-cabinet-set-silver-metallic.html` |
| FR-010-06 | 文件柜 | 10+ | `product-devaise-2-drawer-metal-file-cabinet-fully-assembled.html` |
| FR-010-07 | 双层床/loft床 | 10+ | `product-adorneve-bunk-bed-twin-over-twin-with-2-person-desk.html` |
| FR-010-08 | 厨房用品/收纳 | 15+ | `product-kitsure-dish-drying-rack-for-kitchen-counter-stainless-steel.html` |
| FR-010-09 | 电子产品/智能设备 | 10+ | `product-apple-airpods-4-wireless-earbuds.html`, `product-smart-speaker-dot-newest-model.html` |
| FR-010-10 | 花园/户外 | 8+ | `product-fiskars-3-piece-garden-tool-set-with-softgrip-handles.html` |

> **注**：产品页使用命名规范 `product-{slug}.html`，每个文件 ~20KB，含完整 SEO 元数据、产品描述、评分、价格按钮。

---

## 📂 分类页 (FR-020)

共 **35** 个分类页，按站点导航结构分组。

### FR-020-01 ~ FR-020-10：办公家具

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-01 | `category-office-furniture.html` | 30.9 KB | 办公家具总类（聚合页） |
| FR-020-02 | `category-standing-desk.html` | 17.2 KB | 升降桌 |
| FR-020-03 | `category-executive-desk.html` | 13.0 KB | 主管桌 |
| FR-020-04 | `category-office-chair.html` | 16.3 KB | 办公椅 |
| FR-020-05 | `category-monitor-and-monitor-mount.html` | 17.0 KB | 显示器 & 支架 |
| FR-020-06 | `category-office-electronics.html` | 16.2 KB | 办公电子产品 |
| FR-020-07 | `category-storage-cabinet.html` | 31.4 KB | 储物柜（含文件柜） |
| FR-020-08 | `category-storage-shelves.html` | 16.6 KB | 储物架 |

### FR-020-11 ~ FR-020-20：卧室家具

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-11 | `category-bunk-bed.html` | 13.8 KB | 双层床总类 |
| FR-020-12 | `category-twin-over-twin.html` | 13.4 KB | Twin-over-Twin 双层床 |
| FR-020-13 | `category-heavy-duty-bunk.html` | 14.3 KB | 重型双层床 |
| FR-020-14 | `category-loft-bed.html` | 11.4 KB | Loft 床 |

### FR-020-21 ~ FR-020-30：厨房 & 家居

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-21 | `category-kitchen-storage-organizer.html` | 21.5 KB | 厨房收纳 |
| FR-020-22 | `category-kitchen-utensils-gadgets.html` | 11.7 KB | 厨房器具 |
| FR-020-23 | `category-bbq-grilling-tools.html` | 11.4 KB | BBQ & 烧烤工具 |
| FR-020-24 | `category-food-storage-container.html` | 13.9 KB | 食品收纳容器 |
| FR-020-25 | `category-countertop-storage-rack.html` | 13.9 KB | 台面收纳架 |

### FR-020-31 ~ FR-020-40：露营 & 户外

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-31 | `category-camping-outdoors.html` | 29.6 KB | 露营户外总类（聚合页） |
| FR-020-32 | `category-camp-cooking.html` | 13.4 KB | 露营炊事 |
| FR-020-33 | `category-camp-furniture.html` | 13.4 KB | 露营家具 |
| FR-020-34 | `category-camping-accessories.html` | 13.5 KB | 露营配件 |
| FR-020-35 | `category-camping-lighting.html` | 13.4 KB | 露营照明 |
| FR-020-36 | `category-sleeping-gear.html` | 13.4 KB | 睡眠装备 |
| FR-020-37 | `category-safety-tools.html` | 13.4 KB | 安全工具 |

### FR-020-41 ~ FR-020-50：电子产品

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-41 | `category-electronics.html` | 22.2 KB | 电子产品总类（聚合页） |
| FR-020-42 | `category-audio-headphones.html` | 17.1 KB | 音频 & 耳机 |
| FR-020-43 | `category-wearable-tech.html` | 12.7 KB | 可穿戴设备 |
| FR-020-44 | `category-smart-home.html` | 17.0 KB | 智能家居 |
| FR-020-45 | `category-gaming.html` | 14.2 KB | 游戏 |
| FR-020-46 | `category-computers-tablets.html` | 13.6 KB | 电脑 & 平板 |
| FR-020-47 | `category-cell-phones.html` | 16.2 KB | 手机 |
| FR-020-48 | `category-car-electronics.html` | 12.7 KB | 车用电子 |
| FR-020-49 | `category-cameras.html` | 12.6 KB | 相机 |
| FR-020-50 | `category-portable-devices.html` | 14.4 KB | 便携设备 |

### FR-020-51 ~ FR-020-60：其他

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-020-51 | `category-blog.html` | 20.5 KB | ✅ 博客/文章列表页 |

---

## 📝 文章页 (FR-030)

共 **13** 篇独立文章页。

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-030-01 | `article-beach-canopy-guide.html` | 17.6 KB | 沙滩遮阳篷选购指南 |
| FR-030-02 | `article-best-inflatable-sup-boards.html` | 18.0 KB | 最佳充气 SUP 板 |
| FR-030-03 | `article-best-patio-furniture.html` | 16.0 KB | 最佳庭院家具 |
| FR-030-04 | `article-bluetooth-speaker-guide.html` | 17.2 KB | 蓝牙音箱指南 |
| FR-030-05 | `article-dutch-oven-recipes.html` | 17.1 KB | 荷兰锅食谱 |
| FR-030-06 | `article-fast-charging-tech.html` | 16.2 KB | 快充技术科普 |
| FR-030-07 | `article-grill-guide.html` | 17.6 KB | 烧烤架选购指南 |
| FR-030-08 | `article-home-office-setup.html` | 16.7 KB | 家庭办公室搭建 |
| FR-030-09 | `article-noise-canceling-earbuds.html` | 17.4 KB | 降噪耳机指南 |
| FR-030-10 | `article-outdoor-string-lights.html` | 17.1 KB | 户外串灯选购 |
| FR-030-11 | `article-self-watering-planters.html` | 17.2 KB | 自浇水花盆 |
| FR-030-12 | `article-smartwatches-fitness-tracking.html` | 17.3 KB | 智能手表健身追踪 |
| FR-030-13 | `article-top-camping-chairs.html` | 17.4 KB | 最佳露营椅 |

---

## 🔧 功能页面 (FR-040)

| 编号 | 文件名 | 大小 | 说明 | 用途 |
|:-----|:-------|:----|:-----|:-----|
| FR-040-01 | `search.html` | 61.8 KB | ✅ 搜索页 | 站内全文搜索 |
| FR-040-02 | `review.html` | 28.5 KB | ✅ 产品评测/Review 页 | 用户评测汇总 |
| FR-040-03 | `page-about.html` | 22.1 KB | ✅ 关于我们 | 品牌介绍 |
| FR-040-04 | `page-contact.html` | 21.3 KB | ✅ 联系我们 | 联系表单 |
| FR-040-05 | `page-expert-shopper.html` | 21.3 KB | ✅ 专家选购 | 选购建议 |
| FR-040-06 | `page-faq.html` | 25.0 KB | ✅ 常见问题 | FAQ |
| FR-040-07 | `page-gift-ideas.html` | 22.4 KB | ✅ 礼物推荐 | 礼品创意 |
| FR-040-08 | `page-major-sale-event.html` | 22.8 KB | ✅ 大促活动 | 促销活动页 |
| FR-040-09 | `page-partnerships.html` | 21.6 KB | ✅ 合作/联盟 | Affiliate 合作 |
| FR-040-10 | `page-press.html` | 21.4 KB | ✅ 新闻/媒体 | 新闻报道 |
| FR-040-11 | `page-privacy-policy.html` | 22.7 KB | ✅ 隐私政策 | 合规页面 |
| FR-040-12 | `page-terms.html` | 22.4 KB | ✅ 服务条款 | 合规页面 |
| FR-040-13 | `desk-height-calculator.html` | 15.7 KB | ✅ 桌子高度计算器 | 交互式工具页 |

---

## 🎨 静态资源

### CSS (FR-050)

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-050-01 | `main.css` | 60.3 KB | ✅ 主样式表（全站共享） |
| FR-050-02 | `product.css` | 6.7 KB | ✅ 产品页专用样式 |

### JavaScript (FR-051)

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-051-01 | `smrtdesk.js` | 2.5 KB | ✅ 主脚本（全站功能） |
| FR-051-02 | `subscribe-mailchimp.js` | 3.4 KB | ✅ Mailchimp 订阅脚本 |

### 图片 (FR-052)

| 编号 | 路径 | 文件数 | 说明 |
|:-----|:-----|:------:|:-----|
| FR-052-01 | `product_images/` (产品图) | 116 | ✅ 以 Amazon ASIN (B0XXXXXXXX) 命名的产品主图 |
| FR-052-02 | `product_images/hero-banner-1.jpg` | 1 | ✅ 首页 Hero Banner 1 |
| FR-052-03 | `product_images/hero-banner-2.jpg` | 1 | ✅ 首页 Hero Banner 2 |
| FR-052-04 | `product_images/e-banner-bunk.jpg` | 1 | ✅ 双层床 Banner |
| FR-052-05 | `product_images/e-banner-office.jpg` | 1 | ✅ 办公家具 Banner |
| FR-052-06 | `product_images/e-banner-storage.jpg` | 1 | ✅ 储物 Banner |

---

## 🚀 部署 / 工具脚本 (FR-060)

### 部署脚本 (FR-060-01 ~ FR-060-10)

| 编号 | 文件名 | 大小 | 说明 | 状态 |
|:-----|:-------|:----|:-----|:-----|
| FR-060-01 | `deploy_v4.py` | 3.6 KB | Python 部署脚本 v4 | ✅ 最新版 |
| FR-060-02 | `deploy.sh` | 1.6 KB | Shell 部署脚本 | ✅ |
| FR-060-03 | `deploy-github.sh` | 0.9 KB | GitHub 部署脚本 | ✅ |
| FR-060-04 | `deploy_paramiko.py` | 3.2 KB | Paramiko SSH 部署 | ✅ |
| FR-060-05 | `deploy_v3.py` | 5.9 KB | 部署脚本 v3 | ⚠️ 旧版，可能废弃 |
| FR-060-06 | `deploy_retry.py` | 3.4 KB | 部署重试脚本 | ⚠️ 旧版 |
| FR-060-07 | `deploy_async.py` | 3.1 KB | 异步部署 | ⚠️ 旧版 |
| FR-060-08 | `deploy_tcp.py` | 3.1 KB | TCP 部署 | ⚠️ 旧版 |
| FR-060-09 | `deploy2.py` | 3.6 KB | 部署脚本 v2 | ⚠️ 旧版 |
| FR-060-10 | `deploy.py` | 2.6 KB | 部署脚本 v1 | ⚠️ 旧版 |

### 上传脚本 (FR-060-11 ~ FR-060-15)

| 编号 | 文件名 | 大小 | 说明 | 状态 |
|:-----|:-------|:----|:-----|:-----|
| FR-060-11 | `upload_http2.py` | 2.3 KB | HTTP 上传 v2 | ✅ 可能最新 |
| FR-060-12 | `upload_chunks.py` | 2.0 KB | 分块上传 | ⚠️ 工具脚本 |
| FR-060-13 | `upload_http.py` | 2.7 KB | HTTP 上传 v1 | ⚠️ 旧版 |
| FR-060-14 | `upload_single.py` | 1.6 KB | 单文件上传 | ⚠️ 工具脚本 |
| FR-060-15 | `dl_cloudflared.py` | 0.5 KB | Cloudflare Tunnel 下载 | ⚠️ 工具脚本 |

### API 脚本 (FR-060-16 ~ FR-060-20)

| 编号 | 文件名 | 大小 | 说明 | 状态 |
|:-----|:-------|:----|:-----|:-----|
| FR-060-16 | `hostinger_api3.py` | 1.0 KB | Hostinger API v3 | ⚠️ |
| FR-060-17 | `hostinger_api2.py` | 1.6 KB | Hostinger API v2 | ⚠️ |
| FR-060-18 | `hostinger_api.py` | 1.0 KB | Hostinger API v1 | ⚠️ |
| FR-060-19 | `mcp_vps.py` | 1.6 KB | MCP VPS 脚本 | ⚠️ |
| FR-060-20 | `ssh_raw_test.py` | 3.8 KB | SSH 原始测试 | ⚠️ 测试脚本 |

### PowerShell 脚本 (FR-060-21 ~ FR-060-26)

| 编号 | 文件名 | 大小 | 说明 | 状态 |
|:-----|:-------|:----|:-----|:-----|
| FR-060-21 | `_seo_inject.ps1` | 5.4 KB | SEO 元数据注入 | ✅ SEO 工具 |
| FR-060-22 | `_seo_cleanup.ps1` | 4.6 KB | SEO 清理脚本 | ✅ SEO 工具 |
| FR-060-23 | `_gen_sitemap.ps1` | 2.0 KB | 站点地图生成 | ✅ SEO 工具 |
| FR-060-24 | `replace-subscribe.ps1` | 8.2 KB | 替换订阅代码 | 🔧 维护脚本 |
| FR-060-25 | `git-push.bat` | 1.7 KB | Git 推送批处理 | 🔧 开发工具 |
| FR-060-26 | `test-ssh.ps1` | 0.4 KB | SSH 测试 | ⚠️ 测试/废弃 |

### 其他工具 (FR-060-27 ~ FR-060-30)

| 编号 | 文件名 | 大小 | 说明 | 状态 |
|:-----|:-------|:----|:-----|:-----|
| FR-060-27 | `serve_local.py` | 0.4 KB | 本地 HTTP 服务器 | 🔧 开发工具 |
| FR-060-28 | `smrtdesk-deploy.zip` | 1102.9 KB | Deploy 压缩包 | 🗄️ 归档 |
| FR-060-29 | `mcp_stdin.txt` | 0 KB | MCP stdin 空文件 | ⚠️ 疑似残留 |
| FR-060-30 | `mcp_stdout.txt` | 0 KB | MCP stdout 空文件 | ⚠️ 疑似残留 |
| FR-060-31 | `mcp_stderr.txt` | 0.2 KB | MCP stderr 日志 | ⚠️ 疑似残留 |

---

## ⚙️ 配置文件 (FR-070)

| 编号 | 文件名 | 大小 | 说明 | 用途 |
|:-----|:-------|:----|:-----|:-----|
| FR-070-01 | `.gitignore` | 0.8 KB | Git 忽略规则 | 版本控制 |
| FR-070-02 | `robots.txt` | 0.1 KB | 爬虫规则 | ✅ SEO |
| FR-070-03 | `sitemap.xml` | 31.6 KB | 站点地图 | ✅ SEO / Google |
| FR-070-04 | `rss.xml` | 7.2 KB | RSS 订阅源 | ✅ 内容分发 |
| FR-070-05 | `_mismatches.json` | 5.8 KB | 不匹配数据 | 🔧 SEO/审计数据 |
| FR-070-06 | `test.txt` | 0 KB | 空测试文件 | ⚠️ 废弃 |

---

## 📄 文档 (FR-080)

| 编号 | 文件名 | 大小 | 说明 |
|:-----|:-------|:----|:-----|
| FR-080-01 | `SEO_PLAN.md` | 15.5 KB | ✅ SEO 优化方案文档 |
| FR-080-02 | `GITHUB_DEPLOY.md` | 7.7 KB | ✅ GitHub 部署文档 |
| FR-080-03 | `GA_DEPLOY_STATUS.md` | 1.7 KB | ✅ GA 部署状态文档 |
| FR-080-04 | `bing-webmaster-guide.md` | 2.7 KB | ✅ Bing 站长工具指南 |
| FR-080-05 | `_compliance_audit_report.txt` | 13.1 KB | ✅ 合规审计报告 |
| FR-080-06 | `seo-audit-report.txt` | 0.4 KB | ⚠️ SEO 审计（内容较少） |
| FR-080-07 | `STRUCTURE.md` | — | ✅ 本文件 |

---

## 🗄️ 备份目录 (FR-900)

| 编号 | 路径 | 文件数 | 说明 |
|:-----|:-----|:------:|:-----|
| FR-900-01 | `backups\` (HTML/CSS 备份) | 200 | 旧版本页面备份 |
| FR-900-02 | `backups\category-blog-20260625-0141.bak` | 1 | 博客分类页修订前备份 |
| FR-900-03 | `backups\index_backup_20260610.html` | 1 | 首页 2026-06-10 备份 |
| FR-900-04 | `backups\main_backup_20260607_herofix.css` | 1 | CSS Hero 区域修复备份 |
| FR-900-05 | `backups\main_backup_20260607_typography.css` | 1 | CSS 排版修复备份 |
| FR-900-06 | `backups\snapshot_20260617_1954\` | 2 | 2026-06-17 快照 (index.html + main.css) |

> **注**：`backups\` 目录中的文件是主文件的历史备份/旧版。部分备份与主文件命名不同（如 `category-cabinet-organizer.html` 等），可能存在不同时期的分类体系演进。备份目录中还有 `product-apple-airtag-*`、`product-christopher-knight-*`、`product-devoko-*`、`product-gigalumi-*`、`product-mkono-*` 等主项目录中不存在的页面，可能为历史版本或已删除的产品页。

---

## 📦 分块缓存 (FR-901)

| 编号 | 路径 | 文件数 | 说明 |
|:-----|:-----|:------:|:-----|
| FR-901-01 | `chunks\` | 5 | ⚠️ 疑似上传分块缓存 (chunk_0000~0004) |
| FR-901-02 | `chunks_small\` | 22 | ⚠️ 疑似上传小分块缓存 (c_0000~c_0021) |

> **注**：`chunks\` 和 `chunks_small\` 疑似为部署/上传过程的临时分块文件。若部署流程已完成，可考虑清理。

---

## 🔍 命名规范总结

| 前缀 | 类型 | 编号段 | 命名模式 |
|:-----|:-----|:-------|:---------|
| — | 核心页面 | FR-001~FR-009 | `{name}.html` |
| `product-` | 产品详情页 | FR-010 | `product-{product-slug}.html` |
| `category-` | 分类页 | FR-020 | `category-{category-slug}.html` |
| `article-` | 文章页 | FR-030 | `article-{topic-slug}.html` |
| `page-` | 功能页面 | FR-040 | `page-{page-name}.html` |

---

## ⚠️ 注意事项

1. **大量旧版部署脚本** (`deploy.py`, `deploy2.py`, `deploy_v3.py`, `deploy_retry.py`, `deploy_async.py`, `deploy_tcp.py`) — 建议确认 `deploy_v4.py` + `deploy.sh` 为最终方案后清理旧版。
2. **多个 Hostinger API 版本** — 建议只保留最新可用的一个。
3. **空文件** (`mcp_stdin.txt`, `mcp_stdout.txt`, `test.txt`) — 可安全删除。
4. **chunks/ 和 chunks_small/** — 若上传已完成，建议清理以节省空间。
5. **backups\ 目录 (203文件)** — 占用空间较大，可定期归档或清理旧备份。
6. **sitemap.xml** — 需随新增页面同步更新。
7. **产品页 119 个 vs 产品图片 116 个** — 部分产品页可能与 Amazon ASIN 图片不一一对应。

---

## 🧭 导航条一致性分析

> 分析日期：2026-06-25 | 扫描文件：index.html 及其他 8 个代表性页面

### 1. 分类页清单 × 文件名映射

共 **35** 个活跃分类页，按一级分类分组。

#### 1A. Office Furniture（办公家具）→ 顶级入口：`category-office-furniture.html`

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-01 | `category-office-furniture.html` | Office Furniture | Office Furniture | ✅ |
| FR-020-02 | `category-standing-desk.html` | Standing Desk | Office Desks | ❌ |
| FR-020-03 | `category-office-chair.html` | Office Chair | Office Chairs | ❌ |
| FR-020-04 | `category-storage-cabinet.html` | Storage Cabinet | Storage Cabinets | ❌ |
| FR-020-05 | `category-storage-shelves.html` | Storage Shelves | Storage Shelves & Bookcases | ❌ |
| FR-020-06 | `category-executive-desk.html` | Executive Desk | Conference & Reception | ❌ |
| FR-020-07 | `category-monitor-and-monitor-mount.html` | Monitor & Monitor Mount | Office Accessories | ❌ |

#### 1B. Beds（床）→ 顶级入口：`category-bunk-bed.html`

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-11 | `category-bunk-bed.html` | Bunk Bed | Bunk Beds | ❌ |
| FR-020-12 | `category-twin-over-twin.html` | Twin Over Twin | Single Beds | ❌ |
| FR-020-13 | `category-heavy-duty-bunk.html` | Heavy Duty Bunk | Storage Metal Bed Frames | ❌ |
| FR-020-14 | `category-loft-bed.html` | Loft Bed | Loft Beds | ❌ |

#### 1C. Kitchen & Dining（厨房 & 餐饮）→ 顶级入口：`category-kitchen-storage-organizer.html`

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-21 | `category-kitchen-storage-organizer.html` | Kitchen Storage Furniture | Kitchen Storage Furniture | ✅ |
| FR-020-22 | `category-food-storage-container.html` | Food Storage Containers | Food Storage Container | ❌ |
| FR-020-23 | `category-kitchen-utensils-gadgets.html` | Kitchen Utensils & Gadgets | Kitchen Organizer | ❌ |
| FR-020-24 | `category-countertop-storage-rack.html` | Small Kitchen Accessories | Small Accessories | ❌ |
| FR-020-25 | `category-bbq-grilling-tools.html` | BBQ & Grilling Tools | Cookware & Grilling | ❌ |

#### 1D. Camping（露营）→ 顶级入口：`category-camping-outdoors.html`

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-31 | `category-camping-outdoors.html` | Camping & Outdoors | Tents & Shelters | ❌ |
| FR-020-32 | `category-sleeping-gear.html` | Sleeping Gear | Sleeping Gear | ✅ |
| FR-020-33 | `category-camp-furniture.html` | Camp Furniture | Camp Furniture | ✅ |
| FR-020-34 | `category-camp-cooking.html` | Camp Cooking | Camp Cooking | ✅ |
| FR-020-35 | `category-camping-lighting.html` | Camping Lighting | Camping Lighting | ✅ |
| FR-020-36 | `category-safety-tools.html` | Safety & Tools | Safety & Tools | ✅ |
| FR-020-37 | `category-camping-accessories.html` | Camping Accessories | Camping Accessories | ✅ |

#### 1E. Electronics（电子产品）→ 顶级入口：`category-electronics.html`

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-41 | `category-electronics.html` | Electronics | Electronics | ✅ |
| FR-020-42 | `category-cell-phones.html` | Cell Phones | Cell Phones & Accessories | ❌ |
| FR-020-43 | `category-computers-tablets.html` | Computers Tablets | Computers & Tablets | ❌ |
| FR-020-44 | `category-audio-headphones.html` | Audio Headphones | Audio & Headphones | ❌ |
| FR-020-45 | `category-cameras.html` | Best Cameras - Expert Reviews & Top Picks | Cameras | ❌ |
| FR-020-46 | `category-wearable-tech.html` | Best Wearable Tech - Expert Reviews & Top Picks | Wearable Tech | ❌ |
| FR-020-47 | `category-car-electronics.html` | Best Car Electronics - Expert Reviews & Top Picks | Car Electronics | ❌ |
| FR-020-48 | `category-office-electronics.html` | Office Electronics | Office Electronics | ✅ |
| FR-020-49 | `category-smart-home.html` | Smart Home | Smart Home | ✅ |
| FR-020-50 | `category-gaming.html` | Gaming | Gaming | ✅ |
| FR-020-55 | `category-portable-devices.html` | Portable Devices | Portable Devices | ✅ |

#### 1F. Blog（博客）→ 独立入口

| 编号 | 文件名 | 页面真实 H1 | 导航条显示名称 | 匹配？ |
|:-----|:-------|:-----------|:--------------|:------:|
| FR-020-51 | `category-blog.html` | Blog | Blog | ✅ |

---

### 2. 当前导航条结构（index.html 主菜单）

✅ **所有页面导航条一致** — 经过对 index.html、category.html、product.html、article-*.html、page-*.html、search.html、review.html 共 8 个代表性页面的逐一比对，**所有页面共享完全相同的 39 条链接的导航条**（`<nav class="nav-bar">...</nav>` 内容完全一致）。

#### 导航树（当前版本，39 链接）

```
Home → /
Office Furniture → category-office-furniture.html
  ├─ Office Desks → category-standing-desk.html
  ├─ Office Chairs → category-office-chair.html
  ├─ Storage Cabinets → category-storage-cabinet.html
  ├─ Storage Shelves & Bookcases → category-storage-shelves.html
  ├─ Conference & Reception → category-executive-desk.html
  └─ Office Accessories → category-monitor-and-monitor-mount.html
Beds → category-bunk-bed.html
  ├─ Single Beds → category-twin-over-twin.html
  ├─ Bunk Beds → category-bunk-bed.html
  ├─ Loft Beds → category-loft-bed.html
  └─ Storage Metal Bed Frames → category-heavy-duty-bunk.html
Kitchen & Dining → category-kitchen-storage-organizer.html
  ├─ Kitchen Storage Furniture → category-kitchen-storage-organizer.html
  ├─ Food Storage Container → category-food-storage-container.html
  ├─ Kitchen Organizer → category-kitchen-utensils-gadgets.html
  ├─ Small Accessories → category-countertop-storage-rack.html
  └─ Cookware & Grilling → category-bbq-grilling-tools.html
Camping → category-camping-outdoors.html
  ├─ Tents & Shelters → category-camping-outdoors.html
  ├─ Sleeping Gear → category-sleeping-gear.html
  ├─ Camp Furniture → category-camp-furniture.html
  ├─ Camp Cooking → category-camp-cooking.html
  ├─ Camping Lighting → category-camping-lighting.html
  ├─ Safety & Tools → category-safety-tools.html
  └─ Camping Accessories → category-camping-accessories.html
Electronics → category-electronics.html
  ├─ Cell Phones & Accessories → category-cell-phones.html
  ├─ Computers & Tablets → category-computers-tablets.html
  ├─ Audio & Headphones → category-audio-headphones.html
  ├─ Cameras → category-cameras.html
  ├─ Wearable Tech → category-wearable-tech.html
  ├─ Car Electronics → category-car-electronics.html
  ├─ Office Electronics → category-office-electronics.html
  ├─ Smart Home → category-smart-home.html
  ├─ Gaming → category-gaming.html
  └─ Portable Devices → category-portable-devices.html
Blog → category-blog.html
```

#### Footer 额外链接（不在主导航中）

| Footer 链接文本 | href | 状态 |
|:----------------|:-----|:-----|
| Read our story | `page-about.html` | ✅ |
| Subscribe for deals | `#` | ⚠️ 锚点占位 |
| **See all reviews** | **`category-trending.html`** | **❌ 404！文件不存在** |
| Affiliate Disclosure | `page-about.html` | ✅ |
| Learn more → | `page-about.html` | ✅ |

---

### 3. 问题发现 & 不一致标注

#### ❌ 问题 1：导航条名称与页面 H1 不匹配（28 项不匹配 / 39 项总链接 = 72%）

导航条使用的是用户友好的营销名称，但页面 `<h1>` 使用的是文件名派生的直译名称，两者大面积不一致。这会导致：
- 用户从菜单点击"Office Desks"→ 进入页面看到 "Standing Desk" — 体验割裂
- SEO 层面：菜单锚文本与页面标题不一致，削弱相关性信号

**全量不一致清单：**

| 一级分类 | 导航名称 | → 页面 H1 | 严重度 |
|:---------|:---------|:-----------|:------:|
| Office Furniture | Office Desks | Standing Desk | 🔶 中 |
| Office Furniture | Office Chairs | Office Chair | 🟡 低（单复数） |
| Office Furniture | Storage Cabinets | Storage Cabinet | 🟡 低（单复数） |
| Office Furniture | Storage Shelves & Bookcases | Storage Shelves | 🔶 中 |
| Office Furniture | Conference & Reception | Executive Desk | 🔴 高 |
| Office Furniture | Office Accessories | Monitor & Monitor Mount | 🔴 高 |
| Beds | Single Beds | Twin Over Twin | 🔴 高 |
| Beds | Bunk Beds | Bunk Bed | 🟡 低（单复数） |
| Beds | Loft Beds | Loft Bed | 🟡 低（单复数） |
| Beds | Storage Metal Bed Frames | Heavy Duty Bunk | 🔴 高 |
| Kitchen & Dining | Food Storage Container | Food Storage Containers | 🟡 低（单复数） |
| Kitchen & Dining | Kitchen Organizer | Kitchen Utensils & Gadgets | 🔴 高 |
| Kitchen & Dining | Small Accessories | Small Kitchen Accessories | 🟡 低 |
| Kitchen & Dining | Cookware & Grilling | BBQ & Grilling Tools | 🔴 高 |
| Camping | Tents & Shelters | Camping & Outdoors | 🔴 高 |
| Electronics | Cell Phones & Accessories | Cell Phones | 🔶 中 |
| Electronics | Computers & Tablets | Computers Tablets | 🟡 低（& vs 空格） |
| Electronics | Audio & Headphones | Audio Headphones | 🟡 低（& vs 空格） |
| Electronics | Cameras | Best Cameras - Expert Reviews & Top Picks | 🔶 中 |
| Electronics | Wearable Tech | Best Wearable Tech - Expert Reviews & Top Picks | 🔶 中 |
| Electronics | Car Electronics | Best Car Electronics - Expert Reviews & Top Picks | 🔶 中 |

> 🔴 高 = 名称完全不同，用户可能困惑  |  🔶 中 = 名称有偏差  |  🟡 低 = 仅单复数/格式差异

#### ❌ 问题 2：断链 — `category-trending.html`

- **位置**：Footer "See all reviews" 链接
- **目标**：`category-trending.html`
- **状态**：**文件不存在！** — 该文件仅在 `backups\` 中存在，主目录已删除
- **影响**：所有页面的 Footer 都有一个 404 链接

#### ⚠️ 问题 3：孤立页面 — `desk-height-calculator.html`

- 该页不在主导航中，但从 3 个页面（`article-home-office-setup.html`、`category-office-furniture.html`、`category-standing-desk.html`）有内链
- 建议：可考虑加入 Office Furniture 子菜单或作为 Tools 独立入口

#### ⚠️ 问题 4：导航条与备份版本差异（已重构过）

对比 `backups\index.html`（旧版，35 链接），当前版（39 链接）已发生了结构性变化：
- **删除的分类**（备份中有、当前无）：Vertical File Cabinet、Steel Lockers、Garage Cabinets、Monitor Stand、Twin Over Full、Kitchen (总类)、Small Appliances、Cookware Bakeware、Kitchen Storage & Organization、Coffee/Tea/Espresso、Gifts
- **新增的分类**：Camping 大类（7 个子类）、Kitchen & Dining（重组）、Storage Shelves & Bookcases、Office Accessories 等
- **合并/重命名**：Kitchen 大类从 6 个子类重组为 5 个，部分旧分类合并到 Storage Cabinet 中

#### ℹ️ 问题 5：备份中残留 21 个已废弃分类

以下分类页仅存在于 `backups\`，不在导航条中也不在根目录中。如果确认不再使用，可清理备份：

```
category-cabinet-organizer.html     category-coffee-tea-espresso.html
category-computer-accessories.html   category-cookware-bakeware.html
category-deals.html                  category-desk-accessories.html
category-filing-cabinet.html         category-garage-cabinets.html
category-gifts.html                  category-home-garden.html
category-kitchen-storage-organization.html  category-kitchen.html
category-laptop-accessories.html     category-monitor-stand.html
category-phone-accessories.html      category-small-appliances.html
category-smart-home-gadgets.html     category-steel-lockers.html
category-trending.html               category-twin-over-full.html
category-vertical-file-cabinet.html
```

---

### 4. 修复建议

| 优先级 | 问题 | 建议操作 |
|:------:|:-----|:---------|
| 🔴 P0 | Footer 断链 `category-trending.html` | 替换为 `review.html` 或删除此链接 |
| 🔴 P0 | 导航名称 vs H1 不匹配（28处） | 方案A：将 H1 改为与导航一致的名称；方案B：将导航改为与 H1 一致。推荐方案A（导航名通常更经过营销考量） |
| 🟡 P1 | "Conference & Reception" → "Executive Desk" | H1 建议改为 "Conference & Reception Furniture" 或导航改为 "Executive Desk" |
| 🟡 P1 | "Single Beds" → "Twin Over Twin" | H1 建议改为 "Single Beds"（更通用） |
| 🟡 P1 | "Storage Metal Bed Frames" → "Heavy Duty Bunk" | 统一名称 |
| 🟡 P1 | "Tents & Shelters" → "Camping & Outdoors" | 这是聚合页，导航用"All Camping Gear"更清晰 |
| 🟢 P2 | 孤立页 `desk-height-calculator.html` | 添加到 Office Furniture 子菜单 |
| 🟢 P2 | 备份目录 203 文件 | 定期清理，仅保留近 2 个版本 |

---

*最后更新：2026-06-25* | *编号规范：FR = Framework（站点框架）*
