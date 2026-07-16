#!/usr/bin/env python3
"""Generate all pages of the Gama Painting redesign from shared templates."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
U = "https://gamapainting.com/wp-content/uploads"

IMG = {
    "exterior": f"{U}/2024/01/Layer-0.png",
    "commercial": f"{U}/2024/01/Background.png",
    "interior": f"{U}/2024/01/IMG_9210.jpeg",
    "cabinet": f"{U}/2024/01/IMG_4669.jpeg",
    "about2": f"{U}/2024/01/About-Us-Gama-2.png",
    "about3": f"{U}/2024/01/About-Us-Gama-3.png",
    "b1": f"{U}/2024/04/01-BEFORE-scaled.jpg",
    "a1": f"{U}/2024/04/02-AFTER-scaled.jpg",
    "b2": f"{U}/2024/04/03-BEFORE-scaled.jpg",
    "a2": f"{U}/2024/04/04-AFTER-scaled.jpg",
    "b3": f"{U}/2024/04/01-BEFORE-copy-0-scaled.jpg",
    "a3": f"{U}/2024/04/02-AFTER-copy-0-scaled.jpg",
}

M1 = f"{U}/2024/01"
M3 = f"{U}/2024/03"

CATS = {
    "kitchen": [f"{M3}/{f}" for f in [
        "Copy-of-IMG_0206-scaled.jpg","Copy-of-IMG_0210-scaled.jpg","Copy-of-IMG_0212-scaled.jpg",
        "Copy-of-IMG_1281-1.jpeg","Copy-of-IMG_2056-1.jpeg","Copy-of-IMG_4539-1.jpg",
        "Copy-of-IMG_4540-1.jpg","Copy-of-IMG_7054-1.jpg","Copy-of-IMG_7064-1.jpg",
        "Copy-of-IMG_8583-scaled.jpg","Copy-of-IMG_8584-scaled.jpg","Copy-of-IMG_8587-scaled.jpg",
        "Copy-of-IMG_8588-scaled.jpg","Copy-of-IMG_8589-1-scaled.jpg","IMG_4669-1.jpeg",
        "IMG_4673-1.jpeg","IMG_4706-1.jpeg",
    ]],
    "interior": [f"{M3}/{f}" for f in [
        "Copy-of-IMG_9214.jpeg","Copy-of-IMG_9178.jpeg","Copy-of-IMG_7276-scaled-e1711499828228.jpg",
        "Copy-of-IMG_8582-scaled.jpg","Copy-of-IMG_7280-scaled-e1711499776309.jpg",
        "Copy-of-IMG_7166-scaled-e1711499798908.jpg","Copy-of-IMG_9153.jpeg","Copy-of-IMG_9130.jpeg",
        "Copy-of-IMG_9215.jpeg","Copy-of-IMG_4829.jpeg","Copy-of-IMG_9159.jpeg","Copy-of-IMG_4825.jpeg",
        "Copy-of-IMG_9191.jpeg","Copy-of-IMG_9210.jpeg","Copy-of-IMG_8573-scaled.jpg",
    ]] + [f"{M1}/1440-s-ocean-blvd-pompano-beach-fl-unit-11c-buildingphoto-{n}.jpg" for n in [2,17,22,14,16,15,5,6,9,4]],
    "venetian": [f"{M3}/Design-sem-nome-{n}-1.jpg" for n in [53,46,47,48,49,50,51,52]],
    "wood": [f"{M3}/{f}" for f in [
        "IMG_2066-1.jpg","9b85679a3113505c4c61a79a3f4ab6bd-1.jpg","c279322b4f9a1dd876b7389511fea13c-1.jpg",
        "077948675129db7155dabdc7bcd137fd-1.jpg","fa1d47ba34dd814a883018a3d07965df-1.jpg","IMG_2065-1.jpg",
        "1fc2b7b63b32ab5a715ec94a392367b0-1.jpg","4-Luxury-Bedrooms-With-Unique-Wall-Details-1.jpeg",
        "659ec2491013ad285159771c77882ebf-1.jpg","a457f08f65387e1c4855200722c396e9-1-e1711500785111.jpg",
        "IMG_2059-1.jpg","IMG_2060-1.jpg","IMG_2061-1.jpg","IMG_2062-1.jpg","IMG_2063-1.jpg",
        "IMG_2064-1-e1711500734324.jpg",
    ]],
    "commercial": [f"{M3}/{f}" for f in [
        "Copy-of-IMG_1621.jpeg","Copy-of-IMG_2213.jpeg","Copy-of-IMG_2262.jpeg","Copy-of-IMG_2717.jpeg",
        "Copy-of-IMG_2766.jpeg","Copy-of-IMG_3207.jpeg","Copy-of-IMG_3209.jpeg","Copy-of-IMG_3212.jpeg",
        "Copy-of-IMG_3213.jpeg","Copy-of-IMG_3222.jpeg","Copy-of-IMG_3229.jpeg","IMG_0616-scaled.jpg",
        "IMG_0620-scaled.jpg","IMG_0621-scaled.jpg","IMG_0622-scaled.jpg","IMG_0623-scaled.jpg",
        "IMG_1886.jpeg","IMG_1888.jpeg","IMG_1897.jpeg","IMG_1898.jpeg",
    ]],
    "exterior": [f"{M3}/{f}" for f in [
        "IMG_8100-scaled.jpg","Copy-of-Design-sem-nome-25.jpg",
        "86f0adedd2e83937c24993147e90d6c2l-m3296405744od-w640_h480_x2.webp",
        "86f0adedd2e83937c24993147e90d6c2l-m625282288od-w640_h480_x2.webp",
        "86f0adedd2e83937c24993147e90d6c2l-m3493032957od-w640_h480_x2.webp",
        "86f0adedd2e83937c24993147e90d6c2l-m3689311293od-w640_h480_x2.webp",
        "Copy-of-Design-sem-nome-26.jpg","Copy-of-Design-sem-nome-27.jpg","Copy-of-Design-sem-nome-28.jpg",
        "Copy-of-Design-sem-nome-29.jpg","Copy-of-Design-sem-nome-30.jpg","Copy-of-IMG_2103-scaled.jpg",
        "Copy-of-IMG_2106-scaled.jpg","Copy-of-IMG_2113-scaled.jpg","Copy-of-IMG_2114-scaled.jpg",
        "Copy-of-IMG_2117-scaled.jpg","Copy-of-IMG_2124-scaled.jpg","IMG_3445.jpeg","IMG_3525.jpeg",
        "IMG_3636.jpeg","IMG_3902.jpeg","IMG_3906.jpeg","IMG_7984-scaled.jpg",
    ]] + [f"{M1}/Copy-of-86f0adedd2e83937c24993147e90d6c2l-m3358513604od-w1024_h768_x2.webp",
          f"{M1}/IMG_3909.jpeg", f"{M1}/IMG_3917.jpeg"],
}

CAT_LABELS = {
    "kitchen": "Kitchen Cabinets",
    "interior": "Interior Painting",
    "venetian": "Venetian Plaster",
    "wood": "Custom Wood Finishing",
    "commercial": "Commercial",
    "exterior": "Exterior Painting",
}

PHONE = "(954) 204-9251"
PHONE_HREF = "tel:+19542049251"
EMAIL = "office@gamapainting.com"
ADDRESS = "471 S Flagler Avenue, Unit 78<br>Pompano Beach, FL 33060"


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>"""


