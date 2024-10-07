# procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_requisitions_get**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_get) | **GET** /rest/v1.0/requisitions | List Requisitions (Subcontractor Invoices) for Project
[**rest_v10_requisitions_id_delete**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_id_delete) | **DELETE** /rest/v1.0/requisitions/{id} | Delete Requisition (Subcontractor Invoice)
[**rest_v10_requisitions_id_get**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_id_get) | **GET** /rest/v1.0/requisitions/{id} | Show Requisition (Subcontractor Invoice)
[**rest_v10_requisitions_id_patch**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_id_patch) | **PATCH** /rest/v1.0/requisitions/{id} | Update Requisition (Subcontractor Invoice)
[**rest_v10_requisitions_post**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_post) | **POST** /rest/v1.0/requisitions | Create Requisition (Subcontractor Invoices) for Commitment
[**rest_v10_requisitions_requisition_id_add_change_order_package_post**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_requisition_id_add_change_order_package_post) | **POST** /rest/v1.0/requisitions/{requisition_id}/add_change_order_package | Add Change Order Package to a Requisition (Subcontractor Invoice)
[**rest_v10_requisitions_requisition_id_detail_get**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_requisition_id_detail_get) | **GET** /rest/v1.0/requisitions/{requisition_id}/detail | Show Detail for Requisition (Subcontractor Invoice)
[**rest_v10_requisitions_requisition_id_remove_change_order_package_delete**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v10_requisitions_requisition_id_remove_change_order_package_delete) | **DELETE** /rest/v1.0/requisitions/{requisition_id}/remove_change_order_package | Remove Change Order Package from a Requisition (Subcontractor Invoice)
[**rest_v11_requisitions_get**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v11_requisitions_get) | **GET** /rest/v1.1/requisitions | List Requisitions (Subcontractor Invoices) for Project
[**rest_v11_requisitions_id_delete**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v11_requisitions_id_delete) | **DELETE** /rest/v1.1/requisitions/{id} | Delete Requisition (Subcontractor Invoice)
[**rest_v11_requisitions_id_get**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v11_requisitions_id_get) | **GET** /rest/v1.1/requisitions/{id} | Show Requisition (Subcontractor Invoice)
[**rest_v11_requisitions_id_patch**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v11_requisitions_id_patch) | **PATCH** /rest/v1.1/requisitions/{id} | Update Requisition (Subcontractor Invoice)
[**rest_v11_requisitions_post**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v11_requisitions_post) | **POST** /rest/v1.1/requisitions | Create Requisition (Subcontractor Invoices) for Commitment
[**rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch**](ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi.md#rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch) | **PATCH** /rest/v2.0/companies/{company_id}/projects/{project_id}/requisitions/{id}/payment_details | Update the Due Date for a Requisition (Subcontractor Invoice)


# **rest_v10_requisitions_get**
> List[RestV10RequisitionsGet200ResponseInner] rest_v10_requisitions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_commitment_id=filters_commitment_id, filters_period_id=filters_period_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id)

List Requisitions (Subcontractor Invoices) for Project

Return a list of Requisitions (Subcontractor Invoices) on a specified project  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_get200_response_inner import RestV10RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_commitment_id = 56 # int | Commitment ID. Returns item(s) with the specified Commitment ID. (optional)
    filters_period_id = 56 # int | Billing Period ID. Returns item(s) with the specified Billing Period ID. (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Requisition (Subcontractor Invoice) status. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)

    try:
        # List Requisitions (Subcontractor Invoices) for Project
        api_response = api_instance.rest_v10_requisitions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_commitment_id=filters_commitment_id, filters_period_id=filters_period_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_commitment_id** | **int**| Commitment ID. Returns item(s) with the specified Commitment ID. | [optional] 
 **filters_period_id** | **int**| Billing Period ID. Returns item(s) with the specified Billing Period ID. | [optional] 
 **filters_status** | **str**| Return item(s) with the specified Requisition (Subcontractor Invoice) status. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 

### Return type

