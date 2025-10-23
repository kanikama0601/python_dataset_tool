import os
import shutil
from pathlib import Path

def collect_and_rename_images(source_folder, output_folder):
    """
    指定されたフォルダ内の全サブフォルダから画像を収集し、
    連番でリネームして出力フォルダに保存する
    
    Args:
        source_folder: 検索元のフォルダパス
        output_folder: 出力先のフォルダパス
    """
    # 対応する画像拡張子
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.JPG', '.JPEG', '.PNG'}
    
    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_folder, exist_ok=True)
    
    # 画像ファイルのリストを収集
    image_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if Path(file).suffix in image_extensions:
                full_path = os.path.join(root, file)
                image_files.append(full_path)
    
    # 画像を連番でコピー
    print(f"見つかった画像: {len(image_files)}枚")
    
    for index, image_path in enumerate(image_files, start=1):
        # 元の拡張子を取得
        original_extension = Path(image_path).suffix
        
        # 新しいファイル名を作成
        new_filename = f"{index}{original_extension}"
        new_filepath = os.path.join(output_folder, new_filename)
        
        # ファイルをコピー
        shutil.copy2(image_path, new_filepath)
        print(f"コピー完了: {image_path} -> {new_filename}")
    
    print(f"\n完了！ {len(image_files)}枚の画像を {output_folder} に保存しました。")

# 使用例
if __name__ == "__main__":
    # 設定: これらのパスを実際のパスに変更してください
    source_folder = "source"  # 元のフォルダ（folder1, folder2などを含む）
    output_folder = "extract"  # 出力先フォルダ
    
    collect_and_rename_images(source_folder, output_folder)