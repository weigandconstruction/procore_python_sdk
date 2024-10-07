# procore_sdk.ProjectManagementSpecificationsSpecificationUploadsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_specification_uploads_get**](ProjectManagementSpecificationsSpecificationUploadsApi.md#rest_v10_projects_project_id_specification_uploads_get) | **GET** /rest/v1.0/projects/{project_id}/specification_uploads | List Specification Uploads
[**rest_v10_projects_project_id_specification_uploads_post**](ProjectManagementSpecificationsSpecificationUploadsApi.md#rest_v10_projects_project_id_specification_uploads_post) | **POST** /rest/v1.0/projects/{project_id}/specification_uploads | Create specification upload


# **rest_v10_projects_project_id_specification_uploads_get**
> List[RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner] rest_v10_projects_project_id_specification_uploads_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_specification_set_id=filters_specification_set_id)

List Specification Uploads

List the Specification Uploads in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_get200_response_inner import RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | The ID of the project to upload to
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified status. (optional)
    filters_specification_set_id = [56] # List[int] | Return items with the specified set ID. (optional)

    try:
        # List Specification Uploads
        api_response = api_instance.rest_v10_projects_project_id_specification_uploads_get(procore_company_id, project_id, page=page, per_page=per_page, filters_status=filters_status, filters_specification_set_id=filters_specification_set_id)
        print("The response of ProjectManagementSpecificationsSpecificationUploadsApi->rest_v10_projects_project_id_specification_uploads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationUploadsApi->rest_v10_projects_project_id_specification_uploads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| The ID of the project to upload to | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_status** | **str**| Return item(s) with the specified status. | [optional] 
 **filters_specification_set_id** | [**List[int]**](int.md)| Return items with the specified set ID. | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner]**](RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_specification_uploads_post**
> List[RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner] rest_v10_projects_project_id_specification_uploads_post(procore_company_id, project_id, rest_v10_projects_project_id_specification_uploads_post_request)

Create specification upload

Upload Specifications that will be pending review

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_get200_response_inner import RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner
from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_post_request import RestV10ProjectsProjectIdSpecificationUploadsPostRequest
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationUploadsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | The ID of the project to upload to
    rest_v10_projects_project_id_specification_uploads_post_request = procore_sdk.RestV10ProjectsProjectIdSpecificationUploadsPostRequest() # RestV10ProjectsProjectIdSpecificationUploadsPostRequest | 

    try:
        # Create specification upload
        api_response = api_instance.rest_v10_projects_project_id_specification_uploads_post(procore_company_id, project_id, rest_v10_projects_project_id_specification_uploads_post_request)
        print("The response of ProjectManagementSpecificationsSpecificationUploadsApi->rest_v10_projects_project_id_specification_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationUploadsApi->rest_v10_projects_project_id_specification_uploads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| The ID of the project to upload to | 
 **rest_v10_projects_project_id_specification_uploads_post_request** | [**RestV10ProjectsProjectIdSpecificationUploadsPostRequest**](RestV10ProjectsProjectIdSpecificationUploadsPostRequest.md)|  | 

### Return type

[**List[RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner]**](RestV10ProjectsProjectIdSpecificationUploadsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid upload |  -  |
**401** | Company or project is not valid, user is not an active contact, company does not have an ERP connection |  -  |
**403** | User has insufficient access |  -  |
**404** | Invalid specification set ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

