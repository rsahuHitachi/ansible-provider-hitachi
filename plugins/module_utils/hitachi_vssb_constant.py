import logging
from telnetlib import AUTHENTICATION
from ansible.module_utils.six.moves.urllib import parse as urlparse


class VSSB_Api(object):
    SERVERID = 'serverId'
    SERVER_DEFAULT = 'localhost'
    SERVER_PORT_DEFAULT = 443
    JOBID = 'jobId'
    AFFECTEDRESOURCES = 'affectedResources'
    STATUS = 'status'
    STATE = 'state'
    ERROR = 'error'
    MESSAGEID = 'messageId'
    MESSAGE = 'message'
    CAUSE = 'cause'
    SOLUTION = 'solution'
    CHANGED = 'changed'
    MSG = 'msg'
    OUTPUTS = 'outputs'
    VOLUMES = 'volumes'
    API_ERROR = 'api_error'
    SINGLE_QUOTE = "'"
    DATA = 'data'
    ID = 'id'
    SERVERNICKNAME = 'serverNickname'
    OSTYPE = 'osType'
    PROTOCOL = 'protocol'
    ISCSI = 'iSCSI'
    ISCSINAME = 'iscsiName'
    NAME = 'name'
    NICKNAME = 'nickname'
    HBAID = 'hbaId'
    PORTID = 'portId'
    VOLUME_BASENAME_START_NUMBER_DEFAULT = 0
    VOLUME_BASENAME_NUMBER_OF_DIGIT_DEFAULT = 5
    CAPACITY = 'capacity'
    NUMBER = 'number'
    NAMEPARAM = 'nameParam'
    BASENAME = 'baseName'
    STARTNUMBER = 'startNumber'
    NUMBEROFDIGIT = 'numberOfDigits'
    POOLID = 'poolId'
    VOLUMEID = 'volumeId'
    TOTALCAPACITY = 'totalCapacity'
    ADDITIONALCAPACITY = 'additionalCapacity'
    TARGETCHAPUSERNAME = 'targetChapUserName'
    TARGETCHAPSECRET = 'targetChapSecret'
    INITIATORCHAPUSERNAME = 'initiatorChapUserName'
    INITIATORCHAPSECRET = 'initiatorChapSecret'
    CHAPUSERID = 'chapUserId'
    HBANAME = 'hbaName'
    PORTNICKNAME = 'portNickname'
    PROTECTONDOMAINID = 'protectionDomainId'
    CONTROLPORTIPV4ADDRESS = 'controlPortIpv4Address'
    STORAGENODEID = 'storageNodeId'
    DRIVECAPACITY = 'driveCapacity'
    DRIVEIDS = 'driveIds'
    ACTIVESTORAGENODEID = 'activeStorageNodeId'
    DATAREBALANCESTATUS = 'dataRebalanceStatus'
    REDUNDANTTYPE = 'redundantType'
    TIME_DEFAULT = 10


class Endpoints(object):
    GET_SERVERS = 'v1/objects/servers'
    POST_SERVERS = 'v1/objects/servers'
    GET_SERVERS_AND_QUERY = 'v1/objects/servers?nickname={}'
    DELETE_SERVERS = 'v1/objects/servers/{}'
    GET_VOLUME_SERVER_CONNECTIONS_AND_ID = 'v1/objects/volume-server-connections?serverId={}'
    DELETE_VOLUMES = 'v1/objects/volumes/{}'
    POST_HBAS = 'v1/objects/servers/{}/hbas'
    GET_HBAS = 'v1/objects/servers/{}/hbas'
    GET_PORTS = 'v1/objects/ports'
    GET_PORTS_AND_QUERY = 'v1/objects/ports?name={}'
    GET_PATHS = 'v1/objects/servers/{}/paths'
    POST_PATHS = 'v1/objects/servers/{}/paths'
    GET_POOLS = 'v1/objects/pools'                               
    GET_POOLS_AND_ID = 'v1/objects/pools/{}'                               
    GET_POOLS_AND_QUERY = 'v1/objects/pools?name={}'
    POST_VOLUMES = 'v1/objects/volumes'
    GET_VOLUMES_AND_QUERY = 'v1/objects/volumes?name={}'
    GET_VOLUMES_AND_NICKNAME = 'v1/objects/volumes?nickname={}'
    GET_VOLUMES_AND_SERVERID = 'v1/objects/volumes?serverId={}'
    POST_VOLUME_SERVER_CONNECTIONS = 'v1/objects/volume-server-connections'
    POST_VOLUMES_EXPAND = 'v1/objects/volumes/{}/actions/expand/invoke'
    GET_CHAPUSERS_AND_QUERY = 'v1/objects/chap-users?targetChapUserName={}'
    POST_CHAPUSERS = 'v1/objects/chap-users'
    DELETE_CHAPUSERS = 'v1/objects/chap-users/{}'
    GET_PORT_AUTH_SETTINGS_CHAPUSERS = 'v1/objects/port-auth-settings/{}/chap-users'
    POST_PORT_AUTH_SETTINGS_CHAPUSERS = 'v1/objects/port-auth-settings/{}/chap-users'
    GET_JOBS = 'v1/objects/jobs/{}'
    GET_STORAGE_NODES_AND_QUERY = 'v1/objects/storage-nodes?protectionDomainId={}'
    GET_DRIVES = 'v1/objects/drives'
    POST_POOLS_EXPAND = 'v1/objects/pools/{}/actions/expand/invoke'
    GET_STORAGE_CONTROLLERS = 'v1/objects/storage-controllers'


