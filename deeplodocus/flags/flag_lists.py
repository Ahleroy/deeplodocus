from deeplodocus.flags.load_as import *
from deeplodocus.flags.dtype import *
from deeplodocus.flags.source import *
from deeplodocus.flags.load import *
from deeplodocus.flags.entry import *
from deeplodocus.flags.lib import *
from deeplodocus.flags.transformer import *
from deeplodocus.flags.shuffle import *
from deeplodocus.flags.save import *
from deeplodocus.flags.verbose import *
from deeplodocus.flags.event import *
from deeplodocus.flags.admin import *
from deeplodocus.flags.dtype import *

# LOAS_AS
DEEP_LIST_LOAD_AS = [
    DEEP_LOAD_AS_IMAGE,
    DEEP_LOAD_AS_VIDEO,
    DEEP_LOAD_AS_BOOLEAN,
    DEEP_LOAD_AS_INTEGER,
    DEEP_LOAD_AS_FLOAT,
    DEEP_LOAD_AS_SEQUENCE,
    DEEP_LOAD_AS_AUDIO,
    DEEP_LOAD_AS_NP_ARRAY,
    DEEP_LOAD_AS_STRING,
    DEEP_LOAD_AS_SEQUENCE
    ]


# SOURCES
DEEP_LIST_SOURCE = [
    DEEP_SOURCE_FILE,
    DEEP_SOURCE_FOLDER,
    DEEP_SOURCE_DATABASE
]

# LOAD METHODS
DEEP_LIST_LOAD_METHOD = [
    DEEP_LOAD_METHOD_MEMORY,
    DEEP_LOAD_METHOD_HARDDRIVE,
    DEEP_LOAD_METHOD_SERVER
]
# ENTRIES
DEEP_LIST_ENTRY = [
    DEEP_ENTRY_INPUT,
    DEEP_ENTRY_LABEL,
    DEEP_ENTRY_OUTPUT,
    DEEP_ENTRY_ADDITIONAL_DATA
]

DEEP_LIST_POINTER_ENTRY = [
    DEEP_ENTRY_INPUT,
    DEEP_ENTRY_LABEL,
    DEEP_ENTRY_ADDITIONAL_DATA
]

# COMPUTER VISION LIBRARIES
DEEP_LIST_CV_LIB = [
    DEEP_LIB_PIL,
    DEEP_LIB_OPENCV
]


# TRANSFORMERS
DEEP_LIST_TRANSFORMERS = [
    DEEP_TRANSFORMER_SEQUENTIAL,
    DEEP_TRANSFORMER_ONE_OF,
    DEEP_TRANSFORMER_SOME_OF
]

# SHUFFLING
DEEP_LIST_SHUFFLE = [
    DEEP_SHUFFLE_NONE,
    DEEP_SHUFFLE_BATCHES,
    DEEP_SHUFFLE_ALL,
    DEEP_SHUFFLE_RANDOM_PICK
]

# SAVE FORMATS
DEEP_LIST_SAVE_FORMATS = [
    DEEP_SAVE_FORMAT_ONNX,
    DEEP_SAVE_FORMAT_PYTORCH
]

# SAVE CONDITIONS
DEEP_LIST_SAVE_CONDITIONS = [
    DEEP_SAVE_CONDITION_LESS,
    DEEP_SAVE_CONDITION_GREATER
]

# VERBOSE
DEEP_LIST_VERBOSE = [
    DEEP_VERBOSE_BATCH,
    DEEP_VERBOSE_EPOCH,
    DEEP_VERBOSE_TRAINING
]

# SAVE SIGNAL
DEEP_LIST_SAVE_SIGNAL = [
    DEEP_SAVE_SIGNAL_END_BATCH,
    DEEP_SAVE_SIGNAL_END_EPOCH,
    DEEP_SAVE_SIGNAL_END_TRAINING,
    DEEP_SAVE_SIGNAL_AUTO
]

# ADMIN COMMANDS
DEEP_LIST_ADMIN = [
    DEEP_ADMIN_HELP,
    DEEP_ADMIN_START_PROJECT,
    DEEP_ADMIN_VERSION,
    DEEP_ADMIN_TRANSFORMER,
    DEEP_ADMIN_OUTPUT_TRANSFORMER,
    DEEP_ADMIN_ONEOF_TRANSFORMER,
    DEEP_ADMIN_SEQUENTIAL_TRANSFORMER,
    DEEP_ADMIN_SOMEOF_TRANSFORMER
]


# DTYPE
DEEP_LIST_DTYPE = [
    DEEP_DTYPE_FLOAT8,
    DEEP_DTYPE_FLOAT16,
    DEEP_DTYPE_FLOAT32,
    DEEP_DTYPE_FLOAT64,
    DEEP_DTYPE_UINT8,
    DEEP_DTYPE_UINT16,
    DEEP_DTYPE_UINT32,
    DEEP_DTYPE_UINT64,
    DEEP_DTYPE_INT8,
    DEEP_DTYPE_INT16,
    DEEP_DTYPE_INT32,
    DEEP_DTYPE_INT64,
    DEEP_DTYPE_STR
]