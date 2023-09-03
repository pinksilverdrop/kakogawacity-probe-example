# kakogawacity-probe-example

## 概要
- G空間情報センターの加古川市公用車走行データを、Python・SQL・QGIS で加工・可視化し、レポーティングすることを想定したコードです。

## サンプルプログラム（コード）
### kakogawa-probe-example.ipynb
- GeoPandas + MovingPandas によるプローブデータ処理
- DuckDB によるデータ抽出
- Kepler.gl for Jupyer によるアニメーション作成
    - 出力結果：probe_animation_20170213.html
- python-pptx によるレポーティング自動化（QGIS で作成した主題図を PowerPoint のスライドに一括出力）
    - 出力結果：probe_pptx_20170213.pptx
- ノートブックをエクスポートした HTML ファイル
  - kakogawacity-probe-example.html
- 補足：今回は短い処理なのでノートブックにすべてのコードを記載いたしましたが、実際の業務ではコード量が多くなって煩雑になるので、Python のスクリプトを別のファイルに保存して、JupyterLab で読み込んで実行することが多いです。

### export_qgis_layout.py
- QGIS で作成したレイアウトを連続印刷するスクリプト
  - QGIS のプロジェクトファイル：kakogawacity-probe-example.qgz
  - `Pythonコンソール` > `エディタの表示` > スクリプトを開いて `スクリプト実行`（緑の矢印）をクリックして実行
- 補足：必要に応じて書き換えて使うことを前提としたスクリプトなので、しっかりとしたエラー処理は実装しておりません。

## データ
- 加古川市公用車走行データ（走行履歴）（2017年） を加工して作成 
    - [G空間情報センター 加古川市_公用車走行データ](https://www.geospatial.jp/ckan/dataset/kakogawacity-car-data)、加古川市、[クリエイティブ・コモンズ・ライセンス表示2.1日本](http://creativecommons.org/licenses/by/2.1/jp/)

- 主題図サンプルの作成には、上記のほかに以下のデータを加工して使用
    - [ESRI 全国市区町村界データ](https://www.esrij.com/products/japan-shp/)
    - [国土数値情報 市町村役場等及び公的集会施設データ（令和4年）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P05-v3_0.html)
    - [国土数値情報 消防署データ（平成24年）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P17.html)
    - [国土数値情報 廃棄物処理施設データ（平成24年）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-P15.html)

## 参考URL
- プローブデータのアニメーション化はこちらのサイト（https://sasan.jafarnejad.io/post/kepler-gl-trip-visualization-python/) を参考にしました。