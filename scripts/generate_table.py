from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUTS_PATH = ROOT / 'outputs'

def main():
  files = list(OUTPUTS_PATH.glob('labels_*.pt'))
  variants = sorted([f.name[7:-3] for f in files])
  for v in variants:
    tag_pattern = '<a href="https://github.com/nmcardoso/ds-distillation/raw/main/outputs/{f}">{f}</a>'
    image = tag_pattern.format(f=f'images_{v}.pt')
    image_zca = tag_pattern.format(f=f'images_zca_{v}.pt')
    labels = tag_pattern.format(f=f'labels_{v}.pt')
    print(f'<tr><td>{v}</td><td>{image}</td><td>{image_zca}</td><td>{labels}</td></tr>')


if __name__ == "__main__":
  main()