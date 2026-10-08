"""Generates docs/*.html for Ängö Entreprenad on the Lindvik Bygg template (lirk)."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])

PHONE, TEL, MAIL = "0705-28 35 20", "+46705283520", "dan@angoentreprenad.se"
ADDR = "Hjälmvik 252, 472 97 Varekil"
MAP = "https://www.google.com/maps/search/?api=1&query=Hj%C3%A4lmvik+252+472+97+Varekil"
FB = "https://www.facebook.com/angoentreprenad/"


LOGO_DARK = '<img src="img/ango-logo.svg" alt="Ängö Entreprenad" width="120" height="50">'
LOGO_LIGHT = '<img src="img/ango-logo-vit.svg" alt="Ängö Entreprenad" width="120" height="50">'
FAVICON = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='7' fill='%231d1d1b'/>"
           "<path d='M10 25 15 9h4l5 16h-4l-3.2-11L14 25z' fill='%23ffd400'/><rect x='12' y='4' width='3' height='3' fill='%23ffd400'/><rect x='18' y='4' width='3' height='3' fill='%23ffd400'/></svg>")
ARR = '<svg class="arr" viewBox="0 0 52 52" fill="none" stroke-width="2.2" aria-hidden="true"><path d="M10 42 42 10M16 10h26v26"/></svg>'

SERVICES = [
    # slug, title, short, photo, position
    ("grundlaggning", "Grundläggning", "Husgrunder för villor, garage, förskolor och flerbostadshus", "grundlaggning.jpg", "50% 50%"),
    ("schakt", "Schakt och sprängning", "Rivning, trädfällning, schakt, sprängning och terrassering", "schakt.jpg", "50% 50%"),
    ("va", "VA och enskilda avlopp", "Vatten, avlopp, dränering och minireningsverk", "va-ror.jpg", "50% 50%"),
    ("vagar", "Vägar och planer", "Vägar, parkeringar, planer och diken", "vagar.jpg", "50% 60%"),
    ("finplanering", "Finplanering", "Gräsmattor, plantering, plattytor, murar och L-stöd", "finplanering.jpg", "50% 60%"),
    ("transporter", "Transporter och kranbil", "Grus, maskintransporter, kranbil och maskinsläp", "transporter.jpg", "50% 50%"),
]


def img(src, pos="50% 50%", alt="", lazy=True):
    return f'<img class="photo" src="img/{src}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""} style="object-position:{pos}">'


def tiles():
    out = []
    for slug, title, short, photo, pos in SERVICES:
        out.append(f'<a class="tile" href="tjanst-{slug}.html">{img(photo, pos)}{ARR}<span><b>{title}</b><small>{short}</small></span></a>')
    return '<div class="tiles">' + "".join(out) + "</div>"


NAV = [("tjanster.html", "Tjänster"), ("projekt.html", "Projekt"), ("maskinpark.html", "Maskinpark"), ("om-oss.html", "Om oss"), ("kontakt.html", "Kontakt")]


def section_of(name):
    if name.startswith("tjanst"):
        return "tjanster.html"
    if name.startswith("projekt"):
        return "projekt.html"
    return name


def header(home=False, name="index.html"):
    label = "till toppen" if home else "till startsidan"
    cur = section_of(name)
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in NAV)
    sub = "".join(f'<li><a href="tjanst-{s}.html">{t}</a></li>' for s, t, *_ in SERVICES)
    main = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header>
  <div class="in nav">
    <a class="logo" href="index.html" aria-label="Ängö Entreprenad, {label}">{LOGO_DARK}</a>
    <nav class="mainnav" aria-label="Huvudmeny">{links}</nav>
    <a class="navphone" href="tel:{TEL}">{PHONE}</a>
    <a class="btn btn-g navcta" href="kontakt.html">Begär offert</a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="overlay" aria-label="Öppna menyn"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="overlay" id="overlay" aria-hidden="true" inert>
  <div class="ov-top"><a class="logo" href="index.html">{LOGO_LIGHT}</a><button class="ov-close" id="menuClose" type="button" aria-label="Stäng menyn">Stäng <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 4l12 12M16 4 4 16"/></svg></button></div>
  <nav class="ov-nav" aria-label="Meny">
    <ul class="ov-main">{main}</ul>
    <div class="ov-cols">
      <div><p class="ov-h">Tjänster</p><ul class="ov-list">{sub}</ul></div>
      <div><p class="ov-h">Kontakt</p><ul class="ov-list"><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li>{ADDR}</li></ul></div>
    </div>
  </nav>
</div>'''


def footer():
    svc = "".join(f'<li><a href="tjanst-{s}.html">{t}</a></li>' for s, t, *_ in SERVICES)
    return f'''<section class="fcta" aria-label="Kontakta oss">
  <div class="in"><div><h2>Har du ett markjobb på gång?</h2><p>Berätta om det, så hör vi av oss. Eller ring Dan direkt på {PHONE}.</p></div><a class="btn btn-w" href="kontakt.html">Kontakta oss</a></div>
</section>
<footer>
  <div class="in">
    <div class="fgrid">
      <div><a class="logo" href="index.html">{LOGO_LIGHT}</a>
        <p style="margin-top:14px;max-width:36ch">Markentreprenad på Orust och i Göteborgsregionen sedan 1984. Ca 20 anställda och en maskinpark på ca 45 enheter.</p>
        <p style="margin-top:12px">Ängö Entreprenad AB<br>{ADDR}<br><a href="tel:{TEL}">{PHONE}</a> · <a href="mailto:{MAIL}">{MAIL}</a></p>
        <div class="social"><a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook (öppnas i ny flik)"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8V6.5c0-.7.5-1.2 1.2-1.2H17V2h-2.8C11.6 2 10 3.7 10 6.3V8H7.5v3.3H10V22h4V11.3h2.8l.5-3.3z"/></svg></a></div>
      </div>
      <div><h4>Vårt erbjudande</h4><ul>{svc}</ul></div>
      <div><h4>Kontakt</h4><ul><li><a href="tel:+46705283520">Dan Johansson, vd</a></li><li><a href="tel:+46705233523">Robert Andreasson, arbetschef</a></li><li><a href="tel:+46705260035">Peter Carlsson, Göteborg</a></li><li><a href="{MAP}" target="_blank" rel="noopener">Hitta hit</a></li></ul></div>
      <div><h4>Om Ängö</h4><ul><li><a href="om-oss.html">Om oss</a></li><li><a href="om-oss.html#historia">Vår historia</a></li><li><a href="projekt.html">Projekt</a></li><li><a href="maskinpark.html">Maskinpark</a></li><li><a href="kontakt.html">Kontakt</a></li></ul></div>
    </div>
    <div class="certs" aria-label="Medlemskap"><span>Medlem i Maskinentreprenörerna</span><span>Org.nr 556900-2263</span></div>
    <div class="fbottom"><span>© 2026 Ängö Entreprenad AB · Foton: Pexels</span><a class="totop" href="#" data-top>Till toppen ↑</a></div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''


def page(name, title, desc, main, home=False):
    full_title = "Ängö Entreprenad – markentreprenad på Orust och i Göteborg" if home else f"{title} – Ängö Entreprenad"
    html = f'''<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">
<link rel="stylesheet" href="assets/site.css">
<link rel="icon" href="data:image/svg+xml,{FAVICON}">
</head>
<body>
{header(home, name)}
<main{' id="top"' if home else ''}>
{main}
</main>
{footer()}'''
    (OUT / name).write_text(html, encoding="utf-8")


def phero(title, lead, photo=None, pos="50% 50%", crumbs=()):
    trail = '<a href="index.html">Start</a> <span aria-hidden="true">›</span> ' + "".join(
        f'<a href="{h}">{t}</a> <span aria-hidden="true">›</span> ' for t, h in crumbs) + f"<span>{title}</span>"
    if photo is None:
        return f'<section class="phero plain"><div class="in"><nav class="crumbs" aria-label="Brödsmulor">{trail}</nav><h1>{title}</h1><p>{lead}</p></div></section>'
    return (f'<section class="phero" aria-label="{title}"><div class="ph">{img(photo, pos)}</div><div class="in">'
            f'<nav class="crumbs" aria-label="Brödsmulor">{trail}</nav><h1>{title}</h1><p>{lead}</p></div></section>')


PEOPLE = [
    ("DJ", "Dan Johansson", "Vd", "Orust", "0705-28 35 20", "+46705283520", "dan@angoentreprenad.se"),
    ("RA", "Robert Andreasson", "Arbetschef och kalkyl", "Orust", "0705-23 35 23", "+46705233523", "robert.andreasson@angoentreprenad.se"),
    ("PC", "Peter Carlsson", "Kalkyl och inköp", "Göteborg", "0705-26 00 35", "+46705260035", "peter@angogbg.se"),
]


def aside_contact(i=0, heading="Prata med oss", button="Skicka en förfrågan"):
    av, name, role, office, phone, tel, mail = PEOPLE[i]
    return (f'<aside class="aside"><h3>{heading}</h3><div class="who"><span class="av" aria-hidden="true">{av}</span><div><b>{name}</b><br>'
            f'<span style="color:var(--muted);font-size:14px">{role}, {office}</span></div></div><dl><div><dt>Telefon</dt><dd><a href="tel:{tel}">{phone}</a></dd></div>'
            f'<div><dt>Mejl</dt><dd><a href="mailto:{mail}">{mail}</a></dd></div></dl><a class="btn btn-g" href="kontakt.html">{button}</a></aside>')


def card3(items):
    return '<div class="cards3" style="margin-top:24px">' + "".join(
        f'<div class="person" style="gap:8px"><b style="font:700 1.15rem var(--display)">{t}</b><span style="font-size:15px;color:var(--muted);line-height:1.55">{b}</span></div>'
        for t, b in items) + "</div>"


LASSBY_CARD = f'<a class="pcard2" href="projekt-lassby.html"><div class="ph">{img("villaomrade.jpg", alt="Låssby, Hisingen")}</div><h3>Låssby</h3><small>Villatomter · Hisingen · 2021–2022</small></a>'

TIMELINE = '''<ol class="timeline"><li><b>1984</b><p>Dan Johansson startar upp ett enmansbolag i namnet Ängö Schakt.</p></li><li><b>1999</b><p>Verksamheten har vuxit till ca tio anställda och bygget av den nuvarande huvudkontorsanläggningen påbörjas på en större industritomt.</p></li><li><b>2013</b><p>Ängö Entreprenad AB bildas. Robert Andreasson och Joakim Olsson, två av våra dåvarande arbetsledare, kliver in som delägare och det nya huvudkontoret står klart.</p></li><li><b>2016</b><p>Dotterbolaget i Göteborg startas. Peter Carlsson och Per Persson kommer in som delägare för att utveckla verksamheten i Göteborgsregionen.</p></li><li><b>2024</b><p>Vi firar 40 år. Joakim Olsson lämnar företaget efter 36 år och Per Persson går i pension.</p></li></ol>'''

PROCESS = '''<ol class="timeline"><li><b>Obebyggd tomt</b><p>Vi går igenom tomten och förutsättningarna tillsammans med dig eller byggföretaget.</p></li><li><b>Sprängning</b><p>Berget sprängs bort där huset och ledningarna ska ligga.</p></li><li><b>Schakt och fyllning</b><p>Vi schaktar, fyller och terrasserar till rätt nivåer.</p></li><li><b>Färdig grund</b><p>Grunden byggs – villa, garage, förskola eller flerbostadshus.</p></li><li><b>Återställning och finplanering</b><p>Marken runt huset återställs, och om du vill finplanerar vi hela tomten.</p></li></ol>'''


def links_row(skip):
    return '<section><div class="in"><h2>Fler tjänster</h2><div class="links-row">' + "".join(
        f'<a href="tjanst-{s}.html">{t}</a>' for s, t, *_ in SERVICES if s != skip) + "</div></div></section>"


# ---------------------------------------------------------------- startsidan
hero = f'''<section class="hero hero-video" aria-label="Välkommen">
    <div class="ph"><video class="photo" autoplay muted loop playsinline preload="auto" poster="img/hero-poster.jpg" aria-hidden="true"><source src="video/hero.mp4" type="video/mp4" media="(min-width: 768px)"><source src="video/hero-mobil.mp4" type="video/mp4"></video></div>
    <div class="in hero-copy">
      <h1>Markarbeten sedan&nbsp;1984.</h1>
      <p class="hero-place">Orust · Göteborg</p>
    </div>
  </section>'''

index_main = f'''  {hero}

  <section id="tjanster">
    <div class="in">
      <div class="headrow"><div><span class="eyebrow">Tjänster</span><h2>Det här gör vi</h2></div><a class="arrow" href="tjanster.html">Alla tjänster</a></div>
      {tiles()}
    </div>
  </section>

  <section class="about" id="om">
    <div class="in about2">
      <div class="media"><div class="ph">{img("team.jpg", "50% 40%", alt="Arbetsledare som går igenom en ritning")}</div></div>
      <div class="txt">
        <span class="eyebrow">Om Ängö</span><h2 style="margin-top:8px">Markentreprenör på Orust i 40 år</h2>
        <p class="lead" style="margin-top:14px">Tillsammans med olika byggföretag utför vi både små och stora markentreprenader – oftast med grundläggning av hus och tillhörande vägar, planer, parkeringar och ledningar. Vi utför även finplanering av alla slag åt både privatpersoner och företag.</p>
        <div class="facts"><div><b>40</b><span>år i branschen</span></div><div><b>20</b><span>anställda</span></div><div><b>45</b><span>maskiner</span></div></div>
        <div class="minis">
          <a class="mini" href="tjanster.html"><b>Tjänster</b><span>Från rivning och sprängning till grund, VA, vägar och finplanering.</span></a>
          <a class="mini" href="om-oss.html#historia"><b>Vår historia</b><span>Från enmansbolaget Ängö Schakt 1984 till i dag.</span></a>
          <a class="mini" href="maskinpark.html"><b>Maskinpark</b><span>Ca 45 enheter – grävmaskiner, lastare, vältar och lastbilar.</span></a>
        </div>
      </div>
    </div>
  </section>

  <section id="projekt">
    <div class="in proj">
      <div>
        <span class="eyebrow">Projekt</span><h2 style="margin-top:8px">Gjort av oss</h2>
        <p class="lead" style="margin-top:14px">Flera hundra husgrunder genom åren – stora som små. Här är ett urval av vad vi gör.</p>
        <a class="btn btn-g" style="margin-top:22px" href="projekt.html">Alla projekt</a>
      </div>
      <div class="tw"><div class="track" id="track" tabindex="0" aria-label="Projekt, svep i sidled">
        <a class="pcard" href="projekt-lassby.html"><div class="ph house">{img("villaomrade.jpg", lazy=False)}</div><div class="meta"><h3>Låssby</h3><small>Hisingen · 2021–2022</small></div></a>
        <a class="pcard" href="tjanst-grundlaggning.html"><div class="ph site">{img("husgrund.jpg", "50% 50%", lazy=False)}</div><div class="meta"><h3>Husgrunder</h3><small>Villor, förskolor och flerbostadshus</small></div></a>
        <a class="pcard" href="tjanst-vagar.html"><div class="ph road">{img("asfalt.jpg", lazy=False)}</div><div class="meta"><h3>Vägar och parkeringar</h3><small>Orust och Göteborgsregionen</small></div></a>
        <a class="pcard" href="tjanst-va.html"><div class="ph forest">{img("ror.jpg", lazy=False)}</div><div class="meta"><h3>Enskilda avlopp</h3><small>Med minireningsverk</small></div></a>
      </div><div class="parrows"><div class="pdots" id="pdots" aria-hidden="true"></div><button id="prev" class="parr" aria-label="Föregående projekt"><svg viewBox="0 0 48 48" width="40" height="40" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M40 24H9M21 11 8 24l13 13"/></svg></button><button id="next" class="parr" aria-label="Nästa projekt"><svg viewBox="0 0 48 48" width="40" height="40" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 24h31M27 11l13 13-13 13"/></svg></button></div>
    </div>
    </div>
  </section>

  <section class="band" id="erbjudande" aria-label="Grundläggning som helhet">
    <div class="ph site" style="--g:linear-gradient(180deg,#5d4630,#2f2418)">{img("armering.jpg", "50% 50%")}</div>
    <div class="in">
      <span class="kicker">Vår specialitet</span>
      <h2>Grundläggning – från obebyggd tomt till färdig grund</h2>
      <p>Vi tar hand om hela processen: sprängning, schakt och fyllning, färdig grund och återställning. Önskas så finplanerar vi även tomten.</p>
      <div><a class="btn btn-w" href="tjanst-grundlaggning.html">Läs om grundläggning</a></div>
    </div>
  </section>
  <div class="in overlap">
    <div class="ocard">
      <div class="ph house" style="border-radius:0">{img("tomt.jpg", "50% 50%")}</div>
      <div class="txt"><h3 style="font-size:1.5rem">Privatperson som ska bygga eller fixa tomten?</h3><p class="lead" style="font-size:1rem">Vi utför finplanering av alla slag åt privatpersoner – gräsmattor, plattytor, murar och plantering.</p><a class="arrow" href="tjanst-finplanering.html">Läs om finplanering</a></div>
    </div>
  </div>

  <section id="historia">
    <div class="in">
      <div class="headrow"><div><span class="eyebrow">Historia</span><h2 style="margin-top:8px">40 år i marken</h2></div><a class="arrow" href="om-oss.html#historia">Hela historien</a></div>
      <div class="newsgrid">
        <a class="news" data-tilt href="om-oss.html#historia"><div class="ph forest">{img("orust-hus.jpg", "50% 60%")}</div><time datetime="1984">1984</time><h3>Ängö Schakt startar</h3><p>Dan Johansson startar upp ett enmansbolag i namnet Ängö Schakt.</p></a>
        <a class="news" data-tilt href="om-oss.html#historia"><div class="ph people">{img("arbetsledare.jpg", "50% 40%")}</div><time datetime="2013">2013</time><h3>Ängö Entreprenad AB bildas</h3><p>Två av våra arbetsledare kliver in som delägare och det nya huvudkontoret står klart.</p></a>
        <a class="news" data-tilt href="om-oss.html#historia"><div class="ph house">{img("goteborg.jpg")}</div><time datetime="2016">2016</time><h3>Vi startar i Göteborg</h3><p>Dotterbolaget startas för att utveckla verksamheten i Göteborgsregionen.</p></a>
      </div>
    </div>
  </section>

  <section class="jobs" id="kontakta" style="background:var(--white)">
    <div class="in">
      <div class="center" style="margin-bottom:30px"><span class="eyebrow">Kontakt</span><h2 style="margin-top:8px">Prata med en av oss</h2></div>
      <div class="jobgrid">
        <div class="big"><div class="ph people">{img("medarbetare.jpg", "50% 30%")}</div>
          <div class="card"><h3 style="font-size:1.4rem">Orust – huvudkontoret</h3><p style="color:rgb(255 255 255/.85)">Dan Johansson, vd: {PHONE}<br>Robert Andreasson, arbetschef och kalkyl: 0705-23 35 23</p><div><a class="btn btn-w" href="tel:{TEL}">Ring Dan</a></div></div></div>
        <div class="side">
          <div class="ph site">{img("hjulgravare.jpg")}</div>
          <div class="card2"><h3 style="font-size:1.35rem">Göteborg</h3><p class="lead" style="font-size:1rem">Peter Carlsson, kalkyl och inköp: 0705-26 00 35. Sedan 2016 finns vi även i Göteborgsregionen.</p><a class="arrow" href="kontakt.html">Alla kontaktuppgifter</a></div>
        </div>
      </div>
    </div>
  </section>

  <section id="genvagar" class="quick">
    <div class="in">
      <div class="shortcuts" aria-label="Genvägar" style="margin-top:0">
        <a class="sc" href="om-oss.html"><div class="ph">{img("team.jpg")}</div><b>Om oss</b></a>
        <a class="sc" href="kontakt.html#kontor"><div class="ph">{img("alvsborgsbron.jpg")}</div><b>Kontor</b></a>
        <a class="sc" href="maskinpark.html"><div class="ph">{img("hjullastare.jpg")}</div><b>Maskinpark</b></a>
        <a class="sc" href="projekt.html"><div class="ph">{img("villaomrade.jpg")}</div><b>Projekt</b></a>
      </div>
    </div>
  </section>

  <section id="faq">
    <div class="in faq">
      <div><span class="eyebrow">Frågor och svar</span><h2 style="margin-top:8px">Undrar du något?</h2><p class="lead" style="margin-top:14px">Här är svaren på det vi får frågor om oftast. Hittar du inte svaret? Ring oss.</p><a class="arrow" style="margin-top:18px" href="kontakt.html">Fråga oss något annat</a></div>
      <div>
        <details><summary>Jobbar ni åt privatpersoner?</summary><p>Ja. Vi utför finplanering av alla slag åt både privatpersoner och företag, och gör även husgrunder, VA och enskilda avlopp åt privatpersoner.</p></details>
        <details><summary>Hur stora grunder gör ni?</summary><p>Både stora och små. Vi har gjort flera hundra husgrunder genom åren – från villor och garage till stora förskolor och flerbostadshus.</p></details>
        <details><summary>Var utför ni uppdrag?</summary><p>Huvudkontoret ligger på Hjälmvik, Orust. Sedan 2016 finns vi även i Göteborgsregionen.</p></details>
        <details><summary>Kan ni ta hela markjobbet?</summary><p>Ja. Från obebyggd tomt via sprängning, schakt och fyllning till färdig grund och återställning – och finplanering om du vill.</p></details>
        <details><summary>Kan ni köra grus och maskiner?</summary><p>Ja. Våra lastbilar kör grus och maskiner, och vi har även kranbil och maskinsläp.</p></details>
      </div>
    </div>
  </section>'''
page("index.html", "Start", "Ängö Entreprenad AB utför små och stora markentreprenader – husgrunder, vägar, planer, parkeringar, VA och finplanering – på Orust och i Göteborgsregionen sedan 1984.", index_main, home=True)

# ---------------------------------------------------------------- tjänster
why = card3([
    ("40 år i marken", "Sedan Dan Johansson startade Ängö Schakt 1984. I dag är vi ca 20 anställda."),
    ("Egen maskinpark", "Ca 45 enheter som vi håller uppdaterade för att möta dagens krav."),
    ("Hela kedjan", "Rivning, sprängning, schakt, grund, VA, vägar och finplanering – en entreprenör."),
    ("Flera hundra grunder", "Från villor och garage till stora förskolor och flerbostadshus."),
    ("Orust och Göteborg", "Huvudkontor på Hjälmvik och eget bolag i Göteborgsregionen sedan 2016."),
    ("Egna transporter", "Lastbilar för grus och maskiner, kranbil och maskinsläp."),
])
page("tjanster.html", "Vårt erbjudande", "Markentreprenader åt byggföretag, företag och privatpersoner.", f'''{phero("Vårt erbjudande", "Små och stora markentreprenader – åt byggföretag, företag och privatpersoner.", "hero-gravmaskin.jpg", "50% 55%")}<section><div class="in">{tiles()}</div></section><section class="related"><div class="in"><div class="content"><div class="prose"><h2 style="margin-top:0">En markentreprenör för hela jobbet</h2><p>Tillsammans med olika byggföretag utför vi både små och stora markentreprenader. Oftast handlar det om grundläggning av hus och tillhörande vägar, planer, parkeringar och ledningar.</p><p>Vi utför även finplanering av alla slag åt både privatpersoner och företag, och våra lastbilar kör grus och maskiner.</p><h2>Det här gör vi</h2><ul><li>Rivning av hus och trädfällning</li><li>Schaktning, sprängning och terrassering</li><li>Grundläggning</li><li>Vatten och avlopp samt enskilda avlopp med minireningsverk</li><li>Vägbyggnation, diken för dränering och grusning</li><li>Gräsmattor, plantering, plattytor, murar och L-stöd</li><li>Kranbilsarbeten och maskintransporter</li></ul></div>{aside_contact(0, "Var jobbar vi?", "Berätta om ditt projekt").replace("<h3>Var jobbar vi?</h3>", "<h3>Var jobbar vi?</h3><p>Orust och Göteborgsregionen. Huvudkontoret ligger på Hjälmvik 252 i Varekil.</p>")}</div></div></section><section><div class="in"><h2>Varför välja Ängö?</h2>{why}</div></section>''')

DETAIL = {
    "grundlaggning": ("Vår specialitet. Husgrunder i alla storlekar – från villor och garage till förskolor och flerbostadshus.",
        '<div class="stats"><div><b>100+</b><span>husgrunder genom åren</span></div><div><b>40 år</b><span>i branschen</span></div><div><b>45</b><span>maskiner</span></div></div>'
        "<p>Grundläggning är vår specialitet. Vi har gjort flera hundra husgrunder genom åren, både stora och små – från villor och garage till stora förskolor och flerbostadshus.</p>"
        "<p>Vi tar hand om hela processen, från obebyggd tomt via sprängning, schakt och fyllning till färdig grund och återställning. Önskas så finplanerar vi även tomten.</p>"
        "<h2>Det här ingår</h2><ul><li>Sprängning, schakt och fyllning</li><li>Terrassering till rätt nivåer</li><li>Färdig grund</li><li>Återställning runt huset</li><li>Finplanering av tomten om så önskas</li></ul>"
        f"<h2>Så går det till</h2>{PROCESS}"
        "<h2>Åt byggföretag och privatpersoner</h2><p>De flesta grunder gör vi tillsammans med olika byggföretag, ofta tillsammans med tillhörande vägar, planer, parkeringar och ledningar. Vi gör även grunder direkt åt privatpersoner.</p>"),
    "schakt": ("Rivning, trädfällning, schaktning, sprängning och terrassering inför byggnation.",
        "<p>Innan något kan byggas måste marken göras redo. Vi river hus, fäller träd, schaktar, spränger och terrasserar – med egna maskiner och egen personal.</p>"
        "<h2>Det här ingår</h2><ul><li>Rivning av hus</li><li>Trädfällning</li><li>Schaktning och fyllning</li><li>Sprängning</li><li>Terrassering</li></ul>"
        "<h2>Rätt maskin för jobbet</h2><p>Vi har larvburna och hjulburna grävmaskiner, dumprar, hjullastare och vältar. Våra lastbilar kör både massor, grus och maskiner till och från arbetsplatsen.</p>"),
    "va": ("Vatten- och avloppsledningar, dränering och enskilda avlopp med minireningsverk.",
        "<p>Vi lägger vatten- och avloppsledningar till nya hus och bostadsområden, och gräver diken för dränering.</p>"
        "<p>Ligger huset utanför det kommunala nätet anlägger vi enskilda avlopp med minireningsverk.</p>"
        "<h2>Det här ingår</h2><ul><li>Vatten- och avloppsledningar</li><li>Enskilda avlopp med minireningsverk</li><li>Diken för dränering</li><li>Ledningar till nya hus och villaområden</li></ul>"),
    "vagar": ("Vägbyggnation, planer, parkeringar, diken för dränering och grusning.",
        "<p>Till husen hör vägar, planer och parkeringar. Vi bygger dem – ofta i samma entreprenad som grundläggningen – och gräver diken för dränering.</p>"
        "<h2>Det här ingår</h2><ul><li>Vägbyggnation</li><li>Planer och parkeringar</li><li>Diken för dränering</li><li>Grusning</li></ul>"
        "<h2>Exempel</h2><p>I Låssby på Hisingen gjorde vi bland annat inmätning av befintliga vägar och nivåer inför projektering och byggnation av åtta villor. <a href=\"projekt-lassby.html\">Läs om projektet</a>.</p>"),
    "finplanering": ("Finplanering av alla slag – åt både privatpersoner och företag.",
        "<p>Vi utför finplanering av alla slag åt både privatpersoner och företag. När grunden är klar och marken återställd kan vi göra färdigt hela tomten.</p>"
        "<h2>Det här ingår</h2><ul><li>Gräsmattor</li><li>Plantering</li><li>Plattytor</li><li>Murar och L-stöd</li><li>Stödmurar med Keystone</li></ul>"
        "<h2>Stödmurar med Keystone</h2><p>Under många år har vi arbetat med stödmurssystemet Keystone.</p>"),
    "transporter": ("Lastbilar för grus och maskiner, kranbil och maskinsläp.",
        "<p>Våra lastbilar kör grus och maskiner. Vi har även kranbil och maskinsläp för tunga lyft och transporter.</p>"
        "<h2>Det här ingår</h2><ul><li>Grus- och massatransporter</li><li>Grusning</li><li>Maskintransporter med maskinsläp</li><li>Kranbilsarbeten</li></ul>"),
}
for slug, title, short, photo, pos in SERVICES:
    lead, body = DETAIL[slug]
    related = f'<section class="related"><div class="in"><h2>Projekt vi har gjort</h2><div style="margin-top:24px"><div class="cards3">{LASSBY_CARD}</div></div></div></section>' if slug in ("grundlaggning", "schakt", "vagar") else ""
    page(f"tjanst-{slug}.html", title, lead, f'''{phero(title, lead, photo, pos, (("Vårt erbjudande", "tjanster.html"),))}<section><div class="in content"><div class="prose">{body}</div>
      {aside_contact(1 if slug in ("grundlaggning", "schakt", "vagar") else 0)}</div></section>{related}{links_row(slug)}''')

# ---------------------------------------------------------------- projekt
page("projekt.html", "Projekt", "Ett urval av Ängö Entreprenads projekt.", f'''{phero("Gjort av oss", "Flera hundra husgrunder och markentreprenader sedan 1984. Här är ett urval.", "hjullastare.jpg")}<section><div class="in"><div class="cards3">{LASSBY_CARD}<a class="pcard2" href="tjanst-grundlaggning.html"><div class="ph">{img("husgrund.jpg", alt="Husgrund")}</div><h3>Husgrunder</h3><small>Villor, garage, förskolor och flerbostadshus</small></a><a class="pcard2" href="tjanst-finplanering.html"><div class="ph">{img("tomt.jpg", alt="Finplanerad tomt")}</div><h3>Finplanering</h3><small>Åt privatpersoner och företag</small></a></div></div></section><section class="related"><div class="in"><div class="content"><div class="prose"><h2 style="margin-top:0">Markentreprenader sedan 1984</h2><p>Tillsammans med olika byggföretag utför vi både små och stora markentreprenader, oftast med grundläggning av hus och tillhörande vägar, planer, parkeringar och ledningar.</p><p>Vi har gjort flera hundra husgrunder genom åren – från villor och garage till stora förskolor och flerbostadshus. Fler referenser berättar vi gärna om när du hör av dig.</p></div>{aside_contact(0, "Vill du veta mer?", "Hör av dig")}</div></div></section>''')

page("projekt-lassby.html", "Låssby", "Schakt för grundläggning och grovplanering av åtta villatomter i Låssby på Hisingen.", f'''{phero("Låssby", "Åtta friliggande villor på Hisingen. Vi var med från första provtagningen till grovplanerade tomter.", "villaomrade.jpg", "50% 50%", (("Projekt", "projekt.html"),))}<section><div class="in content"><div class="prose"><div class="stats"><div><b>5 600 m²</b><span>yta</span></div><div><b>8</b><span>villatomter</span></div><div><b>2021–2022</b><span>tid</span></div></div><p>Varberghus planerar att bygga åtta stycken friliggande villor i Låssby på Hisingen.</p><p>Vi var med tidigt efter de arkeologiska utgrävningarna och genomförde en geoteknisk undersökning, miljöprovtagning och inmätning av befintliga vägar och nivåer inför projektering och byggnation.</p><h2>Vårt uppdrag</h2><ul><li>Geoteknisk undersökning</li><li>Miljöprovtagning</li><li>Inmätning av befintliga vägar och nivåer</li><li>Schakt för grundläggning</li><li>Grovplanering av tomterna</li></ul></div>
      <aside class="aside"><h3>Fakta</h3><dl><div><dt>Yta</dt><dd>5 600 m²</dd></div><div><dt>Tid</dt><dd>2021–2022</dd></div><div><dt>Plats</dt><dd>Låssby, Hisingen</dd></div><div><dt>Beställare</dt><dd>Varbergshus</dd></div></dl><a class="btn btn-g" href="kontakt.html">Göra något liknande?</a></aside></div></section>{links_row("")}''')

# ---------------------------------------------------------------- maskinpark
machines = card3([
    ("Larvburna grävmaskiner", "För schakt, sprängning, grundläggning och VA."),
    ("Hjulburna grävmaskiner", "Snabba att flytta mellan arbetsplatser, bra för vägar och ledningar."),
    ("Dumprar", "Flyttar massor inom arbetsplatsen."),
    ("Hjullastare", "Lastning, grusning och terrassering."),
    ("Vältar", "Packning av vägar, planer och grunder."),
    ("Lastbilar", "Kör grus och maskiner. Kranbil och maskinsläp finns också."),
])
page("maskinpark.html", "Maskinpark", "En modern maskinpark på ca 45 enheter.", f'''{phero("Maskinpark", "En modern maskinpark på ca 45 enheter – rätt maskin för varje jobb.", "hjullastare.jpg", "50% 60%")}<section><div class="in content"><div class="prose"><div class="stats"><div><b>45</b><span>enheter</span></div><div><b>6</b><span>maskintyper</span></div><div><b>20</b><span>anställda</span></div></div><p>Vi strävar efter att hålla maskinparken uppdaterad för att möta dagens krav och minska vår miljöpåverkan.</p><p>Med egna maskiner och egna förare kan vi ta hela markjobbet – och våra lastbilar kör både grus och maskiner.</p></div>{aside_contact(1, "Behöver du en maskin?", "Skicka en förfrågan")}</div></section><section class="related"><div class="in"><h2>I parken</h2>{machines}</div></section>''')

# ---------------------------------------------------------------- om oss
people_html = "".join(f'<div class="person"><span class="av" aria-hidden="true">{av}</span><b>{n}</b><span>{r}, {o}</span></div>' for av, n, r, o, *_ in PEOPLE)
page("om-oss.html", "Om oss", "Ängö Entreprenad – markentreprenör på Orust sedan 1984.", f'''{phero("Om Ängö Entreprenad", "Från enmansbolaget Ängö Schakt 1984 till ca 20 anställda och 45 maskiner.", "orust-hus.jpg", "50% 60%")}<section><div class="in content"><div class="prose"><h2 style="margin-top:0">Markentreprenör på Orust</h2><p>Tillsammans med olika byggföretag utför vi både små och stora markentreprenader – oftast med grundläggning av hus och tillhörande vägar, planer, parkeringar och ledningar. Vi utför även finplanering av alla slag åt både privatpersoner och företag.</p><p>I dag är vi ca 20 anställda och har en modern maskinpark på ca 45 enheter. Huvudkontoret ligger på Hjälmvik, Orust, och sedan 2016 finns vi även i Göteborgsregionen.</p>
  <h2 id="historia">Vår historia</h2>{TIMELINE}
  <h2>Ledning och kontakt</h2><div class="people">{people_html}</div></div>
  <aside class="aside"><h3>Ängö i siffror</h3><dl><div><dt>Grundat</dt><dd>1984 som Ängö Schakt</dd></div><div><dt>Anställda</dt><dd>Ca 20</dd></div><div><dt>Maskiner</dt><dd>Ca 45 enheter</dd></div><div><dt>Kontor</dt><dd>Orust och Göteborg</dd></div></dl><a class="btn btn-g" href="kontakt.html">Kontakta oss</a></aside></div></section><section class="related"><div class="in"><h2>Våra kontor</h2>{card3([("Orust – huvudkontor", "Hjälmvik 252, 472 97 Varekil. Här finns vd, arbetschef och kalkyl."), ("Göteborg", "Dotterbolaget som sedan 2016 utvecklar verksamheten i Göteborgsregionen.")])}</div></section>''')

# ---------------------------------------------------------------- kontakt
contact_cards = "".join(
    f'<div class="office"><b>{n}</b><span>{r}, {o}</span><span><a href="tel:{t}">{p}</a></span><span><a href="mailto:{m}">{m}</a></span></div>'
    for av, n, r, o, p, t, m in PEOPLE)
types = "".join(f"<option>{t}</option>" for t in ["Grundläggning", "Schakt och sprängning", "VA eller enskilt avlopp", "Väg eller parkering", "Finplanering", "Transporter eller kranbil", "Annat"])
page("kontakt.html", "Kontakt", "Kontakta Ängö Entreprenad på Orust och i Göteborg.", f'''{phero("Kontakta oss", f"Ring Dan Johansson på {PHONE} eller mejla {MAIL}.")}<section><div class="in content"><form class="cform" data-mail="{MAIL}">
    <h2>Skicka en förfrågan</h2>
    <label for="cn">Namn<input id="cn" name="namn" data-label="Namn" required autocomplete="name"></label>
    <label for="ce">Mejl<input id="ce" name="mejl" data-label="Mejl" type="email" required autocomplete="email"></label>
    <label for="cp">Telefon<input id="cp" name="telefon" data-label="Telefon" type="tel" autocomplete="tel"></label>
    <label for="ct">Vad gäller det?<select id="ct" name="typ" data-label="Gäller">{types}</select></label>
    <label for="cm">Meddelande<textarea id="cm" name="meddelande" data-label="Meddelande" required placeholder="Var ligger tomten och vad behöver göras?"></textarea></label>
    <button class="btn btn-g" type="submit" style="justify-self:start">Skicka</button>
    <p class="form-ok" hidden tabindex="-1">Tack! Ditt mejlprogram öppnas med förfrågan ifylld – skicka mejlet så hör vi av oss.</p>
  </form>
  <aside class="aside"><h3>Besöksadress</h3><p>Ängö Entreprenad AB<br>Hjälmvik 252<br>472 97 Varekil</p><a class="btn btn-g" href="{MAP}" target="_blank" rel="noopener">Hitta hit</a><h3 style="margin-top:22px">Organisationsnummer</h3><p>556900-2263</p></aside></div></section>
  <section class="related" id="kontor"><div class="in"><h2>Kontaktpersoner</h2><div class="offices" style="margin-top:24px">{contact_cards}</div></div></section>''')

(OUT / "404.html").write_text('''<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sidan finns inte – Ängö Entreprenad</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#f7f3e4;color:#1d1d1b;font:17px/1.6 system-ui,sans-serif;text-align:center;padding:20px}h1{color:#1d1d1b;margin:0 0 8px}a{color:#1d1d1b;font-weight:700}</style></head>
<body><div><h1>Sidan finns inte</h1><p>Den här sidan hittades inte. <a href="./">Till startsidan</a></p></div></body></html>
''', encoding="utf-8")
print("ok", len(list(OUT.glob("*.html"))))
