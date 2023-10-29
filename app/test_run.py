import nbformat
from nbconvert.preprocessors import ExecutePreprocessor



def test_run(notebook_path):
    with open(notebook_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)

    executor = ExecutePreprocessor(timeout=600, kernel_name='myenv-kernel')
    executor.preprocess(notebook, {'metadata': {'path': '.'}})

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)


