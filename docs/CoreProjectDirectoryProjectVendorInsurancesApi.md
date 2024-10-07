# procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_get**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_get) | **GET** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances | List project vendor insurances
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete) | **DELETE** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances/{id} | Delete project vendor insurance
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get) | **GET** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances/{id} | Show project vendor insurance
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances/{id} | Update project vendor insurance
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_post**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_post) | **POST** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances | Create project vendor insurance
[**rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch**](CoreProjectDirectoryProjectVendorInsurancesApi.md#rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch) | **PATCH** /rest/v1.0/projects/{project_id}/vendors/{vendor_id}/insurances/sync | Sync Project Vendor Insurances


# **rest_v10_projects_project_id_vendors_vendor_id_insurances_get**
> List[Insurance] rest_v10_projects_project_id_vendors_vendor_id_insurances_get(procore_company_id, project_id, vendor_id, page=page, per_page=per_page)

List project vendor insurances

Return a list of Insurances from the specified Project Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List project vendor insurances
        api_response = api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_get(procore_company_id, project_id, vendor_id, page=page, per_page=per_page)
        print("The response of CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Insurance]**](Insurance.md)

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

# **rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete**
> rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete(procore_company_id, project_id, vendor_id, id)

Delete project vendor insurance

Delete the specified Project Vendor Insurance.

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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    id = 56 # int | ID

    try:
        # Delete project vendor insurance
        api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete(procore_company_id, project_id, vendor_id, id)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **id** | **int**| ID | 

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

# **rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get**
> Insurance rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get(procore_company_id, project_id, vendor_id, id)

Show project vendor insurance

Show detail on the specified Project Vendor Insurance.

### Example


```python
import procore_sdk
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    id = 56 # int | ID

    try:
        # Show project vendor insurance
        api_response = api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get(procore_company_id, project_id, vendor_id, id)
        print("The response of CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **id** | **int**| ID | 

### Return type

[**Insurance**](Insurance.md)

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

# **rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch**
> Insurance rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch(procore_company_id, project_id, vendor_id, id, body33)

Update project vendor insurance

Update the specified Project Vendor Insurance.

### Example


```python
import procore_sdk
from procore_sdk.models.body33 import Body33
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    id = 56 # int | ID
    body33 = procore_sdk.Body33() # Body33 | 

    try:
        # Update project vendor insurance
        api_response = api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch(procore_company_id, project_id, vendor_id, id, body33)
        print("The response of CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **id** | **int**| ID | 
 **body33** | [**Body33**](Body33.md)|  | 

### Return type

[**Insurance**](Insurance.md)

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

# **rest_v10_projects_project_id_vendors_vendor_id_insurances_post**
> Insurance rest_v10_projects_project_id_vendors_vendor_id_insurances_post(procore_company_id, project_id, vendor_id, body33)

Create project vendor insurance

Create a new Insurance associated with the specified Project Vendor.

### Example


```python
import procore_sdk
from procore_sdk.models.body33 import Body33
from procore_sdk.models.insurance import Insurance
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    body33 = procore_sdk.Body33() # Body33 | 

    try:
        # Create project vendor insurance
        api_response = api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_post(procore_company_id, project_id, vendor_id, body33)
        print("The response of CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **body33** | [**Body33**](Body33.md)|  | 

### Return type

[**Insurance**](Insurance.md)

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

# **rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch**
> ArrayOfCompanyVendorInsurances rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch(procore_company_id, project_id, vendor_id, insurance_sync_body)

Sync Project Vendor Insurances

This endpoint creates or updates a batch of Project Vendor Insurances.

### Example


```python
import procore_sdk
from procore_sdk.models.array_of_company_vendor_insurances import ArrayOfCompanyVendorInsurances
from procore_sdk.models.insurance_sync_body import InsuranceSyncBody
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
    api_instance = procore_sdk.CoreProjectDirectoryProjectVendorInsurancesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    vendor_id = 56 # int | Vendor ID
    insurance_sync_body = procore_sdk.InsuranceSyncBody() # InsuranceSyncBody | 

    try:
        # Sync Project Vendor Insurances
        api_response = api_instance.rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch(procore_company_id, project_id, vendor_id, insurance_sync_body)
        print("The response of CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreProjectDirectoryProjectVendorInsurancesApi->rest_v10_projects_project_id_vendors_vendor_id_insurances_sync_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **vendor_id** | **int**| Vendor ID | 
 **insurance_sync_body** | [**InsuranceSyncBody**](InsuranceSyncBody.md)|  | 

### Return type

[**ArrayOfCompanyVendorInsurances**](ArrayOfCompanyVendorInsurances.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of Project Vendor Insurances |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

