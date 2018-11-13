import os
import __main__

#
# ENTRIES
#

DEEP_ENTRY_INPUT = 0
DEEP_ENTRY_LABEL = 1
DEEP_ENTRY_OUTPUT = 2
DEEP_ENTRY_ADDITIONAL_DATA = 3

#
# TYPE FLAGS
#

DEEP_TYPE_FILE = 0
DEEP_TYPE_FOLDER = 1
DEEP_TYPE_IMAGE = 2
DEEP_TYPE_VIDEO = 3
DEEP_TYPE_INTEGER = 4
DEEP_TYPE_FLOAT = 5
DEEP_TYPE_BOOLEAN = 6
DEEP_TYPE_SOUND = 7
DEEP_TYPE_SEQUENCE = 8
DEEP_TYPE_NP_ARRAY = 9

#
# NOTIFICATION FLAGS
#

DEEP_NOTIF_INFO = 0
DEEP_NOTIF_DEBUG = 1
DEEP_NOTIF_SUCCESS = 2
DEEP_NOTIF_WARNING = 3
DEEP_NOTIF_ERROR = 4
DEEP_NOTIF_FATAL = 5
DEEP_NOTIF_INPUT = 6
DEEP_NOTIF_RESULT = 7

#
# COMPUTER VISION LIBRARY
#

DEEP_LIB_OPENCV = 0
DEEP_LIB_PIL = 1

#
# HISTORY SAVING CONDITION
#

DEEP_SAVE_CONDITION_END_BATCH = 0         # Highly not recommended
DEEP_SAVE_CONDITION_END_EPOCH = 1
DEEP_SAVE_CONDITION_END_TRAINING = 2
DEEP_SAVE_CONDITION_AUTO = 3                # Highly recommended

#
# DATA MEMORIZATION CONDITION
#

DEEP_MEMORIZE_BATCHES = 0
DEEP_MEMORIZE_EPOCHS = 1


#
# VERBOSE
#

DEEP_VERBOSE_BATCH = 2
DEEP_VERBOSE_EPOCH = 1
DEEP_VERBOSE_TRAINING = 0

#
# SHUFFLE
#

DEEP_SHUFFLE_NONE = 0
DEEP_SHUFFLE_ALL = 1
DEEP_SHUFFLE_BATCHES = 2

#
# SAVE NETWORK FORMAT
#

DEEP_SAVE_NET_FORMAT_ONNX = 0
DEEP_SAVE_NET_FORMAT_PYTORCH = 1

#
# DEEP EXTENSIONS
#
DEEP_EXT_LOGS = "logs"
DEEP_EXT_YAML = "yaml"
DEEP_EXT_JPG = "jpg"

#
# DEEP CONFIG FLAGS
#
DEEP_CONFIG_DIVIDER = "/"

DEEP_CONFIG_DATA = "data"
DEEP_CONFIG_DATA_DATALOADER = "dataloader"
DEEP_CONFIG_DATA_DATALOADER_BATCH_SIZE = "batch_size"
DEEP_CONFIG_DATA_DATALOADER_NUM_WORKERS = "num_workers"
DEEP_CONFIG_DATA_DATASET = "dataset"
DEEP_CONFIG_DATA_DATASET_TEST = "test"
DEEP_CONFIG_DATA_DATASET_TEST_INPUTS = "inputs"
DEEP_CONFIG_DATA_DATASET_TEST_LABELS = "labels"
DEEP_CONFIG_DATA_DATASET_TEST_ADDITIONAL_DATA = "additional_data"
DEEP_CONFIG_DATA_DATASET_TRAIN = "train"
DEEP_CONFIG_DATA_DATASET_TRAIN_INPUTS = "inputs"
DEEP_CONFIG_DATA_DATASET_TRAIN_LABELS = "labels"
DEEP_CONFIG_DATA_DATASET_TRAIN_ADDITIONAL_DATA = "additional_data"
DEEP_CONFIG_DATA_DATASET_VALIDATION = "validation"
DEEP_CONFIG_DATA_DATASET_VALIDATION_INPUTS = "inputs"
DEEP_CONFIG_DATA_DATASET_VALIDATION_LABELS = "labels"
DEEP_CONFIG_DATA_DATASET_VALIDATION_ADDITIONAL_DATA = "additional_data"
DEEP_CONFIG_HISTORY = "history"
DEEP_CONFIG_LOSS = "loss"
DEEP_CONFIG_METRICS = "metrics"
DEEP_CONFIG_NETWORK = "network"
DEEP_CONFIG_OPTIMIZER = "optimizer"
DEEP_CONFIG_PROJECT = "project"
DEEP_CONFIG_PROJECT_CV_LIBRARY = "cv_library"
DEEP_CONFIG_PROJECT_NAME = "name"
DEEP_CONFIG_PROJECT_WRITE_LOGS = "write_logs"
DEEP_CONFIG_TRANSFORM = "transform"

DEEP_CONFIG_FILES = {DEEP_CONFIG_PROJECT: "%s.%s" % (DEEP_CONFIG_PROJECT, DEEP_EXT_YAML),
                     DEEP_CONFIG_DATA: "%s.%s" % (DEEP_CONFIG_DATA, DEEP_EXT_YAML),
                     DEEP_CONFIG_TRANSFORM: "%s.%s" % (DEEP_CONFIG_TRANSFORM, DEEP_EXT_YAML),
                     DEEP_CONFIG_NETWORK: "%s.%s" % (DEEP_CONFIG_NETWORK, DEEP_EXT_YAML),
                     DEEP_CONFIG_OPTIMIZER: "%s.%s" % (DEEP_CONFIG_OPTIMIZER, DEEP_EXT_YAML),
                     DEEP_CONFIG_METRICS: "%s.%s" % (DEEP_CONFIG_METRICS, DEEP_EXT_YAML),
                     DEEP_CONFIG_LOSS: "%s.%s" % (DEEP_CONFIG_LOSS, DEEP_EXT_YAML),
                     DEEP_CONFIG_HISTORY: "%s.%s" % (DEEP_CONFIG_HISTORY, DEEP_EXT_YAML)}