[**List[RestV10RequisitionsGet200ResponseInner]**](RestV10RequisitionsGet200ResponseInner.md)

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

# **rest_v10_requisitions_id_delete**
> rest_v10_requisitions_id_delete(procore_company_id, id, project_id)

Delete Requisition (Subcontractor Invoice)

Delete specified Requisition (Subcontractor Invoice)

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Requisition (Subcontractor Invoice)
        api_instance.rest_v10_requisitions_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requisitions_id_get**
> RestV10RequisitionsGet200ResponseInner rest_v10_requisitions_id_get(procore_company_id, id, project_id)

Show Requisition (Subcontractor Invoice)

Return a Requisition (Subcontractor Invoice) on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_get200_response_inner import RestV10RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v10_requisitions_id_get(procore_company_id, id, project_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**RestV10RequisitionsGet200ResponseInner**](RestV10RequisitionsGet200ResponseInner.md)

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

# **rest_v10_requisitions_id_patch**
> RestV11RequisitionsGet200ResponseInner rest_v10_requisitions_id_patch(procore_company_id, id, body21)

Update Requisition (Subcontractor Invoice)

Update a specified Requisition (Subcontractor Invoice). Users without admin permissions can only update a requisition (sub invoice) if it is the most recent and has a status of 'draft' or 'revise_and_resubmit'. Users with admin permissions can update a requisition (sub invoice) regardless of its status or whether it is the most recent.

### Example


```python
import procore_sdk
from procore_sdk.models.body21 import Body21
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    body21 = procore_sdk.Body21() # Body21 | 

    try:
        # Update Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v10_requisitions_id_patch(procore_company_id, id, body21)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **body21** | [**Body21**](Body21.md)|  | 

### Return type

[**RestV11RequisitionsGet200ResponseInner**](RestV11RequisitionsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requisitions_post**
> RestV11RequisitionsGet200ResponseInner rest_v10_requisitions_post(procore_company_id, body21)

Create Requisition (Subcontractor Invoices) for Commitment

Create a new Requisition (Subcontractor Invoices) for the specified Commitment

### Example


```python
import procore_sdk
from procore_sdk.models.body21 import Body21
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body21 = procore_sdk.Body21() # Body21 | 

    try:
        # Create Requisition (Subcontractor Invoices) for Commitment
        api_response = api_instance.rest_v10_requisitions_post(procore_company_id, body21)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body21** | [**Body21**](Body21.md)|  | 

### Return type

