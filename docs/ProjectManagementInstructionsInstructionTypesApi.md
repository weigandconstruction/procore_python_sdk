# procore_sdk.ProjectManagementInstructionsInstructionTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_instruction_types_get**](ProjectManagementInstructionsInstructionTypesApi.md#rest_v10_projects_project_id_instruction_types_get) | **GET** /rest/v1.0/projects/{project_id}/instruction_types | List Instruction Types on a project
[**rest_v10_projects_project_id_instruction_types_id_delete**](ProjectManagementInstructionsInstructionTypesApi.md#rest_v10_projects_project_id_instruction_types_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/instruction_types/{id} | Delete Instruction Type
[**rest_v10_projects_project_id_instruction_types_id_get**](ProjectManagementInstructionsInstructionTypesApi.md#rest_v10_projects_project_id_instruction_types_id_get) | **GET** /rest/v1.0/projects/{project_id}/instruction_types/{id} | Show Instruction Type
[**rest_v10_projects_project_id_instruction_types_id_patch**](ProjectManagementInstructionsInstructionTypesApi.md#rest_v10_projects_project_id_instruction_types_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/instruction_types/{id} | Update Instruction Type
[**rest_v10_projects_project_id_instruction_types_post**](ProjectManagementInstructionsInstructionTypesApi.md#rest_v10_projects_project_id_instruction_types_post) | **POST** /rest/v1.0/projects/{project_id}/instruction_types | Create Instruction Types


# **rest_v10_projects_project_id_instruction_types_get**
> List[RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType] rest_v10_projects_project_id_instruction_types_get(procore_company_id, project_id, page=page, per_page=per_page)

List Instruction Types on a project

Return a list of all Instruction Types from a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner_instruction_type import RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Instruction Types on a project
        api_response = api_instance.rest_v10_projects_project_id_instruction_types_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType]**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instruction Types listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instruction_types_id_delete**
> rest_v10_projects_project_id_instruction_types_id_delete(procore_company_id, project_id, id)

Delete Instruction Type

Delete the specified Instruction Type.

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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID

    try:
        # Delete Instruction Type
        api_instance.rest_v10_projects_project_id_instruction_types_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Instruction ID | 

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
**200** | Instruction deleted successfully |  -  |
**403** | User does not have permission to delete Instruction Type |  -  |
**404** | Instruction Type not found |  -  |
**500** | Error deleting Instruction Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instruction_types_id_get**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType rest_v10_projects_project_id_instruction_types_id_get(procore_company_id, project_id, id)

Show Instruction Type

Return detailed information on the specified Instruction Type.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner_instruction_type import RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID

    try:
        # Show Instruction Type
        api_response = api_instance.rest_v10_projects_project_id_instruction_types_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Instruction ID | 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instruction Type shown successfully |  -  |
**403** | User does not have permission to view Instruction |  -  |
**404** | Instruction Type not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instruction_types_id_patch**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType rest_v10_projects_project_id_instruction_types_id_patch(procore_company_id, project_id, id, body76)

Update Instruction Type

Update the specified Instruction Type.

### Example


```python
import procore_sdk
from procore_sdk.models.body76 import Body76
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner_instruction_type import RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID
    body76 = procore_sdk.Body76() # Body76 | 

    try:
        # Update Instruction Type
        api_response = api_instance.rest_v10_projects_project_id_instruction_types_id_patch(procore_company_id, project_id, id, body76)
        print("The response of ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Instruction ID | 
 **body76** | [**Body76**](Body76.md)|  | 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instruction Type updated successfully |  -  |
**403** | User does not have permission to update Instruction Type |  -  |
**404** | Instruction Type not found |  -  |
**422** | Error updating Instruction Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instruction_types_post**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType rest_v10_projects_project_id_instruction_types_post(procore_company_id, project_id, body76)

Create Instruction Types

Create a new Instruction Type associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body76 import Body76
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner_instruction_type import RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body76 = procore_sdk.Body76() # Body76 | 

    try:
        # Create Instruction Types
        api_response = api_instance.rest_v10_projects_project_id_instruction_types_post(procore_company_id, project_id, body76)
        print("The response of ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionTypesApi->rest_v10_projects_project_id_instruction_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body76** | [**Body76**](Body76.md)|  | 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType**](RestV10ProjectsProjectIdInstructionsGet200ResponseInnerInstructionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Instruction Type created successfully |  -  |
**403** | User does not have permission to create Instruction Type |  -  |
**422** | Error creating Instruction Type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

