# Generated by ariadne-codegen on 2023-03-10 15:46
# Source: schema.graphql

from enum import Enum


class AttributeDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DOUBLE = "DOUBLE"
    INTEGER = "INTEGER"
    LONG = "LONG"
    STRING = "STRING"


class CampaignLifecycleState(str, Enum):
    DEPLOYED = "DEPLOYED"
    IN_PROGRESS = "IN_PROGRESS"


class ConnectionType(str, Enum):
    file = "file"
    gcs = "gcs"
    gcsFileStream = "gcsFileStream"
    hive = "hive"
    jdbc = "jdbc"
    jdbc_cdata = "jdbc_cdata"
    jdbc_generic = "jdbc_generic"
    mongo = "mongo"
    s3 = "s3"
    s3FileStream = "s3FileStream"


class ContentType(str, Enum):
    csv = "csv"
    json = "json"
    parquet = "parquet"


class ExplorationType(str, Enum):
    EPSILON_GREEDY = "EPSILON_GREEDY"
    RND = "RND"
    SOFTMAX = "SOFTMAX"
    SQUARE_CB = "SQUARE_CB"


class JobStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    ERROR = "ERROR"
    QUEUED = "QUEUED"
    SUBMITTED = "SUBMITTED"


class MeasureFrequency(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    YEARLY = "YEARLY"


class MissionLifecycleState(str, Enum):
    ARCHIVED = "ARCHIVED"
    DEPLOYED = "DEPLOYED"
    EDITING = "EDITING"
    READY_FOR_DEPLOYMENT = "READY_FOR_DEPLOYMENT"
    REVIEWING = "REVIEWING"
    SIMULATING = "SIMULATING"


class PolicyEvaluation(str, Enum):
    DM = "DM"
    DR = "DR"
    IPS = "IPS"
    MTR = "MTR"


class ResourceType(str, Enum):
    DATA_SOURCE = "DATA_SOURCE"
    PROFILE_SCHEMA = "PROFILE_SCHEMA"


class ScriptLanguage(str, Enum):
    Javascript = "Javascript"
    Python = "Python"
    RobotFramework = "RobotFramework"


class SimulationStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"
    INITIALIZING = "INITIALIZING"
    PLANNING = "PLANNING"
    REFINING = "REFINING"
    RUNNING = "RUNNING"
    TRAINING = "TRAINING"
    UNKNOWN = "UNKNOWN"


class SinkKind(str, Enum):
    BATCH = "BATCH"
    STREAMING = "STREAMING"


class SourceKind(str, Enum):
    batch = "batch"
    streaming = "streaming"


class StreamStatus(str, Enum):
    AWAITING = "AWAITING"
    PROCESSING = "PROCESSING"


class TimeoutUnit(str, Enum):
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    MONTH = "MONTH"
    SECOND = "SECOND"
    WEEK = "WEEK"
    YEAR = "YEAR"


class UserQueryDialectSpec(str, Enum):
    NATIVE = "NATIVE"
    SPARK_SQL = "SPARK_SQL"


class ValueDirection(str, Enum):
    DOWN = "DOWN"
    NONE = "NONE"
    UP = "UP"


class WriteMode(str, Enum):
    APPEND = "APPEND"
    ERROR = "ERROR"
    OVERWRITE = "OVERWRITE"
