headers = {
    'Content-Type': "application/json",
    'Connection': "keep-alive"
}

header2 = {
    'Look': "here",
    'Content-Type': "application/text"
}

headers.update(header2)

print(headers)
