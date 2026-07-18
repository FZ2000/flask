"""Throwaway demo helper with intentionally planted issues (deleted after the demo)."""
from __future__ import annotations

import subprocess

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # planted: hardcoded credential (dummy example key)


def get_user(conn, user_id):
    cur = conn.cursor()
    # planted: SQL injection via string concatenation
    cur.execute("SELECT * FROM users WHERE id = " + str(user_id))
    return cur.fetchone()


def run_cmd(cmd):
    # planted: shell=True command injection
    return subprocess.run(cmd, shell=True)
