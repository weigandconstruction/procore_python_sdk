# procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_equipment_logs_get**](ProjectManagementDailyLogAdminEquipmentLogsApi.md#rest_v10_projects_project_id_equipment_logs_get) | **GET** /rest/v1.0/projects/{project_id}/equipment_logs | List Equipment Logs
[**rest_v10_projects_project_id_equipment_logs_id_delete**](ProjectManagementDailyLogAdminEquipmentLogsApi.md#rest_v10_projects_project_id_equipment_logs_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/equipment_logs/{id} | Delete Equipment Log
[**rest_v10_projects_project_id_equipment_logs_id_get**](ProjectManagementDailyLogAdminEquipmentLogsApi.md#rest_v10_projects_project_id_equipment_logs_id_get) | **GET** /rest/v1.0/projects/{project_id}/equipment_logs/{id} | Show Equipment Logs
[**rest_v10_projects_project_id_equipment_logs_id_patch**](ProjectManagementDailyLogAdminEquipmentLogsApi.md#rest_v10_projects_project_id_equipment_logs_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/equipment_logs/{id} | Update Equipment Log
[**rest_v10_projects_project_id_equipment_logs_post**](ProjectManagementDailyLogAdminEquipmentLogsApi.md#rest_v10_projects_project_id_equipment_logs_post) | **POST** /rest/v1.0/projects/{project_id}/equipment_logs | Create Equipment Log


# **rest_v10_projects_project_id_equipment_logs_get**
> List[RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner] rest_v10_projects_project_id_equipment_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, per_page=per_page, page=page)

List Equipment Logs

Returns all Equipment Logs for the current date.  See [Working with Daily Logs](https://developers.procore.com/documentation/daily-logs) for information on filtering the response using the log\\_date, start\\_date, and end\\_date parameters. Note that if none of the date parameters are provided in the call, only logs from the current date are returned.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    log_date = '2013-10-20' # date | Date of specific logs desired in YYYY-MM-DD format (optional)
    start_date = '2013-10-20' # date | Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) (optional)
    end_date = '2013-10-20' # date | End date of specific logs desired in YYYY-MM-DD format (use together with start_date) (optional)
    filters_created_by_id = 56 # int | Return item(s) created by the specified User ID (optional)
    filters_location_id = 56 # int | Return item(s) with the specified Location ID. (optional)
    per_page = 56 # int | Elements per page (optional)
    page = 56 # int | Page (optional)

    try:
        # List Equipment Logs
        api_response = api_instance.rest_v10_projects_project_id_equipment_logs_get(procore_company_id, project_id, log_date=log_date, start_date=start_date, end_date=end_date, filters_created_by_id=filters_created_by_id, filters_location_id=filters_location_id, per_page=per_page, page=page)
        print("The response of ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **log_date** | **date**| Date of specific logs desired in YYYY-MM-DD format | [optional] 
 **start_date** | **date**| Start date of specific logs desired in YYYY-MM-DD format (use together with end_date) | [optional] 
 **end_date** | **date**| End date of specific logs desired in YYYY-MM-DD format (use together with start_date) | [optional] 
 **filters_created_by_id** | **int**| Return item(s) created by the specified User ID | [optional] 
 **filters_location_id** | **int**| Return item(s) with the specified Location ID. | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **page** | **int**| Page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner]**](RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_equipment_logs_id_delete**
> rest_v10_projects_project_id_equipment_logs_id_delete(procore_company_id, project_id, id)

Delete Equipment Log

Delete single Equipment Log.

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
    api_instance = procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Equipment Log ID

    try:
        # Delete Equipment Log
        api_instance.rest_v10_projects_project_id_equipment_logs_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Equipment Log ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not delete due to errors |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_equipment_logs_id_get**
> RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_equipment_logs_id_get(procore_company_id, project_id, id)

Show Equipment Logs

Returns single Equipment Log.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Equipment Log ID

    try:
        # Show Equipment Logs
        api_response = api_instance.rest_v10_projects_project_id_equipment_logs_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Equipment Log ID | 

### Return type

[**RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | User does not have right permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_equipment_logs_id_patch**
> RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_equipment_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_equipment_logs_post_request, run_configurable_validations=run_configurable_validations)

Update Equipment Log

Update single Equipment Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_post_request import RestV10ProjectsProjectIdEquipmentLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Equipment Log ID
    rest_v10_projects_project_id_equipment_logs_post_request = procore_sdk.RestV10ProjectsProjectIdEquipmentLogsPostRequest() # RestV10ProjectsProjectIdEquipmentLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_equipment_logs_id_patch(procore_company_id, project_id, id, rest_v10_projects_project_id_equipment_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Equipment Log ID | 
 **rest_v10_projects_project_id_equipment_logs_post_request** | [**RestV10ProjectsProjectIdEquipmentLogsPostRequest**](RestV10ProjectsProjectIdEquipmentLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Can not update due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_equipment_logs_post**
> RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner rest_v10_projects_project_id_equipment_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_equipment_logs_post_request, run_configurable_validations=run_configurable_validations)

Create Equipment Log

Creates single Equipment Log.  #### See - [Daily Log guide](https://developers.procore.com/documentation/daily-logs) - for additional info on * Attachments * Locations

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_get200_response_inner import RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_post_request import RestV10ProjectsProjectIdEquipmentLogsPostRequest
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
    api_instance = procore_sdk.ProjectManagementDailyLogAdminEquipmentLogsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_projects_project_id_equipment_logs_post_request = procore_sdk.RestV10ProjectsProjectIdEquipmentLogsPostRequest() # RestV10ProjectsProjectIdEquipmentLogsPostRequest | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Equipment Log
        api_response = api_instance.rest_v10_projects_project_id_equipment_logs_post(procore_company_id, project_id, rest_v10_projects_project_id_equipment_logs_post_request, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementDailyLogAdminEquipmentLogsApi->rest_v10_projects_project_id_equipment_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_projects_project_id_equipment_logs_post_request** | [**RestV10ProjectsProjectIdEquipmentLogsPostRequest**](RestV10ProjectsProjectIdEquipmentLogsPostRequest.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner**](RestV10ProjectsProjectIdEquipmentLogsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Can not create due to errors |  -  |
**403** | User does not have right permissions |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

