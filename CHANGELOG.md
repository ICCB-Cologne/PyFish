# Changelog

## [1.1.0] - 2026-04-15

### Added
- `-V, --curved` option: smooths filled areas using piecewise Hermite interpolation with S-curve transitions. Adds a gray background and centers the plot when population is empty at the first step.
- `-E, --separate` option: places children equidistant from each other within their parent band. By default, children now emerge from the center of the parent.
- Linear interpolation mode: `-I 0` now performs linear interpolation between known data points. Negative values (default) fill missing values with 0.
- Default smooth value changed to `-1` (no smoothing). Negative values disable smoothing explicitly.
- `--curved` and `--smooth` are now mutually exclusive.
- Automatic root creation: if multiple nodes have no parent, or if population IDs are not listed in the parent tree, a synthetic root with zero population is created to parent them all.
- `tests/generate_doc_images.py` script to regenerate all documentation images.

### Fixed
- FutureWarning for pandas `fillna(inplace=True)` on DataFrame slices.

### Changed
- Migrated repository URLs from Bitbucket to GitHub.

## [1.0.3] - Initial tracked version
