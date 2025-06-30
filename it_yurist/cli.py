import argparse
from pathlib import Path
from datetime import date

TEMPLATE_DIR = Path(__file__).parent / 'templates'


def render_template(name: str, **context) -> str:
    template_path = TEMPLATE_DIR / name
    if not template_path.exists():
        raise FileNotFoundError(f"Template '{name}' not found")
    text = template_path.read_text(encoding='utf-8')
    return text.format(**context)


def generate_nda(args):
    context = {
        'company': args.company,
        'partner': args.partner,
        'date': args.date or date.today().isoformat(),
    }
    output = render_template('nda_template.txt', **context)
    if args.output:
        Path(args.output).write_text(output, encoding='utf-8')
    else:
        print(output)


def main(argv=None):
    parser = argparse.ArgumentParser(description='it-yurist legal document generator')
    subparsers = parser.add_subparsers(dest='command')

    nda_parser = subparsers.add_parser('nda', help='Generate a simple NDA')
    nda_parser.add_argument('--company', required=True, help='Company name')
    nda_parser.add_argument('--partner', required=True, help='Partner name')
    nda_parser.add_argument('--date', help='Date of agreement (YYYY-MM-DD)')
    nda_parser.add_argument('--output', help='Output file path')
    nda_parser.set_defaults(func=generate_nda)

    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
