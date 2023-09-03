import os

parent = iface.mainWindow()

def input_layer_name():
    vlayer_names = [
        layer.name()
        for layer in QgsProject.instance().mapLayers().values()
        if layer.type() == QgsVectorLayer.VectorLayer
    ]

    vlayer_name, ok = QInputDialog.getItem(
        parent, "走行経路のレイヤ選択", "レイヤ名", vlayer_names, editable=False
    )

    if not ok:
        QMessageBox.warning(parent, "Warning", "レイヤ名が未選択です。")
        raise ValueError("No layer name selected.")

    return vlayer_name


def input_layout_name():
    layout_names = [
            layout.name() 
            for layout in QgsProject.instance().layoutManager().printLayouts()
    ]

    layout_name, ok = QInputDialog.getItem(
        parent, "印刷レイアウト選択", "レイアウト名", layout_names, editable=False
    )

    if not ok:
        QMessageBox.warning(parent, "Warning", "レイアウト名が未選択です。")
        raise ValueError("No layout name selected.")

    return layout_name


def input_output_folder():
    output_folder = QFileDialog.getExistingDirectory(
        parent, "出力先フォルダ選択", QgsProject.instance().homePath()
    )

    if not output_folder:
        QMessageBox.warning(parent, "Warning", "出力先フォルダが未選択です。")
        raise ValueError("No folder selected.")

    return output_folder


# レイヤ名・レイアウト名・出力フォルダをダイアログボックスで入力
vlayer_name = input_layer_name()
layout_name = input_layout_name()
output_folder = input_output_folder()

# レイヤ名からレイヤを取得
vlayer = QgsProject.instance().mapLayersByName(vlayer_name)[0]

# レイヤを表示
root = QgsProject.instance().layerTreeRoot()
node_vlayer = root.findLayer(vlayer.id())
node_vlayer.setItemVisibilityChecked(True)

# 印刷前に、レイヤのカテゴリ値のアイテムはすべて非表示にしておく
renderer = vlayer.renderer()
categories = renderer.categories()

for i, cat in enumerate(categories):
    renderer.updateCategoryRenderState(i, False)

vlayer.setRenderer(renderer)
vlayer.triggerRepaint()

# レイアウトを取得して印刷設定をする
layout = QgsProject.instance().layoutManager().layoutByName(layout_name)
exporter = QgsLayoutExporter(layout)
settings = exporter.ImageExportSettings()
settings.dpi = 100

# レイヤのアイテムを一つずつ表示してレイアウト印刷を実行
for i, cat in enumerate(categories):
    renderer.updateCategoryRenderState(i, True)
    vlayer.setRenderer(renderer)
    vlayer.triggerRepaint()

    img_path = os.path.join(output_folder, f"{cat.value()}.png")
    exporter.exportToImage(img_path, settings)

    print("Export image...", img_path)

    renderer.updateCategoryRenderState(i, False)
    vlayer.setRenderer(renderer)
    vlayer.triggerRepaint()

# レイヤのカテゴリ値のアイテムをすべて表示する
for i, cat in enumerate(categories):
    renderer.updateCategoryRenderState(i, True)

vlayer.setRenderer(renderer)
vlayer.triggerRepaint()

QMessageBox.information(parent, "Information", "レイアウト印刷が完了しました。")
