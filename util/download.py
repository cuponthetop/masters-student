import collections
import logging
from tqdm import tqdm


def concatenate_urls(common_url, distinct_urls):
    assert not isinstance(common_url, collections.Sequence), "common_url is collection.Sequence"
    assert isinstance(distinct_urls, collections.Sequence), "distinc_urls is not collection.Sequence"

    return (common_url + distinct_part for distinct_part in distinct_urls)


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
        t = TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc=filepath.split('/')[-1], position=position)
    else:
        # create null object for report_hook
        t = {'update_to': (lambda: None)}
    return t


def download_files(file_urls, filepaths, num_worker=4, timeout=900, show_progress=True):
    def download_file(url, filepath, position, tqdm_instance):
        import urllib

        urllib.urlretrieve(url, filepath, report_hook=tqdm_instance.update_to)

    from multiprocessing import Pool
    assert isinstance(file_urls, collections.Sequence), "file_urls is not collection.Sequence"
    assert isinstance(filepaths, collections.Sequence), "filepaths is not collection.Sequence"
    assert file_urls.length == filepaths.length, "dimension of filepaths and file_urls does not match"

    maybe_tqdms = (create_tqdm_with_filename(filepath, position) for (filepath, position) in
                   zip(filepaths, range(filepaths.length)))

    with Pool(num_worker) as pool:

        result = pool.starmap_async(download_file, zip(file_urls, filepaths, range(file_urls.length), maybe_tqdms))

        pool.close()
        pool.join()

    (tqdm_instance.close() for tqdm_instance in maybe_tqdms)

    return result.get(timeout)
