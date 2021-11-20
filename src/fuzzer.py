import sys
from parser import parse_args
from post_requests import make_post_requests
from html_parser import parse

def build_list(files):
    """
        Build the Python list with the codes to be used as payloads, starting
        from one or more text file(s) (like "bypass1.txt") in which codes are listed.
        Args:
            files       -- list of inputfiles
        Local Variables:
            a_file      -- one of the multiple files as input
        Returns:
            codes       -- list of codes to be used
    """
    codes = []
    for a_file in files:
        f_open = open(a_file, "r")
        lines = f_open.readlines()
        f_open.close()
        for line in lines:
            codes.append(line.replace("\n", ""))

    return codes


def main():
    """
    Main routine of the fuzzer.

    """
    args = parse_args(sys.argv[1:])
    codes = build_list(args.filelist)
    forms = parse(args.url)
    for form in forms:
        if form.get("method") == "post":
            make_post_requests(form, codes)


if __name__ == '__main__':
    main()
