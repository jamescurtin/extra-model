[![codecov](https://codecov.io/gh/wayfair-incubator/extra-model/branch/main/graph/badge.svg?token=HXSGN5IUzu)](https://codecov.io/gh/wayfair-incubator/extra-model)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![GitHub license](https://img.shields.io/github/license/wayfair-incubator/extra-model)](https://github.com/wayfair-incubator/extra-model/blob/main/LICENSE)
![PyPI](https://img.shields.io/pypi/v/extra-model)

# extra-model

Code to run the Extra [algorithm](https://www.aclweb.org/anthology/D18-1384/) for unsupervised topic/aspect extraction on English texts.

[Read the Official Documentation here][official_documentation]

## Quick start


**IMPORTANT**:
1. When running Extra inside docker-container, make sure that Docker process has enough resources.
For example, on Mac/Windows it should have at least 8 Gb of RAM available to it. [Read More about RAM Requirements][ram_requirements]
1. GitHub repo does **not** come with Glove Embeddings. See section `Downloading Embeddings` for how to download the required embeddings.


### Using docker-compose

First, build the image:

```bash
docker-compose build
```

Then, run following command to make sure that `extra-model` was installed correctly:

```bash
docker-compose run test
```

#### Downloading Embeddings

Next step is to download the embeddings (we use [Glove](https://nlp.stanford.edu/projects/glove/) from Stanford in this project).

To download the required embeddings, run the following command:

```bash
docker-compose run --rm setup
```

The embeddings will be downloaded, unzipped and formatted into a space-efficient format. Files will be saved in the `embeddings/` directory in the root of the project directory. If the process fails, it can be safely restarted. If you want to restart the process with new files, delete all files except `README.md` in the `embeddings/` directory.

#### [Optional] Run `docker-compose build` again

After you've downloaded the embeddings, you may want to run `docker-compose build` again. 
This will build an image with embeddings already present inside the image. 

The tradeoff here is that the image will be much bigger, but you won't spend ~2 minutes each time you run `extra-model` waiting for embeddings to be mounted into the container.
On the other hand, building an image with embeddings in the context will increase build time from ~3 minutes to ~10 minutes.

#### Run `extra-model`

Finally, running `extra-model` is as simple as:

```bash
docker-compose run extra-model /package/tests/resources/100_comments.csv
```

NOTE: when using this approach, input file should be mounted inside the container.
By default, everything from `extra-model` folder will be mounted to `/package/` folder.
This can be changed in `docker-compose.yaml`

This will produce a `result.csv` file in `/io/` (default setting) folder.

Location of the output can be changed by supplying second path, e.g.:

```bash
docker-compose run extra-model /package/tests/resources/100_comments.csv /io/another_folder
```

The output filename can also be changed if you want it to be something else than `result.csv` by supplying a third argument:

```bash
docker-compose run extra-model /package/tests/resources/100_comments.csv /io/another_folder another_filename.csv
```

More examples, as well as an explanation of input/output are available in [official documentation](official_documentation).

### Using command line

TODO: add this section.

# Authors

`extra-model` was written by `mbalyasin@wayfair.com`, `mmozer@wayfair.com`.

[official_documentation]: https://wayfair-incubator.github.io/extra-model/site
[ram_requirements]: https://wayfair-incubator.github.io/extra-model/site/ram_requirements