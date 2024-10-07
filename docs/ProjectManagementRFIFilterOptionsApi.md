# procore_sdk.ProjectManagementRFIFilterOptionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_rfis_filter_options_assigned_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_assigned_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/assigned_id | List available RFI assigned_id filter options
[**rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/ball_in_court_id | List available RFI ball in court filter options
[**rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/cost_code_id | List available RFI cost code options
[**rest_v10_projects_project_id_rfis_filter_options_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options | List available RFI filters
[**rest_v10_projects_project_id_rfis_filter_options_location_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_location_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/location_id | List available RFIs locations
[**rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/prefix_stage_id | List available RFI Prefix Stage filter options
[**rest_v10_projects_project_id_rfis_filter_options_priority_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_priority_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/priority | List available RFI Priority filter options
[**rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/received_from_login_information_id | List available RFI received from filter options
[**rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/responsible_contractor_id | List available RFI responsible contractor filter options
[**rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/rfi_manager_id | List available RFI RFI Manager filter options
[**rest_v10_projects_project_id_rfis_filter_options_status_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_status_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/status | List available RFI status filter options
[**rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get**](ProjectManagementRFIFilterOptionsApi.md#rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/filter_options/sub_job_id | List available RFI Sub Job filter options


# **rest_v10_projects_project_id_rfis_filter_options_assigned_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_assigned_id_get(procore_company_id, project_id)

List available RFI assigned_id filter options

Returns a list of assigned_id filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI assigned_id filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_assigned_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_assigned_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_assigned_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsBallInCourtIdGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get(procore_company_id, project_id)

List available RFI ball in court filter options

Returns a list of available RFI ball in court filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsBallInCourtIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI ball in court filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_ball_in_court_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsBallInCourtIdGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsBallInCourtIdGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get(procore_company_id, project_id)

List available RFI cost code options

Returns a list of RFI cost code options for a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI cost code options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_cost_code_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_get**
> RestV10ProjectsProjectIdRfisFilterOptionsGet200Response rest_v10_projects_project_id_rfis_filter_options_get(procore_company_id, project_id)

List available RFI filters

Returns a list of filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_get200_response import RestV10ProjectsProjectIdRfisFilterOptionsGet200Response
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI filters
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10ProjectsProjectIdRfisFilterOptionsGet200Response**](RestV10ProjectsProjectIdRfisFilterOptionsGet200Response.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_location_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_location_id_get(procore_company_id, project_id)

List available RFIs locations

Returns a list of RFI locations for a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFIs locations
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_location_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_location_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_location_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsPrefixStageIdGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get(procore_company_id, project_id)

List available RFI Prefix Stage filter options

Returns all Filter Options for Prefix Stage defined by the project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsPrefixStageIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI Prefix Stage filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_prefix_stage_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsPrefixStageIdGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsPrefixStageIdGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_priority_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_priority_get(procore_company_id, project_id)

List available RFI Priority filter options

Returns a list of available Priority options for RFIs

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_priority_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI Priority filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_priority_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_priority_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_priority_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsPriorityGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get(procore_company_id, project_id)

List available RFI received from filter options

Returns a list of received from filter options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI received from filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_received_from_login_information_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get(procore_company_id, project_id)

List available RFI responsible contractor filter options

Returns a list of responsible contractor filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI responsible contractor filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_responsible_contractor_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsRfiManagerIdGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get(procore_company_id, project_id)

List available RFI RFI Manager filter options

Returns a list of available RFI Manager filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsRfiManagerIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI RFI Manager filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_rfi_manager_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsRfiManagerIdGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsRfiManagerIdGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_status_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_status_get(procore_company_id, project_id)

List available RFI status filter options

Returns a list of status filter fields and options for RFIs on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_status_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI status filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_status_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsStatusGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get**
> List[RestV10ProjectsProjectIdRfisFilterOptionsSubJobIdGet200ResponseInner] rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get(procore_company_id, project_id)

List available RFI Sub Job filter options

Returns all Filter Options for Sub Jobs defined by the project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get200_response_inner import RestV10ProjectsProjectIdRfisFilterOptionsSubJobIdGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIFilterOptionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.

    try:
        # List available RFI Sub Job filter options
        api_response = api_instance.rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get(procore_company_id, project_id)
        print("The response of ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIFilterOptionsApi->rest_v10_projects_project_id_rfis_filter_options_sub_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10ProjectsProjectIdRfisFilterOptionsSubJobIdGet200ResponseInner]**](RestV10ProjectsProjectIdRfisFilterOptionsSubJobIdGet200ResponseInner.md)

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

