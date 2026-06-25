# Repository Guidance

Hapax repositories must live under `hapax-systems`. Do not create, move, or point
automation at a Hapax repository under `ryanklee`.

External review and analysis from CodeRabbit, Claude, Codex, Codecov, and
Semgrep is advisory in this repository unless a governed Hapax task explicitly
promotes a stable aggregate check to a branch-protection gate. Preserve the
repository-owned `all-green` CI aggregate as the merge-readiness signal.

Secrets belong in GitHub repository or organization secrets, `pass`, or
`hapax-secrets`; never commit secret values.
