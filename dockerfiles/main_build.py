import shlex
import subprocess
import os

# シェルコマンドを実行する
def exec_cmd(cmd):
    tokens = shlex.split(cmd)
    subprocess.run(tokens)

# コマンドの実行結果が返り値になる。コマンドの返り値がコマンドになるものに使う。
# 注意点は改行コードを削除すること
def get_cmd_stdout(cmd):
    tokens = shlex.split(cmd)
    tokens = subprocess.run(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tokens.stdout.decode("utf8").replace('\n','')

# リポジトリ名を取得
REPO_APP = 'aws ecr describe-repositories --repository-names app --output text --query "repositories[0].repositoryUri"'
REPO_APP = get_cmd_stdout(REPO_APP)
REPO_WEB = 'aws ecr describe-repositories --repository-names web --output text --query "repositories[0].repositoryUri"'
REPO_WEB = get_cmd_stdout(REPO_WEB)

if __name__ == "__main__":
    # flask+uwsgi+pythonのDockerfileをビルド
    build_app = 'docker build -t {}:latest ./app/'.format(REPO_APP)
    exec_cmd(build_app)

    # nginxのDockerfileをビルド
    build_web = 'docker build -t {}:latest ./nginx/'.format(REPO_WEB)
    exec_cmd(build_web)

    # イメージをpush
    for repo in [REPO_APP, REPO_WEB]:
        push_image = 'docker push {}:latest'.format(repo)
        exec_cmd(push_image)
