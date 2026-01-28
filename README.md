## AWS個人学習プロジェクト

### 目的
- AWSサービスを理解し、インフラ環境を自分で設計・構築できるスキルを習得する。
- DevOps文化やツールの理解を深め、CI/CDパイプラインを設計・実装し、開発・運用の効率化を図る。

### 要件定義
以下を構築する
- アプリ
  - Streamlit（Python）
  - 外部APIで株価取得
  - グラフ描画
  - RDS連携

- 実行環境
  - ローカル：Docker Desktop
  - 本番：EC2 + Docker

- CI/CD
  - GitHub Actions
  - mainブランチにプッシュ
  - pytest実行
  - Dockerイメージ作成
  - EC2へデプロイ（コンテナ再起動）

- AWSインフラ環境

