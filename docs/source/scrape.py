from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://example.com")

print("Status:", r.status_code)
print("Title:", r.html.find("title", first=True).text)
