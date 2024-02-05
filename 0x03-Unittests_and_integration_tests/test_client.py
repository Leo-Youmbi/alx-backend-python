#!/usr/bin/env python3
"""A module for testing the client module.
"""
import unittest
from unittest.mock import PropertyMock, patch

from client import GithubOrgClient


class TestClient(unittest.TestCase):
    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )


if __name__ == "__main__":
    unittest.main()
