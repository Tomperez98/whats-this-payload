"""Release GitHub."""
import webbrowser
from urllib.parse import urlencode
import tomli
import pkg_resources  # type: ignore[import]
import pathlib


def main() -> None:
    """Open a tab ready to review and approve for new release."""
    pkg_data = tomli.loads(pathlib.Path("pyproject.toml").read_text(encoding="utf-8"))
    version = pkg_resources.get_distribution("whats_this_payload").version

    params = urlencode(
        query={
            "title": "v{version}".format(version=version),
            "tag": "v{version}".format(version=version),
        }
    )

    webbrowser.open_new_tab(
        url="{source}/releases/new?{params}".format(
            source=pkg_data["project"]["urls"]["Source"], params=params
        )
    )


if __name__ == "__main__":
    main()
