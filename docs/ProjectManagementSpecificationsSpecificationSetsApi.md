# procore_sdk.ProjectManagementSpecificationsSpecificationSetsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_specification_sets_get**](ProjectManagementSpecificationsSpecificationSetsApi.md#rest_v10_projects_project_id_specification_sets_get) | **GET** /rest/v1.0/projects/{project_id}/specification_sets | List Specification Sets
[**rest_v10_projects_project_id_specification_sets_id_get**](ProjectManagementSpecificationsSpecificationSetsApi.md#rest_v10_projects_project_id_specification_sets_id_get) | **GET** /rest/v1.0/projects/{project_id}/specification_sets/{id} | Show Specification Set
[**rest_v10_projects_project_id_specification_sets_post**](ProjectManagementSpecificationsSpecificationSetsApi.md#rest_v10_projects_project_id_specification_sets_post) | **POST** /rest/v1.0/projects/{project_id}/specification_sets | Create Specification Set


# **rest_v10_projects_project_id_specification_sets_get**
> List[RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner] rest_v10_projects_project_id_specification_sets_get(procore_company_id, project_id, page=page, per_page=per_page)

List Specification Sets

List the Specification Sets in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_get200_response_inner import RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | The ID of the project for the new set
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Specification Sets
        api_response = api_instance.rest_v10_projects_project_id_specification_sets_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| The ID of the project for the new set | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner]**](RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Company or project is not valid, user is not an active contact, company does not have an ERP connection |  -  |
**403** | User has insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_specification_sets_id_get**
> RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner rest_v10_projects_project_id_specification_sets_id_get(procore_company_id, project_id, id)

Show Specification Set

Show a specific Specification Set

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_get200_response_inner import RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | ID of the specification section to show

    try:
        # Show Specification Set
        api_response = api_instance.rest_v10_projects_project_id_specification_sets_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| ID of the specification section to show | 

### Return type

[**RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner**](RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Company or project is not valid, user is not an active contact, company does not have an ERP connection |  -  |
**403** | User has insufficient access |  -  |
**404** | Invalid specification set ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_specification_sets_post**
> RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner rest_v10_projects_project_id_specification_sets_post(procore_company_id, project_id, rest_v10_projects_project_id_specification_sets_post_request)

Create Specification Set

Create a new Specification Set in the specified project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_get200_response_inner import RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_specification_sets_post_request import RestV10ProjectsProjectIdSpecificationSetsPostRequest
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSetsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | The ID of the project for the new set
    rest_v10_projects_project_id_specification_sets_post_request = procore_sdk.RestV10ProjectsProjectIdSpecificationSetsPostRequest() # RestV10ProjectsProjectIdSpecificationSetsPostRequest | 

    try:
        # Create Specification Set
        api_response = api_instance.rest_v10_projects_project_id_specification_sets_post(procore_company_id, project_id, rest_v10_projects_project_id_specification_sets_post_request)
        print("The response of ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSetsApi->rest_v10_projects_project_id_specification_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| The ID of the project for the new set | 
 **rest_v10_projects_project_id_specification_sets_post_request** | [**RestV10ProjectsProjectIdSpecificationSetsPostRequest**](RestV10ProjectsProjectIdSpecificationSetsPostRequest.md)|  | 

### Return type

[**RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner**](RestV10ProjectsProjectIdSpecificationSetsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid set |  -  |
**401** | Company or project is not valid, user is not an active contact, company does not have an ERP connection |  -  |
**403** | User has insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