def header(active="", static=False):
    cls = "site-header is-static" if static else "site-header"
    def a(href, label, key):
        act = ' class="active"' if key == active else ""
        return f'<a href="{href}"{act}>{label}</a>'
    return f"""
<header class="{cls}">
  <a class="brand" href="index.html" aria-label="Gama Painting — Home"><img class="brand-mark" src="img/logo.png" alt="Gama Painting"></a>
  <nav class="main-nav">
    {a("index.html#services", "Services", "services")}
    {a("about.html", "About", "about")}
    {a("gallery.html", "Gallery", "gallery")}
    {a("contact.html", "Contact", "contact")}
  </nav>
  <div class="header-cta">
    <a class="header-phone" href="{PHONE_HREF}">{PHONE}</a>
    <a class="btn" href="contact.html">Free Estimate</a>
    <button class="nav-toggle" aria-label="Menu">Menu</button>
  </div>
</header>
<nav class="mobile-menu">
  <a href="index.html">Home</a>
  <a href="index.html#services">Services</a>
  <a href="about.html">About</a>
  <a href="gallery.html">Gallery</a>
  <a href="contact.html">Contact</a>
</nav>"""


FOOTER = f"""
<footer class="site-footer">
  <div class="footer-grid">
    <div>
      <span class="label">(Explore)</span>
      <a href="index.html">Home</a>
      <a href="about.html">About Us</a>
      <a href="gallery.html">Gallery</a>
      <a href="contact.html">Contact</a>
    </div>
    <div>
      <span class="label">(Services)</span>
      <a href="interior-painting.html">Interior Painting</a>
      <a href="exterior-painting.html">Exterior Painting</a>
      <a href="commercial.html">Commercial</a>
      <a href="kitchen-cabinets.html">Kitchen Cabinets</a>
      <a href="wood-finishing.html">Custom Wood Finishing</a>
      <a href="faux-decorative.html">Faux &amp; Decorative</a>
    </div>
    <div>
      <span class="label">(Location)</span>
      <p>{ADDRESS}</p>
      <a href="https://maps.google.com/?q=471+S+Flagler+Avenue+Pompano+Beach+FL" target="_blank" rel="noopener">Open in Maps ↗</a>
    </div>
    <div>
      <span class="label">(Contact)</span>
      <a href="{PHONE_HREF}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="https://www.facebook.com/gamapainting/" target="_blank" rel="noopener">Facebook ↗</a>
      <a href="https://www.instagram.com/gamapainting1/" target="_blank" rel="noopener">Instagram ↗</a>
    </div>
  </div>
  <div class="footer-mark">Gama</div>
  <div class="footer-base">
    <span>©2026 Gama Painting, LLC. All rights reserved.</span>
    <span>Family owned &amp; operated — Est. 2008</span>
    <span>Licensed &amp; insured — Pompano Beach, FL</span>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>"""


