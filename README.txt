HOT PURSUIT – OPEN WORLD RACER  ·  HD + STORY CAMPAIGN UPDATE
=============================================================
INSTALL (replace your old index.html / setup.py with these)
 1. Put index.html, setup.py, start.bat, start.sh in your game folder, next to your model files
    (or put new models in an "uploads" folder there).
 2. Windows: double-click start.bat   |  Mac/Linux: ./start.sh
    (runs setup.py -> builds models/ + models/manifest.json, then serves http://localhost:8000)
 3. Open http://localhost:8000 in Chrome/Edge. Needs internet once for three.js (CDN).

WHAT'S NEW
 * Options > Graphics: Standard / High HD (4x MSAA, 1.5x res, 3072 shadows) / Ultra HD (8x MSAA, 2x res, 4096 shadows).
   Anisotropic textures, speed blur + vignette + chromatic edge, optional rain weather (Options > Weather).
 * New cars (garage): Dodge Charger SRT8 (2007 + second model), Nissan GT-R, Dodge SRT Tomahawk X Vision GT.
   They also appear as rivals. Wheels spin; if a car faces backwards press F in-game (saved).
 * CJ (GTA San Andreas character) stands next to your spawn in the open-world city, playing his idle animation.
 * New locations: Asphalt Injection Tokyo + Los Angeles (race/pursuit/campaign), Monaco (EXPERIMENTAL – USDZ,
   no road detection, uses a generated ring line).
 * Story Campaign (main menu): 9 chapters from NFS_and_GTA_Missions_Guide:
   NFS Underground, Most Wanted Blacklist (15 rivals, #15 -> Razor #1), Carbon canyon duels, Hot Pursuit,
   Heat (night + rain), Unbound (4 weeks -> The Grand), GTA Vice City, San Andreas (CJ), GTA V.
   Each mission unlocks after the previous one. Types: checkpoint sprints, time attack, delivery (cargo),
   stunts, drift, rival duels, cop pursuits with heat levels, speedtraps (must be fast at checkpoints).
   Add ?unlock=1 to the URL to open every mission.
 * Your original Championship (100 missions per location) is unchanged and now includes Tokyo/LA/Monaco.

IF SOMETHING LOOKS WRONG
 * Open the browser console (F12). Send me the red messages + which car/location.
 * Tokyo/LA scale or road line off: tell me, I tune cfg.size / road regex in ZONES.
 * Low FPS: Options > Graphics > Standard, Shadows off.
