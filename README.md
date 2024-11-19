## 環境構築

1. リポジトリのクローン

```
git clone https://github.com/masatotezuka/langchain-azure-openai-sample-app.git
```

2. 環境変数の設定

```
cp .env.template .env
```

自前で用意したエンドポイントと API キーを.env に設定する

3. コンテナイメージの作成

```
docker compose up --build
```

## 実行

下記の curl コマンドをターミナルで叩く

```
curl "https://5bjtgeuqxnqsvrs4a53wt4lhsa0hhlps.lambda-url.ap-northeast-1.on.aws/" -d '{"target": "男性"}'
```
