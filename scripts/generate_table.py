from pathlib import Path

ROOT = Path(__file__).parent.parent
OUTPUTS_PATH = ROOT / 'outputs'

def main():
  files = list(OUTPUTS_PATH.glob('labels_*.pt'))
  variants = sorted([f.name[7:-3] for f in files])
  for v in variants:
    image = f'<a href="">image_{v}.pt</a>'
    image_zca = f'<a href="">image_zca_{v}.pt</a>'
    labels = f'<a href="">labels_{v}.pt</a>'
    print(f'<tr><td>{v}</td><td>{image}</td><td>{image_zca}</td><td>{labels}</td></tr>')


if __name__ == "__main__":
  main()