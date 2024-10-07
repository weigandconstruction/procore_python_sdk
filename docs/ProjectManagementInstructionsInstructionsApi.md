# procore_sdk.ProjectManagementInstructionsInstructionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_instructions_get**](ProjectManagementInstructionsInstructionsApi.md#rest_v10_projects_project_id_instructions_get) | **GET** /rest/v1.0/projects/{project_id}/instructions | List Instructions on a project
[**rest_v10_projects_project_id_instructions_id_delete**](ProjectManagementInstructionsInstructionsApi.md#rest_v10_projects_project_id_instructions_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/instructions/{id} | Delete Instruction
[**rest_v10_projects_project_id_instructions_id_get**](ProjectManagementInstructionsInstructionsApi.md#rest_v10_projects_project_id_instructions_id_get) | **GET** /rest/v1.0/projects/{project_id}/instructions/{id} | Show Instruction
[**rest_v10_projects_project_id_instructions_id_patch**](ProjectManagementInstructionsInstructionsApi.md#rest_v10_projects_project_id_instructions_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/instructions/{id} | Update Instruction
[**rest_v10_projects_project_id_instructions_post**](ProjectManagementInstructionsInstructionsApi.md#rest_v10_projects_project_id_instructions_post) | **POST** /rest/v1.0/projects/{project_id}/instructions | Create Instructions


# **rest_v10_projects_project_id_instructions_get**
> List[RestV10ProjectsProjectIdInstructionsGet200ResponseInner] rest_v10_projects_project_id_instructions_get(procore_company_id, project_id, page=page, per_page=per_page)

List Instructions on a project

Return a list of all Instructions from a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner import RestV10ProjectsProjectIdInstructionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Instructions on a project
        api_response = api_instance.rest_v10_projects_project_id_instructions_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdInstructionsGet200ResponseInner]**](RestV10ProjectsProjectIdInstructionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instructions listed successfully |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instructions_id_delete**
> rest_v10_projects_project_id_instructions_id_delete(procore_company_id, project_id, id)

Delete Instruction

Delete the specified Instruction.

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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID

    try:
        # Delete Instruction
        api_instance.rest_v10_projects_project_id_instructions_id_delete(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_id_delete: %s\n" % e)
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
**403** | User does not have permission to delete Instruction |  -  |
**404** | Instruction not found |  -  |
**500** | Error deleting Instruction |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instructions_id_get**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInner rest_v10_projects_project_id_instructions_id_get(procore_company_id, project_id, id)

Show Instruction

Return detailed information on the specified Instruction.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner import RestV10ProjectsProjectIdInstructionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID

    try:
        # Show Instruction
        api_response = api_instance.rest_v10_projects_project_id_instructions_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Instruction ID | 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInner**](RestV10ProjectsProjectIdInstructionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instruction shown successfully |  -  |
**403** | User does not have permission to view Instruction |  -  |
**404** | Instruction not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instructions_id_patch**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInner rest_v10_projects_project_id_instructions_id_patch(procore_company_id, project_id, id, body75, send_emails=send_emails)

Update Instruction

Update the specified Instruction.

### Example


```python
import procore_sdk
from procore_sdk.models.body75 import Body75
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner import RestV10ProjectsProjectIdInstructionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | Instruction ID
    body75 = procore_sdk.Body75() # Body75 | 
    send_emails = True # bool | Designates whether or not emails will be sent (default false) (optional)

    try:
        # Update Instruction
        api_response = api_instance.rest_v10_projects_project_id_instructions_id_patch(procore_company_id, project_id, id, body75, send_emails=send_emails)
        print("The response of ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| Instruction ID | 
 **body75** | [**Body75**](Body75.md)|  | 
 **send_emails** | **bool**| Designates whether or not emails will be sent (default false) | [optional] 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInner**](RestV10ProjectsProjectIdInstructionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instruction updated successfully |  -  |
**403** | User does not have permission to update Instruction |  -  |
**404** | Instruction not found |  -  |
**422** | Error updating Instruction |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_instructions_post**
> RestV10ProjectsProjectIdInstructionsGet200ResponseInner rest_v10_projects_project_id_instructions_post(procore_company_id, project_id, body74)

Create Instructions

Create a new Instruction associated with the specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.body74 import Body74
from procore_sdk.models.rest_v10_projects_project_id_instructions_get200_response_inner import RestV10ProjectsProjectIdInstructionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementInstructionsInstructionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    body74 = procore_sdk.Body74() # Body74 | 

    try:
        # Create Instructions
        api_response = api_instance.rest_v10_projects_project_id_instructions_post(procore_company_id, project_id, body74)
        print("The response of ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementInstructionsInstructionsApi->rest_v10_projects_project_id_instructions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **body74** | [**Body74**](Body74.md)|  | 

### Return type

[**RestV10ProjectsProjectIdInstructionsGet200ResponseInner**](RestV10ProjectsProjectIdInstructionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Instruction created successfully |  -  |
**403** | User does not have permission to create Instruction |  -  |
**422** | Error creating Instruction |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

