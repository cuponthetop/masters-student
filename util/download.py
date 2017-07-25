import collections
from os import sep
from tqdm import tqdm
from os.path import join


def concatenate_urls(common_url, distinct_urls, extension):
    assert isinstance(distinct_urls, collections.Sequence), "distinc_urls is not collection.Sequence"

    return list(join(common_url, distinct_part + "." + extension) for distinct_part in distinct_urls)


class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""
    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def create_tqdm_with_filename(filepath, position, show_progress=True):
    if show_progress:
        t = TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc=filepath.split(sep)[-1], position=position)
    else:
        # create null object for report_hook
        t = {'update_to': (lambda: None), 'close': (lambda: None)}
    return t


def download_file(url, filepath, position=None, show_progress=True):
    from urllib.request import urlretrieve

    tqdm_instance = create_tqdm_with_filename(filepath=filepath, position=position, show_progress=show_progress)
    filename, headers = urlretrieve(url, filepath, reporthook=tqdm_instance.update_to)

    # tqdm_instance.close()

    return filename, repr(headers)


def download_files(file_urls, filepaths, num_worker=4, show_progress=True):
    # from multiprocessing import Pool
    from itertools import starmap
    assert isinstance(file_urls, collections.Sequence), "file_urls is not collection.Sequence"
    assert isinstance(filepaths, collections.Sequence), "filepaths is not collection.Sequence"
    assert len(file_urls) == len(filepaths), "dimension of filepaths and file_urls does not match"

    result = list(map(download_file, file_urls, filepaths, [show_progress] * len(file_urls)))

    return result
