from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import os
import html

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "roles.json"), "r", encoding="utf-8") as f:
    roles_data = json.load(f)


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        req_path = self.path.split("?")[0]
        if req_path == "/":
            req_path = "/index.html"

        # Sanitize path to prevent directory traversal
        clean_path = os.path.normpath(req_path.lstrip("/"))
        file_path = os.path.abspath(os.path.join(BASE_DIR, clean_path))

        # Ensure requested file is strictly inside BASE_DIR and exists
        if not file_path.startswith(BASE_DIR) or not os.path.isfile(file_path):
            self.send_error(404, "File Not Found")
            return

        try:
            with open(file_path, "rb") as file:
                self.send_response(200)
                if file_path.endswith(".html"):
                    self.send_header("Content-type", "text/html; charset=utf-8")
                elif file_path.endswith(".css"):
                    self.send_header("Content-type", "text/css; charset=utf-8")
                elif file_path.endswith(".json"):
                    self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(file.read())
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {e}")

    def do_POST(self):
        if self.path == "/analyze":
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)
            form = urllib.parse.parse_qs(data.decode("utf-8", errors="replace"))

            branch = form.get("branch", [""])[0]
            role = form.get("role", [""])[0]
            skills = form.get("skills", [""])[0]

            user_skills = [s.strip().lower() for s in skills.split(",") if s.strip()]

            if branch not in roles_data or role not in roles_data[branch]:
                self.send_error(400, "Selected Branch or Role data is currently unavailable.")
                return

            role_data = roles_data[branch][role]
            required = role_data.get("skills", [])
            roadmap = role_data.get("roadmap", [])

            required_lower = [s.lower() for s in required]
            missing = [s for s in required_lower if s not in user_skills]

            if len(required_lower) > 0:
                match = int(((len(required_lower) - len(missing)) / len(required_lower)) * 100)
            else:
                match = 100

            # Safely escape HTML to prevent XSS
            missing_html = "".join(f"<li>{html.escape(s.title())}</li>" for s in missing)
            roadmap_html = "".join(f"<li>{html.escape(r)}</li>" for r in roadmap)

            result_file_path = os.path.join(BASE_DIR, "result.html")
            with open(result_file_path, "r", encoding="utf-8") as file:
                result_page = file.read()

            result_page = result_page.replace("{{branch}}", html.escape(branch))
            result_page = result_page.replace("{{role}}", html.escape(role))
            result_page = result_page.replace("{{match}}", str(match))
            result_page = result_page.replace("{{missing_skills}}", missing_html)
            result_page = result_page.replace("{{roadmap}}", roadmap_html)

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(result_page.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
