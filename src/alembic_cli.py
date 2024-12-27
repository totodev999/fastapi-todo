import sys
import subprocess
from pathlib import Path


def alembic_revision():
    alembic_ini_path = Path("src/alembic.ini").resolve()
    if len(sys.argv) > 1:
        # 引数としてコメントを受け取る
        comment = sys.argv[1]
    else:
        # コメントがない場合、エラーを表示
        print("You need to pass a comment as an argument.")
        sys.exit(1)

    # Alembicコマンドを実行
    subprocess.run(
        ["alembic", "-c", alembic_ini_path, "revision", "--autogenerate", "-m", comment]
    )


def alembic_migrate():
    alembic_ini_path = Path("src/alembic.ini").resolve()

    # Alembicコマンドを実行
    subprocess.run(["alembic", "-c", alembic_ini_path, "upgrade", "head"])
