import click
import webbrowser
import urllib


@click.command()
@click.argument("keyword", type=str)
def cli(keyword):
    url = "http://google.com/search?"
    query = urllib.urlencode({'q': keyword.encode("utf-8")})
    webbrowser.open(url + query)
