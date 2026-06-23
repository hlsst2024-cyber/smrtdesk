// ============================================================
// SmrtDesk Mailchimp Ajax Subscribe - 部署就绪版
// ============================================================
// 使用方法：
// 1. 大哥在 Mailchimp 注册后获取 u 和 id 参数
// 2. 填入下面 mcU 和 mcId
// 3. 运行批量替换脚本 replace-subscribe.ps1 部署到所有页面
// ============================================================

// ★★★ 替换为真实值 ★★★
var mcU = 'REPLACE_WITH_REAL_U';   // Mailchimp u 参数
var mcId = 'REPLACE_WITH_REAL_ID'; // Mailchimp id 参数

// 构建 Mailchimp JSONP URL（第4个字符是 datacenter）
var dc = mcU.length > 3 ? mcU.charAt(3) : '1';
var mcURL = 'https://smrtdesk.us' + dc + '.list-manage.com/subscribe/post-json?u='
  + encodeURIComponent(mcU) + '&id=' + encodeURIComponent(mcId) + '&c=?';

// Footer subscribe - Mailchimp 真实版
(function(){
  var subBtn = document.querySelector('.footer-subscribe-text');
  var emailInput = document.querySelector('.footer-input');
  if (!subBtn || !emailInput) return;
  
  subBtn.addEventListener('click', function(e) {
    e.preventDefault();
    var email = emailInput.value.trim();
    if (!email || email.indexOf('@') === -1 || email.indexOf('.') === -1) {
      alert('Please enter a valid email address');
      return;
    }
    
    // Loading state
    var originalText = subBtn.textContent;
    subBtn.textContent = 'Subscribing...';
    subBtn.style.pointerEvents = 'none';
    subBtn.style.opacity = '0.7';
    
    // JSONP call to Mailchimp
    var script = document.createElement('script');
    var cb = 'mc_cb_' + Math.random().toString(36).substr(2, 9);
    
    window[cb] = function(data) {
      delete window[cb];
      if (script.parentNode) script.parentNode.removeChild(script);
      
      subBtn.textContent = originalText;
      subBtn.style.pointerEvents = '';
      subBtn.style.opacity = '';
      
      if (data.result === 'success') {
        alert('Thanks for subscribing! Check your inbox to confirm.');
        emailInput.value = '';
      } else {
        var msg = data.msg || 'Something went wrong. Please try again.';
        // Mailchimp returns useful error messages like 
        // "xxx@yy.com is already subscribed"
        alert(msg.replace(/<[^>]*>/g, ''));
      }
    };
    
    script.src = mcURL + '&EMAIL=' + encodeURIComponent(email);
    // Mailchimp JSONP needs callback wrapped differently - use &c param
    // The cb param name varies; try both patterns
    script.onerror = function() {
      // Fallback: try without callback
      var f = document.createElement('form');
      f.method = 'POST';
      f.action = 'https://smrtdesk.us' + dc + '.list-manage.com/subscribe/post?u='
        + encodeURIComponent(mcU) + '&id=' + encodeURIComponent(mcId);
      f.target = '_blank';
      f.style.display = 'none';
      
      var i = document.createElement('input');
      i.type = 'hidden';
      i.name = 'EMAIL';
      i.value = email;
      f.appendChild(i);
      
      document.body.appendChild(f);
      f.submit();
      document.body.removeChild(f);
      
      delete window[cb];
      if (script.parentNode) script.parentNode.removeChild(script);
      subBtn.textContent = originalText;
      subBtn.style.pointerEvents = '';
      subBtn.style.opacity = '';
      emailInput.value = '';
    };
    
    document.head.appendChild(script);
  });
})();
