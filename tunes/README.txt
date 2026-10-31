PITCH: offline app
==================
Files: index.html, manifest.webmanifest, sw.js, icons/ (keep them together in one folder).

Offline apps ("PWAs") must be served over HTTPS (or from localhost) the first time.
After that first visit everything is cached and Pitch works with no connection at all.

1) PUT IT ONLINE ONCE (free, ~2 minutes), any of:
   - Netlify Drop: go to app.netlify.com/drop and drag the Pitch folder onto the page.
   - GitHub Pages: upload the files to a repo, then Settings > Pages.
   - Cloudflare Pages / Vercel: upload the folder as a static site.

2) INSTALL IT
   - iPhone/iPad (Safari): open the link > Share > Add to Home Screen.
   - Android (Chrome): open the link > menu > Install app (or Add to Home screen).
   - Desktop (Chrome/Edge): click the install icon at the right of the address bar.
   Open it once while online; after that it launches from its own icon, even in airplane mode.

DESKTOP WITHOUT HOSTING: in this folder run   python3 -m http.server 8000
then open http://localhost:8000 in Chrome/Edge and install it from the address bar.

UPDATING: change the files, re-upload, and bump CACHE = 'pitch-v1' to 'pitch-v2' in sw.js.
Settings (reference A4, saved tempos, custom instruments) are stored on the device.
