import os
import zipfile

def compress_files(directory, file_types, output_directory):
  """指定されたディレクトリ内のファイルを探索し、それらをZIP形式で圧縮する。

  Args:
    directory: 圧縮するディレクトリ。
    file_types: 圧縮するファイルタイプ。
    output_directory: 圧縮されたファイルを保存するディレクトリ。

  Returns:
    圧縮されたファイルのパス。
  """

  # 指定されたディレクトリ内を探索し、ファイルのリストを作成する。
  files = []
  for root, dirs, filenames in os.walk(directory):
    for filename in filenames:
      if os.path.splitext(filename)[1] in file_types:
        files.append(os.path.join(root, filename))

  # 選択されたファイルをZIP形式で圧縮する。
  output_file = os.path.join(output_directory, os.path.basename(directory) + '.zip')
  with zipfile.ZipFile(output_file, 'w') as zip_file:
    for file in files:
      zip_file.write(file)

  return output_file

if __name__ == '__main__':
  # コマンドラインからディレクトリパス、対象となるファイルタイプ、出力ディレクトリパスを受け取る。
  directory = input('圧縮するディレクトリを入力してください: ')
  file_types = input('圧縮するファイルタイプを入力してください: ').split()
  output_directory = input('圧縮されたファイルを保存するディレクトリを入力してください: ')

  # ファイルを圧縮する。
  output_file = compress_files(directory, file_types, output_directory)

  # 圧縮されたファイルのパスを出力する。
  print('圧縮されたファイルは{}にあります。'.format(output_file))
