def main():
    from string import ascii_letters, digits
    from subprocess import run
    from sys import executable, stderr, stdout
    from tempfile import NamedTemporaryFile

    print("Just read the flag.txt! Very simple!")

    def readline():
        while line := input("> "):
            yield "".join(
                char for char in line if char in Rf":+-*/\#{ascii_letters}{digits}"
            )

    with NamedTemporaryFile("r+t", encoding="utf-8", delete_on_close=False) as file:
        file.write("\n".join(readline()))
        file.close()
        run(
            (executable, file.name),
            encoding="utf-8",
            stdin=None,
            stdout=stdout,
            stderr=stderr,
            timeout=1,
        )


if __name__ == "__main__":
    main()
