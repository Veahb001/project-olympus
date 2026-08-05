from pathlib import Path


ROOT = Path(__file__).parent.parent


def test_markdown_files_have_content():
    markdown_files = list(ROOT.rglob("*.md"))

    assert len(markdown_files) > 0

    for file in markdown_files:
        content = file.read_text(encoding="utf-8")
        assert len(content.strip()) > 20, f"{file} is empty"