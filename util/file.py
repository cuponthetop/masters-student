import os
import logging


def make_dir(dirpath):
    try:
        os.makedirs(name=dirpath, exist_ok=True)
        logging.info('Successfully created directory - %s' % dirpath)
    except:
        raise


def clean_dir(dirpath):
    import shutil
    if shutil.rmtree.avoids_symlink_attacks:
        import stat

        def grant_permission_retry(*args):
            func, path, _ = args  # onerror returns a tuple containing function, path and     exception info
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)

        shutil.rmtree(path=dirpath, onerror=grant_permission_retry)
    else:
        logging.warning('shutil.rmtree is not safe in your OS, abort cleaning directory - %s' % dirpath)
    make_dir(dirpath)


def file_exists(filepath):
    from pathlib import Path
    return Path(filepath).is_file()
