import shlex
import subprocess
import os

# シェルコマンドを実行する
def exec_cmd(cmd):
    tokens = shlex.split(cmd)
    subprocess.run(tokens)

# コマンドの実行結果が返り値になる。コマンドの返り値がコマンドになるものに使う
def get_cmd_stdout(cmd):
    tokens = shlex.split(cmd)
    tokens = subprocess.run(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tokens.stdout.decode("utf8")


# ecrにログイン
LOGIN_TO_ECR = 'aws ecr get-login --region $AWS_DEFAULT_REGION --no-include-email'
# LOGIN_TO_ECR = 'aws ecr get-login --no-include-email --region ap-northeast-1'
LOGIN_TO_ECR = get_cmd_stdout(LOGIN_TO_ECR)
exec_cmd(LOGIN_TO_ECR)


    