DEEP_CONFIG = {DEEP_CONFIG_PROJECT: [DEEP_CONFIG_PROJECT_NAME,
                                     DEEP_CONFIG_PROJECT_CV_LIBRARY,
                                     DEEP_CONFIG_PROJECT_WRITE_LOGS],
               DEEP_CONFIG_DATA: [{DEEP_CONFIG_DATA_DATALOADER: [DEEP_CONFIG_DATA_DATALOADER_BATCH_SIZE,
                                                                 DEEP_CONFIG_DATA_DATALOADER_NUM_WORKERS]},
                                  {DEEP_CONFIG_DATA_DATASET: [{DEEP_CONFIG_DATA_DATASET_TRAIN: [DEEP_CONFIG_DATA_DATASET_TRAIN_INPUTS,
                                                                                        DEEP_CONFIG_DATA_DATASET_TRAIN_LABELS,
                                                                                        DEEP_CONFIG_DATA_DATASET_TRAIN_ADDITIONAL_DATA],
                                                               DEEP_CONFIG_DATA_DATASET_VALIDATION: [DEEP_CONFIG_DATA_DATASET_VALIDATION_INPUTS,
                                                                                                     DEEP_CONFIG_DATA_DATASET_VALIDATION_LABELS,
                                                                                                     DEEP_CONFIG_DATA_DATASET_VALIDATION_ADDITIONAL_DATA],
                                                               DEEP_CONFIG_DATA_DATASET_TEST: [DEEP_CONFIG_DATA_DATASET_TEST_INPUTS,
                                                                                               DEEP_CONFIG_DATA_DATASET_TEST_LABELS,
                                                                                               DEEP_CONFIG_DATA_DATASET_TEST_ADDITIONAL_DATA]}]}]}

#
# DEEP MESSAGES / TEXT / STATEMENTS
#
DEEP_MSG_ALREADY_AWAKE = "I am already awake !"
DEEP_MSG_CONFIG_NOT_FOUND = "Configuration not found : %s is missing from %s configurations"
DEEP_MSG_DIR_NOT_FOUND = "Directory not found : %s"
DEEP_MSG_FILE_NOT_FOUND = "File not found : %s"
DEEP_MSG_INSTRUCTRION = "Awaiting instruction ..."
DEEP_MSG_LOAD_CONFIG_FAIL = "Project configurations are incomplete"
DEEP_MSG_LOAD_CONFIG_FILE = "File loaded : Configurations from %s successfully imported"
DEEP_MSG_LOAD_CONFIG_START = "Loading project configurations from %s ..."
DEEP_MSG_LOAD_CONFIG_SUCCESS = "Finished loading project configurations from %s"
DEEP_MSG_REMOVE_COMMAND = "Illegal command %s"
DEEP_MSG_REMOVE_LOGS = "%s%s%s is False : Notification logs have been removed" % (DEEP_CONFIG_PROJECT,
                                                                                 DEEP_CONFIG_DIVIDER,
                                                                                 DEEP_CONFIG_PROJECT_WRITE_LOGS)

FINISHED_TRAINING = "Finished training"
SUMMARY = "Summary"
TOTAL_LOSS = "Total Loss"
WALL_TIME = "Wall Time"
RELATIVE_TIME = "Relative Time"
EPOCH = "Epoch"
BATCH = "Batch"
TRAINING = "Training"
VALIDATION = "Validation"
TIME_FORMAT = "%Y:%m:%d:%H:%M:%S"
EPOCH_END = "End of Epoch [%i/%i]"
EPOCH_START = "Start of Epoch [%i/%i]"
HISTORY_SAVED = "History saved to %s"


#
# COMPARISON FOR THE OVERWATCH METRIC
#

DEEP_COMPARE_SMALLER = 0
DEEP_COMPARE_BIGGER = 1

#
# ABSOLUTE PATHS TO WORKING DIRECTORIES
#

DEEP_PATH_NOTIFICATION = r"%s/logs" % os.path.dirname(os.path.abspath(__main__.__file__))
DEEP_PATH_RESULTS = r"%s/results" % os.path.dirname(os.path.abspath(__main__.__file__))
DEEP_PATH_HISTORY = r"%s/results/history" % os.path.dirname(os.path.abspath(__main__.__file__))
DEEP_PATH_SAVE_MODEL = r"%s/results/models" % os.path.dirname(os.path.abspath(__main__.__file__))

#
# DEEP EXIT FLAGS
#
DEEP_EXIT_FLAGS = ["q", "quit", "quit"]

#
# DEEP FILTER OUT OF BOUND COMMANDS
#
DEEP_FILTER = ["wake"]
DEEP_FILTER_ENDS_WITH = []
DEEP_FILTER_INCLUDES = ["__"]
DEEP_FILTER_STARTS_WITH = ["__"]
DEEP_FILTER_STARTS_ENDS_WITH = ["__"]

#
# DEEP_ENCODE_FLAGS
#
DEEP_ENCODE_ASCII = "ascii"
DEEP_ENCODE_UTF8 = "utf-8"