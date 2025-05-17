penguin_305_details = {'species': 'Adlie', 'flipper_length': 190.0,
                       'body_mass': 3050.0, 'tracked': True, 'sex': 'FEMALE'}

if penguin_305_details['sex']:
    sex_is_true = penguin_305_details["sex"] is True
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

if penguin_305_details['tracked']:
    tracked_is_true = penguin_305_details["tracked"] is True
    print(f"{penguin_305_details['tracked']}: {tracked_is_true}")
