# Bing Webmaster 提交指南 — SmrtDesk

> 创建时间：2026-06-24
> 站点：https://www.smrtdesk.xyz/
> Sitemap：https://www.smrtdesk.xyz/sitemap.xml（含 199 页）

---

## 步骤 1：登录 Bing Webmaster Tools

1. 浏览器打开 **https://www.bing.com/webmasters**
2. 点击右上角 **Sign In**，用 **微软账号** 登录（Outlook/Hotmail/Live 都可以）
3. 如果没有微软账号，用任意邮箱注册一个免费 Microsoft 账号

---

## 步骤 2：添加站点

1. 登录后，在首页输入框输入：**smrtdesk.xyz**
2. 点击 **Add** 按钮

---

## 步骤 3：验证站点所有权

Bing 提供 3 种验证方式，按优先级排列：

### 推荐方案 A：HTML Meta 标签 ✅（最快）
1. 选择验证方式为 **HTML Meta Tag**
2. Bing 会生成一个类似这样的 meta 标签：
   ```html
   <meta name="msvalidate.01" content="XXXXXXXXXXXXXXXXXXXX" />
   ```
3. **把验证码发给小盈**，我来加到所有页面的 `<head>` 中并部署
4. 部署完成后（约 1 分钟），点击 **Verify** 按钮

### 备选方案 B：DNS 验证
1. 选择 **DNS** 方式
2. Bing 会生成一条 TXT 记录值
3. 在你的域名 DNS 管理后台（Cloudflare / Namecheap 等）添加 TXT 记录
4. 等待 DNS 生效（可能几小时），点击 Verify

### 备选方案 C：XML 文件上传
1. 下载 Bing 提供的 XML 验证文件
2. 把文件放到网站根目录（即 smrtdesk 项目根目录）
3. 告诉我文件名和内容，我来添加到项目

---

## 步骤 4：提交 Sitemap

验证通过后：
1. 左侧菜单点击 **Sitemaps**
2. 点击 **Submit sitemap**
3. 输入：`https://www.smrtdesk.xyz/sitemap.xml`
4. 点击 **Submit**

---

## 步骤 5：检查提交状态

提交后 24-48 小时内，Bing 会开始抓取：
1. 在 **Site Explorer** 中查看已索引页面数
2. 在 **URL Inspection** 中检查具体页面状态
3. 查看 **Search Performance** 获取搜索点击数据

---

## 已完成的技术准备

以下 SEO 优化已由小盈完成：
- ✅ 所有 197 页面 sitemap.xml 已就绪
- ✅ 产品页 Schema.org Product 结构化数据（含 price/rating/brand/offers）
- ✅ 分类页 CollectionPage schema
- ✅ 文章页 Article schema（含 datePublished/dateModified）
- ✅ 页面 canonical 链接
- ✅ Google Analytics (GA4) 已配置
- ✅ Google Search Console 已提交
- ✅ Google 站点验证已完成
- ✅ robots.txt 允许所有爬虫

---

## 额外建议（可选，有时间再做）

1. **Bing URL Submission API**：如果有大量新页面，可以用 API 批量提交
2. **IndexNow**：Bing 支持 IndexNow 协议，可以配置到 git push hook 中自动通知
3. **定期检查**：每 1-2 周登录查看搜索效果报告

---

如果遇到任何问题，截图发给小盈。
