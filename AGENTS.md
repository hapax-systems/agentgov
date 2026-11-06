# Repository Guidance

This repository is published by **Hapax Research Lab** under the `hapax-systems`
GitHub organization. Do not create, move, or point repository automation at any
personal user namespace or outside `hapax-systems`.

External review and analysis from CodeRabbit, Claude, Codex, Codecov, and
Semgrep is advisory in this repository unless a governed Hapax Research Lab task
explicitly promotes a stable aggregate check to a branch-protection gate.
Preserve the repository-owned `all-green` CI aggregate as the merge-readiness
signal.

Secrets belong in the deployment secret store or GitHub repository/organization
secrets; never commit secret values.
