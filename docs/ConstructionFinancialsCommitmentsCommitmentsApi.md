# procore_sdk.ConstructionFinancialsCommitmentsCommitmentsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_commitments_get**](ConstructionFinancialsCommitmentsCommitmentsApi.md#rest_v10_commitments_get) | **GET** /rest/v1.0/commitments | List Commitments
[**rest_v10_commitments_id_get**](ConstructionFinancialsCommitmentsCommitmentsApi.md#rest_v10_commitments_id_get) | **GET** /rest/v1.0/commitments/{id} | Show a Commitment Contract


# **rest_v10_commitments_get**
> List[Commitment] rest_v10_commitments_get(procore_company_id, project_id, page=page, per_page=per_page)

List Commitments

Returns a list of Commitments.

### Example


```python
import procore_sdk
from procore_sdk.models.commitment import Commitment
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsCommitmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)

    try:
        # List Commitments
        api_response = api_instance.rest_v10_commitments_get(procore_company_id, project_id, page=page, per_page=per_page)
        print("The response of ConstructionFinancialsCommitmentsCommitmentsApi->rest_v10_commitments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsCommitmentsApi->rest_v10_commitments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 

### Return type

[**List[Commitment]**](Commitment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Per-Page - Number of items retrieved per page <br>  * Total - Total number of items to be retrieved <br>  * Link - Link headers for the first, prev, next, and last link <br>  |
**401** | User does not have correct permissions. |  -  |
**403** | User does not have correct permissions. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_commitments_id_get**
> Commitment1 rest_v10_commitments_id_get(procore_company_id, id, project_id)

Show a Commitment Contract

Returns detailed information on a Commitment Contract.  ### Special notes (Tiers)  The visibility of Change Order Packages, Potential Change Orders & Change Order Requests depends on the number of tiers defined in the Commitment Contract as follows:  1-tier: Change Order Packages  2-tier: Change Order Packages, Potential Change Orders  3-tier: Change Order Packages, Change Order Requests, Potential Change Orders

### Example


```python
import procore_sdk
from procore_sdk.models.commitment1 import Commitment1
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsCommitmentsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show a Commitment Contract
        api_response = api_instance.rest_v10_commitments_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsCommitmentsApi->rest_v10_commitments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsCommitmentsApi->rest_v10_commitments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**Commitment1**](Commitment1.md)

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
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

