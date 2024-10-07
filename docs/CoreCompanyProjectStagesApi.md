# procore_sdk.CoreCompanyProjectStagesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_project_stages_get**](CoreCompanyProjectStagesApi.md#rest_v10_companies_company_id_project_stages_get) | **GET** /rest/v1.0/companies/{company_id}/project_stages | List Project Stages
[**rest_v10_companies_company_id_project_stages_id_delete**](CoreCompanyProjectStagesApi.md#rest_v10_companies_company_id_project_stages_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/project_stages/{id} | Delete project stage
[**rest_v10_companies_company_id_project_stages_id_get**](CoreCompanyProjectStagesApi.md#rest_v10_companies_company_id_project_stages_id_get) | **GET** /rest/v1.0/companies/{company_id}/project_stages/{id} | Show project stage
[**rest_v10_companies_company_id_project_stages_id_patch**](CoreCompanyProjectStagesApi.md#rest_v10_companies_company_id_project_stages_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/project_stages/{id} | Update project stage
[**rest_v10_companies_company_id_project_stages_post**](CoreCompanyProjectStagesApi.md#rest_v10_companies_company_id_project_stages_post) | **POST** /rest/v1.0/companies/{company_id}/project_stages | Create project stage


# **rest_v10_companies_company_id_project_stages_get**
> List[ProjectStage2] rest_v10_companies_company_id_project_stages_get(procore_company_id, company_id, page=page, per_page=per_page, project_id=project_id)

List Project Stages

Return a list of Project Stages.

### Example


```python
import procore_sdk
from procore_sdk.models.project_stage2 import ProjectStage2
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
    api_instance = procore_sdk.CoreCompanyProjectStagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    project_id = 56 # int | Project ID is required if retrieving a list of project stages for RFI users (optional)

    try:
        # List Project Stages
        api_response = api_instance.rest_v10_companies_company_id_project_stages_get(procore_company_id, company_id, page=page, per_page=per_page, project_id=project_id)
        print("The response of CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **project_id** | **int**| Project ID is required if retrieving a list of project stages for RFI users | [optional] 

### Return type

[**List[ProjectStage2]**](ProjectStage2.md)

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

# **rest_v10_companies_company_id_project_stages_id_delete**
> rest_v10_companies_company_id_project_stages_id_delete(procore_company_id, company_id, id)

Delete project stage

Delete the specified Project Stage.

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
    api_instance = procore_sdk.CoreCompanyProjectStagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project stage

    try:
        # Delete project stage
        api_instance.rest_v10_companies_company_id_project_stages_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project stage | 

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

# **rest_v10_companies_company_id_project_stages_id_get**
> ProjectStage2 rest_v10_companies_company_id_project_stages_id_get(procore_company_id, company_id, id)

Show project stage

Show detail on a specified Project Stage.

### Example


```python
import procore_sdk
from procore_sdk.models.project_stage2 import ProjectStage2
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
    api_instance = procore_sdk.CoreCompanyProjectStagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project stage

    try:
        # Show project stage
        api_response = api_instance.rest_v10_companies_company_id_project_stages_id_get(procore_company_id, company_id, id)
        print("The response of CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project stage | 

### Return type

[**ProjectStage2**](ProjectStage2.md)

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

# **rest_v10_companies_company_id_project_stages_id_patch**
> ProjectStage2 rest_v10_companies_company_id_project_stages_id_patch(procore_company_id, company_id, id, body35)

Update project stage

Update the specified Project Stage.

### Example


```python
import procore_sdk
from procore_sdk.models.body35 import Body35
from procore_sdk.models.project_stage2 import ProjectStage2
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
    api_instance = procore_sdk.CoreCompanyProjectStagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | ID of the project stage
    body35 = procore_sdk.Body35() # Body35 | 

    try:
        # Update project stage
        api_response = api_instance.rest_v10_companies_company_id_project_stages_id_patch(procore_company_id, company_id, id, body35)
        print("The response of CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| ID of the project stage | 
 **body35** | [**Body35**](Body35.md)|  | 

### Return type

[**ProjectStage2**](ProjectStage2.md)

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

# **rest_v10_companies_company_id_project_stages_post**
> ProjectStage2 rest_v10_companies_company_id_project_stages_post(procore_company_id, company_id, body35)

Create project stage

Create a new Project Stage in the specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.body35 import Body35
from procore_sdk.models.project_stage2 import ProjectStage2
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
    api_instance = procore_sdk.CoreCompanyProjectStagesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    body35 = procore_sdk.Body35() # Body35 | 

    try:
        # Create project stage
        api_response = api_instance.rest_v10_companies_company_id_project_stages_post(procore_company_id, company_id, body35)
        print("The response of CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreCompanyProjectStagesApi->rest_v10_companies_company_id_project_stages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **body35** | [**Body35**](Body35.md)|  | 

### Return type

[**ProjectStage2**](ProjectStage2.md)

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

