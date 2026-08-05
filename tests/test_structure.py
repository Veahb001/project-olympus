from pathlib import Path


ROOT = Path(__file__).parent.parent


def test_required_directories_exist():
    required = [
        "devices",
        "docker",
        "network",
        "services",
        "scripts",
        "olympus-docs",
    ]

    for directory in required:
        assert (ROOT / directory).exists(), f"Missing directory: {directory}"


def test_readme_exists():
    assert (ROOT / "README.md").exists()