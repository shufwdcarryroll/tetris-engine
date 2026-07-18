
from __future__ import annotations

from typing import Dict, List, Set

from src.tetris_engine.const import DEFAULT_WIDTH, DEFAULT_ZERO
from tetris_engine.shapes import cells_for


class Board:
    def __init__(self, width: int = DEFAULT_WIDTH) -> None:
        if width <= DEFAULT_ZERO:
            raise ValueError(f"width must be greater than 0, got {width}")
        self.width = width
        self._rows: Dict[int, Set[int]] = {}
        self._col_heights: List[int] = [DEFAULT_ZERO] * width

    def drop(self, letter: str, left_col: int) -> None:
        cells = cells_for(letter)
        self._validate_columns(letter, left_col, cells)
        landing_row = self._landing_row(left_col, cells)
        touched_rows = self._place(left_col, cells, landing_row)
        self._clear_completed_rows(touched_rows)

    def _validate_columns(self, letter: str, left_col: int, cells) -> None:
        rightmost = left_col + max(dx for dx, _ in cells)
        if left_col < DEFAULT_ZERO or rightmost >= self.width:
            raise ValueError(
                f"piece {letter!r} at column {left_col} would span "
                f"columns {left_col}..{rightmost}, outside the "
                f"{self.width}-wide grid"
            )

    def _landing_row(self, left_col: int, cells) -> int:
        deepest_local_row: Dict[int, int] = {}
        for dx, dy in cells:
            if dy > deepest_local_row.get(dx, -1):
                deepest_local_row[dx] = dy
        # crux of logic
        return max(
            self._col_heights[left_col + dx] + dy
            for dx, dy in deepest_local_row.items()
        )

    def _place(self, left_col: int, cells, landing_row: int) -> Set[int]:
        touched_rows: Set[int] = set()
        for dx, dy in cells:
            col = left_col + dx
            row = landing_row - dy
            self._rows.setdefault(row, set()).add(col)
            if row + 1 > self._col_heights[col]:
                self._col_heights[col] = row + 1
            touched_rows.add(row)
        return touched_rows

    def _clear_completed_rows(self, candidate_rows: Set[int]) -> None:
        full_rows = sorted(
            row for row in candidate_rows
            if len(self._rows.get(row, ())) == self.width
        )
        if not full_rows:
            return

        full_set = set(full_rows)
        kept = {row: cols for row, cols in self._rows.items() if row not in full_set}
        self._rows = {
            row - sum(1 for cleared in full_rows if cleared < row): cols
            for row, cols in kept.items()
        }
        self._recompute_heights()

    def _recompute_heights(self) -> None:
        heights = [DEFAULT_ZERO] * self.width
        for row, cols in self._rows.items():
            for col in cols:
                if row + 1 > heights[col]:
                    heights[col] = row + 1
        self._col_heights = heights

    @property
    def height(self) -> int:
        return max(self._col_heights, default=DEFAULT_ZERO)

    def column_heights(self) -> List[int]:
        return list(self._col_heights)

    def occupied_cells(self) -> Set[tuple]:
        return {(row, col) for row, cols in self._rows.items() for col in cols}
