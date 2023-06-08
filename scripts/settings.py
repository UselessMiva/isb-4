import json
import logging

logger = logging.getLogger()
logger.setLevel('INFO')

SETTINGS = {
  'hash': "0438cbc33cb25114ed4ae1cf863527401db733c2d55a01563a84f2955ad5233a129a0220fec715208fee40c9710343d402e22f97f1f8b3dc312f7a20e6585ad2",
  'bin': ["427409", "427695", "424542", "424543", "424544", "442197", "4421942", "442195", "442196", "479578", "480110", "480111", "480112", "480113", "480114", "481776", "481777", "481779", "483983", "427400", "427402", "427403", "427404", "427406", "427407", "427408", "427411", "427412", "427413"],
  'last_four_numbers': "0877",
  'card_number': "files/card_number.txt",
  'csv_statistics': "files/statistics.csv",
  'png_statistics': "files/statistics.png",
  'luhn_result': "files/luhn_result.txt"
}

def read_settings(file_with_settings: str = 'files/settings.json') -> dict:
    """
    Фукнция считывает настройки из файла
    :param file_with_settings: Путь к файлу с настройками
    :return: Настройки
    """
    settings = None
    try:
        with open(file_with_settings, 'r') as f:
            settings = json.load(f)
        logging.info("Настройки успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать настройки")
    return settings


if __name__ == "__main__":
    with open('files/settings.json', 'w') as f:
        json.dump(SETTINGS, f)