CTA_FORM = f"""
<section class="section cta" id="estimate">
  <div class="cta-grid">
    <div class="reveal">
      <span class="label">(Get in touch)</span>
      <h2 class="display h-xl" style="margin:1.6rem 0 2rem">Color your<br>world <em>today</em></h2>
      <p>Tell us about your project and our team will reach out to schedule a free, no-pressure on-site estimate — usually within one business day.</p>
      <p style="margin-top:2.5rem"><a class="btn btn--light" href="{PHONE_HREF}">Call {PHONE}</a></p>
    </div>
    <form class="form reveal" novalidate>
      <div class="field"><label for="f-name">Full name</label><input id="f-name" type="text" placeholder="Your name" required></div>
      <div class="field-row">
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" type="tel" placeholder="(000) 000-0000" required></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" type="email" placeholder="you@email.com" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-zip">Project zip code</label><input id="f-zip" type="text" placeholder="33060"></div>
        <div class="field"><label for="f-city">City</label><input id="f-city" type="text" placeholder="Pompano Beach"></div>
      </div>
      <div class="field">
        <label for="f-type">Project type</label>
        <select id="f-type">
          <option>Kitchen Cabinet Refinishing</option>
          <option>Interior Painting</option>
          <option>Exterior Painting</option>
          <option>Commercial</option>
          <option>Wood Finishing / Decorative</option>
        </select>
      </div>
      <button class="btn btn--light" type="submit">Request free estimate</button>
      <p class="form__ok">Thank you — your message has been received. We will get back to you shortly.</p>
    </form>
  </div>
</section>"""


def page(filename, title, desc, body, active="", static_header=False):
    html = head(title, desc) + header(active, static_header) + body + FOOTER
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(html)
    print("wrote", filename)


# ----------------------------------------------------------------
# HOME
# ----------------------------------------------------------------

marquee_items = "".join(
    "<span>Interior</span><span>—</span><span>Exterior</span><span>—</span>"
    "<span><em>Kitchen Cabinets</em></span><span>—</span><span>Commercial</span><span>—</span>"
    "<span>Wood Finishes</span><span>—</span><span><em>Venetian Plaster</em></span><span>—</span>"
    for _ in range(2)
)

quotes_html = """
<div class="quotes reveal">
  <figure class="quote">
    <blockquote class="quote__text">They took on a kitchen remodel other painters wouldn't touch — difficult tile and all — and delivered flawlessly.</blockquote>
    <figcaption class="quote__who">Layne Cook — Kitchen Remodel</figcaption>
  </figure>
  <figure class="quote">
    <blockquote class="quote__text">Painting our cabinets felt stressful until this team showed up. Responsive, careful, and kind from start to finish.</blockquote>
    <figcaption class="quote__who">Donna LaVoie — Cabinet Painting</figcaption>
  </figure>
  <figure class="quote">
    <blockquote class="quote__text">We've trusted Gama with both our commercial property and our home. Same excellence, every single time.</blockquote>
    <figcaption class="quote__who">Larry Cook — Commercial &amp; Residential</figcaption>
  </figure>
  <figure class="quote">
    <blockquote class="quote__text">Flexible with our schedule, meticulous with the details — the quality of our full-home repaint was exceptional.</blockquote>
    <figcaption class="quote__who">Roger Lindemann — Full Home</figcaption>
  </figure>
</div>"""

faq_home = """
<div class="faq reveal">
  <details class="faq-item">
    <summary><span class="faq-item__num">( 1 )</span><span class="faq-item__q">How long will my project take?</span><span class="faq-item__icon">+</span></summary>
    <p class="faq-item__a">Kitchen cabinets are transformed in 7–8 days with our CRAFT-PRO method. Interior and exterior projects are scoped during your free on-site estimate, and we commit to the timeline before the first brush touches a wall.</p>
  </details>
  <details class="faq-item">
    <summary><span class="faq-item__num">( 2 )</span><span class="faq-item__q">Do you subcontract your work?</span><span class="faq-item__icon">+</span></summary>
    <p class="faq-item__a">Never. Every project is executed by our own trained, in-house team — the same craftsmen who have carried our name since 2008. It is how we guarantee the result.</p>
  </details>
  <details class="faq-item">
    <summary><span class="faq-item__num">( 3 )</span><span class="faq-item__q">Are you licensed and insured?</span><span class="faq-item__icon">+</span></summary>
    <p class="faq-item__a">Yes — Gama Painting, LLC is fully licensed and insured, and experienced in projects of every size, from a single room to entire commercial properties.</p>
  </details>
  <details class="faq-item">
    <summary><span class="faq-item__num">( 4 )</span><span class="faq-item__q">Which paints do you use?</span><span class="faq-item__icon">+</span></summary>
    <p class="faq-item__a">We work with premium products from Benjamin Moore and Sherwin-Williams, matched to each surface and to South Florida's climate.</p>
  </details>
  <details class="faq-item">
    <summary><span class="faq-item__num">( 5 )</span><span class="faq-item__q">What areas do you serve?</span><span class="faq-item__icon">+</span></summary>
    <p class="faq-item__a">We are based in Pompano Beach and serve the South Florida region — Broward, Miami-Dade and Palm Beach counties.</p>
  </details>
</div>"""

