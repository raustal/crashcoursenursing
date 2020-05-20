def normal_bmi_weights(height):
    low_norm = (((int(height) ** 2) * 18.5) / 703)
    hi_norm = (((int(height) ** 2) * 24.9) / 703)
    return 'The normal weight ranges are ' + str(round(low_norm, 1)) + ' lbs - ' + str(round(hi_norm, 1)) + ' lbs.'