[**RestV11RequisitionsGet200ResponseInner**](RestV11RequisitionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requisitions_requisition_id_add_change_order_package_post**
> List[RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInner] rest_v10_requisitions_requisition_id_add_change_order_package_post(procore_company_id, requisition_id, commitment_id, project_id, change_order_package_id)

Add Change Order Package to a Requisition (Subcontractor Invoice)

The Add Change Order Package endpoint allows for the addition of a Change Order Package to a Requisition (Subcontractor Invoice) which will cause change_order_items to be added to the Requisition (Subcontractor Invoice)

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_add_change_order_package_post201_response_inner import RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    commitment_id = 56 # int | Commitment ID
    project_id = 56 # int | Unique identifier for the project.
    change_order_package_id = 56 # int | Change Order Package ID

    try:
        # Add Change Order Package to a Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v10_requisitions_requisition_id_add_change_order_package_post(procore_company_id, requisition_id, commitment_id, project_id, change_order_package_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_requisition_id_add_change_order_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_requisition_id_add_change_order_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **commitment_id** | **int**| Commitment ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **change_order_package_id** | **int**| Change Order Package ID | 

### Return type

[**List[RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInner]**](RestV10RequisitionsRequisitionIdAddChangeOrderPackagePost201ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_requisitions_requisition_id_detail_get**
> List[RestV10RequisitionsRequisitionIdDetailGet200ResponseInner] rest_v10_requisitions_requisition_id_detail_get(procore_company_id, requisition_id, project_id)

Show Detail for Requisition (Subcontractor Invoice)

Return Requisition (Subcontractor Invoice) Detail

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_requisitions_requisition_id_detail_get200_response_inner import RestV10RequisitionsRequisitionIdDetailGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Show Detail for Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v10_requisitions_requisition_id_detail_get(procore_company_id, requisition_id, project_id)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_requisition_id_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_requisition_id_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

### Return type

[**List[RestV10RequisitionsRequisitionIdDetailGet200ResponseInner]**](RestV10RequisitionsRequisitionIdDetailGet200ResponseInner.md)

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

# **rest_v10_requisitions_requisition_id_remove_change_order_package_delete**
> rest_v10_requisitions_requisition_id_remove_change_order_package_delete(procore_company_id, requisition_id, commitment_id, project_id, change_order_package_id)

Remove Change Order Package from a Requisition (Subcontractor Invoice)

Remove a specified Change Order Package from a Requisition (Subcontractor Invoice)

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    requisition_id = 56 # int | Requisition (Subcontractor Invoice) ID
    commitment_id = 56 # int | Commitment ID
    project_id = 56 # int | Unique identifier for the project.
    change_order_package_id = 56 # int | Change Order Package ID

    try:
        # Remove Change Order Package from a Requisition (Subcontractor Invoice)
        api_instance.rest_v10_requisitions_requisition_id_remove_change_order_package_delete(procore_company_id, requisition_id, commitment_id, project_id, change_order_package_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v10_requisitions_requisition_id_remove_change_order_package_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **requisition_id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **commitment_id** | **int**| Commitment ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **change_order_package_id** | **int**| Change Order Package ID | 

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
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_requisitions_get**
> List[RestV11RequisitionsGet200ResponseInner] rest_v11_requisitions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_commitment_id=filters_commitment_id, filters_period_id=filters_period_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, view=view)

List Requisitions (Subcontractor Invoices) for Project

Return a list of Requisitions (Subcontractor Invoices) on a specified project  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_commitment_id = 56 # int | Commitment ID. Returns item(s) with the specified Commitment ID. (optional)
    filters_period_id = 56 # int | Billing Period ID. Returns item(s) with the specified Billing Period ID. (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified Requisition (Subcontractor Invoice) status. (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset (optional)
    filters_origin_id = 'filters_origin_id_example' # str | Origin ID. Returns item(s) with the specified Origin ID. (optional)
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. (optional)

    try:
        # List Requisitions (Subcontractor Invoices) for Project
        api_response = api_instance.rest_v11_requisitions_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_commitment_id=filters_commitment_id, filters_period_id=filters_period_id, filters_status=filters_status, filters_created_at=filters_created_at, filters_updated_at=filters_updated_at, filters_origin_id=filters_origin_id, view=view)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_commitment_id** | **int**| Commitment ID. Returns item(s) with the specified Commitment ID. | [optional] 
 **filters_period_id** | **int**| Billing Period ID. Returns item(s) with the specified Billing Period ID. | [optional] 
 **filters_status** | **str**| Return item(s) with the specified Requisition (Subcontractor Invoice) status. | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset | [optional] 
 **filters_origin_id** | **str**| Origin ID. Returns item(s) with the specified Origin ID. | [optional] 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. | [optional] 

### Return type

[**List[RestV11RequisitionsGet200ResponseInner]**](RestV11RequisitionsGet200ResponseInner.md)

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

# **rest_v11_requisitions_id_delete**
> rest_v11_requisitions_id_delete(procore_company_id, id, project_id)

Delete Requisition (Subcontractor Invoice)

Delete specified Requisition (Subcontractor Invoice)

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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.

    try:
        # Delete Requisition (Subcontractor Invoice)
        api_instance.rest_v11_requisitions_id_delete(procore_company_id, id, project_id)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_requisitions_id_get**
> RestV11RequisitionsGet200ResponseInner rest_v11_requisitions_id_get(procore_company_id, id, project_id, view=view)

Show Requisition (Subcontractor Invoice)

Return a Requisition (Subcontractor Invoice) on a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    project_id = 56 # int | Unique identifier for the project.
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. (optional)

    try:
        # Show Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v11_requisitions_id_get(procore_company_id, id, project_id, view=view)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **project_id** | **int**| Unique identifier for the project. | 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. | [optional] 

### Return type

[**RestV11RequisitionsGet200ResponseInner**](RestV11RequisitionsGet200ResponseInner.md)

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

# **rest_v11_requisitions_id_patch**
> RestV11RequisitionsGet200ResponseInner rest_v11_requisitions_id_patch(procore_company_id, id, body20, view=view)

Update Requisition (Subcontractor Invoice)

Update a specified Requisition (Subcontractor Invoice). Users without admin permissions can only update a requisition (sub invoice) if it is the most recent and has a status of 'draft' or 'revise_and_resubmit'. Users with admin permissions can update a requisition (sub invoice) regardless of its status or whether it is the most recent. Requisition items are optional.

### Example


```python
import procore_sdk
from procore_sdk.models.body20 import Body20
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    id = 56 # int | Requisition (Subcontractor Invoice) ID
    body20 = procore_sdk.Body20() # Body20 | 
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. (optional)

    try:
        # Update Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v11_requisitions_id_patch(procore_company_id, id, body20, view=view)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **id** | **int**| Requisition (Subcontractor Invoice) ID | 
 **body20** | [**Body20**](Body20.md)|  | 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. | [optional] 

### Return type

[**RestV11RequisitionsGet200ResponseInner**](RestV11RequisitionsGet200ResponseInner.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v11_requisitions_post**
> RestV11RequisitionsGet200ResponseInner rest_v11_requisitions_post(procore_company_id, body19, view=view)

Create Requisition (Subcontractor Invoices) for Commitment

Create a new Requisition (Subcontractor Invoices) for the specified Commitment

### Example


```python
import procore_sdk
from procore_sdk.models.body19 import Body19
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    body19 = procore_sdk.Body19() # Body19 | 
    view = 'view_example' # str | Specifies which view (which attributes) of the resource is going to be present in the response. (optional)

    try:
        # Create Requisition (Subcontractor Invoices) for Commitment
        api_response = api_instance.rest_v11_requisitions_post(procore_company_id, body19, view=view)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v11_requisitions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **body19** | [**Body19**](Body19.md)|  | 
 **view** | **str**| Specifies which view (which attributes) of the resource is going to be present in the response. | [optional] 

### Return type

[**RestV11RequisitionsGet200ResponseInner**](RestV11RequisitionsGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch**
> RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch200Response rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch(procore_company_id, company_id, project_id, id, payment_due_date)

Update the Due Date for a Requisition (Subcontractor Invoice)

Updates the Due Date for a Requisition (Subcontractor Invoice)

### Example


```python
import procore_sdk
from procore_sdk.models.payment_due_date import PaymentDueDate
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch200_response import RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch200Response
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
    api_instance = procore_sdk.ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    company_id = 'company_id_example' # str | Unique identifier for the company.
    project_id = 'project_id_example' # str | Unique identifier for the project.
    id = 'id_example' # str | Unique identifier for the Requisition (Subcontractor Invoice)
    payment_due_date = procore_sdk.PaymentDueDate() # PaymentDueDate | 

    try:
        # Update the Due Date for a Requisition (Subcontractor Invoice)
        api_response = api_instance.rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch(procore_company_id, company_id, project_id, id, payment_due_date)
        print("The response of ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstructionFinancialsCommitmentsRequisitionsSubcontractorInvoicesApi->rest_v20_companies_company_id_projects_project_id_requisitions_id_payment_details_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **company_id** | **str**| Unique identifier for the company. | 
 **project_id** | **str**| Unique identifier for the project. | 
 **id** | **str**| Unique identifier for the Requisition (Subcontractor Invoice) | 
 **payment_due_date** | [**PaymentDueDate**](PaymentDueDate.md)|  | 

### Return type

[**RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch200Response**](RestV20CompaniesCompanyIdProjectsProjectIdRequisitionsIdPaymentDetailsPatch200Response.md)

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

