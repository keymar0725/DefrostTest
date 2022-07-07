# DefrostTest
解凍テストcsvデータによるグラフ自動生成プログラム


計測ソフトより生成したCSVファイルを読み込み、1時間ごとの温度を新しいリストに追加し、それをプロットする

その際、

# Requirement

* python3.10.5
* Pandas

# Installation

```bash
pip install pandas
```

# Usage

任意のディレクトリでclone

```bash
git clone https://github.com/keymar0725/DefrostTest.git
```


```bash
cd DefrostTest
python plot_csv.py argv0 argv1 argv2
```

* argv0: csvファイルのパス
* argv1: チャンネル（センサ）数
* argv2: プロットピッチ (1min = 60, 1hour = 3600)


# Example

```bash
~\\home\\DefrostTest > python plot_csv.py import/解凍テスト久原本家食品(段ボール有り).CSV 9 3600
```

# Author

* Takahashi KEISUKE
* FTE
* takahashikeisuke2525@gmail.com
