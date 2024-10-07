# procore_sdk.ProjectManagementRFIRFIsApi

All URIs are relative to *https://api.procore.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_v10_projects_project_id_rfis_get**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_get) | **GET** /rest/v1.0/projects/{project_id}/rfis | List RFIs
[**rest_v10_projects_project_id_rfis_id_get**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_id_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/{id} | Show RFI
[**rest_v10_projects_project_id_rfis_id_patch**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_id_patch) | **PATCH** /rest/v1.0/projects/{project_id}/rfis/{id} | Update RFI
[**rest_v10_projects_project_id_rfis_id_recycle_patch**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_id_recycle_patch) | **PATCH** /rest/v1.0/projects/{project_id}/rfis/{id}/recycle | Recycle RFI
[**rest_v10_projects_project_id_rfis_id_retrieve_patch**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_id_retrieve_patch) | **PATCH** /rest/v1.0/projects/{project_id}/rfis/{id}/retrieve | Retrieve Recycled RFI
[**rest_v10_projects_project_id_rfis_idpdf_get**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_idpdf_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/{id}.pdf | Show RFI in PDF format
[**rest_v10_projects_project_id_rfis_patch**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_patch) | **PATCH** /rest/v1.0/projects/{project_id}/rfis | Batch Update RFIs
[**rest_v10_projects_project_id_rfis_post**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_post) | **POST** /rest/v1.0/projects/{project_id}/rfis | Create RFI
[**rest_v10_projects_project_id_rfis_recycle_bin_get**](ProjectManagementRFIRFIsApi.md#rest_v10_projects_project_id_rfis_recycle_bin_get) | **GET** /rest/v1.0/projects/{project_id}/rfis/recycle_bin | List Recycled RFIs


# **rest_v10_projects_project_id_rfis_get**
> List[RestV10ProjectsProjectIdRfisGet200ResponseInner] rest_v10_projects_project_id_rfis_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_assigned_id=filters_assigned_id, filters_created_at=filters_created_at, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_cost_code_id=filters_cost_code_id, filters_received_from_login_information_id=filters_received_from_login_information_id, filters_ball_in_court_id=filters_ball_in_court_id, filters_location_id=filters_location_id, filters_updated_at=filters_updated_at, filters_rfi_manager_id=filters_rfi_manager_id, search=search, sort_attribute=sort_attribute, sort_direction=sort_direction)

List RFIs

Returns all RFIs in a specified Project.  See [Filtering on List Actions](https://developers.procore.com/documentation/filtering-on-list-actions) for information on using the filtering capabilities provided by this endpoint.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner import RestV10ProjectsProjectIdRfisGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_id = [56] # List[int] | Return item(s) with the specified IDs. (optional)
    filters_status = 'filters_status_example' # str | Return item(s) with the specified RFI Status. (optional)
    filters_assigned_id = 'filters_assigned_id_example' # str | Assigned ID (optional)
    filters_created_at = '2013-10-20' # date | Return item(s) created within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_responsible_contractor_id = 56 # int | Responsible Contractor ID (optional)
    filters_cost_code_id = 'filters_cost_code_id_example' # str | Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. (optional)
    filters_received_from_login_information_id = 'filters_received_from_login_information_id_example' # str | Received From Login Information ID. Returns item(s) with the specified Received From Login Information ID. (optional)
    filters_ball_in_court_id = 56 # int | User ID. Return item(s) where the specified User ID is the Ball in Court. (optional)
    filters_location_id = [56] # List[int] | Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)
    filters_rfi_manager_id = 56 # int | Return item(s) with the specified RFI Manager ID. (optional)
    search = 'search_example' # str | Search for RFIs by subject or number. This parameter will return all RFIs that match the search term. (optional)
    sort_attribute = 'sort_attribute_example' # str | The attribute by which to sort the list of RFIs (optional)
    sort_direction = 'sort_direction_example' # str | If passed a sort attribute, determines which direction to sort (optional)

    try:
        # List RFIs
        api_response = api_instance.rest_v10_projects_project_id_rfis_get(procore_company_id, project_id, page=page, per_page=per_page, filters_id=filters_id, filters_status=filters_status, filters_assigned_id=filters_assigned_id, filters_created_at=filters_created_at, filters_responsible_contractor_id=filters_responsible_contractor_id, filters_cost_code_id=filters_cost_code_id, filters_received_from_login_information_id=filters_received_from_login_information_id, filters_ball_in_court_id=filters_ball_in_court_id, filters_location_id=filters_location_id, filters_updated_at=filters_updated_at, filters_rfi_manager_id=filters_rfi_manager_id, search=search, sort_attribute=sort_attribute, sort_direction=sort_direction)
        print("The response of ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_id** | [**List[int]**](int.md)| Return item(s) with the specified IDs. | [optional] 
 **filters_status** | **str**| Return item(s) with the specified RFI Status. | [optional] 
 **filters_assigned_id** | **str**| Assigned ID | [optional] 
 **filters_created_at** | **date**| Return item(s) created within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_responsible_contractor_id** | **int**| Responsible Contractor ID | [optional] 
 **filters_cost_code_id** | **str**| Cost Code ID. Returns item(s) with the specified Cost Code ID or within the specified range of Cost Code IDs. | [optional] 
 **filters_received_from_login_information_id** | **str**| Received From Login Information ID. Returns item(s) with the specified Received From Login Information ID. | [optional] 
 **filters_ball_in_court_id** | **int**| User ID. Return item(s) where the specified User ID is the Ball in Court. | [optional] 
 **filters_location_id** | [**List[int]**](int.md)| Location ID. Returns item(s) with the specified Location ID or a range of Location IDs. | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 
 **filters_rfi_manager_id** | **int**| Return item(s) with the specified RFI Manager ID. | [optional] 
 **search** | **str**| Search for RFIs by subject or number. This parameter will return all RFIs that match the search term. | [optional] 
 **sort_attribute** | **str**| The attribute by which to sort the list of RFIs | [optional] 
 **sort_direction** | **str**| If passed a sort attribute, determines which direction to sort | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRfisGet200ResponseInner]**](RestV10ProjectsProjectIdRfisGet200ResponseInner.md)

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

# **rest_v10_projects_project_id_rfis_id_get**
> RestV10ProjectsProjectIdRfisPost201Response rest_v10_projects_project_id_rfis_id_get(procore_company_id, project_id, id)

Show RFI

Return detailed information about a specified RFI in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response import RestV10ProjectsProjectIdRfisPost201Response
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | RFI ID

    try:
        # Show RFI
        api_response = api_instance.rest_v10_projects_project_id_rfis_id_get(procore_company_id, project_id, id)
        print("The response of ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| RFI ID | 

### Return type

[**RestV10ProjectsProjectIdRfisPost201Response**](RestV10ProjectsProjectIdRfisPost201Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_id_patch**
> RestV10ProjectsProjectIdRfisPost201Response rest_v10_projects_project_id_rfis_id_patch(procore_company_id, project_id, id, rfi_update_body, run_configurable_validations=run_configurable_validations)

Update RFI

Updates a specified RFI in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rfi_update_body import RFIUpdateBody
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response import RestV10ProjectsProjectIdRfisPost201Response
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | RFI ID
    rfi_update_body = procore_sdk.RFIUpdateBody() # RFIUpdateBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Update RFI
        api_response = api_instance.rest_v10_projects_project_id_rfis_id_patch(procore_company_id, project_id, id, rfi_update_body, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| RFI ID | 
 **rfi_update_body** | [**RFIUpdateBody**](RFIUpdateBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdRfisPost201Response**](RestV10ProjectsProjectIdRfisPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_id_recycle_patch**
> rest_v10_projects_project_id_rfis_id_recycle_patch(procore_company_id, project_id, id)

Recycle RFI

Send a specified RFI to the Recycle Bin.

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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | RFI ID

    try:
        # Recycle RFI
        api_instance.rest_v10_projects_project_id_rfis_id_recycle_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_recycle_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| RFI ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_id_retrieve_patch**
> rest_v10_projects_project_id_rfis_id_retrieve_patch(procore_company_id, project_id, id)

Retrieve Recycled RFI

Retrieve a specified RFI from the Recycle Bin.

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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | RFI ID

    try:
        # Retrieve Recycled RFI
        api_instance.rest_v10_projects_project_id_rfis_id_retrieve_patch(procore_company_id, project_id, id)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_id_retrieve_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| RFI ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_idpdf_get**
> rest_v10_projects_project_id_rfis_idpdf_get(procore_company_id, project_id, id, only_official=only_official)

Show RFI in PDF format

Return detailed information (as a PDF) about a specified RFI in a specified Project.

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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    id = 56 # int | RFI ID
    only_official = True # bool | If true, include only official responses; if false return all responses. (optional)

    try:
        # Show RFI in PDF format
        api_instance.rest_v10_projects_project_id_rfis_idpdf_get(procore_company_id, project_id, id, only_official=only_official)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_idpdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **id** | **int**| RFI ID | 
 **only_official** | **bool**| If true, include only official responses; if false return all responses. | [optional] 

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
**302** | Redirect to PDF download URL |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_patch**
> rest_v10_projects_project_id_rfis_patch(procore_company_id, project_id, rfi_body2, run_configurable_validations=run_configurable_validations)

Batch Update RFIs

Update specified RFIs in a specified project. Specify the RFIs by their IDs. Pass in the same values for each specified RFI for the action to succeed.

### Example


```python
import procore_sdk
from procore_sdk.models.rfi_body2 import RFIBody2
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_body2 = procore_sdk.RFIBody2() # RFIBody2 | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Batch Update RFIs
        api_instance.rest_v10_projects_project_id_rfis_patch(procore_company_id, project_id, rfi_body2, run_configurable_validations=run_configurable_validations)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_body2** | [**RFIBody2**](RFIBody2.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_post**
> RestV10ProjectsProjectIdRfisPost201Response rest_v10_projects_project_id_rfis_post(procore_company_id, project_id, rfi_body, run_configurable_validations=run_configurable_validations)

Create RFI

Creates a new RFI in a specified Project.

### Example


```python
import procore_sdk
from procore_sdk.models.rfi_body import RFIBody
from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response import RestV10ProjectsProjectIdRfisPost201Response
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    rfi_body = procore_sdk.RFIBody() # RFIBody | 
    run_configurable_validations = False # bool | If true, validations are run for the corresponding Configurable Field Set. (optional) (default to False)

    try:
        # Create RFI
        api_response = api_instance.rest_v10_projects_project_id_rfis_post(procore_company_id, project_id, rfi_body, run_configurable_validations=run_configurable_validations)
        print("The response of ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **rfi_body** | [**RFIBody**](RFIBody.md)|  | 
 **run_configurable_validations** | **bool**| If true, validations are run for the corresponding Configurable Field Set. | [optional] [default to False]

### Return type

[**RestV10ProjectsProjectIdRfisPost201Response**](RestV10ProjectsProjectIdRfisPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_v10_projects_project_id_rfis_recycle_bin_get**
> List[RestV10ProjectsProjectIdRfisGet200ResponseInner] rest_v10_projects_project_id_rfis_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)

List Recycled RFIs

Returns all deleted RFIs in a specified Project

### Example


```python
import procore_sdk
from procore_sdk.models.rest_v10_projects_project_id_rfis_get200_response_inner import RestV10ProjectsProjectIdRfisGet200ResponseInner
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
    api_instance = procore_sdk.ProjectManagementRFIRFIsApi(api_client)
    procore_company_id = 56 # int | Unique company identifier associated with the Procore User Account.
    project_id = 56 # int | Unique identifier for the project.
    page = 56 # int | Page (optional)
    per_page = 56 # int | Elements per page (optional)
    filters_updated_at = '2013-10-20' # date | Return item(s) last updated within the specified ISO 8601 datetime range. Formats: `YYYY-MM-DD`...`YYYY-MM-DD` - Date `YYYY-MM-DDTHH:MM:SSZ`...`YYYY-MM-DDTHH:MM:SSZ` - DateTime with UTC Offset `YYYY-MM-DDTHH:MM:SS+XX:00`...`YYYY-MM-DDTHH:MM:SS+XX:00` - Datetime with Custom Offset (optional)

    try:
        # List Recycled RFIs
        api_response = api_instance.rest_v10_projects_project_id_rfis_recycle_bin_get(procore_company_id, project_id, page=page, per_page=per_page, filters_updated_at=filters_updated_at)
        print("The response of ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_recycle_bin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectManagementRFIRFIsApi->rest_v10_projects_project_id_rfis_recycle_bin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **procore_company_id** | **int**| Unique company identifier associated with the Procore User Account. | 
 **project_id** | **int**| Unique identifier for the project. | 
 **page** | **int**| Page | [optional] 
 **per_page** | **int**| Elements per page | [optional] 
 **filters_updated_at** | **date**| Return item(s) last updated within the specified ISO 8601 datetime range. Formats: &#x60;YYYY-MM-DD&#x60;...&#x60;YYYY-MM-DD&#x60; - Date &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;...&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - DateTime with UTC Offset &#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60;...&#x60;YYYY-MM-DDTHH:MM:SS+XX:00&#x60; - Datetime with Custom Offset | [optional] 

### Return type

[**List[RestV10ProjectsProjectIdRfisGet200ResponseInner]**](RestV10ProjectsProjectIdRfisGet200ResponseInner.md)

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