home_body = f"""
<section class="hero">
  <div class="hero__media"><img src="{U}/2024/03/Copy-of-IMG_9210.jpeg" alt="Grand foyer with curved staircase painted by Gama Painting" style="object-position:center 65%"></div>
  <h1 class="display hero__title">Gama</h1>
  <div class="hero__strap">
    <p>Coloring your world, coloring your future. Premium residential &amp; commercial painting, crafted by one family since 2008.</p>
    <a class="btn btn--light" href="contact.html">Free on-site estimate</a>
    <span class="label label--light">Scroll</span>
  </div>
</section>

<div class="marquee"><div class="marquee__track">{marquee_items}</div></div>

<section class="section" id="about">
  <div class="split">
    <div class="split__copy reveal">
      <span class="label">(About)</span>
      <h2 class="display h-xl">Craft in every <em>coat.</em><br>Family in every detail.</h2>
      <p class="lead">Every surface we touch reflects a commitment to excellence — from the first estimate to the final walkthrough.</p>
      <p class="body-copy">Gama Painting is led by Rodrigo Gama and Ingrid Salas, a husband-and-wife team who built their business the old way: one impeccable project, one earned referral at a time. We use top-tier products, the latest equipment, and we never subcontract — so the people who promise the quality are the ones holding the brush.</p>
      <a class="text-link" href="about.html">Our story</a>
    </div>
    <div class="portrait-stack reveal">
      <img src="{IMG['about2']}" alt="Rodrigo Gama and Ingrid Salas, owners of Gama Painting">
    </div>
  </div>
  <div class="stats">
    <div class="stat reveal"><div class="stat__num">18<sup>yrs</sup></div><p class="stat__cap">of craft — family founded in 2008.</p></div>
    <div class="stat reveal"><div class="stat__num">4.9<sup>★</sup></div><p class="stat__cap">Google rating across 50+ verified reviews.</p></div>
    <div class="stat reveal"><div class="stat__num">5<sup>yr</sup></div><p class="stat__cap">workmanship warranty on cabinet refinishing.</p></div>
    <div class="stat reveal"><div class="stat__num">0</div><p class="stat__cap">subcontractors. Every brush is ours.</p></div>
  </div>
</section>

<section class="section section--line" id="services">
  <div class="section-head reveal">
    <div>
      <span class="label">(Our services)</span>
      <h2 class="display h-xl">What we <em>do</em></h2>
    </div>
    <a class="text-link" href="gallery.html">View the work</a>
  </div>
  <div class="service-rows reveal">
    <a class="service-row" href="interior-painting.html">
      <span class="service-row__idx">( 01 )</span>
      <span class="service-row__name">Interior Painting</span>
      <span class="service-row__desc">One room or your entire home — prepared, painted and reviewed to standard.</span>
      <img class="service-row__thumb" src="{IMG['interior']}" alt="">
    </a>
    <a class="service-row" href="exterior-painting.html">
      <span class="service-row__idx">( 02 )</span>
      <span class="service-row__name">Exterior Painting</span>
      <span class="service-row__desc">Curb appeal engineered to survive the South Florida sun and storms.</span>
      <img class="service-row__thumb" src="{IMG['exterior']}" alt="">
    </a>
    <a class="service-row" href="kitchen-cabinets.html">
      <span class="service-row__idx">( 03 )</span>
      <span class="service-row__name">Kitchen Cabinets</span>
      <span class="service-row__desc">Factory-smooth refinishing in under 8 days, with a 5-year warranty.</span>
      <img class="service-row__thumb" src="{IMG['cabinet']}" alt="">
    </a>
    <a class="service-row" href="commercial.html">
      <span class="service-row__idx">( 04 )</span>
      <span class="service-row__name">Commercial</span>
      <span class="service-row__desc">Offices and retail spaces that look as professional as the work inside them.</span>
      <img class="service-row__thumb" src="{IMG['commercial']}" alt="">
    </a>
    <a class="service-row" href="wood-finishing.html">
      <span class="service-row__idx">( 05 )</span>
      <span class="service-row__name">Custom Wood Finishing</span>
      <span class="service-row__desc">Wooden pieces transformed into refined works of art.</span>
      <img class="service-row__thumb" src="{CATS['wood'][0]}" alt="">
    </a>
    <a class="service-row" href="faux-decorative.html">
      <span class="service-row__idx">( 06 )</span>
      <span class="service-row__name">Faux &amp; Decorative</span>
      <span class="service-row__desc">Venetian plaster and decorative finishes with two thousand years of history.</span>
      <img class="service-row__thumb" src="{CATS['venetian'][0]}" alt="">
    </a>
  </div>
</section>

<section class="section section--tint">
  <div class="section-head reveal">
    <div>
      <span class="label">(Before &amp; after)</span>
      <h2 class="display h-xl">The <em>proof</em> is in the finish</h2>
    </div>
    <a class="text-link" href="kitchen-cabinets.html">Kitchen cabinets</a>
  </div>
  <div class="ba-grid reveal">
    <div class="ba">
      <img src="{IMG['b1']}" alt="Kitchen before refinishing">
      <img class="ba__after" src="{IMG['a1']}" alt="Kitchen after refinishing">
      <div class="ba__handle"></div>
      <span class="ba__tag ba__tag--before">Before</span>
      <span class="ba__tag ba__tag--after">After</span>
      <input type="range" min="0" max="100" value="50" aria-label="Before and after comparison">
    </div>
    <div class="ba">
      <img src="{IMG['b2']}" alt="Kitchen before refinishing">
      <img class="ba__after" src="{IMG['a2']}" alt="Kitchen after refinishing">
      <div class="ba__handle"></div>
      <span class="ba__tag ba__tag--before">Before</span>
      <span class="ba__tag ba__tag--after">After</span>
      <input type="range" min="0" max="100" value="50" aria-label="Before and after comparison">
    </div>
  </div>
</section>

<section class="section section--line">
  <div class="section-head reveal">
    <div>
      <span class="label">(Our beliefs)</span>
      <h2 class="display h-xl">A standard worth <em>signing</em></h2>
    </div>
  </div>
  <div class="values reveal">
    <div class="value-item">
      <span class="value-item__num">( 1 )</span>
      <span class="value-item__name">Family owned<br>&amp; operated</span>
      <p class="value-item__desc">We treat every client the way we would like to be treated — with honesty, care and respect for your home.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 2 )</span>
      <span class="value-item__name">We over-deliver</span>
      <p class="value-item__desc">The estimate is a floor, not a ceiling. Our goal is to hand back a result that exceeds what was promised.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 3 )</span>
      <span class="value-item__name">Licensed<br>&amp; insured</span>
      <p class="value-item__desc">Fully credentialed professionals with the experience to handle projects of any size, residential or commercial.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 4 )</span>
      <span class="value-item__name">Nothing<br>subcontracted</span>
      <p class="value-item__desc">The team that quotes your project is the team that paints it. Accountability, from first coat to last.</p>
    </div>
  </div>
</section>

<section class="section section--line">
  <div class="rating-line reveal">
    <span class="stars">★★★★★</span>
    <span class="label">Rated “Excellent” — 4.9 on Google, 50+ reviews</span>
  </div>
  {quotes_html}
  <div class="partner-line reveal" style="margin-top:4rem">
    <span class="label">(Trusted partners)</span>
    <span>Benjamin Moore</span>
    <span>Sherwin-Williams</span>
  </div>
</section>

<section class="section section--line">
  <div class="section-head reveal">
    <div>
      <span class="label">(FAQ)</span>
      <h2 class="display h-xl">Your questions, <em>answered</em></h2>
    </div>
  </div>
  {faq_home}
</section>

{CTA_FORM}
"""

