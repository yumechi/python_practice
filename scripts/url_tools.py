import argparse    # 1. argparseをインポート


def get_args():
    parser = argparse.ArgumentParser(description='URLのエンコードでコードをします')
    
    parser.add_argument('-d', '--decode')
    parser.add_argument('-e', '--encode')

    return parser.parse_args()

def run(settings) -> None:
    import urllib.parse

    if settings.decode:
        print(f"{settings.decode}: {urllib.parse.unquote(settings.decode)}" )
    if settings.encode:
        print(f"{settings.encode}: {urllib.parse.quote(settings.encode)}")



if __name__ == "__main__":
    settings = get_args()
    run(settings)
