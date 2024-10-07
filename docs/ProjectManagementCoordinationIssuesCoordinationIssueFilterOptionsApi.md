# procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_coordination_issues_filter_options_assignee_company_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_assignee_company_id_get) | **GET** /rest/v1.0/coordination_issues/filter_options/assignee_company_id | List Assignee Company Filter Options
[**rest_v10_coordination_issues_filter_options_assignee_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_assignee_id_get) | **GET** /rest/v1.0/coordination_issues/filter_options/assignee_id | List Assignee Filter Options
[**rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get) | **GET** /rest/v1.0/coordination_issues/filter_options/coordination_issue_file_id | List Coordination Issue File Filter Options
[**rest_v10_coordination_issues_filter_options_created_by_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_created_by_id_get) | **GET** /rest/v1.0/coordination_issues/filter_options/created_by_id | List Creator Filter Options
[**rest_v10_coordination_issues_filter_options_created_from_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_created_from_get) | **GET** /rest/v1.0/coordination_issues/filter_options/created_from | List Creation Source Filter Options
[**rest_v10_coordination_issues_filter_options_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_get) | **GET** /rest/v1.0/coordination_issues/filter_options | List Available Filters for Coordination Issues
[**rest_v10_coordination_issues_filter_options_location_id_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_location_id_get) | **GET** /rest/v1.0/coordination_issues/filter_options/location_id | List Location Filter Options
[**rest_v10_coordination_issues_filter_options_status_get**](ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi.md#rest_v10_coordination_issues_filter_options_status_get) | **GET** /rest/v1.0/coordination_issues/filter_options/status | List Status Filter Options


# **rest_v10_coordination_issues_filter_options_assignee_company_id_get**
> List[RestV10CoordinationIssuesFilterOptionsAssigneeCompanyIdGet200ResponseInner] rest_v10_coordination_issues_filter_options_assignee_company_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)

List Assignee Company Filter Options

Returns a list of available assignee vendor filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_assignee_company_id_get200_response_inner import RestV10CoordinationIssuesFilterOptionsAssigneeCompanyIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)

    try:
        # List Assignee Company Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_assignee_company_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_assignee_company_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_assignee_company_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsAssigneeCompanyIdGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsAssigneeCompanyIdGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_assignee_id_get**
> List[RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner] rest_v10_coordination_issues_filter_options_assignee_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)

List Assignee Filter Options

Returns a list of available assignee filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_assignee_id_get200_response_inner import RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)

    try:
        # List Assignee Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_assignee_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_assignee_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_assignee_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get**
> List[RestV10CoordinationIssuesFilterOptionsCoordinationIssueFileIdGet200ResponseInner] rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get(procore_company_id, project_id)

List Coordination Issue File Filter Options

Returns a list of available source file filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get200_response_inner import RestV10CoordinationIssuesFilterOptionsCoordinationIssueFileIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Coordination Issue File Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_coordination_issue_file_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsCoordinationIssueFileIdGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsCoordinationIssueFileIdGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_created_by_id_get**
> List[RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner] rest_v10_coordination_issues_filter_options_created_by_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)

List Creator Filter Options

Returns a list of available creator filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_assignee_id_get200_response_inner import RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)

    try:
        # List Creator Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_created_by_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_created_by_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_created_by_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsAssigneeIdGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_created_from_get**
> List[RestV10CoordinationIssuesFilterOptionsCreatedFromGet200ResponseInner] rest_v10_coordination_issues_filter_options_created_from_get(procore_company_id, project_id)

List Creation Source Filter Options

Returns a list of available creation source filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_created_from_get200_response_inner import RestV10CoordinationIssuesFilterOptionsCreatedFromGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Creation Source Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_created_from_get(procore_company_id, project_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_created_from_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_created_from_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsCreatedFromGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsCreatedFromGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_get**
> List[RestV10CoordinationIssuesFilterOptionsGet200ResponseInner] rest_v10_coordination_issues_filter_options_get(procore_company_id, project_id)

List Available Filters for Coordination Issues

This endpoint returns filters that are available to filter Coordination Issues an array of objects

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_get200_response_inner import RestV10CoordinationIssuesFilterOptionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List Available Filters for Coordination Issues
        api_response = api_instance.rest_v10_coordination_issues_filter_options_get(procore_company_id, project_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_location_id_get**
> List[RestV10CoordinationIssuesFilterOptionsLocationIdGet200ResponseInner] rest_v10_coordination_issues_filter_options_location_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)

List Location Filter Options

Returns a list of available location filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_location_id_get200_response_inner import RestV10CoordinationIssuesFilterOptionsLocationIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)

    try:
        # List Location Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_location_id_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_location_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_location_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsLocationIdGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsLocationIdGet200ResponseInner.md)

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

# **rest_v10_coordination_issues_filter_options_status_get**
> List[RestV10CoordinationIssuesFilterOptionsStatusGet200ResponseInner] rest_v10_coordination_issues_filter_options_status_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)

List Status Filter Options

Returns a list of available status filters that can be used to filter Coordination Issues

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_coordination_issues_filter_options_status_get200_response_inner import RestV10CoordinationIssuesFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_bim_file_id = 56 # int | Filter item(s) with matching BIM File ids (optional)

    try:
        # List Status Filter Options
        api_response = api_instance.rest_v10_coordination_issues_filter_options_status_get(procore_company_id, project_id, filters_bim_file_id=filters_bim_file_id)
        print("The response of ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementCoordinationIssuesCoordinationIssueFilterOptionsApi->rest_v10_coordination_issues_filter_options_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_bim_file_id** | **int**| Filter item(s) with matching BIM File ids | [optional] 

### Return type

[**List[RestV10CoordinationIssuesFilterOptionsStatusGet200ResponseInner]**](RestV10CoordinationIssuesFilterOptionsStatusGet200ResponseInner.md)

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

