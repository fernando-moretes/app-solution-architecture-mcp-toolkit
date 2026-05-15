import argparse
from .adr import build_adr
from .well_architected import checklist

def main(argv=None):
    parser = argparse.ArgumentParser(description="Solution Architecture Toolkit")
    sub = parser.add_subparsers(dest="command", required=True)
    adr = sub.add_parser("adr")
    adr.add_argument("--title", required=True)
    adr.add_argument("--context", required=True)
    adr.add_argument("--decision", required=True)
    sub.add_parser("well-architected")
    args = parser.parse_args(argv)
    if args.command == "adr":
        print(build_adr(args.title, args.context, args.decision).to_markdown())
    elif args.command == "well-architected":
        print(checklist())
