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

git clone in any dirctory

```bash
git clone https://github.com/keymar0725/DefrostTest.git
```


```bash
cd DefrostTest
python main.py (argv0) (argv1) (argv2)
```

or

```bash
python ./(cloned dir)/DefrostTest/main.py argv0 argv1 argv2
```

* argv0: csv file path
* argv1: Channel number
* argv2: Plot pitch (1min = 60, 1hour = 3600)


# Example

```bash
python plot_csv.py import/example_01.CSV 9 3600
```

# Author

* Takahashi KEISUKE
* FTE
* takahashikeisuke2525@gmail.com
