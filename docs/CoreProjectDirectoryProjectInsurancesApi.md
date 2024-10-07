# procore_sdk.CoreProjectDirectoryProjectInsurancesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_insurances_get**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_get) | **GET** /rest/v1.0/projects/{project_id}/insurances | List project insurances
[**rest_v10_projects_project_id_insurances_id_delete**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/insurances/{id} | Delete project insurance
[**rest_v10_projects_project_id_insurances_id_get**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_id_get) | **GET** /rest/v1.0/projects/{project_id}/insurances/{id} | Show project insurance
[**rest_v10_projects_project_id_insurances_id_patch**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/insurances/{id} | Update project insurance
[**rest_v10_projects_project_id_insurances_post**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_post) | **POST** /rest/v1.0/projects/{project_id}/insurances | Create project insurance
[**rest_v10_projects_project_id_insurances_sync_patch**](CoreProjectDirectoryProjectInsurancesApi.md#rest_v10_projects_project_id_insurances_sync_patch) | **PATCH** /rest/v1.0/projects/{project_id}/insurances/sync | Sync Project Insurances


# **rest_v10_projects_project_id_insurances_get**
> List[Insurance] rest_v10_projects_project_id_insurances_get(procore_company_id, project_id, page=page, per_page=per_page)

List project insurances

Return a list of all Insurances associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List project insurances
        api_response = api_instance.rest_v10_projects_project_id_insurances_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Insurance]**](Insurance.md)

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

# **rest_v10_projects_project_id_insurances_id_delete**
> rest_v10_projects_project_id_insurances_id_delete(procore_company_id, project_id, id)

Delete project insurance

Delete the specified Insurance.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Delete project insurance
        api_instance.rest_v10_projects_project_id_insurances_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_insurances_id_get**
> Insurance rest_v10_projects_project_id_insurances_id_get(procore_company_id, project_id, id)

Show project insurance

Return detailed information on the specified Insurance.

### Example


```python
import procore_sdk
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID

    try:
        # Show project insurance
        api_response = api_instance.rest_v10_projects_project_id_insurances_id_get(procore_company_id, project_id, id)
        print("The response of CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 

### Return type

[**Insurance**](Insurance.md)

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

# **rest_v10_projects_project_id_insurances_id_patch**
> Insurance rest_v10_projects_project_id_insurances_id_patch(procore_company_id, project_id, id, body39)

Update project insurance

Update the specified Insurance.

### Example


```python
import procore_sdk
from procore_sdk.models.body39 import Body39
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID
    body39 = procore_sdk.Body39() # Body39 | 

    try:
        # Update project insurance
        api_response = api_instance.rest_v10_projects_project_id_insurances_id_patch(procore_company_id, project_id, id, body39)
        print("The response of CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID | 
 **body39** | [**Body39**](Body39.md)|  | 

### Return type

[**Insurance**](Insurance.md)

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

# **rest_v10_projects_project_id_insurances_post**
> Insurance rest_v10_projects_project_id_insurances_post(procore_company_id, project_id, body39)

Create project insurance

Create a new Insurance associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body39 import Body39
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body39 = procore_sdk.Body39() # Body39 | 

    try:
        # Create project insurance
        api_response = api_instance.rest_v10_projects_project_id_insurances_post(procore_company_id, project_id, body39)
        print("The response of CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body39** | [**Body39**](Body39.md)|  | 

### Return type

[**Insurance**](Insurance.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_insurances_sync_patch**
> ArrayOfProjectInsurances rest_v10_projects_project_id_insurances_sync_patch(procore_company_id, project_id, insurance_sync_body1)

Sync Project Insurances

This endpoint creates or updates a batch of Project Insurances.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_project_insurances import ArrayOfProjectInsurances
from procore_sdk.models.insurance_sync_body1 import InsuranceSyncBody1
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    insurance_sync_body1 = procore_sdk.InsuranceSyncBody1() # InsuranceSyncBody1 | 

    try:
        # Sync Project Insurances
        api_response = api_instance.rest_v10_projects_project_id_insurances_sync_patch(procore_company_id, project_id, insurance_sync_body1)
        print("The response of CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectInsurancesApi->rest_v10_projects_project_id_insurances_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **insurance_sync_body1** | [**InsuranceSyncBody1**](InsuranceSyncBody1.md)|  | 

### Return type

[**ArrayOfProjectInsurances**](ArrayOfProjectInsurances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Project Insurances |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

