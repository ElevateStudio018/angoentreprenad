# Ängö Entreprenad – webbplats

Ny webbplats för [Ängö Entreprenad AB](https://angoentreprenad.se/), byggd på samma mall som
[Lindvik Bygg-sidan i lirk](https://elevatestudio018.github.io/lirk/) (vitt, beige och skogsgrönt,
Bricolage Grotesque + Source Sans 3). Designen, `site.css` och `site.js` är desamma; texten är Ängös egen.

## Sidor

Allt ligger i [`docs/`](docs/) och behöver inga verktyg – öppna `docs/index.html` i en webbläsare.

- `index.html` – startsidan
- `tjanster.html` + sex tjänstesidor: grundläggning, schakt och sprängning, VA och enskilda avlopp,
  vägar och planer, finplanering, transporter och kranbil
- `projekt.html`, `projekt-lassby.html`
- `maskinpark.html`, `om-oss.html` (med historia), `kontakt.html`

Kontaktformuläret öppnar ett ifyllt mejl till dan@angoentreprenad.se.

## Bilder

Fotona i `docs/img/` är stockbilder från [Pexels](https://www.pexels.com) (samma som i mallen) och
fungerar som platshållare. Byt dem mot Ängös egna bilder genom att ersätta filerna med samma namn.

## Ändra text

Sidorna genereras av `scripts/build.py`. Ändra texten där och kör:

```bash
python3 scripts/build.py docs
```

## Publicera

Slå på GitHub Pages i repots inställningar: *Deploy from a branch*, mappen `/docs`.
