import argparse
import subprocess
from datetime import datetime
from pathlib import Path


def copy_text(text):
    process = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    process.communicate(input=text.encode('utf-16le'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--text')
    args = parser.parse_args()

    content = ''

    if args.file:
        p = Path(args.file)
        if p.exists():
            content = p.read_text(encoding='utf-8', errors='replace')
        else:
            content = 'FILE NOT FOUND: ' + str(p)

    if args.text:
        content = args.text

    if not content.strip():
        content = 'EMPTY INPUT'

    message = (
        'ION LOCAL ASSISTANT REPORT\n\n'
        'Please analyze this local assistant output and give the next safe step.\n\n'
        f'Time: {datetime.now().isoformat()}\n\n'
        'DATA:\n'
        f'{content}\n'
    )

    out_dir = Path(__file__).resolve().parent.parent / 'storage' / 'bridge'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / 'last_message.txt'
    out_file.write_text(message, encoding='utf-8')

    copy_text(message)

    print('BRIDGE READY')
    print(out_file)
    print('TEXT COPIED TO CLIPBOARD')


if __name__ == '__main__':
    main()
