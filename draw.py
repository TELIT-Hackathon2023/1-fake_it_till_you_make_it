import cv2

num_cells_x = 20
num_cells_y = 20

def create_numbered_grid(image, num_cells_x, num_cells_y):
    grid_size_x = image.shape[1] // num_cells_x
    grid_size_y = image.shape[0] // num_cells_y

    for y in range(num_cells_y):
        for x in range(num_cells_x):
            top_left = (x * grid_size_x, y * grid_size_y)
            bottom_right = ((x + 1) * grid_size_x, (y + 1) * grid_size_y)

            cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), 1)

            cell_number = y * num_cells_x + x + 1
            cv2.putText(image, str(cell_number), (top_left[0] + 5, top_left[1] + grid_size_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return image


image_path = 'image1.png'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
else:
    numbered_image = create_numbered_grid(image, num_cells_x, num_cells_y)

    output_image_path = 'image2.png'
    cv2.imwrite(output_image_path, numbered_image)
    print(f"Image with numbered grid saved as {output_image_path}")


square_number = 148

y = (square_number - 1) // num_cells_x
x = (square_number - 1) % num_cells_x

print(f"Квадрат {square_number} має координати: x={x}, y={y}")