page("index.html", "Gama Painting — Premium Painting in South Florida",
     "Family owned & operated painting company in Pompano Beach, FL. Interior, exterior, commercial, kitchen cabinets and decorative finishes since 2008.",
     home_body, active="")


# ----------------------------------------------------------------
# SERVICE PAGES
# ----------------------------------------------------------------

def steps_html(steps):
    rows = []
    for i, (name, desc) in enumerate(steps, 1):
        rows.append(f"""
    <div class="step reveal">
      <span class="step__num">( {i} )</span>
      <span class="step__name">{name}</span>
      <p class="step__desc">{desc}</p>
    </div>""")
    return '<div class="steps">' + "".join(rows) + "</div>"


def masonry_html(urls, initial=None):
    imgs = "".join(
        f'<img src="{u}" alt="Gama Painting project" loading="lazy"'
        + (' class="is-hidden"' if initial is not None and i >= initial else "") + ">"
        for i, u in enumerate(urls))
    return f'<div class="masonry reveal">{imgs}</div>'


def service_page(filename, num, title_html, title_plain, lead, hero_img, overview, steps, cat, extra=""):
    body = f"""
<section class="page-hero">
  <span class="label reveal">(Service — {num})</span>
  <h1 class="display h-xxl reveal">{title_html}</h1>
  <p class="lead reveal" style="max-width:52ch;margin-top:2.5rem">{lead}</p>
</section>
<div class="full-image reveal"><img src="{hero_img}" alt="{title_plain} by Gama Painting"></div>

<section class="section">
  <div class="split">
    <div class="reveal">
      <span class="label">(Overview)</span>
      <h2 class="display h-lg" style="margin-top:1.6rem">{overview[0]}</h2>
    </div>
    <div class="split__copy reveal">
      {"".join(f'<p class="body-copy" style="max-width:52ch">{p}</p>' for p in overview[1:])}
      <a class="text-link" href="contact.html">Request a free estimate</a>
    </div>
  </div>
</section>

<section class="section section--line">
  <div class="section-head reveal">
    <div>
      <span class="label">(The process)</span>
      <h2 class="display h-xl">How we <em>work</em></h2>
    </div>
  </div>
  {steps_html(steps)}
</section>

{extra}

<section class="section section--line section--tint">
  <div class="section-head reveal">
    <div>
      <span class="label">(Project gallery — {len(CATS[cat])} photos)</span>
      <h2 class="display h-xl">{CAT_LABELS[cat]}, in the <em>field</em></h2>
    </div>
    <a class="text-link" href="gallery.html">All categories</a>
  </div>
  {masonry_html(CATS[cat])}
</section>

{CTA_FORM}
"""
    page(filename, f"{title_plain} — Gama Painting",
         f"{title_plain} in South Florida by Gama Painting — family owned & operated since 2008.",
         body, static_header=True)


