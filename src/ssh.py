from os import getenv
from utils import commandArgsToExcludedStr
from collections import namedtuple
from enum import Enum
import paramiko


class SshError(Enum):
    Unknown = 0
    CommandExecutionError = 1


class SshResult:
    def __init(self):
        self.data = ""
        self.hasError = False
        self.error = SshError.Unknown
        self.stderr = ""

    @staticmethod
    def Data(data: str):
        result = SshResult()
        result.hasError = False
        result.data = data
        return result

    @staticmethod
    def Error(error: SshError, stderr: str):
        result = SshResult()
        result.error = error
        result.stderr = stderr
        return result


class SshClient:
    def __init__(self):
        host = getenv("SSH_HOST")
        port = getenv("SSH_PORT")
        username = getenv("SSH_USERNAME")
        password = getenv("SSH_PASSWORD")
        privateKeyFilename = getenv("SSH_KEY_FILENAME")

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            key_filename=privateKeyFilename)

    def ExecuteCommand(self, command: str, args: list[str] = []) -> SshResult:
        stdin, stdout, stderr = self.client.exec_command(
            command + " " + commandArgsToExcludedStr(args))

        if stdout.channel.recv_exit_status() != 0:
            return SshResult.Error(
                error=SshError.CommandExecutionError,
                stderr=str(stderr.read().decode("utf8")))

        return SshResult.Data(str(stdout.read().decode("utf8")))

    def Dispose(self):
        self.client.close()
