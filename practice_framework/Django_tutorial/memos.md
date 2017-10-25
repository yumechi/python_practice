# Django tutorialをやってみる
## 参照先

公式のもの

https://docs.djangoproject.com/ja/1.11/intro/tutorial01/

## tutorial02

データベースをやるらしいですよ。

## Databaseの設定

mysite/settings.py を編集する。デフォルトではSQLiteを使用する。
（本番ではポスグレとか使ってね  [参照先](https://docs.djangoproject.com/ja/1.11/topics/install/#database-installation)）

DATABASESの'default'項目内の設定を変える。
ENGINEがデータベースの種類（SQliteとか、postgresqlとか、mysqlとか）
NAMEがデータベースの名前（デフォルト値もあるみたい）

SQLite以外の場合は、USER、PASSOWORD、HOSTなどの設定も必要。

**TIPS**
`TIME_ZONE` の設定は罠がある。'JST' とか正しそうだけど、実際はエラーになる。
https://torina.top/detail/339/

> TIME_ZONE = 'Asia/Tokyo'

これらの設定をしたら、下記コマンドを実行してやるとこのようなログが流れる。
`INSTALLED_APP` の設定に従い、必要なデータベーステーブルを作成してくれる。

```
[10/25 23:48:05] $ python manage.py migrate                      (git)-[master]
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```
時間があったら中身を見てみましょう。（ちょっと今は流す）

次回はモデルの作成から。


