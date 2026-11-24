# Validation status

Snapshot: 23 November 2026. Version 0.2.0 is a local pilot package, ready for host installation testing.

## Locally checked

- Fourteen named skills with bundled references and no external skill/tool connection dependency.
- Seventy-three competency groups and an acyclic prerequisite map.
- Thirty-six original numerical tasks, including direct-discounting checks, probability moments, duration repricing and state-by-state binomial replication.
- Readiness handling for unknown areas, duplicate task families, helped answers, verified delayed retrieval, stale evidence and later failures.
- Learning-log initialization, full event persistence, idempotent retries, derived-file reconstruction, unique safe paths, write locking and personal-workspace boundaries.
- Study-plan persistence, completed-block updates, valid competency IDs, no preparation on/after a stated exam date, and daily confirmed-capacity checks.
- Internal Markdown links, portable package paths and distribution allowlist.
- Original README SVG illustrations rendered and visually inspected.

Run the reproducible package checks with Python 3.10 or later:

```bash
python tools/check_package.py
```

Python is a maintainer test dependency, not a prerequisite for a student using the plugin in a supported ChatGPT environment. The journal/scoring helpers use the standard library; native host file tools and transparent manual evidence summaries remain supported alternatives.

## Still to verify in a real learner environment

- ChatGPT/Edu installation, plugin selection, discovery of all skills and access to sibling references.
- Always-on protocol updates using that host's actual file/export tools.
- Real multi-turn teaching behavior, plan personalization and return-session retrieval.
- Subject-matter review by the course owner of the full conceptual coverage and extended summary.
- Learning outcomes and empirical calibration of the readiness index.

No claim of a completed live student pilot, production deployment, statistical score calibration or complete reconstruction of oral classroom explanations is made. Original lecture decks, instructor audit extracts and historical assessment files are not shipped. The published source hashes identify provenance; they do not themselves prove semantic correctness.
