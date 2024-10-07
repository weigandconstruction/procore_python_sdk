# procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_timecards/bulk_create | Bulk Create Time and material timecards
[**rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_timecards/bulk_destroy | Bulk Delete Time and material timecards
[**rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_timecards/bulk_update | Bulk Update Time and material timecards
[**rest_v10_projects_project_id_time_and_material_timecards_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_timecards | List Time And Material Timecards
[**rest_v10_projects_project_id_time_and_material_timecards_id_delete**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/time_and_material_timecards/{id} | Delete Time And Material Timecard
[**rest_v10_projects_project_id_time_and_material_timecards_id_get**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_id_get) | **GET** /rest/v1.0/projects/{project_id}/time_and_material_timecards/{id} | Show Time And Material Timecard
[**rest_v10_projects_project_id_time_and_material_timecards_id_patch**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/time_and_material_timecards/{id} | Update Time And Material Timecard
[**rest_v10_projects_project_id_time_and_material_timecards_post**](FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi.md#rest_v10_projects_project_id_time_and_material_timecards_post) | **POST** /rest/v1.0/projects/{project_id}/time_and_material_timecards | Create Time And Material Timecard


# **rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post**
> List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post(procore_company_id, project_id, time_and_material_timecard_bulk_create_body)

Bulk Create Time and material timecards

Bulk create Time and material timecards with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
from procore_sdk.models.time_and_material_timecard_bulk_create_body import TimeAndMaterialTimecardBulkCreateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_timecard_bulk_create_body = procore_sdk.TimeAndMaterialTimecardBulkCreateBody() # TimeAndMaterialTimecardBulkCreateBody | 

    try:
        # Bulk Create Time and material timecards
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post(procore_company_id, project_id, time_and_material_timecard_bulk_create_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_timecard_bulk_create_body** | [**TimeAndMaterialTimecardBulkCreateBody**](TimeAndMaterialTimecardBulkCreateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete**
> List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete(procore_company_id, project_id, time_and_material_timecard_bulk_destroy_body)

Bulk Delete Time and material timecards

Bulk delete Time and material timecards with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
from procore_sdk.models.time_and_material_timecard_bulk_destroy_body import TimeAndMaterialTimecardBulkDestroyBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_timecard_bulk_destroy_body = procore_sdk.TimeAndMaterialTimecardBulkDestroyBody() # TimeAndMaterialTimecardBulkDestroyBody | 

    try:
        # Bulk Delete Time and material timecards
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete(procore_company_id, project_id, time_and_material_timecard_bulk_destroy_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_destroy_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_timecard_bulk_destroy_body** | [**TimeAndMaterialTimecardBulkDestroyBody**](TimeAndMaterialTimecardBulkDestroyBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch**
> List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch(procore_company_id, project_id, time_and_material_timecard_bulk_update_body)

Bulk Update Time and material timecards

Bulk update Time and material timecards with one request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
from procore_sdk.models.time_and_material_timecard_bulk_update_body import TimeAndMaterialTimecardBulkUpdateBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_timecard_bulk_update_body = procore_sdk.TimeAndMaterialTimecardBulkUpdateBody() # TimeAndMaterialTimecardBulkUpdateBody | 

    try:
        # Bulk Update Time and material timecards
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch(procore_company_id, project_id, time_and_material_timecard_bulk_update_body)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_bulk_update_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_timecard_bulk_update_body** | [**TimeAndMaterialTimecardBulkUpdateBody**](TimeAndMaterialTimecardBulkUpdateBody.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_get**
> List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner] rest_v10_projects_project_id_time_and_material_timecards_get(procore_company_id, project_id, page=page, per_page=per_page)

List Time And Material Timecards

Return a list of all Time And Material Timecards

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Time And Material Timecards
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner]**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_id_delete**
> RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner rest_v10_projects_project_id_time_and_material_timecards_id_delete(procore_company_id, id, project_id)

Delete Time And Material Timecard

Detete a specific Time And Material Timecard.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project to get the time and material timecards for
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Time And Material Timecard
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_id_delete(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project to get the time and material timecards for | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_id_get**
> RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner rest_v10_projects_project_id_time_and_material_timecards_id_get(procore_company_id, id, project_id)

Show Time And Material Timecard

Return detailed information about a specific Time And Material Timecard.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project to get the time and material timecards for
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Time And Material Timecard
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_id_get(procore_company_id, id, project_id)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project to get the time and material timecards for | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_id_patch**
> RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner rest_v10_projects_project_id_time_and_material_timecards_id_patch(procore_company_id, id, project_id, time_and_material_timecard_body, run_configurable_validations=run_configurable_validations)

Update Time And Material Timecard

Update a specified Time And Material Timecard.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
from procore_sdk.models.time_and_material_timecard_body import TimeAndMaterialTimecardBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID of the project to get the time and material timecards for
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_timecard_body = procore_sdk.TimeAndMaterialTimecardBody() # TimeAndMaterialTimecardBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update Time And Material Timecard
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_id_patch(procore_company_id, id, project_id, time_and_material_timecard_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID of the project to get the time and material timecards for | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_timecard_body** | [**TimeAndMaterialTimecardBody**](TimeAndMaterialTimecardBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_time_and_material_timecards_post**
> RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner rest_v10_projects_project_id_time_and_material_timecards_post(procore_company_id, project_id, time_and_material_timecard_body, run_configurable_validations=run_configurable_validations)

Create Time And Material Timecard

Create a new Time And Material Timecard Entry.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_timecards_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner
from procore_sdk.models.time_and_material_timecard_body import TimeAndMaterialTimecardBody
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
    api_instance = procore_sdk.FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    time_and_material_timecard_body = procore_sdk.TimeAndMaterialTimecardBody() # TimeAndMaterialTimecardBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create Time And Material Timecard
        api_response = api_instance.rest_v10_projects_project_id_time_and_material_timecards_post(procore_company_id, project_id, time_and_material_timecard_body, run_configurable_validations=run_configurable_validations)
        print("The response of FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FieldProductivityTimeAndMaterialsTimeAndMaterialTimecardApi->rest_v10_projects_project_id_time_and_material_timecards_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **time_and_material_timecard_body** | [**TimeAndMaterialTimecardBody**](TimeAndMaterialTimecardBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner**](RestV10ProjectsProjectIdTimeAndMaterialTimecardsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

