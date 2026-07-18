"""Demo helper — contains intentionally PLANTED issues for testing the PR reviewer.

This file exists only on a throwaway demo branch of a personal fork; it is
deleted after the test. Every issue below is a deliberate, well-known bad
pattern the reviewer is expected to flag.
"""
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


def average(nums):
    # planted: unhandled empty-input edge case -> ZeroDivisionError
    return sum(nums) / len(nums)
