# Stopwatch & To-Do List

**[한국어](#korean) | [日本語](#japanese)**

---

<a id="korean"></a>

## 🇰🇷 한국어

### 📌 프로젝트 개요

Python(tkinter)으로 만든 데스크톱 스톱워치 앱입니다. 버튼 하나로 To-Do 리스트를 별도 창으로 띄워 함께 쓸 수 있습니다.

군 복무 중 온라인 코딩 문제를 풀며 Python을 독학하던 시기에 만들었습니다. 친구와 토익 공부를 하면서 문제 푸는 시간을 재야 했는데, 이미 공개된 스톱워치를 쓰는 대신 익히고 있던 Python으로 직접 만들어 보기로 했습니다. **독학한 언어로 처음 만든 데스크톱 앱**입니다.

| 항목 | 내용 |
|---|---|
| 개발 기간 | 2024년 6월 ~ 8월 최초 개발 / 2026년 2월 · 10월 리팩터링 |
| 개발 형태 | 개인 프로젝트 |
| 언어 · 라이브러리 | Python 3, tkinter (표준 라이브러리만 사용) |
| 빌드 | PyInstaller (macOS `.app`) |

### ✨ 주요 기능

**스톱워치**
- Start / Stop / Reset
- 현재 시각 표시
- 단축키: `Space` 시작/정지, `R` 리셋
- 시스템 시각이 바뀌어도 경과 시간이 정확하게 유지됨

**To-Do 리스트**
- 메인 창의 **ToDo_list** 버튼으로 별도 창에서 열기
- 작업 추가 (**Add Task** 버튼 또는 `Enter`)
- 체크박스로 완료 표시(취소선), 완료한 작업은 **Delete**로 삭제
- 작업이 많으면 스크롤 (마우스 휠 / 트랙패드)
- `~/.stopwatch_todo.json`에 자동 저장되어 다시 열어도 유지됨

### 🔄 버전 이력

- **2024년** — 스톱워치와 To-Do 리스트 최초 구현
- **2026년** — 코드 전면 정리. 경과 시간 계산 방식 개선, 단축키 추가, To-Do 저장 · 스크롤 기능 추가

### ▶️ 실행 방법

Python 3만 있으면 됩니다. 확인한 환경은 macOS 27 / Python 3.14 / Tk 9.1입니다.

```bash
python3 main.py
```

To-Do 리스트만 단독으로 실행:

```bash
python3 todo_list.py
```

**macOS 앱 빌드 (선택)**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyinstaller pillow
pyinstaller idea.spec
```

결과물은 `dist/idea.app`에 생성됩니다.

---

<a id="japanese"></a>

## 🇯🇵 日本語

### 📌 プロジェクト概要

Python（tkinter）で開発したデスクトップ向けストップウォッチアプリです。ボタン一つで To-Do リストを別ウィンドウで開き、併せて使うことができます。

兵役中、オンラインのコーディング問題を解きながら Python を独学していた時期に制作しました。友人と TOEIC の勉強をする中で問題を解く時間を計る必要があり、既存のストップウォッチを使うのではなく、学んでいた Python で自作してみることにしました。**独学で身につけた言語で初めて作ったデスクトップアプリ**です。

| 項目 | 内容 |
|---|---|
| 開発期間 | 2024年6月〜8月 初期開発 / 2026年2月・10月 リファクタリング |
| 開発体制 | 個人開発 |
| 言語・ライブラリ | Python 3、tkinter（標準ライブラリのみ使用） |
| ビルド | PyInstaller（macOS `.app`） |

### ✨ 主な機能

**ストップウォッチ**
- Start / Stop / Reset
- 現在時刻の表示
- ショートカットキー: `Space` で開始/停止、`R` でリセット
- システム時刻が変わっても経過時間を正確に保持

**To-Do リスト**
- メインウィンドウの **ToDo_list** ボタンで別ウィンドウとして表示
- タスクの追加（**Add Task** ボタンまたは `Enter`）
- チェックボックスで完了表示（取り消し線）、完了したタスクは **Delete** で削除
- タスクが多い場合はスクロール可能（マウスホイール / トラックパッド）
- `~/.stopwatch_todo.json` に自動保存され、開き直しても保持

### 🔄 バージョン履歴

- **2024年** — ストップウォッチと To-Do リストを初期実装
- **2026年** — コードを全面的に整理。経過時間の計算方式を改善し、ショートカットキー、To-Do の保存・スクロール機能を追加

### ▶️ 実行方法

Python 3 があれば動作します。動作確認環境は macOS 27 / Python 3.14 / Tk 9.1 です。

```bash
python3 main.py
```

To-Do リストのみを単体で起動する場合:

```bash
python3 todo_list.py
```

**macOS アプリのビルド（任意）**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pyinstaller pillow
pyinstaller idea.spec
```

成果物は `dist/idea.app` に出力されます。
