import argparse

from nilearn.connectome import ConnectivityMeasure
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_files', nargs='+')

    args = parser.parse_args()

    measure = ConnectivityMeasure(
        kind='correlation',
        standardize='zscore_sample'
    )
    X = []
    for p in args.input_files:
        X.append(np.load(p))
    y = measure.fit_transform(X)
    for i, p in enumerate(args.input_files):
        np.save(p.replace('.npy', '_corr.npy'), y[i])


if __name__ == '__main__':
    main()
