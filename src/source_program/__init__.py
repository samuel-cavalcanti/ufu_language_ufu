# try:
#     from source_program.source_program import SourceProgram, SourceProgramException
#     from source_program.tensor_source_program import TensorSourceProgram
# except ImportError:
#     from .tensor_source_program import TensorSourceProgram
#     from .source_program import SourceProgram, SourceProgramException

from .tensor_source_program import TensorSourceProgram
from .source_program import SourceProgram, SourceProgramException
