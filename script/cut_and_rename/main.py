import os

data_name = "monkey"
data_dir = "./chinese_vs_monkey/"+data_name
target_count = 200
bike_img_filepath = []

if not os.path.isdir(data_dir):
    print(f"エラー: ディレクトリ '{data_dir}' が見つかりません。実行を中止します。")
else:
    try:
        filename_list = sorted(os.listdir(data_dir))
    except Exception as e:
        print(f"ファイルリストの取得中にエラーが発生しました: {e}")
        filename_list = []
    files_to_keep = []
    index = 0
    while len(files_to_keep) < target_count and index < len(filename_list):
        original_file = filename_list[index]
        if original_file != ".DS_Store" and original_file.lower().endswith('.jpg'):
            files_to_keep.append(original_file)
            
        index += 1
        
    print(f"✅ 保持対象のJPGファイル {len(files_to_keep)} 件を特定しました。")
    file_counter = 0 
    for file_name in filename_list:
        original_path = os.path.join(data_dir, file_name)
        
        if file_name in files_to_keep:
            new_file_name = f"{data_name}_{file_counter:03d}.jpg"
            new_path = os.path.join(data_dir, new_file_name)        
            try:
                os.rename(original_path, new_path)
                bike_img_filepath.append(new_file_name)
                print(f"🔄 リネーム: {file_name} -> {new_file_name}")
                file_counter += 1
            except OSError as e:
                print(f"⚠️ リネームエラー ({file_name}): {e}")
                
        else:
            if os.path.isfile(original_path):
                try:
                    os.remove(original_path)
                    print(f"🗑️ 削除: {file_name} (非JPGまたは対象外)")
                except OSError as e:
                    print(f"⚠️ 削除エラー ({file_name}): {e}")

    print("\n--- 処理完了 ---")
    print(f"最終的に残ったファイル数: {len(bike_img_filepath)}")