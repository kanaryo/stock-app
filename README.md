## AWS個人学習プロジェクト(2026年1月より開始、随時更新）

### 概要
- AWS学習を目的に、株価可視化Webアプリをフルスタックで構築。
- Docker + CI/CD + AWS による本番運用までを一貫して実装。

### 目的
- AWSサービスを理解し、インフラ環境を自分で設計・構築できるスキルを習得する。
- DevOps文化やツールの理解を深め、CI/CDパイプラインを設計・実装し、開発・運用の効率化を図る。

### アプリURL
- https://kanai-stock-app.com/

### システム構成
- User → Route53 → ALB → EC2(Docker) → Streamlit
- GitHub Actions → ECR → EC2 自動デプロイ

### AWSインフラ構成
<img width="1301" height="561" alt="AWSインフラ構成図_01 drawio" src="https://github.com/user-attachments/assets/045d64d9-f8d4-43ab-8713-d53c2efba9f2" />

### 技術スタック
- Python / Streamlit / yfinance
- Docker / docker-compose
- AWS (EC2, ECR, ALB, Route53, ACM)
- GitHub Actions (CI/CD)

### 要件定義
以下を構築する
- アプリケーション要件
  - [x] Streamlit（Python）
  - [X] 外部APIで株価取得
  - [x] グラフ描画
  - [ ] RDB連携

- 実行環境
  - [x] ローカル：Docker Desktop
  - [x] 本番：EC2 + Docker
  - [x] コンテナイメージ管理：Amazon ECR

- CI/CD
  - [x] GitHub Actions によるCI/CD構築
  - [x] main ブランチへの push をトリガーに自動実行
  - [x] pytest による自動テスト
  - [x] Docker イメージのビルドおよび ECR への push
  - [x] EC2 でのコンテナ更新・再起動による自動デプロイ

- インフラ・ネットワーク
  - [x] ALB 経由でのアプリケーション公開
  - [x] セキュリティグループによる通信制御
  - [x] IAM Role を利用した安全な AWS リソースアクセス

- セキュリティ・運用
  - [x] ACM による SSL/TLS 証明書管理
  - [x] Route53 による独自ドメイン設定
  - [x] HTTP → HTTPS のリダイレクト対応
