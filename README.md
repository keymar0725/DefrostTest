# DefrostTest
解凍テストcsvデータによるグラフ自動生成プログラム


計測ソフトより生成したCSVファイルを読み込み、1時間ごとの温度を新しいリストに追加し、それをプロットする

その際、

# Requirement

* python3.10.5
* Pandas
* Matplotlib

# Installation

```bash
pip install pandas
pip install matplotlib
```

# Usage

git clone in any dirctory

```bash
git clone https://github.com/keymar0725/DefrostTest.git
```


make image of graph.

```bash
cd DefrostTest
python3 main.py argv1 argv2 argv3 argv4
```

or

```bash
python3 ./(cloned dir)/DefrostTest/main.py argv1 argv2 argv3 argv4
```

* argv1: Path to csv file
* argv2: Channel number
* argv3: Plot pitch
    ex)1s = 1, 1min = 60, 1hour = 3600
* argv4: Enviroment channel

# Example

```bash
python plot_csv.py ./import/example_01.CSV 9 3600 1
```

![ダンボール有](https://user-images.githubusercontent.com/47661559/177715451-16ba89ac-fcd3-4529-a745-0fc2129ee838.jpg)

# Author

* Takahashi KEISUKE
* FTE
* takahashikeisuke2525@gmail.com
