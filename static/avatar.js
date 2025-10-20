document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("a[href^='http']").forEach(link => {
    let url = new URL(link.href);
    // ignore internal links
    if (url.origin === window.location.origin) return;
    if (url.origin === 'https://waylonwalker.com') return;
    if (url.origin === 'https://wayl.one') return;
    let faviconUrl = "https://avatars.wayl.one/avatar/" + encodeURIComponent(url.origin) + "/";
    link.style.setProperty('--favicon-url', `url(${faviconUrl})`);
    link.setAttribute("data-favicon", faviconUrl);
  });
});
