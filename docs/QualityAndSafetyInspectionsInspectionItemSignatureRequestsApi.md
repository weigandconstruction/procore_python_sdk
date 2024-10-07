# procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post**](QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post) | **POST** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests/find_or_create | Finds or Creates a Inspection Item Signature Request
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get**](QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests | Get a list of Inspection Item Signature Requests
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete**](QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete) | **DELETE** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests/{id} | Deletes an Inspection Item Signature Request
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get**](QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get) | **GET** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests/{id} | Show a Inspection Item Signature Request
[**rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post**](QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi.md#rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post) | **POST** /rest/v2.0/companies/{company_id}/projects/{project_id}/inspection_items/{item_id}/signature_requests | Creates a Inspection Item Signature Request


# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post(procore_company_id, company_id, project_id, item_id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request)

Finds or Creates a Inspection Item Signature Request

Tries to find a Inspection Item Signature Request for a specified Inspection, creates one if it doesn't exist.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post201_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request = procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest() # RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest |  (optional)

    try:
        # Finds or Creates a Inspection Item Signature Request
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post(procore_company_id, company_id, project_id, item_id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request)
        print("The response of QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_find_or_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest.md)|  | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get(procore_company_id, company_id, project_id, item_id, page=page, per_page=per_page, filters_id=filters_id)

Get a list of Inspection Item Signature Requests

Get a list of Inspection Item Signature Requests for a specified Inspection.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200Response
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    page = 56 # int | Page (optional)
    per_page = 10 # int | Elements per page (optional) (default to 10)
    filters_id = ['filters_id_example'] # List[str] | Return Signature Request(s) with the specified IDs (optional)

    try:
        # Get a list of Inspection Item Signature Requests
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get(procore_company_id, company_id, project_id, item_id, page=page, per_page=per_page, filters_id=filters_id)
        print("The response of QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] [default to 10]
 **filters_id** | [**List[str]**](str.md)| Return Signature Request(s) with the specified IDs | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200Response.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete**
> rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete(procore_company_id, company_id, project_id, item_id, id)

Deletes an Inspection Item Signature Request

Deletes the specified Inspection Item Signature Request

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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    id = 'id_example' # str | Unique identifier of the Inspection Item Signature

    try:
        # Deletes an Inspection Item Signature Request
        api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete(procore_company_id, company_id, project_id, item_id, id)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **id** | **str**| Unique identifier of the Inspection Item Signature | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get(procore_company_id, company_id, project_id, item_id, id)

Show a Inspection Item Signature Request

Show the specified Inspection Item Signature Request.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post201_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    id = 'id_example' # str | Unique identifier of the Inspection Item Signature

    try:
        # Show a Inspection Item Signature Request
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get(procore_company_id, company_id, project_id, item_id, id)
        print("The response of QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **id** | **str**| Unique identifier of the Inspection Item Signature | 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post**
> RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post(procore_company_id, company_id, project_id, item_id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request)

Creates a Inspection Item Signature Request

Creates a Inspection Item Signature Request for a specified Inspection.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post201_response import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest
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
    api_instance = procore_sdk.QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    item_id = 'item_id_example' # str | Unique identifier for the inspection item.
    rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request = procore_sdk.RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest() # RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest |  (optional)

    try:
        # Creates a Inspection Item Signature Request
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post(procore_company_id, company_id, project_id, item_id, rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request=rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request)
        print("The response of QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityAndSafetyInspectionsInspectionItemSignatureRequestsApi->rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **item_id** | **str**| Unique identifier for the inspection item. | 
 **rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_post_request** | [**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPostRequest.md)|  | [optional] 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response**](RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsPost201Response.md)

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

