from iot_storytelling_backend import config


def create_reaction(qr_code, position):
    result = {}
    for device in range(0, config.NUMBER_ACTUATORS):
        result[str(device)] = device_reaction(device, qr_code, position)

    result['Sensor'] = device_reaction(-1, qr_code, position)
    return result


def device_reaction(device, qr_code, position):
    """
    :param device: [-1, config.NUMBER_ACTUATORS]
    :param qr_code: [not defined]
    :param position: [1, 4]
    :return: reaction event for :param device
    """
    
    audio_nr = 0
    image_nr = 0
    text_nr = 0

    result = {
        "audio": config.audio_files[audio_nr],
        "image": config.image_files[image_nr],
        "text": config.text_files[text_nr]
    }
    return result
