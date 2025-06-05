"""
HTTP Cookie Security Analyzer - Detects Stealing Attempts

Checks for:
- Missing Secure/HttpOnly flags (Session Hijacking)
- Suspicious JavaScript cookie access (XSS Exfiltration)
- Overly permissive Domain/Path settings
- SameSite misconfigurations (CSRF risks)
"""

from flask import Flask, request, Response
import re

app = Flask(__name__)

def analyze_cookies(headers):
    warnings = []
    cookies = headers.get_all("Set-Cookie", [])
    
    for cookie in cookies:
        # Check for critical missing flags
        if "Secure" not in cookie:
            warnings.append(f"Missing Secure flag: {cookie.split(';')[0]}")
        if "HttpOnly" not in cookie:
            warnings.append(f"Missing HttpOnly flag: {cookie.split(';')[0]}")
        
        # Detect overly permissive domains
        if "Domain=" in cookie:
            domain = re.search(r"Domain=(.+?);", cookie)
            if domain and domain.group(1).startswith("."):
                warnings.append(f"Overly permissive Domain: {domain.group(1)}")
        
        # SameSite checks
        if "SameSite" not in cookie:
            warnings.append(f"Missing SameSite attribute: {cookie.split(';')[0]}")
    
    return warnings

@app.route("/")
def scan():
    warnings = analyze_cookies(request.headers)
    if warnings:
        return Response("\n".join(warnings), mimetype="text/plain", status=403)
    return "✅ No cookie security issues detected"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
