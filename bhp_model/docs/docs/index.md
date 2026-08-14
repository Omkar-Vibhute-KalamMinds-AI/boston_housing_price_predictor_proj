# MlProject documentation!

## Description

Boston house prise prediction projecy

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `gsutil rsync` to recursively sync files in `data/` up to `gs://KalamMinds_bp_project/data/`.
* `make sync_data_down` will use `gsutil rsync` to recursively sync files in `gs://KalamMinds_bp_project/data/` to `data/`.


