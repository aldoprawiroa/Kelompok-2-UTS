import glob, docx, os

f = glob.glob('Laporan/*.docx')[0]
doc = docx.Document(f)
os.makedirs('presentation_assets', exist_ok=True)

for rel in doc.part.rels.values():
    if 'image' in rel.target_ref:
        fname = os.path.basename(rel.target_ref)
        with open(os.path.join('presentation_assets', fname), 'wb') as out:
            out.write(rel.target_part.blob)

print("Saved all images to presentation_assets with original names!")
