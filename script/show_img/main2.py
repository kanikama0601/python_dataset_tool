import os
import matplotlib.pyplot as plt
from PIL import Image # PILをインポート

# bike
bike_img_filepath = []
bike_data_dir = "./carvsbike/Bikes"
try:
    filename_list = sorted(os.listdir(bike_data_dir))
except FileNotFoundError:
    print(f"エラー: ディレクトリが見つかりません: {bike_data_dir}")
    filename_list = []

index = 0
while len(bike_img_filepath) < 6 and index < len(filename_list):
    file = filename_list[index]
    if file != ".DS_Store":
        full_path = os.path.join(bike_data_dir, file)
        bike_img_filepath.append(full_path)
    index += 1 

# car
car_img_filepath = []
car_data_dir = "./carvsbike/Cars"
try:
    filename_list = sorted(os.listdir(car_data_dir))
except FileNotFoundError:
    print(f"エラー: ディレクトリが見つかりません: {car_data_dir}")
    filename_list = []

index = 0
while len(car_img_filepath) < 6 and index < len(filename_list):
    file = filename_list[index]
    if file != ".DS_Store":
        full_path = os.path.join(car_data_dir, file)
        car_img_filepath.append(full_path)
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
                # PIL (Pillow) を使って画像を読み込む
                img = Image.open(full_path)
                
                # matplotlibで表示するためにnumpy配列に変換
                img_array = plt.imread(full_path) 
                
                ax.imshow(img_array)
                
                # PILのImageオブジェクトからサイズを取得
                width, height = img.size 
                image_size_str = f"{width} x {height}"

                ax.set_title(f"{file_name}\n({image_size_str} pixels)", fontsize=10)
            
            except Exception as e:
                ax.text(0.5, 0.5, f"画像読込エラー:\n{file_name}", ha='center', va='center', fontsize=10)
                ax.set_title(f"{file_name}\n(サイズ情報なし)", fontsize=10)
                # エラーメッセージを出力して原因究明に役立てる
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