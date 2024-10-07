# procore_sdk.ProjectManagementProjectScheduleScheduleIntegrationApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_schedule_integration_download_get**](ProjectManagementProjectScheduleScheduleIntegrationApi.md#rest_v10_schedule_integration_download_get) | **GET** /rest/v1.0/schedule_integration/download | Download schedule file
[**rest_v10_schedule_integration_get**](ProjectManagementProjectScheduleScheduleIntegrationApi.md#rest_v10_schedule_integration_get) | **GET** /rest/v1.0/schedule_integration | List Schedule Imports
[**rest_v10_schedule_integration_patch**](ProjectManagementProjectScheduleScheduleIntegrationApi.md#rest_v10_schedule_integration_patch) | **PATCH** /rest/v1.0/schedule_integration | Upload schedule file
[**rest_v10_schedule_integration_put**](ProjectManagementProjectScheduleScheduleIntegrationApi.md#rest_v10_schedule_integration_put) | **PUT** /rest/v1.0/schedule_integration | Upload schedule file


# **rest_v10_schedule_integration_download_get**
> rest_v10_schedule_integration_download_get(procore_company_id, project_id)

Download schedule file

Download the most recently uploaded schedule file.

### Example


```python
import procore_sdk
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleIntegrationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Download schedule file
        api_instance.rest_v10_schedule_integration_download_get(procore_company_id, project_id)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleIntegrationApi->rest_v10_schedule_integration_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/vnd.ms-project, application/msproj, application/msproject, application/x-msproject, application/x-ms-project, application/x-dos_ms_project, application/mpp, zz-application/zz-winassoc-mpp, application/x-project, application/xer, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_schedule_integration_get**
> List[RestV10ScheduleIntegrationGet200ResponseInner] rest_v10_schedule_integration_get(procore_company_id, project_id, page=page, per_page=per_page)

List Schedule Imports

Return a list of schedule imports for this project, most recent first.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_schedule_integration_get200_response_inner import RestV10ScheduleIntegrationGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleIntegrationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Schedule Imports
        api_response = api_instance.rest_v10_schedule_integration_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementProjectScheduleScheduleIntegrationApi->rest_v10_schedule_integration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleIntegrationApi->rest_v10_schedule_integration_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ScheduleIntegrationGet200ResponseInner]**](RestV10ScheduleIntegrationGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_schedule_integration_patch**
> rest_v10_schedule_integration_patch(procore_company_id, project_id, schedule_integration)

Upload schedule file

DEPRECATED: This endpoint is a duplicate of the `PUT` endpoint. It will be removed in a future version of the API. Use the `PUT` method instead.  Upload a schedule file.  #### Supported File Formats  | Type | Source                                                        | |------|---------------------------------------------------------------| | MPP  | Microsoft Project                                             | | MPX  | Microsoft Project, SureTrak                                   | | XER  | Primavera P6, Primavera Contractor                            | | PP   | Asta Powerproject, Asta Easyplan                              | | XML  | Formatted for Microsoft Project, e.g. Smartsheet, OpenProject | | XML  | Primavera PMXML                                               | | PPX  | Phoenix Project Manager                                       | | FTS  | FastTrack Schedule                                            | | POD  | ProjectLibre                                                  | | GAN  | GanttProject                                                  | | PEP  | TurboProject                                                  | | PRX  | Primavera P3                                                  | | STX  | Primavera SureTrak                                            | | CDPX | ConceptDraw PROJECT                                           | | CDPZ | ConceptDraw PROJECT                                           | | SP   | Synchro Scheduler                                             | | SEDF | USACE Standard Data Exchange Format                           | | ZIP  | Compressed file containing one of the supported file types    |

### Example


```python
import procore_sdk
from procore_sdk.models.schedule_integration import ScheduleIntegration
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleIntegrationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_integration = procore_sdk.ScheduleIntegration() # ScheduleIntegration | 

    try:
        # Upload schedule file
        api_instance.rest_v10_schedule_integration_patch(procore_company_id, project_id, schedule_integration)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleIntegrationApi->rest_v10_schedule_integration_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **schedule_integration** | [**ScheduleIntegration**](ScheduleIntegration.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

# **rest_v10_schedule_integration_put**
> rest_v10_schedule_integration_put(procore_company_id, project_id, schedule_integration)

Upload schedule file

Upload a schedule file.  #### Supported File Formats  | Type | Source                                                        | |------|---------------------------------------------------------------| | MPP  | Microsoft Project                                             | | MPX  | Microsoft Project, SureTrak                                   | | XER  | Primavera P6, Primavera Contractor                            | | PP   | Asta Powerproject, Asta Easyplan                              | | XML  | Formatted for Microsoft Project, e.g. Smartsheet, OpenProject | | XML  | Primavera PMXML                                               | | PPX  | Phoenix Project Manager                                       | | FTS  | FastTrack Schedule                                            | | POD  | ProjectLibre                                                  | | GAN  | GanttProject                                                  | | PEP  | TurboProject                                                  | | PRX  | Primavera P3                                                  | | STX  | Primavera SureTrak                                            | | CDPX | ConceptDraw PROJECT                                           | | CDPZ | ConceptDraw PROJECT                                           | | SP   | Synchro Scheduler                                             | | SEDF | USACE Standard Data Exchange Format                           | | ZIP  | Compressed file containing one of the supported file types    |

### Example


```python
import procore_sdk
from procore_sdk.models.schedule_integration import ScheduleIntegration
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
    api_instance = procore_sdk.ProjectManagementProjectScheduleScheduleIntegrationApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    schedule_integration = procore_sdk.ScheduleIntegration() # ScheduleIntegration | 

    try:
        # Upload schedule file
        api_instance.rest_v10_schedule_integration_put(procore_company_id, project_id, schedule_integration)
    except Exception as e:
        print("Exception when calling ProjectManagementProjectScheduleScheduleIntegrationApi->rest_v10_schedule_integration_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **schedule_integration** | [**ScheduleIntegration**](ScheduleIntegration.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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

