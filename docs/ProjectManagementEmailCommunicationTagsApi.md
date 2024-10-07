# procore_sdk.ProjectManagementEmailCommunicationTagsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_communication_tags_get**](ProjectManagementEmailCommunicationTagsApi.md#rest_v10_communication_tags_get) | **GET** /rest/v1.0/communication_tags | List communication tags
[**rest_v10_communication_tags_post**](ProjectManagementEmailCommunicationTagsApi.md#rest_v10_communication_tags_post) | **POST** /rest/v1.0/communication_tags | Create communication tag


# **rest_v10_communication_tags_get**
> List[RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner] rest_v10_communication_tags_get(procore_company_id, project_id, page=page, per_page=per_page)

List communication tags

List communication tags on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_communications_id_get200_response_all_of_communication_tags_inner import RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner
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
    api_instance = procore_sdk.ProjectManagementEmailCommunicationTagsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List communication tags
        api_response = api_instance.rest_v10_communication_tags_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ProjectManagementEmailCommunicationTagsApi->rest_v10_communication_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailCommunicationTagsApi->rest_v10_communication_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner]**](RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_communication_tags_post**
> RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner rest_v10_communication_tags_post(procore_company_id, project_id, rest_v10_communication_tags_post_request)

Create communication tag

Create a communication tag on a given project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_communication_tags_post_request import RestV10CommunicationTagsPostRequest
from procore_sdk.models.rest_v10_communications_id_get200_response_all_of_communication_tags_inner import RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner
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
    api_instance = procore_sdk.ProjectManagementEmailCommunicationTagsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rest_v10_communication_tags_post_request = procore_sdk.RestV10CommunicationTagsPostRequest() # RestV10CommunicationTagsPostRequest | 

    try:
        # Create communication tag
        api_response = api_instance.rest_v10_communication_tags_post(procore_company_id, project_id, rest_v10_communication_tags_post_request)
        print("The response of ProjectManagementEmailCommunicationTagsApi->rest_v10_communication_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementEmailCommunicationTagsApi->rest_v10_communication_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rest_v10_communication_tags_post_request** | [**RestV10CommunicationTagsPostRequest**](RestV10CommunicationTagsPostRequest.md)|  | 

### Return type

[**RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner**](RestV10CommunicationsIdGet200ResponseAllOfCommunicationTagsInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

