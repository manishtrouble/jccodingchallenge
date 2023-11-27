from wctool.WCTool import WCTool
import typer
from typer import Typer

app = Typer()


@app.command()
def main(file: str, c: bool = typer.Option(False, "--byte-count", "-c", help="Count bytes in the file"),
         m: bool = typer.Option(False, "--char-count", "-m", help="Count characters in the file"),
         w: bool = typer.Option(False, "--word-count", "-w", help="Count words in the file"),
         l: bool = typer.Option(False, "--line-count", "-l", help="Count lines in the file")):

    ccwc = WCTool(file_path=file)
    output = ""

    options_provided = [c, m, w, l]

    if not any(options_provided):
        byte = ccwc.byte_count()
        words = ccwc.word_count()
        lines = ccwc.line_count()
        output = f"{lines} {words} {byte} {file}"
    else:
        if l:
            line_count = ccwc.line_count()
            output += f"{line_count} "
        if w:
            word_count = ccwc.word_count()
            output += f"{word_count} "
        if c:
            byte_count = ccwc.byte_count()
            output += f"{byte_count} "
        if m:
            char_count = ccwc.char_count()
            output += f"{char_count} "
        output += file

    typer.echo(output.strip())


if __name__ == "__main__":
    app()