class Http(object):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
    BASE_URL = '/ConfigurationManager/simple/'
    CONTENT_TYPE = 'Content-Type'
    APPLICATION_JSON = 'application/json'
    HEADERS_JSON = {
        CONTENT_TYPE: APPLICATION_JSON
    }
    HTTP = 'http://'
    HTTPS = 'https://'
    DEFAULT_PORT = 443
    DEFAULT_SSL_PORT = 443
    OPEN_URL_TIMEOUT = 300
    USER_AGENT = 'automation-module'


class ModuleArgs(object):
    NULL = "None"
    CHECK_MODE = 'check_mode'
    SERVER = 'management_address'
    SERVER_PORT = 'management_port'
    USER = 'user'
    PASSWORD = 'password'
    SERVER_NICKNAME = 'server_nickname'
    OS_TYPE = 'os_type'
    ISCSI_NAME = 'iscsi_name'
    TARGET_PORT_NAME = 'target_port_name'
    POOL_NAME = 'pool_name'
    CAPACITY = 'capacity_mb'
    NUMBER = 'number'
    BASE_NAME = 'base_name'
    START_NUMBER = 'start_number'
    NUMBER_OF_DIGIT = 'number_of_digit'
    VOLUME_NAME = 'volume_name'
    TARGET_CHAP_USER_NAME = 'target_chap_user_name'
    TARGET_CHAP_SECRET = 'target_chap_secret'
    INITIATOR_CHAP_USER_NAME = 'initiator_chap_user_name'
    INITIATOR_CHAP_USER_SECRET = 'initiator_chap_secret'
    POOL_EXPAND_CAPACITY = 'pool_expand_capacity'
    EXPAND_POOL_PROCESS1_INFO = 'expand_pool_process1_info'
    DEVICE_COUNT = 'device_count'
    EC2_INSTANCE_INFO = 'ec2_instance_info'
    SYSTEM_CONFIGRATION_FILE = 'system_configuration_file'
    VM_CONFIGRATION_FILE = 'vm_configuration_file'
    DRIVE_COUNT_IN_NODE = 'drive_count_in_node'
    ADDITINAL_DRIVE_COUNT_IN_NODE = 'additional_drive_count_in_node'
    ADD_STORAGENODE_PROCESS1_INFO = 'add_storagenode_process1_info'
    TIME_A = 'time_a'
    TIME_B = 'time_b'
    TIME_C = 'time_c'
    TIME_D = 'time_d'


class AutomationConstants(object):
    PORT_NUMBER_MIN = 0
    PORT_NUMBER_MAX = 49151
    NAME_PARAMS_MIN = 1
    NAME_PARAMS_MAX = 256
    MIN_SIZE_ALLOWED = 1
    MAX_SIZE_ALLOWED = 999999999999
    MAX_TIME_ALLOWED = 999
    MIN_TIME_ALLOWED = 1
    CHAP_SECRET_MIN = 12
    CHAP_SECRET_MAX = 32


class ErrorMessages(object):
    INVALID_PORT_NUMBER_ERR = 'The specified value is invalid' +\
        ' ({}: {}). Specify the value within a valid range (min: ' +\
        str(AutomationConstants.PORT_NUMBER_MIN) + ', max: ' +\
        str(AutomationConstants.PORT_NUMBER_MAX) + ').'
    HTTP_4xx_ERRORS = 'Invalid request sent by the client.' +\
        ' API responded with client error code ({}). Reason: {}'
    HTTP_5xx_ERRORS = 'The server encountered an unexpected ' +\
        'condition. API responded with server error code ({}). Reason: {}'
    API_COMMUNICATION_ERR = 'Communication with the target server' +\
        ' failed. Reason: {}'
    NOT_AVAILABLE = 'Not Available.'
    REQUIRED_VALUE_ERR = 'The value for the parameter is' +\
        ' required. ({}) Specify a valid value.'
    API_TIMEOUT_ERR = 'A timeout occurred because no response' +\
        ' was received from the server.'
    INVALID_TYPE_VALUE = 'The specified value is not an integer' +\
        ' type ({}: {}). Specify an integer value.'
    INVALID_NAME_SIZE = 'The argument of the parameter name length is invalid' +\
        ' ({}: {}). Specify in a valid range characters'
    INVALID_SIZE_VALUE = 'The specified size argument has an invalid range' +\
        ' ({}: {}). Specify in a valid range.'
    INVALID_TIME_VALUE = 'The specified time argument has an invalid range' +\
        ' ({}: {}). Specify in a valid range.'
    INVALID_SECRET_SIZE = 'The specified value is invalid' +\
        ' ({}: {}). Secret should be 12 to 32 chars.'


class LogMessages(object):
    ENTER_METHOD = 'Enter method: {}'
    LEAVE_METHOD = 'Leave method: {}'
    API_REQUEST_START = 'API Request: {} {}'
    API_RESPONSE = 'API Response: {}'


class Log(object):
    SYSLOG_IDENTIFIER = 'SYSLOG_IDENTIFIER'
    PRIORITY = 'PRIORITY'
    # There is no applicable level in Python for following priorities
    # 0(Emergency), 1(Alert), 5(Notice)
    ARGS = {
        logging.DEBUG: {PRIORITY: 7},
        logging.INFO: {PRIORITY: 6},
        logging.WARNING: {PRIORITY: 4},
        logging.ERROR: {PRIORITY: 3},
        logging.CRITICAL: {PRIORITY: 2},
    }