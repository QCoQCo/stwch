# Stopwatch & To-Do List

> 아래에서 언어를 선택해 펼쳐 보세요.  
> 下で言語を選んで展開してください。

---

<details open>
<summary><strong>🇰🇷 한국어</strong></summary>

tkinter 기반의 **스톱워치** 데스크톱 앱입니다. 버튼 하나로 **To-Do 리스트** 창을 함께 띄워 쓸 수 있습니다.

## 기능

### 스톱워치

- **Start** — 타이머 시작
- **Stop** — 타이머 일시 정지
- **Reset** — 시간을 00:00:00으로 초기화
- 실시간 시계 표시 (현재 시각)
- 단축키: `Space` 시작/정지, `R` 리셋
- 시스템 시각이 바뀌어도(서머타임, 시계 동기화) 경과 시간이 정확하게 유지됨

### To-Do 리스트

- 메인 창의 **ToDo_list** 버튼으로 별도 창에서 열기 (이미 열려 있으면 해당 창을 앞으로 가져옴)
- 작업 추가: **Add Task** 버튼 또는 `Enter`
- 체크박스로 완료 표시 (취소선), 완료한 작업은 **Delete** 버튼으로 삭제
- 작업이 많으면 스크롤 가능 (마우스 휠/트랙패드)
- 작업 목록은 `~/.stopwatch_todo.json`에 자동 저장되어 다시 열어도 유지됨

## 실행 방법

### 요구 사항

- Python 3.x
- 표준 라이브러리만 사용 (tkinter, datetime, json) — 별도 패키지 설치 불필요

### 실행

```bash
python main.py
```

To-Do 리스트만 단독 실행:

```bash
python todo_list.py
```

## 프로젝트 구조

```
stwch/
├── main.py       # 메인 앱 (스톱워치 + To-Do 열기)
├── todo_list.py  # To-Do 리스트 모듈
├── icon.ico      # 앱 아이콘
├── idea.spec     # PyInstaller 빌드 설정
└── README.md
```

## 실행 파일 빌드 (macOS)

PyInstaller로 macOS 앱 번들을 빌드할 수 있습니다.

```bash
pip install pyinstaller
pyinstaller idea.spec
```

빌드 결과는 `dist/idea.app` (macOS 앱)에 생성됩니다. `dist/idea/` 폴더에는 실행 파일과 의존 파일이 함께 들어 있습니다.

> `.ico` 아이콘을 macOS용으로 변환하려면 Pillow가 필요합니다 (`pip install pillow`).

## 기술 스택

- **GUI**: tkinter
- **시간 처리**: `time.monotonic` (경과 시간), `datetime` (현재 시각)
- **저장**: `json`
- **빌드**: PyInstaller (선택)

## 화면 구성

- 메인 창: 1200×720, 검정 배경
- 스톱워치 표시: 노란 배경, 큰 폰트
- To-Do 창: 600×300 (크기 조절 가능), 검정 배경

</details>

---

<details>
<summary><strong>🇯🇵 日本語</strong></summary>

tkinter ベースの **ストップウォッチ** デスクトップアプリです。ボタン一つで **To-Do リスト** ウィンドウも開けます。

## 機能

### ストップウォッチ

- **Start** — タイマー開始
- **Stop** — 一時停止
- **Reset** — 00:00:00 にリセット
- リアルタイム時計表示（現在時刻）
- ショートカット: `Space` 開始/停止、`R` リセット
- システム時刻が変わっても（サマータイム、時刻同期）経過時間は正確に保持

### To-Do リスト

- メイン画面の **ToDo_list** ボタンで別ウィンドウで開く（既に開いている場合はそのウィンドウを前面に表示）
- タスク追加: **Add Task** ボタンまたは `Enter`
- チェックボックスで完了表示（取り消し線）、完了したタスクは **Delete** ボタンで削除
- タスクが多い場合はスクロール可能（マウスホイール/トラックパッド）
- タスク一覧は `~/.stopwatch_todo.json` に自動保存され、再度開いても保持

## 実行方法

### 必要環境

- Python 3.x
- 標準ライブラリのみ（tkinter, datetime, json）— 追加インストール不要

### 実行

```bash
python main.py
```

To-Do リストのみ単体実行:

```bash
python todo_list.py
```

## プロジェクト構成

```
stwch/
├── main.py       # メインアプリ（ストップウォッチ + To-Do 起動）
├── todo_list.py  # To-Do リストモジュール
├── icon.ico      # アプリアイコン
├── idea.spec     # PyInstaller ビルド設定
└── README.md
```

## 実行ファイルのビルド (macOS)

PyInstaller で macOS アプリバンドルをビルドできます。

```bash
pip install pyinstaller
pyinstaller idea.spec
```

ビルド結果は `dist/idea.app`（macOS アプリ）に出力されます。`dist/idea/` フォルダには実行ファイルと依存ファイルが入っています。

> `.ico` アイコンを macOS 用に変換するには Pillow が必要です（`pip install pillow`）。

## 技術スタック

- **GUI**: tkinter
- **時間処理**: `time.monotonic`（経過時間）、`datetime`（現在時刻）
- **保存**: `json`
- **ビルド**: PyInstaller（任意）

## 画面構成

- メインウィンドウ: 1200×720、黒背景
- ストップウォッチ表示: 黄背景、大フォント
- To-Do ウィンドウ: 600×300（サイズ変更可）、黒背景

</details>
