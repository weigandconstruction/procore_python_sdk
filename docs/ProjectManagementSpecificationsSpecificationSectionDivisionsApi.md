# procore_sdk.ProjectManagementSpecificationsSpecificationSectionDivisionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_specification_section_divisions_get**](ProjectManagementSpecificationsSpecificationSectionDivisionsApi.md#rest_v10_specification_section_divisions_get) | **GET** /rest/v1.0/specification_section_divisions | List Specification Section Divisions for a Project
[**rest_v10_specification_section_divisions_post**](ProjectManagementSpecificationsSpecificationSectionDivisionsApi.md#rest_v10_specification_section_divisions_post) | **POST** /rest/v1.0/specification_section_divisions | Create Specification Section Division for a Project


# **rest_v10_specification_section_divisions_get**
> List[SpecificationSectionDivision] rest_v10_specification_section_divisions_get(procore_company_id, project_id, page=page, per_page=per_page)

List Specification Section Divisions for a Project

### Example


```python
import procore_sdk
from procore_sdk.models.specification_section_division import SpecificationSectionDivision
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionDivisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Specification Section Divisions for a Project
        api_response = api_instance.rest_v10_specification_section_divisions_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementSpecificationsSpecificationSectionDivisionsApi->rest_v10_specification_section_divisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionDivisionsApi->rest_v10_specification_section_divisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[SpecificationSectionDivision]**](SpecificationSectionDivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_specification_section_divisions_post**
> SpecificationSectionDivision rest_v10_specification_section_divisions_post(procore_company_id, project_id=project_id, rest_v10_specification_section_divisions_post_request=rest_v10_specification_section_divisions_post_request)

Create Specification Section Division for a Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_specification_section_divisions_post_request import RestV10SpecificationSectionDivisionsPostRequest
from procore_sdk.models.specification_section_division import SpecificationSectionDivision
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionDivisionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project. (optional)
    rest_v10_specification_section_divisions_post_request = procore_sdk.RestV10SpecificationSectionDivisionsPostRequest() # RestV10SpecificationSectionDivisionsPostRequest |  (optional)

    try:
        # Create Specification Section Division for a Project
        api_response = api_instance.rest_v10_specification_section_divisions_post(procore_company_id, project_id=project_id, rest_v10_specification_section_divisions_post_request=rest_v10_specification_section_divisions_post_request)
        print("The response of ProjectManagementSpecificationsSpecificationSectionDivisionsApi->rest_v10_specification_section_divisions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionDivisionsApi->rest_v10_specification_section_divisions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | [optional] 
 **rest_v10_specification_section_divisions_post_request** | [**RestV10SpecificationSectionDivisionsPostRequest**](RestV10SpecificationSectionDivisionsPostRequest.md)|  | [optional] 

### Return type

[**SpecificationSectionDivision**](SpecificationSectionDivision.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

