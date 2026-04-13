from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json

PORT = 8000

with open("roles.json", "r") as f:
    roles_data = json.load(f)


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            file = open(self.path[1:], "rb")
            self.send_response(200)

            if self.path.endswith(".html"):
                self.send_header("Content-type", "text/html")
            elif self.path.endswith(".css"):
                self.send_header("Content-type", "text/css")

            self.end_headers()
            self.wfile.write(file.read())
            file.close()

        except:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/analyze":

            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            form = urllib.parse.parse_qs(data.decode())

            branch = form.get("branch", [""])[0]
            role = form.get("role", [""])[0]
            skills = form.get("skills", [""])[0]

            user_skills = [s.strip().lower() for s in skills.split(",")]

            role_data = roles_data[branch][role]
            required = role_data["skills"]
            roadmap = role_data["roadmap"]

            required_lower = [s.lower() for s in required]

            missing = [s for s in required_lower if s not in user_skills]

            match = int(((len(required_lower) - len(missing)) / len(required_lower)) * 100)

            # Prepare HTML list
            missing_html = "".join(f"<li>{s.title()}</li>" for s in missing)
            roadmap_html = "".join(f"<li>{r}</li>" for r in roadmap)

            # Load template
            with open("result.html", "r") as file:
                result_page = file.read()

            # Replace placeholders
            result_page = result_page.replace("{{branch}}", branch)
            result_page = result_page.replace("{{role}}", role)
            result_page = result_page.replace("{{match}}", str(match))
            result_page = result_page.replace("{{missing_skills}}", missing_html)
            result_page = result_page.replace("{{roadmap}}", roadmap_html)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(result_page.encode())


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()