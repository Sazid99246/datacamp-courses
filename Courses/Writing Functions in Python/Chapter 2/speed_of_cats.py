image = get_image_from_instagram()

with timer():
    print('Numpy version')
    process_with_numpy(image)

with timer():
    print('Pytorch version')
    process_with_pytorch(image)
