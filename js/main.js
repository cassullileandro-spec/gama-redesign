/* GAMA Painting — interactions */

// header: solid on scroll
const header = document.querySelector('.site-header');
const onScroll = () => header.classList.toggle('is-solid', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// mobile menu
const toggle = document.querySelector('.nav-toggle');
const menu = document.querySelector('.mobile-menu');
if (toggle && menu) {
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.textContent = open ? 'Close' : 'Menu';
  });
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    menu.classList.remove('open');
    toggle.textContent = 'Menu';
  }));
}

// scroll reveal
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// before/after sliders
document.querySelectorAll('.ba').forEach(ba => {
  const range = ba.querySelector('input[type="range"]');
  const after = ba.querySelector('.ba__after');
  const handle = ba.querySelector('.ba__handle');
  if (!range) return;
  range.addEventListener('input', () => {
    after.style.clipPath = `inset(0 0 0 ${range.value}%)`;
    handle.style.left = `${range.value}%`;
  });
});

// FAQ: close siblings
document.querySelectorAll('.faq').forEach(faq => {
  faq.querySelectorAll('details').forEach(d => {
    d.addEventListener('toggle', () => {
      if (d.open) faq.querySelectorAll('details[open]').forEach(o => { if (o !== d) o.open = false; });
    });
  });
});

// gallery: load more (reveals 6 per click)
document.querySelectorAll('.load-more').forEach(btn => {
  btn.addEventListener('click', () => {
    const grid = btn.closest('section').querySelector('.masonry');
    const hidden = grid.querySelectorAll('img.is-hidden');
    [...hidden].slice(0, 6).forEach(img => img.classList.remove('is-hidden'));
    const left = grid.querySelectorAll('img.is-hidden').length;
    const counter = btn.querySelector('span');
    if (left === 0) btn.closest('.load-more-wrap').style.display = 'none';
    else if (counter) counter.textContent = `(+${left})`;
  });
});

// estimate form (demo submit)
document.querySelectorAll('form.form').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    form.querySelectorAll('.field, .btn').forEach(el => el.style.display = 'none');
    const ok = form.querySelector('.form__ok');
    if (ok) ok.style.display = 'block';
  });
});
