import os
import pandas as pd

from scripts.pipeline_config import DATA_INPUT_DIR


def _read_csv_or_empty(csv_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(csv_path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def params_distribution():
    dataframes = []

    # Сбор списка датасетов
    for i in range(1, 7):
        csv_path = os.path.join(DATA_INPUT_DIR, f"params_{i}.csv")
        df = _read_csv_or_empty(csv_path)
        dataframes.append(df)
    non_empty_dfs = [df for df in dataframes if not df.empty]

    # Общий датасет
    if non_empty_dfs:
        params_df = pd.concat(non_empty_dfs, ignore_index=True)
    else:
        params_df = pd.DataFrame()

    line_cnt = len(params_df)
    min_lines = line_cnt // 6
    extra_lines = line_cnt % 6
    start_idx = 0
    # Равномерное распределение исходных данных по датасетам
    for i in range(1, 7):
        add_one = 1 if i <= extra_lines else 0
        end_idx = start_idx + min_lines + add_one
        cur_params_df = params_df.iloc[start_idx:end_idx].reset_index(drop=True)
        csv_path = os.path.join(DATA_INPUT_DIR, f"params_{i}.csv")
        cur_params_df.to_csv(csv_path, index=False, encoding="utf-8")
        start_idx = end_idx


if __name__ == "__main__":
    params_distribution()
