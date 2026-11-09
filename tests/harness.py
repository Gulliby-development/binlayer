"""Row tests: every row builds a fresh database, runs a setup script and prints one view."""

import sqlite3

import pytest

from binlayer import VIEWS, connect, render


def row(setup, view, expected):
    return (setup, view, expected)


def run_row(setup, view):
    conn = connect()
    try:
        conn.executescript(setup)
        rows = conn.execute(f"select * from {view} order by {VIEWS[view]}").fetchall()
        return render(rows)
    except sqlite3.Error as error:
        return f"error: {error}\n"
    finally:
        conn.close()


def rows_test(rows):
    ids = [f"row{n}" for n in range(1, len(rows) + 1)]

    @pytest.mark.parametrize(("setup", "view", "expected"), rows, ids=ids)
    def test_rows(setup, view, expected):
        assert run_row(setup, view) == expected

    return test_rows