service_page(
    "interior-painting.html", "01",
    "Interior <em>painting</em>", "Interior Painting",
    "One room or your entire home — a personalized project, guided through every step of the process, within your budget.",
    IMG["interior"],
    ["Walls that feel as good as they look.",
     "Are you planning on painting one room, or your entire home? Our trained painters treat both with the same discipline: meticulous preparation, premium products from Benjamin Moore and Sherwin-Williams, and a finish that holds up to daily life.",
     "Every interior project is personalized to your taste and budget — and we walk the result with you before we call it done."],
    [
        ("Taping &amp; covering", "Hardware, floors and fixtures are protected before a single can of paint is opened."),
        ("Wall preparation", "Cracks and imperfections are filled with plaster compound until the surface reads as new."),
        ("Sanding", "Every patched area is sanded perfectly smooth — the finish is only as good as what's beneath it."),
        ("Cleaning", "All dust is removed so nothing stands between the wall and the paint."),
        ("Priming &amp; sealing", "Applied whenever the surface, stains or a color change call for it."),
        ("Painting", "Brushes for the detail work, rollers for the broad planes — even coverage, crisp lines."),
        ("Final walkthrough", "We review every room with you against our quality standards before we leave."),
    ],
    "interior",
)

service_page(
    "exterior-painting.html", "02",
    "Exterior <em>painting</em>", "Exterior Painting",
    "Discoloration, chalking and paint breakdown from extreme weather can make your home look worn. We restore it — and protect it.",
    IMG["exterior"],
    ["Curb appeal, built to survive Florida.",
     "The South Florida sun, salt and storms are brutal on paint. Our exterior system starts with deep preparation — pressure washing, repairs, caulking — because protection matters as much as color.",
     "The result: a home that looks new, valued higher, and shielded against the weather that faded it in the first place."],
    [
        ("Pressure washing", "Years of dirt, chalk and buildup are stripped away so the new film can bond."),
        ("Repairs", "Damaged or deteriorated areas are repaired or removed before any coating goes on."),
        ("Caulking", "Doors and windows are sealed against moisture and driving rain."),
        ("Taping &amp; covering", "Fixtures, glass and landscaping are protected throughout the job."),
        ("Priming", "Applied whenever a color change or bare surface demands it."),
        ("Sealing", "A sealed substrate keeps humidity out and the finish uniform."),
        ("Two-coat application", "Sprayed in two full coats for an even, factory-smooth film."),
        ("Final walkthrough", "We inspect every elevation with you before we call the project complete."),
    ],
    "exterior",
)

service_page(
    "commercial.html", "03",
    "Commercial <em>painting</em>", "Commercial Painting",
    "A faded or dingy exterior makes your business look unprofessional. Ours is the crew that makes sure that never happens.",
    IMG["commercial"],
    ["Your building is your first impression.",
     "Clients judge a business before they walk through the door. We paint offices, retail spaces and commercial properties with the same preparation discipline as our residential work — scheduled around your operation to keep disruption near zero.",
     "Licensed, insured, and experienced with projects of every scale."],
    [
        ("Site assessment", "Scope, access and scheduling planned around your business hours."),
        ("Pressure washing", "Facades stripped of grime, chalk and mildew."),
        ("Repairs &amp; caulking", "Stucco, trim and joints restored and sealed."),
        ("Protection", "Signage, glass and walkways masked and covered."),
        ("Priming &amp; sealing", "The substrate prepared for maximum coating life."),
        ("Two-coat application", "Commercial-grade products, sprayed for uniformity."),
        ("Final walkthrough", "Reviewed with you, punch-list closed, site left spotless."),
    ],
    "commercial",
)

kitchen_extra = f"""
<section class="section section--line">
  <div class="section-head reveal">
    <div>
      <span class="label">(Before &amp; after)</span>
      <h2 class="display h-xl">Drag to <em>believe</em></h2>
    </div>
  </div>
  <div class="ba-grid reveal">
    <div class="ba">
      <img src="{IMG['b1']}" alt="Kitchen before refinishing">
      <img class="ba__after" src="{IMG['a1']}" alt="Kitchen after refinishing">
      <div class="ba__handle"></div>
      <span class="ba__tag ba__tag--before">Before</span>
      <span class="ba__tag ba__tag--after">After</span>
      <input type="range" min="0" max="100" value="50" aria-label="Before and after comparison">
    </div>
    <div class="ba">
      <img src="{IMG['b3']}" alt="Kitchen before refinishing">
      <img class="ba__after" src="{IMG['a3']}" alt="Kitchen after refinishing">
      <div class="ba__handle"></div>
      <span class="ba__tag ba__tag--before">Before</span>
      <span class="ba__tag ba__tag--after">After</span>
      <input type="range" min="0" max="100" value="50" aria-label="Before and after comparison">
    </div>
  </div>
  <div class="stats">
    <div class="stat reveal"><div class="stat__num">8<sup>days</sup></div><p class="stat__cap">or less, from disassembly to reveal.</p></div>
    <div class="stat reveal"><div class="stat__num">5<sup>yr</sup></div><p class="stat__cap">workmanship warranty, in writing.</p></div>
    <div class="stat reveal"><div class="stat__num">0</div><p class="stat__cap">dust and strong odors in your home.</p></div>
    <div class="stat reveal"><div class="stat__num">2<sup>-3</sup></div><p class="stat__cap">coats of lacquer, plus clear topcoat.</p></div>
  </div>
</section>"""

