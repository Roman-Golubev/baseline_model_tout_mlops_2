import os
import pandas as pd

from scripts.baseline_model import baseline_model
from scripts.pipeline_config import DATA_INPUT_DIR, DATA_OUTPUT_DIR, API_CONFIGS, API_NUM


def _save_batch(results_lst, output_dir, output_prefix, pkl_num):
    os.makedirs(output_dir, exist_ok=True)
    pkl_path = os.path.join(output_dir, f"{output_prefix}_{pkl_num}.pkl")
    pd.DataFrame(results_lst).to_pickle(pkl_path)
    print(f"Saved {pkl_path} with {len(results_lst)} results")


def bootstrap_calculation(api_num=API_NUM):
    cfg = API_CONFIGS[api_num]
    input_path = os.path.join(DATA_INPUT_DIR, cfg["params_file"])
    output_dir = os.path.join(DATA_OUTPUT_DIR, cfg["output_dir"])
    output_prefix_0 = cfg["output_prefix_0"]
    output_prefix_1 = cfg["output_prefix_1"]

    
    results_lst = []
    results_config_lst = []
    pkl_num = 1
    params_df = pd.read_csv(input_path)
    # итерирование по строкам исходных данных
    for calc_idx in range(11):
        row = params_df.iloc[0]
        # расчёт с адаптивным конфигурированием
        try:
            results_config_dict = baseline_model(row)
        except TimeoutError:
            results_config_dict = {
                'TEM_type': row['TEM_type'], 'Tchm0': row['Tchm0'], 'Tccm0': row['Tccm0'], 'N0': row['N0'], 'I0': row['I0'],
                'eta0': row['eta0'], 'aTEM': row['aTEM'], 'aTE': row['aTE'], 'Ncoup': row['Ncoup'], 'hTEM': row['hTEM'], 'mTEM': row['mTEM'],
                'prop': row['prop'], 'fin_type': row['fin_type'], 'hhm': row['hhm'], 'deltahm': row['deltahm'],
                'shaghm': row['shaghm'], 'dekvhm': row['dekvhm'], 'ledhm': row['ledhm'], 'lbdNTEG': row['lbdNTEG'], 'roNTEG': row['roNTEG'],
                'lbdOTEG': row['lbdOTEG'], 'roOTEG': row['roOTEG'], 'Lpolez': row['Lpolez'], 'nTEMrowmax': row['nTEMrowmax'],
                'rowmax': row['rowmax'], 'wbefdif': row['wbefdif'], 'Thm0': row['Thm0'], 'Thmpr': row['Thmpr'], 'wcment': row['wcment'],
                'Tcm0': row['Tcm0'], 'Tcmpr': row['Tcmpr'], 'rtchmmax': row['rtchmmax'], 'rtcwmax': row['rtcwmax'], 'd': row['d'],
                'Ne': row['Ne'], 'alphaGD': row['alphaGD'], 'gDT': row['gDT'],
                'message': "TimeoutError", 'mTEMisp': None, 'Tcm': None, 'Thm': None, 'Pelem_arr': None,
                'Qhm_arr': None, 'Rhm_arr': None, 'Rcm_arr': None, 'Tchm_arr': None, 'Tccm_arr': None,
                'widthhm': None, 'BTEG': None, 'widthcm': None, 'LTEG': None, 'heightsum': None,
                'mTEG': None, 'mTEG_empty': None, 'nNTEG': None, 'cmflownum': None, 'cmcannummax': None,
                'cmcannummin': None, 'cmgrmax': None, 'TEMlayq2': None, 'rownumtot1': None, 'nTEMrowhm': None,
                'UA': None, 'NTU': None, 'eps': None, 'Rhm': None, 'Rcm': None,
                'kT': None, 'Qhm': None, 'qhmplot': None, 'Tchm': None, 'Tccm': None,
                'deltaTc': None, 'eta': None, 'Pelem': None, 'PTEG': None, 'Nrtccm': None,
                'Pus': None, 'Arthm_HE': None, 'Arthm': None, 'massflow_hm_HE': None, 'massflow_hm': None,
                'rtchmap': None, 'rtchm': None, 'whm': None, 'ThmTEGout': None, 'temkGhm': None,
                'alphateplfhm': None, 'Artcm_HE': None, 'Artcm': None, 'massflow_cm_HE': None, 'massflow_cm': None,
                'rtccmap': None, 'rtccm': None, 'wcm': None, 'TcmTEGout': None, 'temkGcm': None,
                'alphateplfcm': None
            }
        row['Lpolez'] = 1
        # расчёт без адаптивного конфигурирования
        try:
            results_dict = baseline_model(row)
        except TimeoutError:
            results_dict = {
                'TEM_type': row['TEM_type'], 'Tchm0': row['Tchm0'], 'Tccm0': row['Tccm0'], 'N0': row['N0'], 'I0': row['I0'],
                'eta0': row['eta0'], 'aTEM': row['aTEM'], 'aTE': row['aTE'], 'Ncoup': row['Ncoup'], 'hTEM': row['hTEM'], 'mTEM': row['mTEM'],
                'prop': row['prop'], 'fin_type': row['fin_type'], 'hhm': row['hhm'], 'deltahm': row['deltahm'],
                'shaghm': row['shaghm'], 'dekvhm': row['dekvhm'], 'ledhm': row['ledhm'], 'lbdNTEG': row['lbdNTEG'], 'roNTEG': row['roNTEG'],
                'lbdOTEG': row['lbdOTEG'], 'roOTEG': row['roOTEG'], 'Lpolez': row['Lpolez'], 'nTEMrowmax': row['nTEMrowmax'],
                'rowmax': row['rowmax'], 'wbefdif': row['wbefdif'], 'Thm0': row['Thm0'], 'Thmpr': row['Thmpr'], 'wcment': row['wcment'],
                'Tcm0': row['Tcm0'], 'Tcmpr': row['Tcmpr'], 'rtchmmax': row['rtchmmax'], 'rtcwmax': row['rtcwmax'], 'd': row['d'],
                'Ne': row['Ne'], 'alphaGD': row['alphaGD'], 'gDT': row['gDT'],
                'message': "TimeoutError", 'mTEMisp': None, 'Tcm': None, 'Thm': None, 'Pelem_arr': None,
                'Qhm_arr': None, 'Rhm_arr': None, 'Rcm_arr': None, 'Tchm_arr': None, 'Tccm_arr': None,
                'widthhm': None, 'BTEG': None, 'widthcm': None, 'LTEG': None, 'heightsum': None,
                'mTEG': None, 'mTEG_empty': None, 'nNTEG': None, 'cmflownum': None, 'cmcannummax': None,
                'cmcannummin': None, 'cmgrmax': None, 'TEMlayq2': None, 'rownumtot1': None, 'nTEMrowhm': None,
                'UA': None, 'NTU': None, 'eps': None, 'Rhm': None, 'Rcm': None,
                'kT': None, 'Qhm': None, 'qhmplot': None, 'Tchm': None, 'Tccm': None,
                'deltaTc': None, 'eta': None, 'Pelem': None, 'PTEG': None, 'Nrtccm': None,
                'Pus': None, 'Arthm_HE': None, 'Arthm': None, 'massflow_hm_HE': None, 'massflow_hm': None,
                'rtchmap': None, 'rtchm': None, 'whm': None, 'ThmTEGout': None, 'temkGhm': None,
                'alphateplfhm': None, 'Artcm_HE': None, 'Artcm': None, 'massflow_cm_HE': None, 'massflow_cm': None,
                'rtccmap': None, 'rtccm': None, 'wcm': None, 'TcmTEGout': None, 'temkGcm': None,
                'alphateplfcm': None
            }
        # сохранение результатов расчётов по одной строке
        results_lst.append(results_dict)
        results_config_lst.append(results_config_dict)
        _save_batch(results_lst, output_dir, output_prefix_0, pkl_num)
        _save_batch(results_config_lst, output_dir, output_prefix_1, pkl_num)
        results_lst = []
        results_config_lst = []
        pkl_num += 1
        # удаление отработанной строки из исходных данных
        if params_df.shape[0] > 1:
            params_df = params_df.iloc[1:].reset_index(drop=True)


if __name__ == "__main__":
    bootstrap_calculation()
