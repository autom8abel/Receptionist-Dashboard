import os
import re
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler

load_dotenv()

class EnvRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/index.html' or self.path == '/':
            self.path = '/index.html'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            with open('index.html', 'r') as f:
                content = f.read()
            
            # Inject environment variables as window globals
            injection = f"""
            <script>
            window.__SUPABASE_URL__ = '{os.getenv("SUPABASE_URL", "")}';
            window.__SUPABASE_ANON_KEY__ = '{os.getenv("SUPABASE_ANON_KEY", "")}';
            </script>
            """
            content = content.replace('</head>', injection + '</head>')
            self.wfile.write(content.encode())
        else:
            super().do_GET()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), EnvRequestHandler)
    print('Serving on http://localhost:8080')
    server.serve_forever()