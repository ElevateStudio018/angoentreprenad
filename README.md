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

Fotona i `docs/img/` är stockbilder från [Pexels](https://www.pexels.com) (fria att använda enligt
Pexels licens), valda för markarbete, maskiner, Orust och Göteborg. Byt gärna ut dem mot Ängös egna
bilder genom att ersätta filerna med samma namn. `villaomrade.jpg` (Låssby) kommer från mallen.

| Fil | Pexels-ID |
| --- | --- |
| `hero-gravmaskin.jpg` | [6245621](https://www.pexels.com/photo/6245621/) |
| `hero-grus.jpg` | [95687](https://www.pexels.com/photo/95687/) |
| `hero-vag.jpg` | [12228684](https://www.pexels.com/photo/12228684/) |
| `grundlaggning.jpg` | [11429201](https://www.pexels.com/photo/11429201/) |
| `schakt.jpg` | [13098128](https://www.pexels.com/photo/13098128/) |
| `va-ror.jpg` | [9389356](https://www.pexels.com/photo/9389356/) |
| `vagar.jpg` | [12274279](https://www.pexels.com/photo/12274279/) |
| `finplanering.jpg` | [7598364](https://www.pexels.com/photo/7598364/) |
| `transporter.jpg` | [12032967](https://www.pexels.com/photo/12032967/) |
| `team.jpg` | [8961064](https://www.pexels.com/photo/8961064/) |
| `husgrund.jpg` | [29735767](https://www.pexels.com/photo/29735767/) |
| `asfalt.jpg` | [19394246](https://www.pexels.com/photo/19394246/) |
| `ror.jpg` | [29301874](https://www.pexels.com/photo/29301874/) |
| `armering.jpg` | [9964624](https://www.pexels.com/photo/9964624/) |
| `tomt.jpg` | [17240696](https://www.pexels.com/photo/17240696/) |
| `hjullastare.jpg` | [461789](https://www.pexels.com/photo/461789/) |
| `traktorgravare.jpg` | [3998410](https://www.pexels.com/photo/3998410/) |
| `orust-hus.jpg` | [34400606](https://www.pexels.com/photo/34400606/) |
| `arbetsledare.jpg` | [8961030](https://www.pexels.com/photo/8961030/) |
| `goteborg.jpg` | [29004795](https://www.pexels.com/photo/29004795/) |
| `medarbetare.jpg` | [8961155](https://www.pexels.com/photo/8961155/) |
| `hjulgravare.jpg` | [36957845](https://www.pexels.com/photo/36957845/) |
| `maskiner.jpg` | [5125783](https://www.pexels.com/photo/5125783/) |
| `alvsborgsbron.jpg` | [31146748](https://www.pexels.com/photo/31146748/) |

## Video i toppen

Startsidans fullskärmshero spelar Ängös egen drönarfilm (tyst, i loop). Originalet (89 MB) är
komprimerat till `docs/video/hero.mp4` (1920×1080, ca 10 MB) och `docs/video/hero-mobil.mp4`
(960×540, ca 3 MB, används på mobil). `docs/img/hero-poster.jpg` visas innan videon har laddats.

För att byta video: komprimera den nya filen på samma sätt, till exempel

```bash
ffmpeg -i ny.mp4 -an -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -movflags +faststart -vf scale=1920:-2 docs/video/hero.mp4
ffmpeg -i ny.mp4 -an -c:v libx264 -preset slow -crf 28 -profile:v main -pix_fmt yuv420p -movflags +faststart -vf scale=960:-2 docs/video/hero-mobil.mp4
```

## Ändra text

Sidorna genereras av `scripts/build.py`. Ändra texten där och kör:

```bash
python3 scripts/build.py docs
```

## Publicera

Slå på GitHub Pages i repots inställningar: *Deploy from a branch*, mappen `/docs`.
