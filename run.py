"""
"""
from masterstudent.tensorflowstudent import TensorFlowStudent
from args import get_parser


# make this contextmanager
def load_config(config_path):
    """
    """
    from yaml import load
    with open(config_path, 'r') as f:
        return load(f)


def run_masters_student(backend_type, config):
    """
    :param backend_type:
    :param config:
    :return:
    """
    student = None
    if backend_type == "tensorflow":
        student = TensorFlowStudent(config)

    student.start()

if __name__ == "__main__":
    args = get_parser().parse_args()

    config = load_config(args.config)

    try:
        backend = config['backend']
        run_masters_student(backend, config)
    except KeyError:
        print('backend not defined')
