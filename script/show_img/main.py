import os
import cv2
import matplotlib.pyplot as plt

# bike
bike_img_filepath = []
data_dir = "./carvsbike/Bikes"
filename_list = sorted(os.listdir(data_dir))
index = 0
while len(bike_img_filepath) < 7 and index < len(filename_list):
    file = filename_list[index]
    if file != ".DS_Store":
        bike_img_filepath.append(file)
    index += 1 

# car
car_img_filepath = []
data_dir = "./carvsbike/Cars"
filename_list = sorted(os.listdir(data_dir))
index = 0
while len(car_img_filepath) < 7 and index < len(filename_list):
    file = filename_list[index]
    if file != ".DS_Store":
        car_img_filepath.append(file)
    index += 1
    
def plot_images_3x2(filepaths, title_prefix="Images"):
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle(title_prefix, fontsize=16)

    axes = axes.flatten()
    
    for i, ax in enumerate(axes):
        if i < len(filepaths):
            full_path = filepaths[i]
            file_name = os.path.basename(full_path)

            try:
                img = cv2.imread(full_path)
                ax.imshow(img)
                height, width = img.shape[:2] 
                image_size_str = f"{width} x {height}"

                ax.set_title(f"{file_name}\n({image_size_str} pixels)", fontsize=10)
            
            except Exception as e:
                ax.text(0.5, 0.5, f"画像読込エラー:\n{file_name}", ha='center', va='center', fontsize=10)
                ax.set_title(f"{file_name}\n(サイズ情報なし)", fontsize=10)
                print(f"画像読込中にエラーが発生しました ({file_name}): {e}")

            ax.axis('off')
        else:
            ax.axis('off')
    plt.tight_layout(rect=[0, 0.03, 1, 0.98])
    plt.show()
    
# 表示
if bike_img_filepath:
    plot_images_3x2(bike_img_filepath, title_prefix="Bike Images (3x2)")
if car_img_filepath:
    plot_images_3x2(car_img_filepath, title_prefix="Car Images (3x2)")