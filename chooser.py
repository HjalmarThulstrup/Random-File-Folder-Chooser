import os, random, argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A script that opens a random file or folder in the folder specified by the user.')
    parser.add_argument('path', help='Path to directory.')
    args = parser.parse_args()
    path = args.path
    if path[-1:] != "/" or path[-1:] != "\\":
        path = path + "/"
    _path = random.choice(os.listdir(args.path))
    path = path + _path
    os.startfile(path)