"""Run:  python setup.py   (Windows)   or   python3 setup.py   (Mac/Linux)
Put this file + index.html next to ALL your model files (.glb/.usdz/.zip), or put the models in an ./uploads folder.
It builds ./models and a models/manifest.json that maps every game asset to whichever copy of the file you have
(extra hash prefixes, 'Copy', dots vs underscores are all handled)."""
import os, re, shutil, zipfile, glob, json, sys
here = os.path.dirname(os.path.abspath(__file__)); md = os.path.join(here, 'models'); os.makedirs(md, exist_ok=True)

def norm(n):
    n = n.lower()
    n = re.sub(r'^[0-9a-f]{8}-', '', n)                    # upload hash prefix
    n = re.sub(r'(_-_copy|_copy|\s-\scopy|_\d$)', '', n.rsplit('.', 1)[0]) + '.' + n.rsplit('.', 1)[-1]
    return re.sub(r'[^a-z0-9/.]+', '_', n)

for src in [here, os.path.join(here, 'uploads')]:
    for f in glob.glob(os.path.join(src, '*')):
        n = os.path.basename(f); ext = n.lower().rsplit('.', 1)[-1]
        if ext in ('glb', 'usdz'):
            dst = os.path.join(md, re.sub(r'^[0-9a-f]{8}-', '', n))
            if not os.path.exists(dst): shutil.copy(f, dst); print('copied', n)
        elif ext == 'zip' and re.search(r'(mazda|nurburg|circuit_de|catalunya)', n, re.I):
            d = os.path.join(md, n[:-4]); 
            if not os.path.isdir(d): zipfile.ZipFile(f).extractall(d); print('extracted', n)

# logical key -> regex that must match the normalised file name (first match wins; more specific first)
PAT = {
 'charger07': r'^2007_dodge_charger', 'chargerS': r'^dodge_charger_srt8\.', 'gtr': r'nissan_gt_r', 'tomahawk': r'tomahawk',
 'cj': r'cj_animated', 'tokyo': r'tokyo', 'la': r'los_angeles', 'monaco': r'monaco',
 'jaguar': r'jaguar_vision', 'monza': r'monza_sp1', 'futuristic': r'futuristic_car', 'mclaren': r'^mclaren_f1',
 'city': r'^city\.', 'building': r'^building\.', 'tank': r'amphibious_tank',
 'lotus': r'lotus_elise', 'odyssey': r'honda_odyssey', 'idr': r'volkswagen_i_d_r_with_interior', 'idr19': r'2019_volkswagen_id',
 'delivery': r'delivery_truck', 'tata': r'tata_signa', 'venom': r'hennessey_venom', 'huracan': r'huracan_trofeo', 'supra': r'supra_gt300',
 'f296': r'296_gt3', 'ford': r'shelby_gt500', 'hk': r'hongkong', 'peak': r'lone_peak', 'ahv': r'ahvenisto', 'kart': r'karting_club',
 'tire': r'tire_wall', 'finish': r'finish_line', 'rampW': r'wooden_stunt_ramp', 'rampI': r'industrial_stunt_ramp',
 'arcade': r'super_bear', 'garage': r'breakout_garage', 'forza': r'forza_horizon', 'wheelA': r'tuner_car_wheel', 'wheelB': r'wheels_sport_for_tuning',
 'skyDay': r'skybox_basic_sky', 'skyEve': r'ghostly_evening', 'skyNight': r'milky_way',
 'mazda': r'mazda_lm_vision.*scene\.gltf', 'nur': r'nurburgring.*scene\.gltf', 'cat': r'circuit_de_catalunya.*scene\.gltf'}
files = []
for root, _, fs in os.walk(md):
    for f in fs:
        if f.lower().endswith(('.glb', '.usdz', '.gltf')) :
            rel = os.path.relpath(os.path.join(root, f), md).replace('\\', '/'); files.append((rel, norm(rel)))
man = {}
for k, rx in PAT.items():
    for rel, nm in files:
        if re.search(rx, nm): man[k] = rel; break
json.dump(man, open(os.path.join(md, 'manifest.json'), 'w'), indent=1)
print('\nMapped %d of %d game assets.' % (len(man), len(PAT)))
for k in PAT:
    if k not in man: print('  missing (game will skip or show an error for it):', k)
print('\nDone. Now run start.bat (Windows) or ./start.sh (Mac/Linux) and open http://localhost:8000')
