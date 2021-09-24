# 経済学のためのDocker活用

このリポジトリは経済学の実証研究のためのDocker活用を紹介する。Dockerでは、自分の分析環境を汚さないで、安全で円滑に複雑なデータ処理やデータ分析のパイプラインを実行することができる。

経済学でよく使われる複雑なデータの種類は地理情報（ラスターデータ、GeoTIFFデータなど）である。
このリポジトリは人工衛星が収集した夜光データを地理的なタイルに集計し、分析可能か形にする、といったパイプラインを用いて、経済学の実証研究におけるDockerの活用のベネフィットを紹介する。

このコードはR Studioや地理情報分析のためのよく使われるRパッケージを含めるDockerイメージ（[rocker/geospatial](https://hub.docker.com/r/rocker/geospatial "rocker/geospatialについて")）を用いて下記の処理を行う：

1. 世界銀行の[Light Every Night](https://registry.opendata.aws/wb-light-every-night/ "Light Every Nightデータについて")データセットの一部をダウンロードする。
2. Uberの[H3 Index](https://eng.uber.com/h3/ "H3 Indexについて")のタイル単位に集計する。
3. R Studio上で処理したデータを分析可能にする。

Dockerの紹介のためだから夜光データの適切な処理だと限らない。
研究のための利用に関してはデータセットの[詳細情報](https://worldbank.github.io/OpenNightLights/wb-light-every-night-readme.html "夜光データの使い方に関して")をご参照ください。

# 利用方法

リポジトリをcloneし、そのメインフォルダーから下記のコマンドを実行することでDockerイメージをビルドする：
```bash
docker build --tag my-first-image .
```
これで `my-first-image`というイメージがビルドされた。

コンテーナーを立ち上げるには以下のコマンドを実行する：
```bash
docker run --rm -e DISABLE_AUTH=true -p 8787:8787 my-first-image
```

ブラウザーのタブを開き、アドレスバーに `localhost:8787`　を入力し、Enterキーを押す。
RStudioの画面が開く。右下にあるファイルブラウザーに表示される `data_analysis.R`というファイルを開き、全てのコマンドを実行する。右下に南関東の平均夜光の分布が表示される。
