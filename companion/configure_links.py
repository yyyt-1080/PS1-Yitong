from pathlib import Path
import argparse,re
p=argparse.ArgumentParser(description='Generate Colab links after the class repository exists.')
p.add_argument('organization');p.add_argument('repository');a=p.parse_args()
for s in [a.organization,a.repository]:
 if not re.fullmatch(r'[A-Za-z0-9_.-]+',s):p.error('Use a valid GitHub path segment')
lines=['# Colab links','Verify repository existence and student access before distributing.','']
for f in sorted(Path('notebooks').glob('*.ipynb')):
 lines.append(f'- [{f.stem}](https://colab.research.google.com/github/{a.organization}/{a.repository}/blob/main/notebooks/{f.name})')
Path('COLAB_LINKS.md').write_text('\n'.join(lines)+'\n')
print('Wrote COLAB_LINKS.md; these links are not automatically verified or published.')
