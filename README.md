# python-code-assignment

This coding assignment consists of 3 simple tasks:

## Utils

You're supposed to implement utility functions in this folder.


- `parse_npm_version` should parse a string that represents a package name with it's version and return this 
info as Python's `dict`. The only complication here is that organisations are prefixed with `@` while it also serves as
a separator for a name and a version.

## API Task

Your task is to connect to GitHub API (public API doesn't require a token) and retrieve information about an organisation
and format it a string that unit tests expect you to return.
You're free to modify the data in an expected string so that the test passes.

Bonus task: The unit test depends on real-world API that is subject to a change. If you manage to mock the API so that a test
is deterministic, it's a huge plus.

## Crawling task

Your goal is to implement a simple crawler that connects to Django's Blog and retrieve titles of latest blog posts.