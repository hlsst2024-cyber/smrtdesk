// Footer subscribe - Mailchimp (Production)
var mcJSONP = 'https://smrtdesk.us4.list-manage.com/subscribe/post-json?u=548b82c7d5b0398148ccebafa&id=7ade717988&c=?';
var mcPostURL = 'https://smrtdesk.us4.list-manage.com/subscribe/post?u=548b82c7d5b0398148ccebafa&id=7ade717988';
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
    var originalText = subBtn.textContent;
    subBtn.textContent = 'Subscribing...';
    subBtn.style.pointerEvents = 'none';
    subBtn.style.opacity = '0.7';
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
        var m = data.msg || 'Something went wrong. Please try again.';
        alert(m.replace(/<[^>]*>/g, ''));
      }
    };
    script.src = mcJSONP + '&EMAIL=' + encodeURIComponent(email);
    script.onerror = function(){
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
  emailInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') { e.preventDefault(); subBtn.click(); }
  });
})();
