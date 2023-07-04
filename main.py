import argparse
from run import run


def main() -> None:
    # Create parser
    parser = argparse.ArgumentParser("python3 main.py")
    subparsers = parser.add_subparsers()

    # create parser for the program run
    parser_run = subparsers.add_parser("run", help="run the specified program")
    parser_run.add_argument("file", type=str, help="specifies the file to run")

    args = parser.parse_args()

    run(args.file)


if __name__ == "__main__":
    main()
