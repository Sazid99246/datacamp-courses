
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

# Check the truthiness of penguin_305_details tracked key
if penguin_305_details['tracked']:
    # If true, check if tracked is True and store it as tracked_is_true
    tracked_is_true = penguin_305_details["tracked"] == True
    # Print the tracked key and tracked_is_true
    print(f"{penguin_305_details['tracked']}: {tracked_is_true