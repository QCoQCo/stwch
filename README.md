# Stopwatch & To-Do List

> 아래에서 언어를 선택해 펼쳐 보세요.  
> 下で言語を選んで展開してください。

---

<details open>
<summary><strong>🇰🇷 한국어</strong></summary>

tkinter 기반의 **스톱워치**와 **To-Do 리스트**를 한 화면에서 사용할 수 있는 데스크톱 앱입니다.

## 기능

### 스톱워치
- **Start** — 타이머 시작
- **Stop** — 타이머 일시 정지
- **Reset** — 시간을 00:00:00으로 초기화
- 실시간 시계 표시 (현재 시각)
- 50ms 간격으로 화면 갱신

### To-Do 리스트
- 메인 창의 **ToDo_list** 버튼으로 별도 창에서 열기
- 작업 추가 (Add Task)
- 완료한 작업에 체크 후 **Delete** 버튼으로 삭제
- 작업 목록을 체크박스로 완료 표시

## 실행 방법

### 요구 사항
- Python 3.x
- 표준 라이브러리만 사용 (tkinter, datetime) — 별도 패키지 설치 불필요

### 실행
```bash
python idea.py
```

To-Do 리스트만 단독 실행:
```bash
python ToDo_list.py
```

## 프로젝트 구조

```
stopwatch/
├── idea.py       # 메인 앱 (스톱워치 + To-Do 열기)
├── ToDo_list.py  # To-Do 리스트 모듈
├── icon.ico      # 앱 아이콘
├── idea.spec     # PyInstaller 빌드 설정
└── README.md
```

## 실행 파일 빌드 (macOS)

PyInstaller로 단일 실행 파일 또는 macOS 앱 번들로 빌드할 수 있습니다.

```bash
pip install pyinstaller
pyinstaller idea.spec
```

빌드 결과는 `dist/idea.app` (macOS 앱) 또는 `dist/idea` (실행 파일)에 생성됩니다.

## 기술 스택

- **GUI**: tkinter
- **시간 처리**: `datetime`, `timedelta`
- **빌드**: PyInstaller (선택)

## 화면 구성

- 메인 창: 1200×720, 검정 배경
- 스톱워치 표시: 노란 배경, 큰 폰트
- To-Do 창: 600×300, 검정 배경

</details>

---

<details>
<summary><strong>🇯🇵 日本語</strong></summary>

tkinter ベースの **ストップウォッチ** と **To-Do リスト** を一つの画面で使えるデスクトップアプリです。

## 機能

### ストップウォッチ
- **Start** — タイマー開始
- **Stop** — 一時停止
- **Reset** — 00:00:00 にリセット
- リアルタイム時計表示（現在時刻）
- 50ms 間隔で画面更新

### To-Do リスト
- メイン画面の **ToDo_list** ボタンで別ウィンドウで開く
- タスク追加（Add Task）
- 完了したタスクにチェック後 **Delete** ボタンで削除
- チェックボックスで完了表示

## 実行方法

### 必要環境
- Python 3.x
- 標準ライブラリのみ（tkinter, datetime）— 追加インストール不要

### 実行
```bash
python idea.py
```

To-Do リストのみ単体実行:
```bash
python ToDo_list.py
```

## プロジェクト構成

```
stopwatch/
├── idea.py       # メインアプリ（ストップウォッチ + To-Do 起動）
├── ToDo_list.py  # To-Do リストモジュール
├── icon.ico      # アプリアイコン
├── idea.spec     # PyInstaller ビルド設定
└── README.md
```

## 実行ファイルのビルド (macOS)

PyInstaller で単体実行ファイルまたは macOS アプリバンドルをビルドできます。

```bash
pip install pyinstaller
pyinstaller idea.spec
```

ビルド結果は `dist/idea.app`（macOS アプリ）または `dist/idea`（実行ファイル）に出力されます。

## 技術スタック

- **GUI**: tkinter
- **時間処理**: `datetime`, `timedelta`
- **ビルド**: PyInstaller（任意）

## 画面構成

- メインウィンドウ: 1200×720、黒背景
- ストップウォッチ表示: 黄背景、大フォント
- To-Do ウィンドウ: 600×300、黒背景

</details>
