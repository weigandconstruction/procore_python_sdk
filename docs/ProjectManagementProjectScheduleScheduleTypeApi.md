# procore_sdk.ProjectManagementProjectScheduleScheduleTypeApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_schedule_type_get**](ProjectManagementProjectScheduleScheduleTypeApi.md#rest_v10_schedule_type_get) | **GET** /rest/v1.0/schedule_type | Show the schedule integration type for a project
[**rest_v10_schedule_type_patch**](ProjectManagementProjectScheduleScheduleTypeApi.md#rest_v10_schedule_type_patch) | **PATCH** /rest/v1.0/schedule_type | Update schedule integration type


# **rest_v10_schedule_type_get**
> RestV10ScheduleTypeGet200Response rest_v10_schedule_type_get(procore_company_id, project_id)

Show the schedule integration type for a project

Return information about the schedule integration configuration for the current project.  #### Schedule Types  | Type                                                 | Key                           | |------------------------------------------------------|-------------------------------| | File-based schedule integration via web browser      | \"Microsoft Project\"           | | File-based schedule integration via Procore Drive    | \"Microsoft Project 2010\"      | | File-based schedule integration via Procore Documents| \"Microsoft Project Documents\" | | Primavera P6 database integration via Procore Drive  | \"Primavera P6\"                |  Note that the schedule types listed as \"Microsoft Project\", \"Microsoft Project 2010\", and \"Microsoft Project Documents\" are functionally identical. In all cases Procore can consume any supported schedule file type and extract data from it, not just Microsoft Project. Schedule files can be upoaded either via Procore Drive, via the Procore Documents tool, or via the Procore Schedule tool, regardless of which of these three types is selected. Where Primavera P6 database integration via Procore Drive is in use, the `p6_id` attribute returned by this API indicates which P6 project Procore Drive is extracting data from.  This endpoint has been deprecated. Instead, use [/rest/v1/project/{project_id}/schedule)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_schedule_type_get200_response import RestV10ScheduleTypeGet200Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show the schedule integration type for a project
        api_response = api_instance.rest_v10_schedule_type_get(procore_company_id, project_id)
        print("The response of ProjectManagementProjectScheduleScheduleTypeApi->rest_v10_schedule_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleTypeApi->rest_v10_schedule_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ScheduleTypeGet200Response**](RestV10ScheduleTypeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_schedule_type_patch**
> RestV10ScheduleTypeGet200Response rest_v10_schedule_type_patch(procore_company_id, body16)

Update schedule integration type

Update the schedule integration type for a project.  #### Schedule Types  | Type                                                 | Key                           | |------------------------------------------------------|-------------------------------| | File-based schedule integration via web browser      | \"Microsoft Project\"           | | File-based schedule integration via Procore Drive    | \"Microsoft Project 2010\"      | | File-based schedule integration via Procore Documents| \"Microsoft Project Documents\" | | Primavera P6 database integration via Procore Drive  | \"Primavera P6\"                |  Note that the schedule types listed as \"Microsoft Project\", \"Microsoft Project 2010\", and \"Microsoft Project Documents\" are functionally identical. In all cases Procore can consume any supported schedule file type and extract data from it, not just Microsoft Project. Schedule files can be upoaded either via Procore Drive, via the Procore Documents tool, or via the Procore Schedule tool, regardless of which of these three types is selected. Where Primavera P6 database integration via Procore Drive is in use, the `p6_id` attribute returned by this API indicates which P6 project Procore Drive is extracting data from.  This endpoint has been deprecated. Instead, use [/rest/v1/project/{project_id}/schedule)

### Example


```python
import procore_sdk
from procore_sdk.models.body16 import Body16
from procore_sdk.models.rest_v10_schedule_type_get200_response import RestV10ScheduleTypeGet200Response
from procore_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.procore.com
# See configuration.py for a list of all supported configuration parameters.
configuration = procore_sdk.Configuration(
    host = "https://api.procore.com"
)


# Enter a context with an instance of the API client
with procore_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleTypeApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body16 = procore_sdk.Body16() # Body16 | 

    try:
        # Update schedule integration type
        api_response = api_instance.rest_v10_schedule_type_patch(procore_company_id, body16)
        print("The response of ProjectManagementProjectScheduleScheduleTypeApi->rest_v10_schedule_type_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleTypeApi->rest_v10_schedule_type_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body16** | [**Body16**](Body16.md)|  | 

### Return type

[**RestV10ScheduleTypeGet200Response**](RestV10ScheduleTypeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

