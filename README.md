# IntelliCheck

**Explainable document-similarity screening for plagiarism review and content comparison.**

IntelliCheck is a lightweight, transparent NLP project that compares two text samples using token overlap and sequence similarity. It is designed as a foundation for an academic-integrity workflow where a reviewer can inspect the evidence instead of relying on an opaque score.

## Why this project

Similarity tools are most useful when they explain *why* two documents look similar. IntelliCheck separates the scoring layer from the human-review decision and keeps the baseline dependency-free so the algorithm is easy to audit.

## Features

- Normalized token extraction for case and punctuation differences.
- Jaccard similarity for shared vocabulary.
- SequenceMatcher score for character-level structure.
- Dependency-free Python demo.
- Clear extension points for sentence embeddings, highlighted matches and batch CSV analysis.

## How it works

1. Normalize each document into comparable tokens.
2. Calculate vocabulary overlap with Jaccard similarity.
3. Compare the original strings with sequence matching.
4. Present both scores for human interpretation.

## Quick start

```bash
python3 app.py
```

## Example output

```text
IntelliCheck demo
{'jaccard': 50.0, 'sequence': 82.35}
```

## Project structure

```text
app.py        # dependency-free comparison demo
README.md     # project documentation
```

## Roadmap

- Add sentence-transformer embeddings for semantic matching.
- Highlight matching spans in an HTML report.
- Add batch processing for a folder of documents.
- Add a reviewer dashboard with exportable audit trails.

## Limitations

A similarity score is not proof of plagiarism. Common phrases, citations and legitimate collaboration can produce high overlap. This demo is for educational and portfolio use only.

## Tech stack

Python 3 · standard library · NLP fundamentals

## Author

Built by **Tallal Kiani** as part of an AI and software-development portfolio.