service_page(
    "kitchen-cabinets.html", "04",
    "Kitchen <em>cabinets</em>", "Kitchen Cabinet Refinishing",
    "Transform your kitchen in less than 8 days — without dust or strong odors — with the CRAFT-PRO method. Backed by a 5-year warranty.",
    IMG["cabinet"],
    ["A new kitchen, without the renovation.",
     "Replacing cabinets costs a fortune and takes weeks. Refinishing them with our CRAFT-PRO method delivers a factory-smooth, showroom finish in under eight days — at a fraction of the cost, while adding real value to your home.",
     "Doors and drawers travel to our shop for a controlled, dust-free finish; the boxes are completed on site with full masking. Your kitchen stays usable throughout."],
    [
        ("Disassembly", "Doors and drawers are removed and taken to our shop for controlled, precise work."),
        ("Deep cleaning", "Years of grease and residue are stripped from every wood surface."),
        ("Machine sanding", "High-tech sanders remove old finishes evenly, without gouging the wood."),
        ("Premium primer", "Two coats of high-adhesion primer build the foundation of the finish."),
        ("Primer sanding", "The primer is sanded to open its pores and lock the paint on."),
        ("Lacquer finish", "Two to three coats of water-based lacquer, plus clear topcoat on high-friction areas."),
        ("Controlled drying", "Doors cure in our drying oven while the team finishes your cabinet boxes on site."),
    ],
    "kitchen",
    extra=kitchen_extra,
)

service_page(
    "wood-finishing.html", "05",
    "Custom wood <em>finishing</em>", "Custom Wood Finishing",
    "Turn your vision into reality — wooden pieces transformed into refined works of art with advanced finishing techniques.",
    CATS["wood"][0],
    ["Wood, elevated to art.",
     "From built-ins and doors to furniture and paneling, we restore and refinish wood with techniques that honor the material — stains, lacquers, glazes and hand-finished details.",
     "Every piece begins with a conversation about your design preferences, and ends with a finish you'll want to touch."],
    [
        ("Vision &amp; consult", "We sit with you to define the look — tone, sheen, texture, character."),
        ("Preparation", "Careful disassembly where needed, deep cleaning and masking."),
        ("Sanding &amp; repair", "Surfaces are restored, imperfections corrected, grain revealed."),
        ("Custom finish", "Stain, lacquer or paint applied in controlled, patient layers."),
        ("Protection &amp; delivery", "Clear protective coats, reassembly, and a final review with you."),
    ],
    "wood",
)

service_page(
    "faux-decorative.html", "06",
    "Faux &amp; <em>decorative</em>", "Faux & Decorative Painting",
    "Venetian plaster and decorative finishes — a craft with origins in the 1st century, perfected in Roman architecture, alive on your walls.",
    CATS["venetian"][0],
    ["Two thousand years of technique.",
     "Venetian plaster traces its origins to Mesopotamia and the palaces of Rome — layers of polished plaster that give walls depth, movement and a glow no flat paint can imitate.",
     "Our decorative team applies these old-world techniques with modern materials, creating feature walls and finishes that make a space unforgettable."],
    [
        ("Sample &amp; color", "We develop physical samples until the tone and texture are exactly right."),
        ("Surface preparation", "Perfectly smooth, sealed substrates — the canvas for the craft."),
        ("Base layers", "Successive coats of plaster, troweled by hand."),
        ("Burnishing", "Polished to draw out depth, marbling and light."),
        ("Sealing &amp; wax", "Protected for durability while preserving the natural sheen."),
    ],
    "venetian",
)


# ----------------------------------------------------------------
# ABOUT
# ----------------------------------------------------------------

about_body = f"""
<section class="page-hero">
  <span class="label reveal">(About us)</span>
  <h1 class="display h-xxl reveal">A family <em>affair</em></h1>
  <p class="lead reveal" style="max-width:52ch;margin-top:2.5rem">Coloring your world, coloring your future — the story of Rodrigo, Ingrid, and eighteen years of earned trust.</p>
</section>
<div class="full-image reveal"><img src="{IMG['about3']}" alt="The Gama Painting team"></div>

<section class="section">
  <div class="split">
    <div class="split__copy reveal">
      <span class="label">(Since 2008)</span>
      <h2 class="display h-xl">Built on <em>referrals,</em> not ads</h2>
      <p class="body-copy" style="max-width:52ch">Gama Painting, LLC was founded in 2008 by Rodrigo Gama and Ingrid Salas with a simple conviction: provide not only the best painting services in South Florida, but an outstanding customer experience to match.</p>
      <p class="body-copy" style="max-width:52ch">Eighteen years later, the formula hasn't changed. Top-tier products. The latest equipment. A trained, in-house team — never subcontractors. And clients treated the way we would want to be treated ourselves.</p>
      <p class="body-copy" style="max-width:52ch">Our growth has come from word of mouth and community relationships — the kind of trust you can't buy, only earn, one project at a time.</p>
      <a class="text-link" href="contact.html">Work with us</a>
    </div>
    <div class="portrait-stack reveal">
      <img src="{IMG['about2']}" alt="Rodrigo Gama and Ingrid Salas">
    </div>
  </div>
  <div class="stats">
    <div class="stat reveal"><div class="stat__num">2008</div><p class="stat__cap">founded — family owned &amp; operated ever since.</p></div>
    <div class="stat reveal"><div class="stat__num">4.9<sup>★</sup></div><p class="stat__cap">Google rating across 50+ verified reviews.</p></div>
    <div class="stat reveal"><div class="stat__num">115<sup>+</sup></div><p class="stat__cap">documented projects across six specialties.</p></div>
    <div class="stat reveal"><div class="stat__num">3</div><p class="stat__cap">counties served — Broward, Miami-Dade, Palm Beach.</p></div>
  </div>
</section>

<section class="section section--line">
  <div class="section-head reveal">
    <div>
      <span class="label">(Our beliefs)</span>
      <h2 class="display h-xl">What we stand <em>on</em></h2>
    </div>
  </div>
  <div class="values reveal">
    <div class="value-item">
      <span class="value-item__num">( 1 )</span>
      <span class="value-item__name">Quality first</span>
      <p class="value-item__desc">Top-tier products and the latest industry equipment on every project, no exceptions.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 2 )</span>
      <span class="value-item__name">Personalization</span>
      <p class="value-item__desc">Every project is customized to the client's needs, taste and budget — never off the shelf.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 3 )</span>
      <span class="value-item__name">Trust &amp; credibility</span>
      <p class="value-item__desc">Licensed, insured, and accountable — the same family name on every contract since 2008.</p>
    </div>
    <div class="value-item">
      <span class="value-item__num">( 4 )</span>
      <span class="value-item__name">Over-delivery</span>
      <p class="value-item__desc">Our reputation was built by handing back more than was promised. We intend to keep it.</p>
    </div>
  </div>
  <div class="partner-line reveal" style="margin-top:4rem">
    <span class="label">(Trusted partners)</span>
    <span>Benjamin Moore</span>
    <span>Sherwin-Williams</span>
  </div>
</section>

{CTA_FORM}
"""
page("about.html", "About Us — Gama Painting",
     "Family owned & operated since 2008, led by Rodrigo Gama and Ingrid Salas. The best painting services in South Florida, with outstanding customer experience.",
     about_body, active="about", static_header=True)


