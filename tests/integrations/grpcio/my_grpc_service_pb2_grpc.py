# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import warnings

import grpc

from . import my_grpc_service_pb2 as my__grpc__service__pb2

GRPC_GENERATED_VERSION = "1.64.1"
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = "1.65.0"
SCHEDULED_RELEASE_DATE = "June 25, 2024"
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION,
        GRPC_GENERATED_VERSION,
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(  # noqa: B028
        f"The grpc package installed is at version {GRPC_VERSION},"  # noqa: ISC003
        + " but the generated code in my_grpc_service_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"  # noqa: E501
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."  # noqa: E501
        + f" This warning will become an error in {EXPECTED_ERROR_RELEASE},"
        + f" scheduled for release on {SCHEDULED_RELEASE_DATE}.",
        RuntimeWarning,
    )


class MyServiceStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MyMethod = channel.unary_unary(
            "/my_grpc_service.MyService/MyMethod",
            request_serializer=my__grpc__service__pb2.MyRequest.SerializeToString,
            response_deserializer=my__grpc__service__pb2.MyResponse.FromString,
            _registered_method=True,
        )


class MyServiceServicer:
    """Missing associated documentation comment in .proto file."""

    def MyMethod(self, request, context):  # noqa: N802
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MyServiceServicer_to_server(servicer, server):  # noqa: N802
    rpc_method_handlers = {
        "MyMethod": grpc.unary_unary_rpc_method_handler(
            servicer.MyMethod,
            request_deserializer=my__grpc__service__pb2.MyRequest.FromString,
            response_serializer=my__grpc__service__pb2.MyResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "my_grpc_service.MyService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "my_grpc_service.MyService",
        rpc_method_handlers,
    )


# This class is part of an EXPERIMENTAL API.
class MyService:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MyMethod(  # noqa: N802
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,  # noqa: FBT002
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/my_grpc_service.MyService/MyMethod",
            my__grpc__service__pb2.MyRequest.SerializeToString,
            my__grpc__service__pb2.MyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
