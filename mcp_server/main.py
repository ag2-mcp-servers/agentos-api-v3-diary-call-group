# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T04:14:42+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity, HTTPBasic
from fastapi import Path, Query
from starlette.requests import Request

from models import (
    AdvertisingBranchModel,
    AdvertisingBranchModelResults,
    AppointmentTypesToSearch,
    DiaryAppointmentDetails,
    DiaryAppointmentModel,
    DiaryAppointmentModelResults,
    DiaryAppointmentTypeModelResults,
    FeedbackSubmissionModel,
    GuestDiaryParametersResultsModel,
    PropertyIdentifier,
    V3DiaryShortNameAllocationsGetResponse,
)

app = MCPProxy(
    contact={'x-twitter': 'agentOSSoftware'},
    title='agentOS API V3, Diary Call Group',
    version='v3-diary',
    servers=[{'url': 'https://live-api.letmc.com'}],
)


@app.get('/v3/diary/{shortName}/allocations', tags=['appointment_query_filters'])
def diary_controller__get_allocations(
    short_name: str = Path(..., alias='shortName'),
    preferred_date: datetime = Query(..., alias='preferredDate'),
    appointment_type: str = Query(..., alias='appointmentType'),
    lettings: Optional[bool] = None,
    property_identifier: Optional[str] = Query(None, alias='propertyIdentifier'),
    branch_i_d: Optional[str] = Query(None, alias='branchID'),
):
    """
    Get a list of all available allocations for a date + 7 days for a specified appointment type
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete('/v3/diary/{shortName}/appointment', tags=['appointment_management'])
def diary_controller__delete_appointment(
    short_name: str = Path(..., alias='shortName'),
    appointment_i_d: str = Query(..., alias='appointmentID'),
):
    """
    Delete an existing appointment using its unique identifier
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/v3/diary/{shortName}/appointment', tags=['appointment_management'])
def diary_controller__get_appointment(
    short_name: str = Path(..., alias='shortName'),
    appointment_i_d: str = Query(..., alias='appointmentID'),
):
    """
    Get an appointment by ID
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post('/v3/diary/{shortName}/appointment', tags=['appointment_management'])
def diary_controller__post_appointment(
    short_name: str = Path(..., alias='shortName'),
    property_identifier: PropertyIdentifier = Query(..., alias='propertyIdentifier'),
    lettings: Optional[bool] = None,
    body: DiaryAppointmentDetails = ...,
):
    """
    Post an appointment into a valid diary allocation
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put('/v3/diary/{shortName}/appointment', tags=['appointment_management'])
def diary_controller__put_appointment(
    short_name: str = Path(..., alias='shortName'),
    appointment_i_d: str = Query(..., alias='appointmentID'),
    lettings: Optional[bool] = None,
    allow_marketing_correspondence: Optional[bool] = Query(
        None, alias='AllowMarketingCorrespondence'
    ),
    body: DiaryAppointmentDetails = ...,
):
    """
    Update an existing appointment using its unique identifier
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v3/diary/{shortName}/appointment/feedback', tags=['appointment_feedback_handling']
)
def diary_controller__add_feedback(
    short_name: str = Path(..., alias='shortName'), body: FeedbackSubmissionModel = ...
):
    """
    Submit appointment feedback
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/v3/diary/{shortName}/appointment/{appointmentID}/cancel',
    tags=['appointment_management'],
)
def diary_controller__cancel_appointment(
    short_name: str = Path(..., alias='shortName'),
    appointment_i_d: str = Path(..., alias='appointmentID'),
):
    """
    Cancel an existing appointment using its unique identifier
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v3/diary/{shortName}/appointmentsbetweendates',
    tags=['appointment_query_filters', 'company_branch_operations'],
)
def diary_controller__get_appointments_between_dates(
    short_name: str = Path(..., alias='shortName'),
    branch_i_d: str = Query(..., alias='branchID'),
    start_date: datetime = Query(..., alias='startDate'),
    end_date: datetime = Query(..., alias='endDate'),
    appointment_types_to_search: AppointmentTypesToSearch = Query(
        ..., alias='appointmentTypesToSearch'
    ),
    offset: int = ...,
    count: int = ...,
):
    """
    A collection of diary appointments linked to a company filtered between specific dates and by appointment type
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/v3/diary/{shortName}/appointmenttypes', tags=['appointment_query_filters'])
def diary_controller__get_appointment_types(
    short_name: str = Path(..., alias='shortName'), offset: int = ..., count: int = ...
):
    """
    A collection of all diary appointment types
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/v3/diary/{shortName}/company/branches', tags=['company_branch_operations'])
def company_controller__get_branches(
    short_name: str = Path(..., alias='shortName'), offset: int = ..., count: int = ...
):
    """
    All branches defined for a company
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v3/diary/{shortName}/company/branches/{branchID}',
    tags=['company_branch_operations'],
)
def get_v3_diary__short_name_company_branches__branch_i_d(
    short_name: str = Path(..., alias='shortName'),
    branch_i_d: str = Path(..., alias='branchID'),
):
    """
    Get a specific branch given its unique Object ID (OID)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v3/diary/{shortName}/recurringappointment',
    tags=['appointment_management', 'appointment_query_filters'],
)
def diary_controller__get_recurring_appointments(
    short_name: str = Path(..., alias='shortName'),
    branch_i_d: str = Query(..., alias='branchID'),
    appointment_types_to_search: AppointmentTypesToSearch = Query(
        ..., alias='appointmentTypesToSearch'
    ),
    offset: int = ...,
    count: int = ...,
):
    """
    Retrieves all recurring appointments:-
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v3/diary/{shortname}/{branchID}/guest/search', tags=['guest_application_matching']
)
def diary_controller__search_guest(
    shortname: str,
    branch_i_d: str = Path(..., alias='branchID'),
    forename: str = ...,
    emailaddress: str = ...,
    surname: str = ...,
    offset: int = ...,
    count: int = ...,
):
    """
    Match Guest Parameters with existing applicants
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
