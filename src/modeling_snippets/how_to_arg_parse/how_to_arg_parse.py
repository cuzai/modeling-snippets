import argparse


class HowToArgParse:
    def __init__(self, arg1: str):
        self.arg1 = arg1

    def __call__(self):
        print(f"Argument received: {self.arg1}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", type=str, required=True)
    args = parser.parse_args()

    how_to_arg_parse = HowToArgParse(arg1=args.arg1)
    how_to_arg_parse()
