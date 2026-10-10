(function () {
  const LIGHT = 'maisondouce';
  const DARK = 'maisondouce-dark';
  const htmlEl = document.documentElement;
  const btn = document.getElementById('themeToggle');

  function syncIcons(theme) {
    if (!btn) return;
    const sun = btn.querySelector('.sun-i');
    const moon = btn.querySelector('.moon-i');
    if (!sun || !moon) return;
    const isDark = theme === DARK;
    // en mode clair on montre la lune (=> passer en sombre), et inversement
    sun.classList.toggle('hidden', !isDark);
    moon.classList.toggle('hidden', isDark);
  }

  syncIcons(htmlEl.getAttribute('data-theme'));

  if (btn) {
    btn.addEventListener('click', () => {
      const current = htmlEl.getAttribute('data-theme') === DARK ? LIGHT : DARK;
      htmlEl.setAttribute('data-theme', current);
      document.cookie = 'theme=' + current + ';path=/;max-age=31536000;samesite=lax';
      syncIcons(current);
    });
  }
})();

const header = document.getElementById('header');
const progress = document.getElementById('scrollProgress');

if (header) {
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    header.classList.toggle('scrolled', y > 30);
    if (progress) {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      progress.value = h > 0 ? (y / h) * 100 : 0;
    }
  });
}

const revealEls = document.querySelectorAll('.reveal');
if (revealEls.length) {
  const io = new IntersectionObserver(
    (entries) => entries.forEach((entry) => { if (entry.isIntersecting) entry.target.classList.add('in'); }),
    { threshold: 0.1 }
  );
  revealEls.forEach((el) => io.observe(el));
}

document.querySelectorAll('.dropdown-content a').forEach((a) => {
  a.addEventListener('click', () => { if (document.activeElement) document.activeElement.blur(); });
});

function handleSubmit(e) {
  e.preventDefault();
  alert("Merci ! (Démo — formulaire à connecter côté serveur.)");
  e.target.reset();
}
