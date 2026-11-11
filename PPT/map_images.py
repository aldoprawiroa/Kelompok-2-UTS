import glob, docx, re

f = glob.glob('Laporan/*.docx')[0]
doc = docx.Document(f)

img_rIds = []
for i, p in enumerate(doc.paragraphs):
    for r in p.runs:
        if 'graphic' in r._element.xml:
            xml = r._element.xml
            m = re.findall(r'r:embed="([^"]+)"', xml)
            prev = doc.paragraphs[i-1].text if i > 0 else ""
            for rId in m:
                target = doc.part.rels[rId].target_ref
                img_rIds.append((i, prev, rId, target))

for idx, (p_idx, prev, rId, target) in enumerate(img_rIds):
    print(f"[{idx}] P{p_idx} rId={rId} target={target} | prev='{prev[:50]}'")
