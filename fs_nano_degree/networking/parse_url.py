from urllib.parse import urlparse, parse_qs

o = urlparse('https://duckduckgo.com/?q=timer&atb=v92-7__&ia=answer')
print(o)

q = parse_qs(o.query)
print(q)
