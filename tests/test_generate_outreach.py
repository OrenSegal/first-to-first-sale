"""Unit tests for signal-outreach's report generator, plus a full-report
smoke test against the example outreach package."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "signal-outreach" / "scripts" / "generate_outreach.py"
EXAMPLE = ROOT / "examples" / "outreach-package.json"

sys.path.insert(0, str(SCRIPT.parent))
import generate_outreach as go  # noqa: E402


def test_esc_escapes_html():
    assert go.esc("<script>alert(1)</script>") == "&lt;script&gt;alert(1)&lt;/script&gt;"


def test_esc_handles_none():
    assert go.esc(None) == ""


def test_clamp_bounds_to_range():
    assert go.clamp(150) == 100
    assert go.clamp(-10) == 0
    assert go.clamp(42) == 42


def test_clamp_handles_non_numeric():
    assert go.clamp("not a number") == 0


def test_items_wraps_scalar_in_list():
    assert go.items("x") == ["x"]
    assert go.items(None) == []
    assert go.items([1, 2]) == [1, 2]


def test_dicts_filters_non_dict_entries():
    assert go.dicts([{"a": 1}, "skip", {"b": 2}, None]) == [{"a": 1}, {"b": 2}]


def test_build_html_smoke():
    data = json.loads(EXAMPLE.read_text())
    output = go.build_html(data)
    assert "<html" in output.lower()
    assert len(output) > 500


def test_generate_outreach_cli_runs_against_example(tmp_path):
    out_path = tmp_path / "report.html"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(EXAMPLE), str(out_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert out_path.exists()
    assert out_path.stat().st_size > 0
