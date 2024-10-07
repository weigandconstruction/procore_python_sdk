# procore_sdk.ProjectManagementSpecificationsSpecificationSectionsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_specification_sections_get**](ProjectManagementSpecificationsSpecificationSectionsApi.md#rest_v10_specification_sections_get) | **GET** /rest/v1.0/specification_sections | List Specification Sections
[**rest_v10_specification_sections_post**](ProjectManagementSpecificationsSpecificationSectionsApi.md#rest_v10_specification_sections_post) | **POST** /rest/v1.0/specification_sections | Create Specification Section for a Project


# **rest_v10_specification_sections_get**
> List[RestV10SpecificationSectionsGet200ResponseInner] rest_v10_specification_sections_get(procore_company_id, project_id, filters_id=filters_id, sort=sort)

List Specification Sections

List the Specification Sections in a Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_specification_sections_get200_response_inner import RestV10SpecificationSectionsGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    sort = 'sort_example' # str | Sorts the specification sections by number Ex. 'sort=number' Use 'sort=-number' to sort in descending order (optional)

    try:
        # List Specification Sections
        api_response = api_instance.rest_v10_specification_sections_get(procore_company_id, project_id, filters_id=filters_id, sort=sort)
        print("The response of ProjectManagementSpecificationsSpecificationSectionsApi->rest_v10_specification_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionsApi->rest_v10_specification_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **sort** | **str**| Sorts the specification sections by number Ex. &#39;sort&#x3D;number&#39; Use &#39;sort&#x3D;-number&#39; to sort in descending order | [optional] 

### Return type

[**List[RestV10SpecificationSectionsGet200ResponseInner]**](RestV10SpecificationSectionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | Company or project is not valid, user is not an active contact |  -  |
**403** | User has insufficient access |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_specification_sections_post**
> RestV10SpecificationSectionsGet200ResponseInner rest_v10_specification_sections_post(procore_company_id, project_id, rest_v10_specification_sections_post_request=rest_v10_specification_sections_post_request)

Create Specification Section for a Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_specification_sections_get200_response_inner import RestV10SpecificationSectionsGet200ResponseInner
from procore_sdk.models.rest_v10_specification_sections_post_request import RestV10SpecificationSectionsPostRequest
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
    api_instance = procore_sdk.ProjectManagementSpecificationsSpecificationSectionsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_specification_sections_post_request = procore_sdk.RestV10SpecificationSectionsPostRequest() # RestV10SpecificationSectionsPostRequest |  (optional)

    try:
        # Create Specification Section for a Project
        api_response = api_instance.rest_v10_specification_sections_post(procore_company_id, project_id, rest_v10_specification_sections_post_request=rest_v10_specification_sections_post_request)
        print("The response of ProjectManagementSpecificationsSpecificationSectionsApi->rest_v10_specification_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementSpecificationsSpecificationSectionsApi->rest_v10_specification_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_specification_sections_post_request** | [**RestV10SpecificationSectionsPostRequest**](RestV10SpecificationSectionsPostRequest.md)|  | [optional] 

### Return type

[**RestV10SpecificationSectionsGet200ResponseInner**](RestV10SpecificationSectionsGet200ResponseInner.md)

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

