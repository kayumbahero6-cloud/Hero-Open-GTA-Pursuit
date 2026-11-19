"""Tiny static file server for the game (standard library only).
Local:   python server.py            -> http://localhost:8000
Render:  start command "python server.py" (Render sets the PORT variable automatically)."""
import os, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,
        '.glb': 'model/gltf-binary', '.gltf': 'model/gltf+json', '.usdz': 'model/vnd.usdz+zip',
        '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json', '': 'application/octet-stream'}
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    def log_message(self, fmt, *args):
        sys.stderr.write('%s - %s\n' % (self.address_string(), fmt % args))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8000'))
    srv = ThreadingHTTPServer(('0.0.0.0', port), Handler)
    print('Serving game on port %d' % port, flush=True)
    srv.serve_forever()
