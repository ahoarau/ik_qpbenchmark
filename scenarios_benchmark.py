#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: Apache-2.0
# Copyright 2024 Inria

from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
import qpbenchmark
from qpbenchmark.benchmark import main


class ScenariosBenchmark(qpbenchmark.ParquetTestSet):
    """Scenarios test set."""

    @property
    def description(self) -> str:
        return (
            "Differential inverse kinematics QP problems "
            "generated from Talos robot motions (static and trajectory)"
        )

    @property
    def title(self) -> str:
        return "Scenarios test set (Talos)"

    @property
    def sparse_only(self) -> bool:
        return False

    def __init__(self):
        script_dir = Path(__file__).resolve().parent
        self.parquet_path = script_dir / "data" / "scenarios_ik.parquet"
        qpbenchmark.TestSet.__init__(self)

    def __iter__(self):
        limit = getattr(self, "limit", 0)
        count = 0
        parquet_file = pq.ParquetFile(self.parquet_path)
        for batch in parquet_file.iter_batches():
            df = batch.to_pandas()
            for _, row in df.iterrows():
                if limit and count >= limit:
                    return
                n = row["q"].size
                pb_data = {}
                for key in qpbenchmark.ProblemList.KEYS:
                    if isinstance(row[key], np.ndarray):
                        # Copy before reshape (reshape requires a writeable array)
                        pb_data[key] = row[key].copy()
                        if key in ("P", "G", "A"):
                            m = pb_data[key].size // n
                            pb_data[key] = pb_data[key].reshape((m, n))
                    else:  # string or None
                        pb_data[key] = row[key]
                yield qpbenchmark.Problem(**pb_data)
                count += 1

    def count_problems(self) -> int:
        parquet_file = pq.ParquetFile(self.parquet_path)
        return parquet_file.metadata.num_rows


if __name__ == "__main__":
    test_set_path = Path(__file__).resolve()
    results_path = (
        test_set_path.parent / "results" / "scenarios_results.parquet"
    )
    main(test_set_path=test_set_path, results_path=results_path)
