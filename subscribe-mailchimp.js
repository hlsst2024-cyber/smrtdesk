// ============================================================
// SmrtDesk Mailchimp Ajax Subscribe - PRODUCTION
// ============================================================
// Mailchimp Audience: SmrtDesk Products (ID: 7ade717988)
// API Key DC: us4
// ============================================================

var mcU = '548b82c7d5b0398148ccebafa';   // Mailchimp u 参数
var mcId = '7ade717988';                 // Mailchimp id (list/audience ID)
var mcDC = 'us4';                        // Datacenter from API key

// 构建 Mailchimp JSONP URL
var mcJSONP = 'https://smrtdesk.us4.list-manage.com/subscribe/post-json?u='
  + encodeURIComponent(mcU) + '&id=' + encodeURIComponent(mcId) + '&c=?';

// Mailchimp POST URL (fallback)
var mcPostURL = 'https://smrtdesk.us4.list-manage.com/subscribe/post?u='
  + encodeURIComponent(mcU) + '&id=' + encodeURIComponent(mcId);

// Footer subscribe - Mailchimp production
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
        // Strip HTML tags from Mailchimp error messages
        alert(msg.replace(/<[^>]*>/g, ''));
      }
    };

    script.src = mcJSONP + '&EMAIL=' + encodeURIComponent(email);
    script.onerror = function() {
      // Fallback: open Mailchimp subscribe page in new tab
      delete window[cb];
      if (script.parentNode) script.parentNode.removeChild(script);

      var f = document.createElement('form');
      f.method = 'POST';
      f.action = mcPostURL;
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

      subBtn.textContent = originalText;
      subBtn.style.pointerEvents = '';
      subBtn.style.opacity = '';
      emailInput.value = '';
    };

    document.head.appendChild(script);
  });

  // Enter key support
  emailInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      subBtn.click();
    }
  });
})();
