# procore_sdk.QualitySafetyInspectionsInspectionTypesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_companies_company_id_inspection_types_get**](QualitySafetyInspectionsInspectionTypesApi.md#rest_v10_companies_company_id_inspection_types_get) | **GET** /rest/v1.0/companies/{company_id}/inspection_types | List Inspection Types
[**rest_v10_companies_company_id_inspection_types_id_delete**](QualitySafetyInspectionsInspectionTypesApi.md#rest_v10_companies_company_id_inspection_types_id_delete) | **DELETE** /rest/v1.0/companies/{company_id}/inspection_types/{id} | Delete Inspection Type
[**rest_v10_companies_company_id_inspection_types_id_get**](QualitySafetyInspectionsInspectionTypesApi.md#rest_v10_companies_company_id_inspection_types_id_get) | **GET** /rest/v1.0/companies/{company_id}/inspection_types/{id} | Show Inspection Type
[**rest_v10_companies_company_id_inspection_types_id_patch**](QualitySafetyInspectionsInspectionTypesApi.md#rest_v10_companies_company_id_inspection_types_id_patch) | **PATCH** /rest/v1.0/companies/{company_id}/inspection_types/{id} | Update Inspection Type
[**rest_v10_companies_company_id_inspection_types_post**](QualitySafetyInspectionsInspectionTypesApi.md#rest_v10_companies_company_id_inspection_types_post) | **POST** /rest/v1.0/companies/{company_id}/inspection_types | Create Inspection Type


# **rest_v10_companies_company_id_inspection_types_get**
> List[InspectionType2] rest_v10_companies_company_id_inspection_types_get(procore_company_id, company_id, page=page, per_page=per_page)

List Inspection Types

Return a list of all Inspection Types associated with a Company.

### Example


```python
import procore_sdk
from procore_sdk.models.inspection_type2 import InspectionType2
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Inspection Types
        api_response = api_instance.rest_v10_companies_company_id_inspection_types_get(procore_company_id, company_id, page=page, per_page=per_page)
        print("The response of QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[InspectionType2]**](InspectionType2.md)

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

# **rest_v10_companies_company_id_inspection_types_id_delete**
> rest_v10_companies_company_id_inspection_types_id_delete(procore_company_id, company_id, id)

Delete Inspection Type

Deletes an Inspection Type for a specified Company.

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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Inspection Type ID

    try:
        # Delete Inspection Type
        api_instance.rest_v10_companies_company_id_inspection_types_id_delete(procore_company_id, company_id, id)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Inspection Type ID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Error Deleting Inspection Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_inspection_types_id_get**
> InspectionType2 rest_v10_companies_company_id_inspection_types_id_get(procore_company_id, company_id, id)

Show Inspection Type

Returns the details for a specified Inspection Type

### Example


```python
import procore_sdk
from procore_sdk.models.inspection_type2 import InspectionType2
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Inspection Type ID

    try:
        # Show Inspection Type
        api_response = api_instance.rest_v10_companies_company_id_inspection_types_id_get(procore_company_id, company_id, id)
        print("The response of QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Inspection Type ID | 

### Return type

[**InspectionType2**](InspectionType2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_inspection_types_id_patch**
> InspectionType2 rest_v10_companies_company_id_inspection_types_id_patch(procore_company_id, company_id, id, inspection_type_body)

Update Inspection Type

Updates an Inspection Type for a specified Company.

### Example


```python
import procore_sdk
from procore_sdk.models.inspection_type2 import InspectionType2
from procore_sdk.models.inspection_type_body import InspectionTypeBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    id = 56 # int | Inspection Type ID
    inspection_type_body = procore_sdk.InspectionTypeBody() # InspectionTypeBody | 

    try:
        # Update Inspection Type
        api_response = api_instance.rest_v10_companies_company_id_inspection_types_id_patch(procore_company_id, company_id, id, inspection_type_body)
        print("The response of QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **id** | **int**| Inspection Type ID | 
 **inspection_type_body** | [**InspectionTypeBody**](InspectionTypeBody.md)|  | 

### Return type

[**InspectionType2**](InspectionType2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**422** | Error Updating Inspection Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_companies_company_id_inspection_types_post**
> InspectionType2 rest_v10_companies_company_id_inspection_types_post(procore_company_id, company_id, inspection_type_body)

Create Inspection Type

Create an Inspection Type for a Company

### Example


```python
import procore_sdk
from procore_sdk.models.inspection_type2 import InspectionType2
from procore_sdk.models.inspection_type_body import InspectionTypeBody
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
    api_instance = procore_sdk.QualitySafetyInspectionsInspectionTypesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 56 # int | Unique identifier for the company.
    inspection_type_body = procore_sdk.InspectionTypeBody() # InspectionTypeBody | 

    try:
        # Create Inspection Type
        api_response = api_instance.rest_v10_companies_company_id_inspection_types_post(procore_company_id, company_id, inspection_type_body)
        print("The response of QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualitySafetyInspectionsInspectionTypesApi->rest_v10_companies_company_id_inspection_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **int**| Unique identifier for the company. | 
 **inspection_type_body** | [**InspectionTypeBody**](InspectionTypeBody.md)|  | 

### Return type

[**InspectionType2**](InspectionType2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**422** | Error Creating Inspection Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

