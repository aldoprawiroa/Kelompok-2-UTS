import glob, docx

files = glob.glob('Laporan/*.docx')
doc = docx.Document(files[0])
for i, p in enumerate(doc.paragraphs):
    for r in p.runs:
        if 'graphic' in r._element.xml:
            prev = doc.paragraphs[i-1].text if i > 0 else ""
            print(f"P{i} [prev: {prev[:60]}] -> {p.text[:60]}")
