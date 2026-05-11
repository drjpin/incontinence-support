import os
import sys
os.chdir("/Users/joshuafritz/Documents/GitHub/incontinence-support/.claude/worktrees/musing-elion")
sys.argv = [""]
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