# ----------------------------------------------------------------
# GALLERY
# ----------------------------------------------------------------

CAT_PAGES = {
    "kitchen": "kitchen-cabinets.html",
    "interior": "interior-painting.html",
    "venetian": "faux-decorative.html",
    "wood": "wood-finishing.html",
    "commercial": "commercial.html",
    "exterior": "exterior-painting.html",
}

gallery_sections = ""
for i, (key, label) in enumerate(CAT_LABELS.items(), 1):
    style = "" if i == 1 else ' class="section--line"'
    gallery_sections += f"""
<section class="section{' section--line' if i > 1 else ''}" style="padding-top:{'2rem' if i == 1 else 'clamp(4rem, 8vw, 7rem)'}" id="{key}">
  <div class="section-head reveal">
    <div>
      <span class="label">( 0{i} — {len(CATS[key])} photos )</span>
      <h2 class="display h-xl">{label}</h2>
    </div>
    <a class="text-link" href="{CAT_PAGES[key]}">About this service</a>
  </div>
  {masonry_html(CATS[key], initial=6)}
  {f'<div class="load-more-wrap"><button class="btn load-more" type="button">Load more <span>(+{len(CATS[key]) - 6})</span></button></div>' if len(CATS[key]) > 6 else ''}
</section>"""

gallery_body = f"""
<section class="page-hero">
  <span class="label reveal">(Gallery)</span>
  <h1 class="display h-xxl reveal">Selected <em>work</em></h1>
  <p class="lead reveal" style="max-width:52ch;margin-top:2.5rem">Kitchens, interiors, exteriors, commercial spaces, Venetian plaster and custom wood — {sum(len(v) for v in CATS.values())} photos from eighteen years in the field.</p>
</section>

{gallery_sections}

{CTA_FORM}
"""
page("gallery.html", "Gallery — Gama Painting",
     "Selected painting projects by Gama Painting: kitchens, interiors, exteriors, commercial spaces and decorative finishes across South Florida.",
     gallery_body, active="gallery", static_header=True)


# ----------------------------------------------------------------
# CONTACT
# ----------------------------------------------------------------

contact_body = f"""
<section class="page-hero">
  <span class="label reveal">(Contact)</span>
  <h1 class="display h-xxl reveal">Let's <em>talk</em></h1>
  <p class="lead reveal" style="max-width:52ch;margin-top:2.5rem">A free, no-pressure on-site estimate is one message away. We usually respond within one business day.</p>
</section>

<section class="section" style="padding-top:2rem">
  <div class="split">
    <div class="split__copy reveal">
      <span class="label">(Visit)</span>
      <p class="lead">{ADDRESS}</p>
      <a class="text-link" href="https://maps.google.com/?q=471+S+Flagler+Avenue+Pompano+Beach+FL" target="_blank" rel="noopener">Open in Maps ↗</a>
    </div>
    <div class="split__copy reveal">
      <span class="label">(Reach us)</span>
      <p class="lead"><a href="{PHONE_HREF}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <div class="partner-line">
        <a class="text-link" href="https://www.facebook.com/gamapainting/" target="_blank" rel="noopener">Facebook ↗</a>
        <a class="text-link" href="https://www.instagram.com/gamapainting1/" target="_blank" rel="noopener">Instagram ↗</a>
      </div>
    </div>
  </div>
</section>

{CTA_FORM}
"""
page("contact.html", "Contact — Gama Painting",
     "Request a free on-site estimate from Gama Painting. Call (954) 204-9251 or send a message — Pompano Beach, South Florida.",
     contact_body, active="contact", static_header=True)

print("done.")
