import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_INPUT_DIR = BASE_DIR / "artifacts" / "data_input"
DATA_OUTPUT_DIR = BASE_DIR / "artifacts" / "data_output"


RUN_TAG = os.getenv("RUN_TAG", "local")
API_NUM = int(os.getenv("API_NUM", "1"))


API_CONFIGS = {
    1: {
        "params_file": "params_1.csv",
        "output_dir": "first_api_results",
        "output_prefix_1": f"first_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"first_api_output_{RUN_TAG}",
    },
    2: {
        "params_file": "params_2.csv",
        "output_dir": "second_api_results",
        "output_prefix_1": f"second_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"second_api_output_{RUN_TAG}",
    },
    3: {
        "params_file": "params_3.csv",
        "output_dir": "third_api_results",
        "output_prefix_1": f"third_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"third_api_output_{RUN_TAG}",
    },
    4: {
        "params_file": "params_4.csv",
        "output_dir": "fourth_api_results",
        "output_prefix_1": f"fourth_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"fourth_api_output_{RUN_TAG}",
    },
    5: {
        "params_file": "params_5.csv",
        "output_dir": "fifth_api_results",
        "output_prefix_1": f"fifth_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"fifth_api_output_{RUN_TAG}",
    },
    6: {
        "params_file": "params_6.csv",
        "output_dir": "sixth_api_results",
        "output_prefix_1": f"sixth_api_config_output_{RUN_TAG}",
        "output_prefix_0": f"sixth_api_output_{RUN_TAG}",
    }
}
